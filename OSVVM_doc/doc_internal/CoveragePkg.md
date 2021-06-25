# Package: CoveragePkg
## Constants
| Name                     | Type                                       | Value                                                                                                                      | Description                                                                        |
| ------------------------ | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| MIN_NUM_BINS             | integer                                    |  2**7                                                                                                                      | power of 2                                                                         |
| ALL_RANGE                | RangeArrayType                             |  (1=>(Integer'left, Integer'right))                                                                                        |                                                                                    |
| COV_COUNT                | integer                                    |  1                                                                                                                         | CovBinBaseType.action values. Note that coverage counting depends on these values  |
| COV_IGNORE               | integer                                    |  0                                                                                                                         |                                                                                    |
| COV_ILLEGAL              | integer                                    |  -1                                                                                                                        |                                                                                    |
| COV_OPT_INIT_PARM_DETECT | CovOptionsType                             |  work.OsvvmGlobalPkg.OPT_INIT_PARM_DETECT                                                                                  |                                                                                    |
| ALL_BIN                  | CovBinType                                 |  (0 => ( BinVal => ALL_RANGE,  Action => COV_COUNT,   Count => 0, AtLeast => 1, Weight => 1 ))                             |                                                                                    |
| ALL_COUNT                | CovBinType                                 |  (0 => ( BinVal => ALL_RANGE,  Action => COV_COUNT,   Count => 0, AtLeast => 1, Weight => 1 ))                             |                                                                                    |
| ALL_ILLEGAL              | CovBinType                                 |  (0 => ( BinVal => ALL_RANGE,  Action => COV_ILLEGAL, Count => 0, AtLeast => 0, Weight => 0 ))                             |                                                                                    |
| ALL_IGNORE               | CovBinType                                 |  (0 => ( BinVal => ALL_RANGE,  Action => COV_IGNORE,  Count => 0, AtLeast => 0, Weight => 0 ))                             |                                                                                    |
| ZERO_BIN                 | CovBinType                                 |  (0 => ( BinVal => (1=>(0,0)), Action => COV_COUNT,   Count => 0, AtLeast => 1, Weight => 1 ))                             |                                                                                    |
| ONE_BIN                  | CovBinType                                 |  (0 => ( BinVal => (1=>(1,1)), Action => COV_COUNT,   Count => 0, AtLeast => 1, Weight => 1 ))                             |                                                                                    |
| NULL_BIN                 | CovBinType(work.RandomPkg.NULL_RANGE_TYPE) |  (others => ( BinVal => ALL_RANGE,  Action => integer'high, Count => 0, AtLeast => integer'high, Weight => integer'high )) |                                                                                    |
## Types
| Name               | Type                                                                  | Description                                                                                                                                                                                                                                                                                 |
| ------------------ | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RangeType          |                                                                       |                                                                                                                                                                                                                                                                                             |
| RangeArrayType     |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovBinBaseType     |                                                                       | Deprecated Used for easy manual entry.  Order: min, max, action Intentionally did not use a record to allow other input formats in the future with VHDL-2008 unconstrained arrays of unconstrained elements  type CovBinManualType is array (natural range <>) of integer_vector(0 to 2) ;  |
| CovBinType         |                                                                       |                                                                                                                                                                                                                                                                                             |
| NextPointModeType  | (RANDOM, INCREMENT, MODE_MINIMUM)                                     |                                                                                                                                                                                                                                                                                             |
| CountModeType      | (COUNT_FIRST, COUNT_ALL)                                              |                                                                                                                                                                                                                                                                                             |
| IllegalModeType    | (ILLEGAL_ON, ILLEGAL_FAILURE, ILLEGAL_OFF)                            |                                                                                                                                                                                                                                                                                             |
| WeightModeType     | (AT_LEAST, WEIGHT, REMAIN, REMAIN_EXP, REMAIN_SCALED, REMAIN_WEIGHT ) |                                                                                                                                                                                                                                                                                             |
| CovMatrix2BaseType |                                                                       | In VHDL-2008 CovMatrix?BaseType and CovMatrix?Type will be subsumed by CovBinBaseType and CovBinType with RangeArrayType as an unconstrained array.                                                                                                                                         |
| CovMatrix2Type     |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix3BaseType |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix3Type     |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix4BaseType |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix4Type     |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix5BaseType |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix5Type     |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix6BaseType |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix6Type     |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix7BaseType |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix7Type     |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix8BaseType |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix8Type     |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix9BaseType |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovMatrix9Type     |                                                                       |                                                                                                                                                                                                                                                                                             |
| CovPType           |                                                                       |                                                                                                                                                                                                                                                                                             |
## Functions
- write <font id="function_arguments">( file f :  text ;  BinVal : RangeArrayType )</font> <font id="function_return">return ()</font>
- write <font id="function_arguments">( variable buf : inout line ; constant BinVal : in RangeArrayType)</font> <font id="function_return">return ()</font>
- ToVendorCovBinVal <font id="function_arguments">(BinVal : RangeArrayType)</font> <font id="function_return">return VendorCovRangeArrayType</font>
**Description**
VendorCov Conversion for Vendor supported functional coverage modeling
- ToMinPoint <font id="function_arguments">(A : RangeArrayType)</font> <font id="function_return">return integer</font>
- ToMinPoint <font id="function_arguments">(A : RangeArrayType)</font> <font id="function_return">return integer_vector</font>
- ToRandPoint <font id="function_arguments">(   BinVal to Random Point
   better as a function, however, inout not supported on functions
  
    variable RV       : inout RandomPType ;
    constant BinVal   : in    RangeArrayType ;
    variable result   : out   integer
  )</font> <font id="function_return">return ()</font>
- ToRandPoint <font id="function_arguments">(   BinVal to Random Point
  
    variable RV       : inout RandomPType ;
    constant BinVal   : in    RangeArrayType ;
    variable result   : out   integer_vector
  )</font> <font id="function_return">return ()</font>
- CompareBins <font id="function_arguments">(  
    variable Bin1       : inout CovPType ;
    variable Bin2       : inout CovPType ;
    variable ErrorCount : inout integer
  )</font> <font id="function_return">return ()</font>
**Description**
Experimental.  Intended primarily for development.
- CompareBins <font id="function_arguments">(  
    variable Bin1       : inout CovPType ;
    variable Bin2       : inout CovPType 
  )</font> <font id="function_return">return ()</font>
**Description**
Experimental.  Intended primarily for development.
- GenBin <font id="function_arguments">(  
    AtLeast       : integer ;
    Weight        : integer ;
    Min, Max      : integer ;
    NumBin        : integer
  )</font> <font id="function_return">return CovBinType</font>
- GenBin <font id="function_arguments">(AtLeast : integer ;  Min, Max, NumBin : integer )</font> <font id="function_return">return CovBinType</font>
**Description**
Each item in range in a separate CovBin
- GenBin <font id="function_arguments">(Min, Max, NumBin : integer )</font> <font id="function_return">return CovBinType</font>
- GenBin <font id="function_arguments">(Min, Max : integer)</font> <font id="function_return">return CovBinType</font>
- GenBin <font id="function_arguments">(A : integer)</font> <font id="function_return">return CovBinType</font>
- GenBin <font id="function_arguments">(  
    AtLeast       : integer ;
    Weight        : integer ;
    A             : integer_vector
  )</font> <font id="function_return">return CovBinType</font>
- GenBin <font id="function_arguments">( AtLeast : integer ;  A : integer_vector )</font> <font id="function_return">return CovBinType</font>
- GenBin <font id="function_arguments">( A : integer_vector )</font> <font id="function_return">return CovBinType</font>
- IllegalBin <font id="function_arguments">( Min, Max, NumBin : integer )</font> <font id="function_return">return CovBinType</font>
- IllegalBin <font id="function_arguments">( Min, Max : integer )</font> <font id="function_return">return CovBinType</font>
**Description**
All items in range in a single CovBin
- IllegalBin <font id="function_arguments">( A : integer )</font> <font id="function_return">return CovBinType</font>
- IgnoreBin <font id="function_arguments">(Min, Max, NumBin : integer)</font> <font id="function_return">return CovBinType</font>
- IgnoreBin <font id="function_arguments">(Min, Max : integer)</font> <font id="function_return">return CovBinType</font>
**Description**
All items in range in a single CovBin
- IgnoreBin <font id="function_arguments">(A : integer)</font> <font id="function_return">return CovBinType</font>
- GenCross <font id="function_arguments">(   2   Cross existing bins
   Use AddCross for adding values directly to coverage database
   Use GenCross for constants
  
    AtLeast     : integer ;
    Weight      : integer ;
    Bin1, Bin2  : CovBinType
  )</font> <font id="function_return">return CovMatrix2Type</font>
- GenCross <font id="function_arguments">(AtLeast : integer ; Bin1, Bin2 : CovBinType)</font> <font id="function_return">return CovMatrix2Type</font>
- GenCross <font id="function_arguments">(Bin1, Bin2 : CovBinType)</font> <font id="function_return">return CovMatrix2Type</font>
- GenCross <font id="function_arguments">(   3  
    AtLeast           : integer ;
    Weight            : integer ;
    Bin1, Bin2, Bin3  : CovBinType
  )</font> <font id="function_return">return CovMatrix3Type</font>
- GenCross <font id="function_arguments">( AtLeast : integer ; Bin1, Bin2, Bin3 : CovBinType )</font> <font id="function_return">return CovMatrix3Type</font>
- GenCross <font id="function_arguments">( Bin1, Bin2, Bin3 : CovBinType )</font> <font id="function_return">return CovMatrix3Type</font>
- GenCross <font id="function_arguments">(   4  
    AtLeast                 : integer ;
    Weight                  : integer ;
    Bin1, Bin2, Bin3, Bin4  : CovBinType
  )</font> <font id="function_return">return CovMatrix4Type</font>
- GenCross <font id="function_arguments">( AtLeast : integer ; Bin1, Bin2, Bin3, Bin4 : CovBinType )</font> <font id="function_return">return CovMatrix4Type</font>
- GenCross <font id="function_arguments">( Bin1, Bin2, Bin3, Bin4 : CovBinType )</font> <font id="function_return">return CovMatrix4Type</font>
- GenCross <font id="function_arguments">(   5  
    AtLeast                       : integer ;
    Weight                        : integer ;
    Bin1, Bin2, Bin3, Bin4, Bin5  : CovBinType
  )</font> <font id="function_return">return CovMatrix5Type</font>
- GenCross <font id="function_arguments">( AtLeast : integer ; Bin1, Bin2, Bin3, Bin4, Bin5 : CovBinType )</font> <font id="function_return">return CovMatrix5Type</font>
- GenCross <font id="function_arguments">( Bin1, Bin2, Bin3, Bin4, Bin5 : CovBinType )</font> <font id="function_return">return CovMatrix5Type</font>
- GenCross <font id="function_arguments">(   6  
    AtLeast                             : integer ;
    Weight                              : integer ;
    Bin1, Bin2, Bin3, Bin4, Bin5, Bin6  : CovBinType
  )</font> <font id="function_return">return CovMatrix6Type</font>
- GenCross <font id="function_arguments">( AtLeast : integer ; Bin1, Bin2, Bin3, Bin4, Bin5, Bin6 : CovBinType )</font> <font id="function_return">return CovMatrix6Type</font>
- GenCross <font id="function_arguments">( Bin1, Bin2, Bin3, Bin4, Bin5, Bin6 : CovBinType )</font> <font id="function_return">return CovMatrix6Type</font>
- GenCross <font id="function_arguments">(   7  
    AtLeast                                   : integer ;
    Weight                                    : integer ;
    Bin1, Bin2, Bin3, Bin4, Bin5, Bin6, Bin7  : CovBinType
  )</font> <font id="function_return">return CovMatrix7Type</font>
- GenCross <font id="function_arguments">( AtLeast : integer ; Bin1, Bin2, Bin3, Bin4, Bin5, Bin6, Bin7 : CovBinType )</font> <font id="function_return">return CovMatrix7Type</font>
- GenCross <font id="function_arguments">( Bin1, Bin2, Bin3, Bin4, Bin5, Bin6, Bin7 : CovBinType )</font> <font id="function_return">return CovMatrix7Type</font>
- GenCross <font id="function_arguments">(   8  
    AtLeast                                         : integer ;
    Weight                                          : integer ;
    Bin1, Bin2, Bin3, Bin4, Bin5, Bin6, Bin7, Bin8  : CovBinType
  )</font> <font id="function_return">return CovMatrix8Type</font>
- GenCross <font id="function_arguments">( AtLeast : integer ; Bin1, Bin2, Bin3, Bin4, Bin5, Bin6, Bin7, Bin8 : CovBinType )</font> <font id="function_return">return CovMatrix8Type</font>
- GenCross <font id="function_arguments">( Bin1, Bin2, Bin3, Bin4, Bin5, Bin6, Bin7, Bin8 : CovBinType )</font> <font id="function_return">return CovMatrix8Type</font>
- GenCross <font id="function_arguments">(   9  
    AtLeast                                               : integer ;
    Weight                                                : integer ;
    Bin1, Bin2, Bin3, Bin4, Bin5, Bin6, Bin7, Bin8, Bin9  : CovBinType
  )</font> <font id="function_return">return CovMatrix9Type</font>
- GenCross <font id="function_arguments">( AtLeast : integer ; Bin1, Bin2, Bin3, Bin4, Bin5, Bin6, Bin7, Bin8, Bin9 : CovBinType )</font> <font id="function_return">return CovMatrix9Type</font>
- GenCross <font id="function_arguments">( Bin1, Bin2, Bin3, Bin4, Bin5, Bin6, Bin7, Bin8, Bin9 : CovBinType )</font> <font id="function_return">return CovMatrix9Type</font>
- to_integer <font id="function_arguments">( B : boolean )</font> <font id="function_return">return integer</font>
**Description**
Utilities.  Remove if added to std.standard
- to_boolean <font id="function_arguments">( I : integer )</font> <font id="function_return">return boolean</font>
- to_integer <font id="function_arguments">( SL : std_logic )</font> <font id="function_return">return integer</font>
- to_std_logic <font id="function_arguments">( I : integer )</font> <font id="function_return">return std_logic</font>
- to_integer_vector <font id="function_arguments">( BV : boolean_vector )</font> <font id="function_return">return integer_vector</font>
- to_boolean_vector <font id="function_arguments">( IV : integer_vector )</font> <font id="function_return">return boolean_vector</font>
- to_integer_vector <font id="function_arguments">( SLV : std_logic_vector )</font> <font id="function_return">return integer_vector</font>
- to_std_logic_vector <font id="function_arguments">( IV : integer_vector )</font> <font id="function_return">return std_logic_vector</font>
