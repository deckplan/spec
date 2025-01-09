# Generated from FuncTestCaseParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FuncTestCaseParser import FuncTestCaseParser
else:
    from FuncTestCaseParser import FuncTestCaseParser

# This class defines a complete listener for a parse tree produced by FuncTestCaseParser.
class FuncTestCaseParserListener(ParseTreeListener):

    # Enter a parse tree produced by FuncTestCaseParser#doc.
    def enterDoc(self, ctx:FuncTestCaseParser.DocContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#doc.
    def exitDoc(self, ctx:FuncTestCaseParser.DocContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#header.
    def enterHeader(self, ctx:FuncTestCaseParser.HeaderContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#header.
    def exitHeader(self, ctx:FuncTestCaseParser.HeaderContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#version.
    def enterVersion(self, ctx:FuncTestCaseParser.VersionContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#version.
    def exitVersion(self, ctx:FuncTestCaseParser.VersionContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#include.
    def enterInclude(self, ctx:FuncTestCaseParser.IncludeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#include.
    def exitInclude(self, ctx:FuncTestCaseParser.IncludeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#testGroupDescription.
    def enterTestGroupDescription(self, ctx:FuncTestCaseParser.TestGroupDescriptionContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#testGroupDescription.
    def exitTestGroupDescription(self, ctx:FuncTestCaseParser.TestGroupDescriptionContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#testCase.
    def enterTestCase(self, ctx:FuncTestCaseParser.TestCaseContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#testCase.
    def exitTestCase(self, ctx:FuncTestCaseParser.TestCaseContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#scalarFuncTestGroup.
    def enterScalarFuncTestGroup(self, ctx:FuncTestCaseParser.ScalarFuncTestGroupContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#scalarFuncTestGroup.
    def exitScalarFuncTestGroup(self, ctx:FuncTestCaseParser.ScalarFuncTestGroupContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#aggregateFuncTestGroup.
    def enterAggregateFuncTestGroup(self, ctx:FuncTestCaseParser.AggregateFuncTestGroupContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#aggregateFuncTestGroup.
    def exitAggregateFuncTestGroup(self, ctx:FuncTestCaseParser.AggregateFuncTestGroupContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#arguments.
    def enterArguments(self, ctx:FuncTestCaseParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#arguments.
    def exitArguments(self, ctx:FuncTestCaseParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#result.
    def enterResult(self, ctx:FuncTestCaseParser.ResultContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#result.
    def exitResult(self, ctx:FuncTestCaseParser.ResultContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#argument.
    def enterArgument(self, ctx:FuncTestCaseParser.ArgumentContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#argument.
    def exitArgument(self, ctx:FuncTestCaseParser.ArgumentContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#aggFuncTestCase.
    def enterAggFuncTestCase(self, ctx:FuncTestCaseParser.AggFuncTestCaseContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#aggFuncTestCase.
    def exitAggFuncTestCase(self, ctx:FuncTestCaseParser.AggFuncTestCaseContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#multiArgAggregateFuncCall.
    def enterMultiArgAggregateFuncCall(self, ctx:FuncTestCaseParser.MultiArgAggregateFuncCallContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#multiArgAggregateFuncCall.
    def exitMultiArgAggregateFuncCall(self, ctx:FuncTestCaseParser.MultiArgAggregateFuncCallContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#compactAggregateFuncCall.
    def enterCompactAggregateFuncCall(self, ctx:FuncTestCaseParser.CompactAggregateFuncCallContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#compactAggregateFuncCall.
    def exitCompactAggregateFuncCall(self, ctx:FuncTestCaseParser.CompactAggregateFuncCallContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#singleArgAggregateFuncCall.
    def enterSingleArgAggregateFuncCall(self, ctx:FuncTestCaseParser.SingleArgAggregateFuncCallContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#singleArgAggregateFuncCall.
    def exitSingleArgAggregateFuncCall(self, ctx:FuncTestCaseParser.SingleArgAggregateFuncCallContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#tableData.
    def enterTableData(self, ctx:FuncTestCaseParser.TableDataContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#tableData.
    def exitTableData(self, ctx:FuncTestCaseParser.TableDataContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#tableRows.
    def enterTableRows(self, ctx:FuncTestCaseParser.TableRowsContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#tableRows.
    def exitTableRows(self, ctx:FuncTestCaseParser.TableRowsContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#dataColumn.
    def enterDataColumn(self, ctx:FuncTestCaseParser.DataColumnContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#dataColumn.
    def exitDataColumn(self, ctx:FuncTestCaseParser.DataColumnContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#columnValues.
    def enterColumnValues(self, ctx:FuncTestCaseParser.ColumnValuesContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#columnValues.
    def exitColumnValues(self, ctx:FuncTestCaseParser.ColumnValuesContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#literal.
    def enterLiteral(self, ctx:FuncTestCaseParser.LiteralContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#literal.
    def exitLiteral(self, ctx:FuncTestCaseParser.LiteralContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#qualifiedAggregateFuncArgs.
    def enterQualifiedAggregateFuncArgs(self, ctx:FuncTestCaseParser.QualifiedAggregateFuncArgsContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#qualifiedAggregateFuncArgs.
    def exitQualifiedAggregateFuncArgs(self, ctx:FuncTestCaseParser.QualifiedAggregateFuncArgsContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#aggregateFuncArgs.
    def enterAggregateFuncArgs(self, ctx:FuncTestCaseParser.AggregateFuncArgsContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#aggregateFuncArgs.
    def exitAggregateFuncArgs(self, ctx:FuncTestCaseParser.AggregateFuncArgsContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#qualifiedAggregateFuncArg.
    def enterQualifiedAggregateFuncArg(self, ctx:FuncTestCaseParser.QualifiedAggregateFuncArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#qualifiedAggregateFuncArg.
    def exitQualifiedAggregateFuncArg(self, ctx:FuncTestCaseParser.QualifiedAggregateFuncArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#aggregateFuncArg.
    def enterAggregateFuncArg(self, ctx:FuncTestCaseParser.AggregateFuncArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#aggregateFuncArg.
    def exitAggregateFuncArg(self, ctx:FuncTestCaseParser.AggregateFuncArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#numericLiteral.
    def enterNumericLiteral(self, ctx:FuncTestCaseParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#numericLiteral.
    def exitNumericLiteral(self, ctx:FuncTestCaseParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#floatLiteral.
    def enterFloatLiteral(self, ctx:FuncTestCaseParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#floatLiteral.
    def exitFloatLiteral(self, ctx:FuncTestCaseParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#nullArg.
    def enterNullArg(self, ctx:FuncTestCaseParser.NullArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#nullArg.
    def exitNullArg(self, ctx:FuncTestCaseParser.NullArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#intArg.
    def enterIntArg(self, ctx:FuncTestCaseParser.IntArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#intArg.
    def exitIntArg(self, ctx:FuncTestCaseParser.IntArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#floatArg.
    def enterFloatArg(self, ctx:FuncTestCaseParser.FloatArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#floatArg.
    def exitFloatArg(self, ctx:FuncTestCaseParser.FloatArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#decimalArg.
    def enterDecimalArg(self, ctx:FuncTestCaseParser.DecimalArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#decimalArg.
    def exitDecimalArg(self, ctx:FuncTestCaseParser.DecimalArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#booleanArg.
    def enterBooleanArg(self, ctx:FuncTestCaseParser.BooleanArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#booleanArg.
    def exitBooleanArg(self, ctx:FuncTestCaseParser.BooleanArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#stringArg.
    def enterStringArg(self, ctx:FuncTestCaseParser.StringArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#stringArg.
    def exitStringArg(self, ctx:FuncTestCaseParser.StringArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#dateArg.
    def enterDateArg(self, ctx:FuncTestCaseParser.DateArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#dateArg.
    def exitDateArg(self, ctx:FuncTestCaseParser.DateArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#timeArg.
    def enterTimeArg(self, ctx:FuncTestCaseParser.TimeArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#timeArg.
    def exitTimeArg(self, ctx:FuncTestCaseParser.TimeArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#timestampArg.
    def enterTimestampArg(self, ctx:FuncTestCaseParser.TimestampArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#timestampArg.
    def exitTimestampArg(self, ctx:FuncTestCaseParser.TimestampArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#timestampTzArg.
    def enterTimestampTzArg(self, ctx:FuncTestCaseParser.TimestampTzArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#timestampTzArg.
    def exitTimestampTzArg(self, ctx:FuncTestCaseParser.TimestampTzArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#intervalYearArg.
    def enterIntervalYearArg(self, ctx:FuncTestCaseParser.IntervalYearArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#intervalYearArg.
    def exitIntervalYearArg(self, ctx:FuncTestCaseParser.IntervalYearArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#intervalDayArg.
    def enterIntervalDayArg(self, ctx:FuncTestCaseParser.IntervalDayArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#intervalDayArg.
    def exitIntervalDayArg(self, ctx:FuncTestCaseParser.IntervalDayArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#fixedCharArg.
    def enterFixedCharArg(self, ctx:FuncTestCaseParser.FixedCharArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#fixedCharArg.
    def exitFixedCharArg(self, ctx:FuncTestCaseParser.FixedCharArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#varCharArg.
    def enterVarCharArg(self, ctx:FuncTestCaseParser.VarCharArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#varCharArg.
    def exitVarCharArg(self, ctx:FuncTestCaseParser.VarCharArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#fixedBinaryArg.
    def enterFixedBinaryArg(self, ctx:FuncTestCaseParser.FixedBinaryArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#fixedBinaryArg.
    def exitFixedBinaryArg(self, ctx:FuncTestCaseParser.FixedBinaryArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#precisionTimestampArg.
    def enterPrecisionTimestampArg(self, ctx:FuncTestCaseParser.PrecisionTimestampArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#precisionTimestampArg.
    def exitPrecisionTimestampArg(self, ctx:FuncTestCaseParser.PrecisionTimestampArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#precisionTimestampTZArg.
    def enterPrecisionTimestampTZArg(self, ctx:FuncTestCaseParser.PrecisionTimestampTZArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#precisionTimestampTZArg.
    def exitPrecisionTimestampTZArg(self, ctx:FuncTestCaseParser.PrecisionTimestampTZArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#listArg.
    def enterListArg(self, ctx:FuncTestCaseParser.ListArgContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#listArg.
    def exitListArg(self, ctx:FuncTestCaseParser.ListArgContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#literalList.
    def enterLiteralList(self, ctx:FuncTestCaseParser.LiteralListContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#literalList.
    def exitLiteralList(self, ctx:FuncTestCaseParser.LiteralListContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#dataType.
    def enterDataType(self, ctx:FuncTestCaseParser.DataTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#dataType.
    def exitDataType(self, ctx:FuncTestCaseParser.DataTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#boolean.
    def enterBoolean(self, ctx:FuncTestCaseParser.BooleanContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#boolean.
    def exitBoolean(self, ctx:FuncTestCaseParser.BooleanContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#i8.
    def enterI8(self, ctx:FuncTestCaseParser.I8Context):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#i8.
    def exitI8(self, ctx:FuncTestCaseParser.I8Context):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#i16.
    def enterI16(self, ctx:FuncTestCaseParser.I16Context):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#i16.
    def exitI16(self, ctx:FuncTestCaseParser.I16Context):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#i32.
    def enterI32(self, ctx:FuncTestCaseParser.I32Context):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#i32.
    def exitI32(self, ctx:FuncTestCaseParser.I32Context):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#i64.
    def enterI64(self, ctx:FuncTestCaseParser.I64Context):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#i64.
    def exitI64(self, ctx:FuncTestCaseParser.I64Context):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#fp32.
    def enterFp32(self, ctx:FuncTestCaseParser.Fp32Context):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#fp32.
    def exitFp32(self, ctx:FuncTestCaseParser.Fp32Context):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#fp64.
    def enterFp64(self, ctx:FuncTestCaseParser.Fp64Context):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#fp64.
    def exitFp64(self, ctx:FuncTestCaseParser.Fp64Context):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#string.
    def enterString(self, ctx:FuncTestCaseParser.StringContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#string.
    def exitString(self, ctx:FuncTestCaseParser.StringContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#binary.
    def enterBinary(self, ctx:FuncTestCaseParser.BinaryContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#binary.
    def exitBinary(self, ctx:FuncTestCaseParser.BinaryContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#timestamp.
    def enterTimestamp(self, ctx:FuncTestCaseParser.TimestampContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#timestamp.
    def exitTimestamp(self, ctx:FuncTestCaseParser.TimestampContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#timestampTz.
    def enterTimestampTz(self, ctx:FuncTestCaseParser.TimestampTzContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#timestampTz.
    def exitTimestampTz(self, ctx:FuncTestCaseParser.TimestampTzContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#date.
    def enterDate(self, ctx:FuncTestCaseParser.DateContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#date.
    def exitDate(self, ctx:FuncTestCaseParser.DateContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#time.
    def enterTime(self, ctx:FuncTestCaseParser.TimeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#time.
    def exitTime(self, ctx:FuncTestCaseParser.TimeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#intervalYear.
    def enterIntervalYear(self, ctx:FuncTestCaseParser.IntervalYearContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#intervalYear.
    def exitIntervalYear(self, ctx:FuncTestCaseParser.IntervalYearContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#uuid.
    def enterUuid(self, ctx:FuncTestCaseParser.UuidContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#uuid.
    def exitUuid(self, ctx:FuncTestCaseParser.UuidContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#userDefined.
    def enterUserDefined(self, ctx:FuncTestCaseParser.UserDefinedContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#userDefined.
    def exitUserDefined(self, ctx:FuncTestCaseParser.UserDefinedContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#booleanType.
    def enterBooleanType(self, ctx:FuncTestCaseParser.BooleanTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#booleanType.
    def exitBooleanType(self, ctx:FuncTestCaseParser.BooleanTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#stringType.
    def enterStringType(self, ctx:FuncTestCaseParser.StringTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#stringType.
    def exitStringType(self, ctx:FuncTestCaseParser.StringTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#binaryType.
    def enterBinaryType(self, ctx:FuncTestCaseParser.BinaryTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#binaryType.
    def exitBinaryType(self, ctx:FuncTestCaseParser.BinaryTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#timestampType.
    def enterTimestampType(self, ctx:FuncTestCaseParser.TimestampTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#timestampType.
    def exitTimestampType(self, ctx:FuncTestCaseParser.TimestampTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#timestampTZType.
    def enterTimestampTZType(self, ctx:FuncTestCaseParser.TimestampTZTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#timestampTZType.
    def exitTimestampTZType(self, ctx:FuncTestCaseParser.TimestampTZTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#intervalYearType.
    def enterIntervalYearType(self, ctx:FuncTestCaseParser.IntervalYearTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#intervalYearType.
    def exitIntervalYearType(self, ctx:FuncTestCaseParser.IntervalYearTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#intervalDayType.
    def enterIntervalDayType(self, ctx:FuncTestCaseParser.IntervalDayTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#intervalDayType.
    def exitIntervalDayType(self, ctx:FuncTestCaseParser.IntervalDayTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#fixedCharType.
    def enterFixedCharType(self, ctx:FuncTestCaseParser.FixedCharTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#fixedCharType.
    def exitFixedCharType(self, ctx:FuncTestCaseParser.FixedCharTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#varCharType.
    def enterVarCharType(self, ctx:FuncTestCaseParser.VarCharTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#varCharType.
    def exitVarCharType(self, ctx:FuncTestCaseParser.VarCharTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#fixedBinaryType.
    def enterFixedBinaryType(self, ctx:FuncTestCaseParser.FixedBinaryTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#fixedBinaryType.
    def exitFixedBinaryType(self, ctx:FuncTestCaseParser.FixedBinaryTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#decimalType.
    def enterDecimalType(self, ctx:FuncTestCaseParser.DecimalTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#decimalType.
    def exitDecimalType(self, ctx:FuncTestCaseParser.DecimalTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#precisionTimestampType.
    def enterPrecisionTimestampType(self, ctx:FuncTestCaseParser.PrecisionTimestampTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#precisionTimestampType.
    def exitPrecisionTimestampType(self, ctx:FuncTestCaseParser.PrecisionTimestampTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#precisionTimestampTZType.
    def enterPrecisionTimestampTZType(self, ctx:FuncTestCaseParser.PrecisionTimestampTZTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#precisionTimestampTZType.
    def exitPrecisionTimestampTZType(self, ctx:FuncTestCaseParser.PrecisionTimestampTZTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#list.
    def enterList(self, ctx:FuncTestCaseParser.ListContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#list.
    def exitList(self, ctx:FuncTestCaseParser.ListContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#parameterizedType.
    def enterParameterizedType(self, ctx:FuncTestCaseParser.ParameterizedTypeContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#parameterizedType.
    def exitParameterizedType(self, ctx:FuncTestCaseParser.ParameterizedTypeContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:FuncTestCaseParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:FuncTestCaseParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#substraitError.
    def enterSubstraitError(self, ctx:FuncTestCaseParser.SubstraitErrorContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#substraitError.
    def exitSubstraitError(self, ctx:FuncTestCaseParser.SubstraitErrorContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#funcOption.
    def enterFuncOption(self, ctx:FuncTestCaseParser.FuncOptionContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#funcOption.
    def exitFuncOption(self, ctx:FuncTestCaseParser.FuncOptionContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#optionName.
    def enterOptionName(self, ctx:FuncTestCaseParser.OptionNameContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#optionName.
    def exitOptionName(self, ctx:FuncTestCaseParser.OptionNameContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#optionValue.
    def enterOptionValue(self, ctx:FuncTestCaseParser.OptionValueContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#optionValue.
    def exitOptionValue(self, ctx:FuncTestCaseParser.OptionValueContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#funcOptions.
    def enterFuncOptions(self, ctx:FuncTestCaseParser.FuncOptionsContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#funcOptions.
    def exitFuncOptions(self, ctx:FuncTestCaseParser.FuncOptionsContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#nonReserved.
    def enterNonReserved(self, ctx:FuncTestCaseParser.NonReservedContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#nonReserved.
    def exitNonReserved(self, ctx:FuncTestCaseParser.NonReservedContext):
        pass


    # Enter a parse tree produced by FuncTestCaseParser#identifier.
    def enterIdentifier(self, ctx:FuncTestCaseParser.IdentifierContext):
        pass

    # Exit a parse tree produced by FuncTestCaseParser#identifier.
    def exitIdentifier(self, ctx:FuncTestCaseParser.IdentifierContext):
        pass



del FuncTestCaseParser