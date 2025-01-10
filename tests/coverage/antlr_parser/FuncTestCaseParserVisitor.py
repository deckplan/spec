# Generated from FuncTestCaseParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FuncTestCaseParser import FuncTestCaseParser
else:
    from FuncTestCaseParser import FuncTestCaseParser

# This class defines a complete generic visitor for a parse tree produced by FuncTestCaseParser.

class FuncTestCaseParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FuncTestCaseParser#doc.
    def visitDoc(self, ctx:FuncTestCaseParser.DocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#header.
    def visitHeader(self, ctx:FuncTestCaseParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#version.
    def visitVersion(self, ctx:FuncTestCaseParser.VersionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#include.
    def visitInclude(self, ctx:FuncTestCaseParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#testGroupDescription.
    def visitTestGroupDescription(self, ctx:FuncTestCaseParser.TestGroupDescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#testCase.
    def visitTestCase(self, ctx:FuncTestCaseParser.TestCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#scalarFuncTestGroup.
    def visitScalarFuncTestGroup(self, ctx:FuncTestCaseParser.ScalarFuncTestGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#aggregateFuncTestGroup.
    def visitAggregateFuncTestGroup(self, ctx:FuncTestCaseParser.AggregateFuncTestGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#arguments.
    def visitArguments(self, ctx:FuncTestCaseParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#result.
    def visitResult(self, ctx:FuncTestCaseParser.ResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#argument.
    def visitArgument(self, ctx:FuncTestCaseParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#aggFuncTestCase.
    def visitAggFuncTestCase(self, ctx:FuncTestCaseParser.AggFuncTestCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#multiArgAggregateFuncCall.
    def visitMultiArgAggregateFuncCall(self, ctx:FuncTestCaseParser.MultiArgAggregateFuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#compactAggregateFuncCall.
    def visitCompactAggregateFuncCall(self, ctx:FuncTestCaseParser.CompactAggregateFuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#singleArgAggregateFuncCall.
    def visitSingleArgAggregateFuncCall(self, ctx:FuncTestCaseParser.SingleArgAggregateFuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#tableData.
    def visitTableData(self, ctx:FuncTestCaseParser.TableDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#tableRows.
    def visitTableRows(self, ctx:FuncTestCaseParser.TableRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#dataColumn.
    def visitDataColumn(self, ctx:FuncTestCaseParser.DataColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#columnValues.
    def visitColumnValues(self, ctx:FuncTestCaseParser.ColumnValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#literal.
    def visitLiteral(self, ctx:FuncTestCaseParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#qualifiedAggregateFuncArgs.
    def visitQualifiedAggregateFuncArgs(self, ctx:FuncTestCaseParser.QualifiedAggregateFuncArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#aggregateFuncArgs.
    def visitAggregateFuncArgs(self, ctx:FuncTestCaseParser.AggregateFuncArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#qualifiedAggregateFuncArg.
    def visitQualifiedAggregateFuncArg(self, ctx:FuncTestCaseParser.QualifiedAggregateFuncArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#aggregateFuncArg.
    def visitAggregateFuncArg(self, ctx:FuncTestCaseParser.AggregateFuncArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#numericLiteral.
    def visitNumericLiteral(self, ctx:FuncTestCaseParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#floatLiteral.
    def visitFloatLiteral(self, ctx:FuncTestCaseParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#nullArg.
    def visitNullArg(self, ctx:FuncTestCaseParser.NullArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#intArg.
    def visitIntArg(self, ctx:FuncTestCaseParser.IntArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#floatArg.
    def visitFloatArg(self, ctx:FuncTestCaseParser.FloatArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#decimalArg.
    def visitDecimalArg(self, ctx:FuncTestCaseParser.DecimalArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#booleanArg.
    def visitBooleanArg(self, ctx:FuncTestCaseParser.BooleanArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#stringArg.
    def visitStringArg(self, ctx:FuncTestCaseParser.StringArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#dateArg.
    def visitDateArg(self, ctx:FuncTestCaseParser.DateArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#timeArg.
    def visitTimeArg(self, ctx:FuncTestCaseParser.TimeArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#timestampArg.
    def visitTimestampArg(self, ctx:FuncTestCaseParser.TimestampArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#timestampTzArg.
    def visitTimestampTzArg(self, ctx:FuncTestCaseParser.TimestampTzArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#intervalYearArg.
    def visitIntervalYearArg(self, ctx:FuncTestCaseParser.IntervalYearArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#intervalDayArg.
    def visitIntervalDayArg(self, ctx:FuncTestCaseParser.IntervalDayArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#fixedCharArg.
    def visitFixedCharArg(self, ctx:FuncTestCaseParser.FixedCharArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#varCharArg.
    def visitVarCharArg(self, ctx:FuncTestCaseParser.VarCharArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#fixedBinaryArg.
    def visitFixedBinaryArg(self, ctx:FuncTestCaseParser.FixedBinaryArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#precisionTimestampArg.
    def visitPrecisionTimestampArg(self, ctx:FuncTestCaseParser.PrecisionTimestampArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#precisionTimestampTZArg.
    def visitPrecisionTimestampTZArg(self, ctx:FuncTestCaseParser.PrecisionTimestampTZArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#listArg.
    def visitListArg(self, ctx:FuncTestCaseParser.ListArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#literalList.
    def visitLiteralList(self, ctx:FuncTestCaseParser.LiteralListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#dataType.
    def visitDataType(self, ctx:FuncTestCaseParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#boolean.
    def visitBoolean(self, ctx:FuncTestCaseParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#i8.
    def visitI8(self, ctx:FuncTestCaseParser.I8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#i16.
    def visitI16(self, ctx:FuncTestCaseParser.I16Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#i32.
    def visitI32(self, ctx:FuncTestCaseParser.I32Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#i64.
    def visitI64(self, ctx:FuncTestCaseParser.I64Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#fp32.
    def visitFp32(self, ctx:FuncTestCaseParser.Fp32Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#fp64.
    def visitFp64(self, ctx:FuncTestCaseParser.Fp64Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#string.
    def visitString(self, ctx:FuncTestCaseParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#binary.
    def visitBinary(self, ctx:FuncTestCaseParser.BinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#timestamp.
    def visitTimestamp(self, ctx:FuncTestCaseParser.TimestampContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#timestampTz.
    def visitTimestampTz(self, ctx:FuncTestCaseParser.TimestampTzContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#date.
    def visitDate(self, ctx:FuncTestCaseParser.DateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#time.
    def visitTime(self, ctx:FuncTestCaseParser.TimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#intervalYear.
    def visitIntervalYear(self, ctx:FuncTestCaseParser.IntervalYearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#uuid.
    def visitUuid(self, ctx:FuncTestCaseParser.UuidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#userDefined.
    def visitUserDefined(self, ctx:FuncTestCaseParser.UserDefinedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#booleanType.
    def visitBooleanType(self, ctx:FuncTestCaseParser.BooleanTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#stringType.
    def visitStringType(self, ctx:FuncTestCaseParser.StringTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#binaryType.
    def visitBinaryType(self, ctx:FuncTestCaseParser.BinaryTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#timestampType.
    def visitTimestampType(self, ctx:FuncTestCaseParser.TimestampTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#timestampTZType.
    def visitTimestampTZType(self, ctx:FuncTestCaseParser.TimestampTZTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#intervalYearType.
    def visitIntervalYearType(self, ctx:FuncTestCaseParser.IntervalYearTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#intervalDayType.
    def visitIntervalDayType(self, ctx:FuncTestCaseParser.IntervalDayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#fixedCharType.
    def visitFixedCharType(self, ctx:FuncTestCaseParser.FixedCharTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#varCharType.
    def visitVarCharType(self, ctx:FuncTestCaseParser.VarCharTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#fixedBinaryType.
    def visitFixedBinaryType(self, ctx:FuncTestCaseParser.FixedBinaryTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#decimalType.
    def visitDecimalType(self, ctx:FuncTestCaseParser.DecimalTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#precisionTimestampType.
    def visitPrecisionTimestampType(self, ctx:FuncTestCaseParser.PrecisionTimestampTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#precisionTimestampTZType.
    def visitPrecisionTimestampTZType(self, ctx:FuncTestCaseParser.PrecisionTimestampTZTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#list.
    def visitList(self, ctx:FuncTestCaseParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#parameterizedType.
    def visitParameterizedType(self, ctx:FuncTestCaseParser.ParameterizedTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:FuncTestCaseParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#substraitError.
    def visitSubstraitError(self, ctx:FuncTestCaseParser.SubstraitErrorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#funcOption.
    def visitFuncOption(self, ctx:FuncTestCaseParser.FuncOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#optionName.
    def visitOptionName(self, ctx:FuncTestCaseParser.OptionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#optionValue.
    def visitOptionValue(self, ctx:FuncTestCaseParser.OptionValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#funcOptions.
    def visitFuncOptions(self, ctx:FuncTestCaseParser.FuncOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#nonReserved.
    def visitNonReserved(self, ctx:FuncTestCaseParser.NonReservedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FuncTestCaseParser#identifier.
    def visitIdentifier(self, ctx:FuncTestCaseParser.IdentifierContext):
        return self.visitChildren(ctx)



del FuncTestCaseParser