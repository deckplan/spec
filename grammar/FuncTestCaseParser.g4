parser grammar FuncTestCaseParser;

options {
    caseInsensitive = true;
    tokenVocab=SubstraitLexer;
    tokenVocab=FuncTestCaseLexer;
}

doc
    : header testGroup+ EOF
    ;

header
    : version include
    ;

version
    : TripleHash (SubstraitScalarTest | SubstraitAggregateTest) Colon FormatVersion
    ;

include
    : TripleHash SubstraitInclude Colon StringLiteral (Comma StringLiteral)*
    ;

testGroupDescription
    : DescriptionLine
    ;

testCase
    : functionName=identifier OParen arguments CParen ( OBracket funcOptions CBracket )? Eq result
    ;

testGroup
    : testGroupDescription? (testCase)+                          #scalarFuncTestGroup
    | testGroupDescription? (aggFuncTestCase)+                   #aggregateFuncTestGroup
    ;

arguments
    : argument (Comma argument)*
    ;

result
    : argument
    | substraitError
    ;

argument
    : nullArg
    | intArg
    | floatArg
    | booleanArg
    | stringArg
    | decimalArg
    | dateArg
    | timeArg
    | timestampArg
    | timestampTzArg
    | intervalYearArg
    | intervalDayArg
    | fixedCharArg
    | varCharArg
    | fixedBinaryArg
    | precisionTimestampArg
    | precisionTimestampTZArg
    | listArg
    ;

aggFuncTestCase
    : aggFuncCall ( OBracket funcOptions CBracket )? Eq result
    ;

aggFuncCall
    : tableData funcName=identifier OParen qualifiedAggregateFuncArgs? CParen           #multiArgAggregateFuncCall
    | tableRows functName=identifier OParen aggregateFuncArgs? CParen                   #compactAggregateFuncCall
    | functName=identifier OParen dataColumn CParen                                     #singleArgAggregateFuncCall
    ;

tableData
    : Define tableName=Identifier OParen dataType (Comma dataType)* CParen Eq tableRows
    ;

tableRows
    : OParen (columnValues (Comma columnValues)*)? CParen
    ;

dataColumn
    : columnValues DoubleColon dataType
    ;

columnValues
    : OParen (literal (Comma literal)*)? CParen
    ;

literal
    : NullLiteral
    | numericLiteral
    | BooleanLiteral
    | StringLiteral
    | DateLiteral
    | TimeLiteral
    | TimestampLiteral
    | TimestampTzLiteral
    | IntervalYearLiteral
    | IntervalDayLiteral
    ;

qualifiedAggregateFuncArgs
    : qualifiedAggregateFuncArg (Comma qualifiedAggregateFuncArg)*
    ;

aggregateFuncArgs
    : aggregateFuncArg (Comma aggregateFuncArg)*
    ;

qualifiedAggregateFuncArg
    : tableName=Identifier Dot ColumnName
    | argument
    ;

aggregateFuncArg
    : ColumnName DoubleColon dataType
    | argument
    ;

numericLiteral
    : DecimalLiteral | IntegerLiteral | floatLiteral
    ;

floatLiteral
    : FloatLiteral | NaN
    ;

nullArg: NullLiteral DoubleColon dataType;

intArg: IntegerLiteral DoubleColon (I8 | I16 | I32 | I64);

floatArg: numericLiteral DoubleColon (FP32 | FP64);

decimalArg
    : numericLiteral DoubleColon decimalType
    ;

booleanArg
    : BooleanLiteral DoubleColon booleanType
    ;

stringArg
    : StringLiteral DoubleColon stringType
    ;

dateArg
    : DateLiteral DoubleColon Date
    ;

timeArg
    : TimeLiteral DoubleColon Time
    ;

timestampArg
    : TimestampLiteral DoubleColon timestampType
    ;

timestampTzArg
    : TimestampTzLiteral DoubleColon timestampTZType
    ;

intervalYearArg
    : IntervalYearLiteral DoubleColon intervalYearType
    ;

intervalDayArg
    : IntervalDayLiteral DoubleColon intervalDayType
    ;

fixedCharArg
    : StringLiteral DoubleColon fixedCharType
    ;

varCharArg
    : StringLiteral DoubleColon varCharType
    ;

fixedBinaryArg
    : StringLiteral DoubleColon fixedBinaryType
    ;

precisionTimestampArg
    : TimestampLiteral DoubleColon precisionTimestampType
    ;

precisionTimestampTZArg
    : TimestampTzLiteral DoubleColon precisionTimestampTZType
    ;

listArg
    : literalList DoubleColon listType
    ;

literalList
    : OBracket (literal (Comma literal)*)? CBracket
    ;

dataType
    : scalarType
    | parameterizedType
    ;

scalarType
  : booleanType             #boolean
  | I8                      #i8
  | I16                     #i16
  | I32                     #i32
  | I64                     #i64
  | FP32                    #fp32
  | FP64                    #fp64
  | stringType              #string
  | binaryType              #binary
  | timestampType           #timestamp
  | timestampTZType         #timestampTz
  | Date                    #date
  | Time                    #time
  | intervalYearType        #intervalYear
  | UUID                    #uuid
  | UserDefined Identifier  #userDefined
  ;

booleanType
    : (Bool | Boolean)
    ;

stringType
    : (Str | String)
    ;

binaryType
    : (Binary | VBin)
    ;

timestampType
    : (Ts | Timestamp)
    ;

timestampTZType
    : (TsTZ | Timestamp_TZ)
    ;

intervalYearType
    : (IYear | Interval_Year)
    ;

intervalDayType
    : (IDay | Interval_Day) isnull=QMark? (OAngleBracket len=numericParameter CAngleBracket)?
    ;

fixedCharType
    : (FChar | FixedChar) isnull=QMark? OAngleBracket len=numericParameter CAngleBracket
    ;

varCharType
    : (VChar | VarChar) isnull=QMark? OAngleBracket len=numericParameter CAngleBracket
    ;

fixedBinaryType
    : (FBin | FixedBinary) isnull=QMark? OAngleBracket len=numericParameter CAngleBracket
    ;

decimalType
    : (Dec | Decimal) isnull=QMark?
        (OAngleBracket precision=numericParameter Comma scale=numericParameter CAngleBracket)?
    ;

precisionTimestampType
    : (PTs | Precision_Timestamp) isnull=QMark? OAngleBracket precision=numericParameter CAngleBracket
    ;

precisionTimestampTZType
    : (PTsTZ | Precision_Timestamp_TZ) isnull=QMark? OAngleBracket precision=numericParameter CAngleBracket
    ;

listType
    : List isnull=QMark? OAngleBracket elemType=dataType CAngleBracket #list
    ;

parameterizedType
    : fixedCharType
    | varCharType
    | fixedBinaryType
    | decimalType
    | intervalDayType
    | precisionTimestampType
    | precisionTimestampTZType
// TODO implement the rest of the parameterized types
//  | Struct isnull='?'? Lt expr (Comma expr)* Gt #struct
//  | NStruct isnull='?'? Lt Identifier expr (Comma Identifier expr)* Gt #nStruct
//  | Map isnull='?'? Lt key=expr Comma value=expr Gt #map
  ;

numericParameter
  : IntegerLiteral #integerLiteral
  ;

substraitError
    : ErrorResult | UndefineResult
    ;

funcOption
    : optionName Colon optionValue
    ;

optionName
    : Overflow | Rounding | NullHandling | SpacesOnly
    | Identifier
    ;

optionValue
    : Error | Saturate | Silent | TieToEven | NaN | Truncate | AcceptNulls | IgnoreNulls
    | BooleanLiteral
    | NullLiteral
    | Identifier
    ;

funcOptions
    : funcOption (Comma funcOption)*
    ;

nonReserved //  IMPORTANT: this rule must only contain tokens
    : And | Or | Truncate
    ;

identifier
    : nonReserved
    | Identifier
    ;
