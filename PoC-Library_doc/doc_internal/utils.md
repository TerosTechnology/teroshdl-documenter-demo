# Package: utils
## Constants
| Name        | Type  | Value   | Description |
| ----------- | ----- | ------- | ----------- |
| C_BCD_MINUS | T_BCD |  "1010" |             |
| C_BCD_OFF   | T_BCD |  "1011" |             |
## Types
| Name             | Type                                                                  | Description                     |
| ---------------- | --------------------------------------------------------------------- | ------------------------------- |
| T_BOOLVEC        |                                                                       |                                 |
| T_INTVEC         |                                                                       |                                 |
| T_NATVEC         |                                                                       |                                 |
| T_POSVEC         |                                                                       |                                 |
| T_REALVEC        |                                                                       |                                 |
| T_IPSTYLE        | (IPSTYLE_UNKNOWN, IPSTYLE_HARD, IPSTYLE_SOFT)                         | Intellectual Property (IP) type |
| T_BIT_ORDER      | (LSB_FIRST, MSB_FIRST)                                                | Bit order                       |
| T_BYTE_ORDER     | (LITTLE_ENDIAN, BIG_ENDIAN)                                           | Byte order (Endian)             |
| T_POLARITY       | (HIGH_ACTIVE, LOW_ACTIVE)                                             | Active logic level              |
| T_CLOCK_EDGE     | (RISING_EDGE, FALLING_EDGE)                                           | active clock edge               |
| T_ROUNDING_STYLE | (ROUND_TO_NEAREST, ROUND_TO_ZERO, ROUND_TO_INF, ROUND_UP, ROUND_DOWN) | rounding style                  |
| T_BCD            |                                                                       |                                 |
| T_BCD_VECTOR     |                                                                       |                                 |
## Functions
- div_ceil <font id="function_arguments">(a : natural; b : positive)</font> <font id="function_return">return natural</font>
**Description**
Calculates: ceil(a / b)
- is_pow2 <font id="function_arguments">(int : natural)</font> <font id="function_return">return boolean</font>
**Description**
is input a power of 2?
- ceil_pow2 <font id="function_arguments">(int : natural)</font> <font id="function_return">return positive</font>
**Description**
round to next power of 2
- floor_pow2 <font id="function_arguments">(int : natural)</font> <font id="function_return">return natural</font>
**Description**
round to previous power of 2
- log2ceil <font id="function_arguments">(arg : positive)</font> <font id="function_return">return natural</font>
**Description**
Calculates: ceil(ld(arg))
- log2ceilnz <font id="function_arguments">(arg : positive)</font> <font id="function_return">return positive</font>
**Description**
Calculates: max(1, ceil(ld(arg)))
- log10ceil <font id="function_arguments">(arg		: positive)</font> <font id="function_return">return natural</font>
**Description**
Calculates: ceil(lg(arg))
- log10ceilnz <font id="function_arguments">(arg	: positive)</font> <font id="function_return">return positive</font>
**Description**
Calculates: max(1, ceil(lg(arg)))
- ite <font id="function_arguments">(cond : boolean; value1 : boolean; value2 : boolean)</font> <font id="function_return">return boolean</font>
- ite <font id="function_arguments">(cond : boolean; value1 : integer; value2 : integer)</font> <font id="function_return">return integer</font>
- ite <font id="function_arguments">(cond : boolean; value1 : REAL;	value2 : REAL)</font> <font id="function_return">return REAL</font>
- ite <font id="function_arguments">(cond : boolean; value1 : std_logic; value2 : std_logic)</font> <font id="function_return">return std_logic</font>
- ite <font id="function_arguments">(cond : boolean; value1 : std_logic_vector; value2 : std_logic_vector)</font> <font id="function_return">return std_logic_vector</font>
- ite <font id="function_arguments">(cond : boolean; value1 : bit_vector; value2 : bit_vector)</font> <font id="function_return">return bit_vector</font>
- ite <font id="function_arguments">(cond : boolean; value1 : unsigned; value2 : unsigned)</font> <font id="function_return">return unsigned</font>
- ite <font id="function_arguments">(cond : boolean; value1 : signed; value2 : signed)</font> <font id="function_return">return signed</font>
- ite <font id="function_arguments">(cond : boolean; value1 : character; value2 : character)</font> <font id="function_return">return character</font>
- ite <font id="function_arguments">(cond : boolean; value1 : string; value2 : string)</font> <font id="function_return">return string</font>
- inc_if <font id="function_arguments">(cond : boolean; value : integer; increment : integer := 1)</font> <font id="function_return">return integer</font>
**Description**
conditional increment / decrement
- dec_if <font id="function_arguments">(cond : boolean; value : integer; decrement : integer := 1)</font> <font id="function_return">return integer</font>
- imin <font id="function_arguments">(arg1 : integer; arg2 : integer)</font> <font id="function_return">return integer</font>
**Description**
Calculates: min(arg1, arg2) for integers
- imin <font id="function_arguments">(vec : T_INTVEC)</font> <font id="function_return">return integer</font>
**Description**
Calculates: min(vec) for a integer vector
- imin <font id="function_arguments">(vec : T_NATVEC)</font> <font id="function_return">return natural</font>
**Description**
Calculates: min(vec) for a natural vector
- imin <font id="function_arguments">(vec : T_POSVEC)</font> <font id="function_return">return positive</font>
**Description**
Calculates: min(vec) for a positive vector
- rmin <font id="function_arguments">(vec : T_REALVEC)</font> <font id="function_return">return real</font>
**Description**
Calculates: min(vec) of real vector
- imax <font id="function_arguments">(arg1 : integer; arg2 : integer)</font> <font id="function_return">return integer</font>
**Description**
Calculates: max(arg1, arg2) for integers
- imax <font id="function_arguments">(vec : T_INTVEC)</font> <font id="function_return">return integer</font>
**Description**
Calculates: max(vec) for a integer vector
- imax <font id="function_arguments">(vec : T_NATVEC)</font> <font id="function_return">return natural</font>
**Description**
Calculates: max(vec) for a natural vector
- imax <font id="function_arguments">(vec : T_POSVEC)</font> <font id="function_return">return positive</font>
**Description**
Calculates: max(vec) for a positive vector
- rmax <font id="function_arguments">(vec : T_REALVEC)</font> <font id="function_return">return real</font>
**Description**
Calculates: max(vec) of real vector
- isum <font id="function_arguments">(vec : T_NATVEC)</font> <font id="function_return">return natural</font>
**Description**
Calculates: sum(vec) for a natural vector
- isum <font id="function_arguments">(vec : T_POSVEC)</font> <font id="function_return">return natural</font>
**Description**
Calculates: sum(vec) for a positive vector
- isum <font id="function_arguments">(vec : T_INTVEC)</font> <font id="function_return">return integer</font>
**Description**
Calculates: sum(vec) of integer vector
- rsum <font id="function_arguments">(vec : T_REALVEC)</font> <font id="function_return">return real</font>
**Description**
Calculates: sum(vec) of real vector
- to_int <font id="function_arguments">(bool : boolean; zero : integer := 0; one : integer := 1)</font> <font id="function_return">return integer</font>
**Description**
to integer: to_int
- to_int <font id="function_arguments">(sl : std_logic; zero : integer := 0; one : integer := 1)</font> <font id="function_return">return integer</font>
- to_sl <font id="function_arguments">(Value : boolean)</font> <font id="function_return">return std_logic</font>
**Description**
to std_logic: to_sl
- to_sl <font id="function_arguments">(Value : character)</font> <font id="function_return">return std_logic</font>
- to_slv <font id="function_arguments">(Value : natural; Size : positive)</font> <font id="function_return">return std_logic_vector</font>
**Description**
short for std_logic_vector(to_unsigned(Value, Size))
- to_BCD <font id="function_arguments">(Digit : integer)</font> <font id="function_return">return T_BCD</font>
- to_BCD <font id="function_arguments">(Digit : character)</font> <font id="function_return">return T_BCD</font>
- to_BCD <font id="function_arguments">(Digit : unsigned)</font> <font id="function_return">return T_BCD</font>
- to_BCD <font id="function_arguments">(Digit : std_logic_vector)</font> <font id="function_return">return T_BCD</font>
- to_BCD_Vector <font id="function_arguments">(Value : integer; Size : natural := 0; Fill : T_BCD := x"0")</font> <font id="function_return">return T_BCD_VECTOR</font>
- to_BCD_Vector <font id="function_arguments">(Value : string; Size : natural := 0; Fill : T_BCD := x"0")</font> <font id="function_return">return T_BCD_VECTOR</font>
- bound <font id="function_arguments">(index : integer; lowerBound : integer; upperBound : integer)</font> <font id="function_return">return integer</font>
**Description**
TODO: comment
- to_index <font id="function_arguments">(slv : unsigned; max : natural := 0)</font> <font id="function_return">return integer</font>
- to_index <font id="function_arguments">(slv : std_logic_vector; max : natural := 0)</font> <font id="function_return">return integer</font>
- is_sl <font id="function_arguments">(c : character)</font> <font id="function_return">return boolean</font>
**Description**
is_*
- slv_or <font id="function_arguments">(vec : std_logic_vector)</font> <font id="function_return">return std_logic</font>
**Description**
Aggregate functions
- slv_nor <font id="function_arguments">(vec : std_logic_vector)</font> <font id="function_return">return std_logic</font>
- slv_and <font id="function_arguments">(vec : std_logic_vector)</font> <font id="function_return">return std_logic</font>
- slv_nand <font id="function_arguments">(vec : std_logic_vector)</font> <font id="function_return">return std_logic</font>
- slv_xor <font id="function_arguments">(vec : std_logic_vector)</font> <font id="function_return">return std_logic</font>
- reverse <font id="function_arguments">(vec : std_logic_vector)</font> <font id="function_return">return std_logic_vector</font>
- reverse <font id="function_arguments">(vec : bit_vector)</font> <font id="function_return">return bit_vector</font>
- reverse <font id="function_arguments">(vec : unsigned)</font> <font id="function_return">return unsigned</font>
- scale <font id="function_arguments">(Value : integer;	Minimum : integer;	Maximum : integer; RoundingStyle : T_ROUNDING_STYLE := ROUND_TO_NEAREST)</font> <font id="function_return">return integer</font>
**Description**
scale a value into a range [Minimum, Maximum]
- scale <font id="function_arguments">(Value : REAL;		Minimum : integer;	Maximum : integer; RoundingStyle : T_ROUNDING_STYLE := ROUND_TO_NEAREST)</font> <font id="function_return">return integer</font>
- scale <font id="function_arguments">(Value : REAL;		Minimum : REAL;			Maximum : REAL)</font> <font id="function_return">return REAL</font>
- resize <font id="function_arguments">(vec : bit_vector; length : natural; fill : bit := '0')</font> <font id="function_return">return bit_vector</font>
- resize <font id="function_arguments">(vec : std_logic_vector; length : natural; fill : std_logic := '0')</font> <font id="function_return">return std_logic_vector</font>
- move <font id="function_arguments">(vec : std_logic_vector; ofs : integer)</font> <font id="function_return">return std_logic_vector</font>
**Description**
Shift the index range of a vector by the specified offset.
- movez <font id="function_arguments">(vec : std_logic_vector)</font> <font id="function_return">return std_logic_vector</font>
**Description**
Shift the index range of a vector making vec'low = 0.
- ascend <font id="function_arguments">(vec : std_logic_vector)</font> <font id="function_return">return std_logic_vector</font>
- descend <font id="function_arguments">(vec : std_logic_vector)</font> <font id="function_return">return std_logic_vector</font>
- lssb <font id="function_arguments">(arg : std_logic_vector)</font> <font id="function_return">return std_logic_vector</font>
- lssb <font id="function_arguments">(arg : bit_vector)</font> <font id="function_return">return bit_vector</font>
- lssb_idx <font id="function_arguments">(arg : std_logic_vector)</font> <font id="function_return">return integer</font>
- lssb_idx <font id="function_arguments">(arg : bit_vector)</font> <font id="function_return">return integer</font>
- mssb <font id="function_arguments">(arg : std_logic_vector)</font> <font id="function_return">return std_logic_vector</font>
**Description**
Most-Significant Set Bit (mssb): computes a vector of the same lengthwith at most one bit set at the leftmost '1' found in arg.
- mssb <font id="function_arguments">(arg : bit_vector)</font> <font id="function_return">return bit_vector</font>
- mssb_idx <font id="function_arguments">(arg : std_logic_vector)</font> <font id="function_return">return integer</font>
- mssb_idx <font id="function_arguments">(arg : bit_vector)</font> <font id="function_return">return integer</font>
- swap <font id="function_arguments">(slv : std_logic_vector; Size : positive)</font> <font id="function_return">return std_logic_vector</font>
**Description**
Swap sub vectors in vector (endian reversal)
- bit_swap <font id="function_arguments">(slv : std_logic_vector; Chunksize : positive)</font> <font id="function_return">return std_logic_vector</font>
**Description**
Swap the bits in a chunk
- genmask_high <font id="function_arguments">(Bits : natural; MaskLength : positive)</font> <font id="function_return">return std_logic_vector</font>
**Description**
generate bit masks
- genmask_low <font id="function_arguments">(Bits : natural; MaskLength : positive)</font> <font id="function_return">return std_logic_vector</font>
- genmask_alternate <font id="function_arguments">(len : positive; lsb : std_logic := '0')</font> <font id="function_return">return std_logic_vector</font>
- onehot2bin <font id="function_arguments">(onehot : std_logic_vector; empty_val : integer := -1)</font> <font id="function_return">return unsigned</font>
**Description**
Encodings===========================================================================One-Hot-Code to Binary-Code. If a non-negative value empty_val is specified, its unsigned representation will be returned upon an all-zero input. As a consequence of specifying this value, no simulation warnings will be issued upon empty inputs. Alleged 1-hot-encoded inputs with more than one bit asserted will always raise a simulation warning.
- gray2bin <font id="function_arguments">(gray_val : std_logic_vector)</font> <font id="function_return">return std_logic_vector</font>
- gray2bin <font id="function_arguments">(gray_val : std_logic_vector)</font> <font id="function_return">return unsigned</font>
- bin2onehot <font id="function_arguments">(value : std_logic_vector)</font> <font id="function_return">return std_logic_vector</font>
**Description**
Binary-Code to One-Hot-Code
- bin2onehot <font id="function_arguments">(value : unsigned)</font> <font id="function_return">return std_logic_vector</font>
- bin2onecold <font id="function_arguments">(value : std_logic_vector)</font> <font id="function_return">return std_logic_vector</font>
**Description**
Binary-Code to One-Cold-Code
- bin2onecold <font id="function_arguments">(value : unsigned)</font> <font id="function_return">return std_logic_vector</font>
- bin2gray <font id="function_arguments">(value : std_logic_vector)</font> <font id="function_return">return std_logic_vector</font>
**Description**
Binary-Code to Gray-Code
- bin2gray <font id="function_arguments">(value : unsigned)</font> <font id="function_return">return std_logic_vector</font>
