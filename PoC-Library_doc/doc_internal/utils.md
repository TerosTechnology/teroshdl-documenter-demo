# Package: utils

- **File**: utils.vhdl
## Constants

| Name        | Type  | Value   | Description |
| ----------- | ----- | ------- | ----------- |
| C_BCD_MINUS | T_BCD |  "1010" |             |
| C_BCD_OFF   | T_BCD |  "1011" |             |
## Types

| Name             | Type                                                                                                                                                                                                                   | Description                                                                                                                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| T_BOOLVEC        | array(natural range <>) of boolean                                                                                                                                                                                     |  deferred constant declaration  Type declarations  ========================================================================== + Vectors of primitive standard types +++++++++++++++++++++++++++++++++++++  |
| T_INTVEC         | array(natural range <>) of integer                                                                                                                                                                                     |                                                                                                                                                                                                            |
| T_NATVEC         | array(natural range <>) of natural                                                                                                                                                                                     |                                                                                                                                                                                                            |
| T_POSVEC         | array(natural range <>) of positive                                                                                                                                                                                    |                                                                                                                                                                                                            |
| T_REALVEC        | array(natural range <>) of REAL                                                                                                                                                                                        |                                                                                                                                                                                                            |
| T_IPSTYLE        | (IPSTYLE_UNKNOWN,<br><span style="padding-left:20px"> IPSTYLE_HARD,<br><span style="padding-left:20px"> IPSTYLE_SOFT)                                                                                                  | + Enums ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  Intellectual Property (IP) type                                                                                                |
| T_BIT_ORDER      | (LSB_FIRST,<br><span style="padding-left:20px"> MSB_FIRST)                                                                                                                                                             |  Bit order                                                                                                                                                                                                 |
| T_BYTE_ORDER     | (LITTLE_ENDIAN,<br><span style="padding-left:20px"> BIG_ENDIAN)                                                                                                                                                        |  Byte order (Endian)                                                                                                                                                                                       |
| T_POLARITY       | (HIGH_ACTIVE,<br><span style="padding-left:20px"> LOW_ACTIVE)                                                                                                                                                          |  Active logic level                                                                                                                                                                                        |
| T_CLOCK_EDGE     | (RISING_EDGE,<br><span style="padding-left:20px"> FALLING_EDGE)                                                                                                                                                        |  active clock edge                                                                                                                                                                                         |
| T_ROUNDING_STYLE | (ROUND_TO_NEAREST,<br><span style="padding-left:20px"> ROUND_TO_ZERO,<br><span style="padding-left:20px"> ROUND_TO_INF,<br><span style="padding-left:20px"> ROUND_UP,<br><span style="padding-left:20px"> ROUND_DOWN)  |  rounding style                                                                                                                                                                                            |
| T_BCD            |                                                                                                                                                                                                                        |  define a new unrelated type T_BCD for arithmetic  QUESTION: extract to an own BCD package? 	=> overloaded operators for +/-/=/... and conversion functions                                                |
| T_BCD_VECTOR     | array(natural range <>) of T_BCD                                                                                                                                                                                       |                                                                                                                                                                                                            |
## Functions
- div_ceil <font id="function_arguments">(a : natural;<br><span style="padding-left:20px"> b : positive) </font> <font id="function_return">return natural </font>
**Description**
 Function declarations
 ==========================================================================
+ Division ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 Calculates: ceil(a / b)

- is_pow2 <font id="function_arguments">(int : natural) </font> <font id="function_return">return boolean </font>
**Description**
+ Power +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 is input a power of 2?

- ceil_pow2 <font id="function_arguments">(int : natural) </font> <font id="function_return">return positive </font>
**Description**
 round to next power of 2

- floor_pow2 <font id="function_arguments">(int : natural) </font> <font id="function_return">return natural </font>
**Description**
 round to previous power of 2

- log2ceil <font id="function_arguments">(arg : positive) </font> <font id="function_return">return natural </font>
**Description**
+ Logarithm ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 Calculates: ceil(ld(arg))

- log2ceilnz <font id="function_arguments">(arg : positive) </font> <font id="function_return">return positive </font>
**Description**
 Calculates: max(1, ceil(ld(arg)))

- log10ceil <font id="function_arguments">(arg		: positive) </font> <font id="function_return">return natural </font>
**Description**
 Calculates: ceil(lg(arg))

- log10ceilnz <font id="function_arguments">(arg	: positive) </font> <font id="function_return">return positive </font>
**Description**
 Calculates: max(1, ceil(lg(arg)))

- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : boolean;<br><span style="padding-left:20px"> value2 : boolean) </font> <font id="function_return">return boolean </font>
**Description**
+ if-then-else (ite) +++++++++++++++++++++++++++++++++++++++++++++++++++++

- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : integer;<br><span style="padding-left:20px"> value2 : integer) </font> <font id="function_return">return integer </font>
- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : REAL;<br><span style="padding-left:20px">	value2 : REAL) </font> <font id="function_return">return REAL </font>
- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : std_logic;<br><span style="padding-left:20px"> value2 : std_logic) </font> <font id="function_return">return std_logic </font>
- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : std_logic_vector;<br><span style="padding-left:20px"> value2 : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : bit_vector;<br><span style="padding-left:20px"> value2 : bit_vector) </font> <font id="function_return">return bit_vector </font>
- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : unsigned;<br><span style="padding-left:20px"> value2 : unsigned) </font> <font id="function_return">return unsigned </font>
- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : signed;<br><span style="padding-left:20px"> value2 : signed) </font> <font id="function_return">return signed </font>
- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : character;<br><span style="padding-left:20px"> value2 : character) </font> <font id="function_return">return character </font>
- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : string;<br><span style="padding-left:20px"> value2 : string) </font> <font id="function_return">return string </font>
- inc_if <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value : integer;<br><span style="padding-left:20px"> increment : integer := 1) </font> <font id="function_return">return integer </font>
**Description**
 conditional increment / decrement

- dec_if <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value : integer;<br><span style="padding-left:20px"> decrement : integer := 1) </font> <font id="function_return">return integer </font>
- imin <font id="function_arguments">(arg1 : integer;<br><span style="padding-left:20px"> arg2 : integer) </font> <font id="function_return">return integer </font>
**Description**
 Calculates: min(arg1, arg2) for integers
- imin <font id="function_arguments">(vec : T_INTVEC) </font> <font id="function_return">return integer </font>
**Description**
 Calculates: min(vec) for a integer vector
- imin <font id="function_arguments">(vec : T_NATVEC) </font> <font id="function_return">return natural </font>
**Description**
 Calculates: min(vec) for a natural vector
- imin <font id="function_arguments">(vec : T_POSVEC) </font> <font id="function_return">return positive </font>
**Description**
 Calculates: min(vec) for a positive vector
- rmin <font id="function_arguments">(vec : T_REALVEC) </font> <font id="function_return">return real </font>
**Description**
 Calculates: min(vec) of real vector
- imax <font id="function_arguments">(arg1 : integer;<br><span style="padding-left:20px"> arg2 : integer) </font> <font id="function_return">return integer </font>
**Description**
 Calculates: max(arg1, arg2) for integers
- imax <font id="function_arguments">(vec : T_INTVEC) </font> <font id="function_return">return integer </font>
**Description**
 Calculates: max(vec) for a integer vector
- imax <font id="function_arguments">(vec : T_NATVEC) </font> <font id="function_return">return natural </font>
**Description**
 Calculates: max(vec) for a natural vector
- imax <font id="function_arguments">(vec : T_POSVEC) </font> <font id="function_return">return positive </font>
**Description**
 Calculates: max(vec) for a positive vector
- rmax <font id="function_arguments">(vec : T_REALVEC) </font> <font id="function_return">return real </font>
**Description**
 Calculates: max(vec) of real vector
- isum <font id="function_arguments">(vec : T_NATVEC) </font> <font id="function_return">return natural </font>
**Description**
 Calculates: sum(vec) for a natural vector
- isum <font id="function_arguments">(vec : T_POSVEC) </font> <font id="function_return">return natural </font>
**Description**
 Calculates: sum(vec) for a positive vector
- isum <font id="function_arguments">(vec : T_INTVEC) </font> <font id="function_return">return integer </font>
**Description**
 Calculates: sum(vec) of integer vector
- rsum <font id="function_arguments">(vec : T_REALVEC) </font> <font id="function_return">return real </font>
**Description**
 Calculates: sum(vec) of real vector
- to_int <font id="function_arguments">(bool : boolean;<br><span style="padding-left:20px"> zero : integer := 0;<br><span style="padding-left:20px"> one : integer := 1) </font> <font id="function_return">return integer </font>
**Description**
+ Conversions ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 to integer: to_int

- to_int <font id="function_arguments">(sl : std_logic;<br><span style="padding-left:20px"> zero : integer := 0;<br><span style="padding-left:20px"> one : integer := 1) </font> <font id="function_return">return integer </font>
- to_sl <font id="function_arguments">(Value : boolean) </font> <font id="function_return">return std_logic </font>
**Description**
 to std_logic: to_sl

- to_sl <font id="function_arguments">(Value : character) </font> <font id="function_return">return std_logic </font>
- to_slv <font id="function_arguments">(Value : natural;<br><span style="padding-left:20px"> Size : positive) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 short for std_logic_vector(to_unsigned(Value, Size))
- to_BCD <font id="function_arguments">(Digit : integer) </font> <font id="function_return">return T_BCD </font>
- to_BCD <font id="function_arguments">(Digit : character) </font> <font id="function_return">return T_BCD </font>
- to_BCD <font id="function_arguments">(Digit : unsigned) </font> <font id="function_return">return T_BCD </font>
- to_BCD <font id="function_arguments">(Digit : std_logic_vector) </font> <font id="function_return">return T_BCD </font>
- to_BCD_Vector <font id="function_arguments">(Value : integer;<br><span style="padding-left:20px"> Size : natural := 0;<br><span style="padding-left:20px"> Fill : T_BCD := x"0") </font> <font id="function_return">return T_BCD_VECTOR </font>
- to_BCD_Vector <font id="function_arguments">(Value : string;<br><span style="padding-left:20px"> Size : natural := 0;<br><span style="padding-left:20px"> Fill : T_BCD := x"0") </font> <font id="function_return">return T_BCD_VECTOR </font>
- bound <font id="function_arguments">(index : integer;<br><span style="padding-left:20px"> lowerBound : integer;<br><span style="padding-left:20px"> upperBound : integer) </font> <font id="function_return">return integer </font>
**Description**
 TODO: comment

- to_index <font id="function_arguments">(slv : unsigned;<br><span style="padding-left:20px"> max : natural := 0) </font> <font id="function_return">return integer </font>
- to_index <font id="function_arguments">(slv : std_logic_vector;<br><span style="padding-left:20px"> max : natural := 0) </font> <font id="function_return">return integer </font>
- is_sl <font id="function_arguments">(c : character) </font> <font id="function_return">return boolean </font>
**Description**
 is_*

- slv_or <font id="function_arguments">(vec : std_logic_vector) </font> <font id="function_return">return std_logic </font>
**Description**
+ Basic Vector Utilities +++++++++++++++++++++++++++++++++++++++++++++++++
 Aggregate functions

- slv_nor <font id="function_arguments">(vec : std_logic_vector) </font> <font id="function_return">return std_logic </font>
- slv_and <font id="function_arguments">(vec : std_logic_vector) </font> <font id="function_return">return std_logic </font>
- slv_nand <font id="function_arguments">(vec : std_logic_vector) </font> <font id="function_return">return std_logic </font>
- slv_xor <font id="function_arguments">(vec : std_logic_vector) </font> <font id="function_return">return std_logic </font>
- reverse <font id="function_arguments">(vec : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 NO slv_xnor! This operation would not be well-defined as
 not xor(vec) /= vec_{n-1} xnor ... xnor vec_1 xnor vec_0 iff n is odd.
 Reverses the elements of the passed Vector.

 @synthesis supported


- reverse <font id="function_arguments">(vec : bit_vector) </font> <font id="function_return">return bit_vector </font>
- reverse <font id="function_arguments">(vec : unsigned) </font> <font id="function_return">return unsigned </font>
- scale <font id="function_arguments">(Value : integer;<br><span style="padding-left:20px">	Minimum : integer;<br><span style="padding-left:20px">	Maximum : integer;<br><span style="padding-left:20px"> RoundingStyle : T_ROUNDING_STYLE := ROUND_TO_NEAREST) </font> <font id="function_return">return integer </font>
**Description**
 scale a value into a range [Minimum, Maximum]

- scale <font id="function_arguments">(Value : REAL;<br><span style="padding-left:20px">		Minimum : integer;<br><span style="padding-left:20px">	Maximum : integer;<br><span style="padding-left:20px"> RoundingStyle : T_ROUNDING_STYLE := ROUND_TO_NEAREST) </font> <font id="function_return">return integer </font>
- scale <font id="function_arguments">(Value : REAL;<br><span style="padding-left:20px">		Minimum : REAL;<br><span style="padding-left:20px">			Maximum : REAL) </font> <font id="function_return">return REAL </font>
- resize <font id="function_arguments">(vec : bit_vector;<br><span style="padding-left:20px"> length : natural;<br><span style="padding-left:20px"> fill : bit := '0') </font> <font id="function_return">return bit_vector </font>
**Description**
 Resizes the vector to the specified length. The adjustment is make on
 on the 'high end of the vector. The 'low index remains as in the argument.
 If the result vector is larger, the extension uses the provided fill value
 (default: '0').
 Use the resize functions of the numeric_std package for value-preserving
 resizes of the signed and unsigned data types.

 @synthesis supported


- resize <font id="function_arguments">(vec : std_logic_vector;<br><span style="padding-left:20px"> length : natural;<br><span style="padding-left:20px"> fill : std_logic := '0') </font> <font id="function_return">return std_logic_vector </font>
- move <font id="function_arguments">(vec : std_logic_vector;<br><span style="padding-left:20px"> ofs : integer) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 Shift the index range of a vector by the specified offset.

- movez <font id="function_arguments">(vec : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 Shift the index range of a vector making vec'low = 0.

- ascend <font id="function_arguments">(vec : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
- descend <font id="function_arguments">(vec : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
- lssb <font id="function_arguments">(arg : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 Least-Significant Set Bit (lssb):
 Computes a vector of the same length as the argument with
 at most one bit set at the rightmost '1' found in arg.

 @synthesis supported


- lssb <font id="function_arguments">(arg : bit_vector) </font> <font id="function_return">return bit_vector </font>
- lssb_idx <font id="function_arguments">(arg : std_logic_vector) </font> <font id="function_return">return integer </font>
**Description**
 Returns the index of the least-significant set bit.

 @synthesis supported


- lssb_idx <font id="function_arguments">(arg : bit_vector) </font> <font id="function_return">return integer </font>
- mssb <font id="function_arguments">(arg : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 Most-Significant Set Bit (mssb): computes a vector of the same length
 with at most one bit set at the leftmost '1' found in arg.

- mssb <font id="function_arguments">(arg : bit_vector) </font> <font id="function_return">return bit_vector </font>
- mssb_idx <font id="function_arguments">(arg : std_logic_vector) </font> <font id="function_return">return integer </font>
- mssb_idx <font id="function_arguments">(arg : bit_vector) </font> <font id="function_return">return integer </font>
- swap <font id="function_arguments">(slv : std_logic_vector;<br><span style="padding-left:20px"> Size : positive) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 Swap sub vectors in vector (endian reversal)

- bit_swap <font id="function_arguments">(slv : std_logic_vector;<br><span style="padding-left:20px"> Chunksize : positive) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 Swap the bits in a chunk

- genmask_high <font id="function_arguments">(Bits : natural;<br><span style="padding-left:20px"> MaskLength : positive) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 generate bit masks

- genmask_low <font id="function_arguments">(Bits : natural;<br><span style="padding-left:20px"> MaskLength : positive) </font> <font id="function_return">return std_logic_vector </font>
- genmask_alternate <font id="function_arguments">(len : positive;<br><span style="padding-left:20px"> lsb : std_logic := '0') </font> <font id="function_return">return std_logic_vector </font>
- onehot2bin <font id="function_arguments">(onehot : std_logic_vector;<br><span style="padding-left:20px"> empty_val : integer := -1) </font> <font id="function_return">return unsigned </font>
**Description**
 Encodings
 ===========================================================================
 One-Hot-Code to Binary-Code.
  If a non-negative value empty_val is specified, its unsigned
  representation will be returned upon an all-zero input. As a consequence
  of specifying this value, no simulation warnings will be issued upon empty
  inputs. Alleged 1-hot-encoded inputs with more than one bit asserted
  will always raise a simulation warning.

- gray2bin <font id="function_arguments">(gray_val : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 Converts Gray-Code into Binary-Code.

 @synthesis supported


- gray2bin <font id="function_arguments">(gray_val : std_logic_vector) </font> <font id="function_return">return unsigned </font>
- bin2onehot <font id="function_arguments">(value : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 Binary-Code to One-Hot-Code

- bin2onehot <font id="function_arguments">(value : unsigned) </font> <font id="function_return">return std_logic_vector </font>
- bin2onecold <font id="function_arguments">(value : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 Binary-Code to One-Cold-Code

- bin2onecold <font id="function_arguments">(value : unsigned) </font> <font id="function_return">return std_logic_vector </font>
- bin2gray <font id="function_arguments">(value : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 Binary-Code to Gray-Code

- bin2gray <font id="function_arguments">(value : unsigned) </font> <font id="function_return">return std_logic_vector </font>
