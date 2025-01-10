# SPDX-License-Identifier: Apache-2.0
from tests.coverage.antlr_parser.FuncTestCaseParser import FuncTestCaseParser
from tests.coverage.antlr_parser.FuncTestCaseParserVisitor import (
    FuncTestCaseParserVisitor,
)
from tests.coverage.nodes import (
    AggregateArgument,
    CaseGroup,
    TestFile,
    TestCase,
    CaseLiteral,
    SubstraitError,
)


class TestCaseVisitor(FuncTestCaseParserVisitor):
    def __init__(self, file_path):
        self.file_path = file_path

    def visitDoc(self, ctx: FuncTestCaseParser.DocContext):
        version, include = self.visitHeader(ctx.header())
        testcases = []
        for group in ctx.testGroup():
            _, group_tests = self.visit(group)
            for test_case in group_tests:
                test_case.base_uri = include
            testcases.extend(group_tests)

        return TestFile(self.file_path, version, include, testcases)

    def visitHeader(self, ctx: FuncTestCaseParser.HeaderContext):
        version = self.visitVersion(ctx.version())
        include = self.visitInclude(ctx.include())
        return version, include

    def visitVersion(self, ctx: FuncTestCaseParser.VersionContext):
        return ctx.FormatVersion().getText()

    def visitInclude(self, ctx: FuncTestCaseParser.IncludeContext):
        # TODO handle multiple includes
        return ctx.StringLiteral(0).getText().strip("'")

    def visitTestGroupDescription(
        self, ctx: FuncTestCaseParser.TestGroupDescriptionContext
    ):
        group = ctx.DescriptionLine().getText().strip("#").strip()
        return CaseGroup(group, "")

    def visitScalarFuncTestGroup(
        self, ctx: FuncTestCaseParser.ScalarFuncTestGroupContext
    ):
        group = self.visitTestGroupDescription(ctx.testGroupDescription())
        test_cases = []
        for test_case in ctx.testCase():
            testcase = self.visitTestCase(test_case)
            testcase.group = group
            test_cases.append(testcase)
        return group, test_cases

    def visitAggregateFuncTestGroup(
        self, ctx: FuncTestCaseParser.AggregateFuncTestGroupContext
    ):
        group = self.visitTestGroupDescription(ctx.testGroupDescription())
        test_cases = []
        for test_case in ctx.aggFuncTestCase():
            testcase = self.visitAggFuncTestCase(test_case)
            testcase.group = group
            test_cases.append(testcase)
        return group, test_cases

    def visitTestCase(self, ctx: FuncTestCaseParser.TestCaseContext):
        # TODO Implement this method
        args = self.visitArguments(ctx.arguments())
        result = self.visitResult(ctx.result())
        options = dict()
        if ctx.funcOptions() is not None:
            options = self.visitFuncOptions(ctx.funcOptions())
        return TestCase(
            func_name=ctx.identifier().getText(),
            base_uri="",
            group=None,
            options=options,
            rows=None,
            args=args,
            result=result,
            comment="",
        )

    def visitAggFuncTestCase(self, ctx: FuncTestCaseParser.AggFuncTestCaseContext):
        testcase = self.visit(ctx.aggFuncCall())
        testcase.result = self.visitResult(ctx.result())
        if ctx.funcOptions() is not None:
            testcase.options = self.visitFuncOptions(ctx.funcOptions())
        return testcase

    def visitSingleArgAggregateFuncCall(
        self, ctx: FuncTestCaseParser.SingleArgAggregateFuncCallContext
    ):
        arg = self.visitDataColumn(ctx.dataColumn())
        return TestCase(
            func_name=ctx.identifier().getText(),
            base_uri="",
            group=None,
            options=dict(),
            rows=None,
            args=[arg],
            result=SubstraitError("uninitialized"),
            comment="",
        )

    def visitCompactAggregateFuncCall(
        self, ctx: FuncTestCaseParser.CompactAggregateFuncCallContext
    ):
        rows = self.visitTableRows(ctx.tableRows())
        args = []
        if ctx.aggregateFuncArgs() is not None:
            args = self.visitAggregateFuncArgs(ctx.aggregateFuncArgs())
        return TestCase(
            func_name=ctx.identifier().getText(),
            base_uri="",
            group=None,
            options=dict(),
            rows=rows,
            args=args,
            result=SubstraitError("uninitialized"),
            comment="",
        )

    def visitMultiArgAggregateFuncCall(
        self, ctx: FuncTestCaseParser.MultiArgAggregateFuncCallContext
    ):
        table_name, column_types, rows = self.visitTableData(ctx.tableData())
        args = []
        if ctx.qualifiedAggregateFuncArgs() is not None:
            args = self.visitQualifiedAggregateFuncArgs(
                ctx.qualifiedAggregateFuncArgs()
            )
        for arg in args:
            if arg.scalar_value is None:
                if arg.table_name != table_name:
                    raise ParseError(
                        "Table name in argument does not match the table name in the function call"
                    )
                column_index = int(arg.column_name[3:])
                arg.column_type = column_types[column_index]

        return TestCase(
            func_name=ctx.identifier().getText(),
            base_uri="",
            group=None,
            options=dict(),
            rows=rows,
            args=args,
            result=SubstraitError("uninitialized"),
            comment="",
        )

    def visitAggregateFuncArgs(self, ctx: FuncTestCaseParser.AggregateFuncArgsContext):
        args = []
        for arg in ctx.aggregateFuncArg():
            args.append(self.visitAggregateFuncArg(arg))
        return args

    def visitAggregateFuncArg(self, ctx: FuncTestCaseParser.AggregateFuncArgContext):
        if ctx.argument() is not None:
            return AggregateArgument("", "", "", self.visitArgument(ctx.argument()))
        data_type = self.visitDataType(ctx.dataType())
        return AggregateArgument(
            ctx.ColumnName().getText(), data_type, "", scalar_value=None
        )

    def visitQualifiedAggregateFuncArgs(
        self, ctx: FuncTestCaseParser.QualifiedAggregateFuncArgsContext
    ):
        args = []
        for arg in ctx.qualifiedAggregateFuncArg():
            args.append(self.visitQualifiedAggregateFuncArg(arg))
        return args

    def visitQualifiedAggregateFuncArg(
        self, ctx: FuncTestCaseParser.QualifiedAggregateFuncArgContext
    ):
        if ctx.argument() is not None:
            return AggregateArgument("", "", "", self.visitArgument(ctx.argument()))
        table_name = ctx.Identifier().getText()
        return AggregateArgument(
            ctx.ColumnName().getText(), "", table_name, scalar_value=None
        )

    def visitTableRows(self, ctx: FuncTestCaseParser.TableRowsContext):
        rows = []
        for row in ctx.columnValues():
            rows.append(self.visitColumnValues(row))
        return rows

    def visitTableData(self, ctx: FuncTestCaseParser.TableDataContext):
        table_name = ctx.Identifier().getText()
        rows = self.visitTableRows(ctx.tableRows())
        column_types = []
        for dataType in ctx.dataType():
            column_types.append(self.visitDataType(dataType))
        return table_name, column_types, rows

    def visitDataColumn(self, ctx: FuncTestCaseParser.DataColumnContext):
        column = self.visitColumnValues(ctx.columnValues())
        column_type = ctx.dataType().getText()
        return CaseLiteral(value=column, type=column_type)

    def visitColumnValues(self, ctx: FuncTestCaseParser.ColumnValuesContext):
        values = []
        type_str = ""
        for literal in ctx.literal():
            value, curr_type = self.visitLiteral(literal)
            if curr_type != "null":
                if type_str == "":
                    type_str = curr_type
                elif type_str != curr_type:
                    raise ParseError("All values in a column must have the same type")
            values.append(value)
        return values

    def visitLiteral(self, ctx: FuncTestCaseParser.LiteralContext):
        if ctx.numericLiteral() is not None:
            return self.visitNumericLiteral(ctx.numericLiteral()), "number"
        if ctx.StringLiteral() is not None:
            return ctx.getText(), "str"
        if ctx.BooleanLiteral() is not None:
            return ctx.getText(), "bool"
        if ctx.DateLiteral() is not None:
            return ctx.getText(), "date"
        if ctx.TimeLiteral() is not None:
            return ctx.getText(), "time"
        if ctx.TimestampLiteral() is not None:
            return ctx.getText(), "ts"
        if ctx.TimestampTzLiteral() is not None:
            return ctx.getText(), "tstz"
        if ctx.IntervalDayLiteral() is not None:
            return ctx.getText(), "iday"
        if ctx.IntervalYearLiteral() is not None:
            return ctx.getText(), "iyear"
        if ctx.NullLiteral() is not None:
            return ctx.getText(), "null"

    def visitFuncOptions(self, ctx: FuncTestCaseParser.FuncOptionsContext):
        options = {}
        for option in ctx.funcOption():
            key, value = self.visitFuncOption(option)
            options[key] = value
        return options

    def visitFuncOption(self, ctx: FuncTestCaseParser.FuncOptionContext):
        key = ctx.optionName().getText()
        value = ctx.optionValue().getText()
        return key, value

    def visitArguments(self, ctx: FuncTestCaseParser.ArgumentsContext):
        arguments = []
        for arg in ctx.argument():
            arguments.append(self.visitArgument(arg))
        return arguments

    def visitArgument(self, ctx: FuncTestCaseParser.ArgumentContext):
        if ctx.intArg() is not None:
            return self.visitIntArg(ctx.intArg())
        if ctx.floatArg() is not None:
            return self.visitFloatArg(ctx.floatArg())
        if ctx.booleanArg() is not None:
            return self.visitBooleanArg(ctx.booleanArg())
        if ctx.stringArg() is not None:
            return self.visitStringArg(ctx.stringArg())
        if ctx.varCharArg() is not None:
            return self.visitVarCharArg(ctx.varCharArg())
        if ctx.decimalArg() is not None:
            return self.visitDecimalArg(ctx.decimalArg())
        if ctx.dateArg() is not None:
            return self.visitDateArg(ctx.dateArg())
        if ctx.timeArg() is not None:
            return self.visitTimeArg(ctx.timeArg())
        if ctx.timestampArg() is not None:
            return self.visitTimestampArg(ctx.timestampArg())
        if ctx.timestampTzArg() is not None:
            return self.visitTimestampTzArg(ctx.timestampTzArg())
        if ctx.intervalDayArg() is not None:
            return self.visitIntervalDayArg(ctx.intervalDayArg())
        if ctx.intervalYearArg() is not None:
            return self.visitIntervalYearArg(ctx.intervalYearArg())
        if ctx.nullArg() is not None:
            return self.visitNullArg(ctx.nullArg())
        if ctx.listArg() is not None:
            return self.visitListArg(ctx.listArg())

        return CaseLiteral(value="unknown_value", type="unknown_type")

    def visitNumericLiteral(self, ctx: FuncTestCaseParser.NumericLiteralContext):
        if ctx.IntegerLiteral() is not None:
            return ctx.IntegerLiteral().getText()
        if ctx.DecimalLiteral() is not None:
            return ctx.DecimalLiteral().getText()
        return self.visitFloatLiteral(ctx.floatLiteral())

    def visitFloatLiteral(self, ctx: FuncTestCaseParser.FloatLiteralContext):
        if ctx.FloatLiteral() is not None:
            return ctx.FloatLiteral().getText()
        return ctx.NaN().getText()

    def visitNullArg(self, ctx: FuncTestCaseParser.NullArgContext):
        datatype = ctx.dataType().getText()
        return CaseLiteral(value=None, type=datatype)

    def visitIntArg(self, ctx: FuncTestCaseParser.IntArgContext):
        type_str = "i8"
        if ctx.I16() is not None:
            type_str = "i16"
        elif ctx.I32() is not None:
            type_str = "i32"
        elif ctx.I64() is not None:
            type_str = "i64"
        return CaseLiteral(value=ctx.IntegerLiteral().getText(), type=type_str)

    def visitFloatArg(self, ctx: FuncTestCaseParser.FloatArgContext):
        # TODO add checks on number of decimal places
        type_str = "fp32"
        if ctx.FP64() is not None:
            type_str = "fp64"
        return CaseLiteral(
            value=self.visitNumericLiteral(ctx.numericLiteral()), type=type_str
        )

    def visitBooleanArg(self, ctx: FuncTestCaseParser.BooleanArgContext):
        return CaseLiteral(value=ctx.BooleanLiteral().getText(), type="bool")

    def visitStringArg(self, ctx: FuncTestCaseParser.StringArgContext):
        return CaseLiteral(value=ctx.StringLiteral().getText(), type="str")

    def visitVarCharArg(self, ctx: FuncTestCaseParser.VarCharArgContext):
        return CaseLiteral(
            value=ctx.StringLiteral().getText(),
            type=ctx.varCharType().getText().lower(),
        )

    def visitDecimalArg(self, ctx: FuncTestCaseParser.DecimalArgContext):
        return CaseLiteral(
            value=self.visitNumericLiteral(ctx.numericLiteral()),
            type=ctx.decimalType().getText().lower(),
        )

    def visitDateArg(self, ctx: FuncTestCaseParser.DateArgContext):
        return CaseLiteral(value=ctx.DateLiteral().getText().strip("'"), type="date")

    def visitTimeArg(self, ctx: FuncTestCaseParser.TimeArgContext):
        return CaseLiteral(value=ctx.TimeLiteral().getText().strip("'"), type="time")

    def visitTimestampArg(self, ctx: FuncTestCaseParser.TimestampArgContext):
        return CaseLiteral(value=ctx.TimestampLiteral().getText().strip("'"), type="ts")

    def visitTimestampTzArg(self, ctx: FuncTestCaseParser.TimestampTzArgContext):
        return CaseLiteral(
            value=ctx.TimestampTzLiteral().getText().strip("'"), type="tstz"
        )

    def visitIntervalDayArg(self, ctx: FuncTestCaseParser.IntervalDayArgContext):
        return CaseLiteral(
            value=ctx.IntervalDayLiteral().getText().strip("'"), type="iday"
        )

    def visitIntervalYearArg(self, ctx: FuncTestCaseParser.IntervalYearArgContext):
        return CaseLiteral(
            value=ctx.IntervalYearLiteral().getText().strip("'"), type="iyear"
        )

    def visitListArg(self, ctx: FuncTestCaseParser.ListArgContext):
        return CaseLiteral(
            value=self.visitLiteralList(ctx.literalList()),
            type=ctx.listType().getText(),
        )

    def visitLiteralList(self, ctx: FuncTestCaseParser.LiteralListContext):
        values = []
        for literal in ctx.literal():
            value, _ = self.visitLiteral(literal)
            values.append(value)
        return values

    def visitResult(self, ctx: FuncTestCaseParser.ResultContext):
        if ctx.argument() is not None:
            return self.visitArgument(ctx.argument())
        return self.visitSubstraitError(ctx.substraitError())

    def visitSubstraitError(self, ctx: FuncTestCaseParser.SubstraitErrorContext):
        if ctx.ErrorResult() is not None:
            return SubstraitError("error")
        if ctx.UndefineResult() is not None:
            return SubstraitError("undefined")
        return SubstraitError("unknown_error")


class ParseError(Exception):
    def __init__(self, message="Parsing error occurred"):
        self.message = message
        super().__init__(self.message)
