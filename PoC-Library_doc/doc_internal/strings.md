# Package: strings

- **File**: strings.vhdl
## Description

use			PoC.FileIO.all;

## Constants

| Name      | Type      | Value                                                                                                                                                                                                                                                                                                                                        | Description |
| --------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_POC_NUL | character |  ite((SYNTHESIS_TOOL /= SYNTHESIS_TOOL_ALTERA_QUARTUS2),<br><span style="padding-left:20px"> NUL,<br><span style="padding-left:20px"> '`');<br><span style="padding-left:20px">  	-- Type declarations 	-- =========================================================================== 	subtype T_RAWCHAR				is std_logic_vector(7 downto 0) |             |
## Types

| Name        | Type                                   | Description |
| ----------- | -------------------------------------- | ----------- |
| T_RAWSTRING | array (natural range <>) of T_RAWCHAR  |             |
## Functions
- to_IPStyle <font id="function_arguments">(str : string) </font> <font id="function_return">return T_IPSTYLE </font>
</br>**Description**
 testing area:
 ===========================================================================

- to_char <font id="function_arguments">(Value : std_logic) </font> <font id="function_return">return character </font>
</br>**Description**
 to_char

- to_char <font id="function_arguments">(rawchar : T_RAWCHAR) </font> <font id="function_return">return character </font>
- to_HexChar <font id="function_arguments">(Value : natural) </font> <font id="function_return">return character </font>
- to_HexChar <font id="function_arguments">(Value : unsigned) </font> <font id="function_return">return character </font>
- chr_isDigit <font id="function_arguments">(chr : character) </font> <font id="function_return">return boolean </font>
</br>**Description**
 chr_is* function

- chr_isLowerHexDigit <font id="function_arguments">(chr : character) </font> <font id="function_return">return boolean </font>
- chr_isUpperHexDigit <font id="function_arguments">(chr : character) </font> <font id="function_return">return boolean </font>
- chr_isHexDigit <font id="function_arguments">(chr : character) </font> <font id="function_return">return boolean </font>
- chr_isLower <font id="function_arguments">(chr : character) </font> <font id="function_return">return boolean </font>
- chr_isLowerAlpha <font id="function_arguments">(chr : character) </font> <font id="function_return">return boolean </font>
- chr_isUpper <font id="function_arguments">(chr : character) </font> <font id="function_return">return boolean </font>
- chr_isUpperAlpha <font id="function_arguments">(chr : character) </font> <font id="function_return">return boolean </font>
- chr_isAlpha <font id="function_arguments">(chr : character) </font> <font id="function_return">return boolean </font>
- raw_format_bool_bin <font id="function_arguments">(Value : boolean) </font> <font id="function_return">return string </font>
</br>**Description**
 raw_format_* functions

- raw_format_bool_chr <font id="function_arguments">(Value : boolean) </font> <font id="function_return">return string </font>
- raw_format_bool_str <font id="function_arguments">(Value : boolean) </font> <font id="function_return">return string </font>
- raw_format_slv_bin <font id="function_arguments">(slv : std_logic_vector) </font> <font id="function_return">return string </font>
- raw_format_slv_oct <font id="function_arguments">(slv : std_logic_vector) </font> <font id="function_return">return string </font>
- raw_format_slv_dec <font id="function_arguments">(slv : std_logic_vector) </font> <font id="function_return">return string </font>
- raw_format_slv_hex <font id="function_arguments">(slv : std_logic_vector) </font> <font id="function_return">return string </font>
- raw_format_nat_bin <font id="function_arguments">(Value : natural) </font> <font id="function_return">return string </font>
- raw_format_nat_oct <font id="function_arguments">(Value : natural) </font> <font id="function_return">return string </font>
- raw_format_nat_dec <font id="function_arguments">(Value : natural) </font> <font id="function_return">return string </font>
- raw_format_nat_hex <font id="function_arguments">(Value : natural) </font> <font id="function_return">return string </font>
- str_format <font id="function_arguments">(Value : REAL;<br><span style="padding-left:20px"> precision : natural := 3) </font> <font id="function_return">return string </font>
</br>**Description**
 str_format_* functions

- to_string <font id="function_arguments">(Value : boolean) </font> <font id="function_return">return string </font>
</br>**Description**
 to_string

- to_string <font id="function_arguments">(Value : integer;<br><span style="padding-left:20px"> base : positive := 10) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">(slv : std_logic_vector;<br><span style="padding-left:20px"> format : character;<br><span style="padding-left:20px"> Length : natural := 0;<br><span style="padding-left:20px"> fill : character := '0') </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">(rawstring : T_RAWSTRING) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">(Value : T_BCD_VECTOR) </font> <font id="function_return">return string </font>
- to_slv <font id="function_arguments">(rawstring : T_RAWSTRING) </font> <font id="function_return">return std_logic_vector </font>
</br>**Description**
 to_slv

- to_digit_bin <font id="function_arguments">(chr : character) </font> <font id="function_return">return T_DIGIT_BIN </font>
</br>**Description**
 to_digit*

- to_digit_oct <font id="function_arguments">(chr : character) </font> <font id="function_return">return T_DIGIT_OCT </font>
- to_digit_dec <font id="function_arguments">(chr : character) </font> <font id="function_return">return T_DIGIT_DEC </font>
- to_digit_hex <font id="function_arguments">(chr : character) </font> <font id="function_return">return T_DIGIT_HEX </font>
- to_digit <font id="function_arguments">(chr : character;<br><span style="padding-left:20px"> base : character := 'd') </font> <font id="function_return">return integer </font>
- to_natural_bin <font id="function_arguments">(str : string) </font> <font id="function_return">return integer </font>
</br>**Description**
 to_natural*

- to_natural_oct <font id="function_arguments">(str : string) </font> <font id="function_return">return integer </font>
- to_natural_dec <font id="function_arguments">(str : string) </font> <font id="function_return">return integer </font>
- to_natural_hex <font id="function_arguments">(str : string) </font> <font id="function_return">return integer </font>
- to_natural <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> base : character := 'd') </font> <font id="function_return">return integer </font>
- to_RawChar <font id="function_arguments">(char : character) </font> <font id="function_return">return T_RAWCHAR </font>
</br>**Description**
 to_raw*

- to_RawString <font id="function_arguments">(str : string) </font> <font id="function_return">return T_RAWSTRING </font>
- resize <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> size : positive;<br><span style="padding-left:20px"> FillChar : character := C_POC_NUL) </font> <font id="function_return">return string </font>
</br>**Description**
 resize

- chr_toLower <font id="function_arguments">(chr : character) </font> <font id="function_return">return character </font>
</br>**Description**
	function resize(rawstr : T_RAWSTRING; size : POSITIVE; FillChar : T_RAWCHAR := x"00")	return T_RAWSTRING;
 Character functions

- chr_toUpper <font id="function_arguments">(chr : character) </font> <font id="function_return">return character </font>
- str_length <font id="function_arguments">(str : string) </font> <font id="function_return">return natural </font>
</br>**Description**
 String functions

- str_equal <font id="function_arguments">(str1 : string;<br><span style="padding-left:20px"> str2 : string) </font> <font id="function_return">return boolean </font>
- str_match <font id="function_arguments">(str1 : string;<br><span style="padding-left:20px"> str2 : string) </font> <font id="function_return">return boolean </font>
- str_imatch <font id="function_arguments">(str1 : string;<br><span style="padding-left:20px"> str2 : string) </font> <font id="function_return">return boolean </font>
- str_pos <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> chr : character;<br><span style="padding-left:20px"> start : natural := 0) </font> <font id="function_return">return integer </font>
- str_pos <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> pattern : string;<br><span style="padding-left:20px"> start : natural := 0) </font> <font id="function_return">return integer </font>
- str_ipos <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> chr : character;<br><span style="padding-left:20px"> start : natural := 0) </font> <font id="function_return">return integer </font>
- str_ipos <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> pattern : string;<br><span style="padding-left:20px"> start : natural := 0) </font> <font id="function_return">return integer </font>
- str_find <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> chr : character) </font> <font id="function_return">return boolean </font>
- str_find <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> pattern : string) </font> <font id="function_return">return boolean </font>
- str_ifind <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> chr : character) </font> <font id="function_return">return boolean </font>
- str_ifind <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> pattern : string) </font> <font id="function_return">return boolean </font>
- str_replace <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> pattern : string;<br><span style="padding-left:20px"> replace : string) </font> <font id="function_return">return string </font>
- str_substr <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> start : integer := 0;<br><span style="padding-left:20px"> Length : integer := 0) </font> <font id="function_return">return string </font>
- str_ltrim <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> char : character := ' ') </font> <font id="function_return">return string </font>
- str_rtrim <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> char : character := ' ') </font> <font id="function_return">return string </font>
- str_trim <font id="function_arguments">(str : string) </font> <font id="function_return">return string </font>
- str_calign <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> Length : natural;<br><span style="padding-left:20px"> FillChar : character := ' ') </font> <font id="function_return">return string </font>
- str_lalign <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> Length : natural;<br><span style="padding-left:20px"> FillChar : character := ' ') </font> <font id="function_return">return string </font>
- str_ralign <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> Length : natural;<br><span style="padding-left:20px"> FillChar : character := ' ') </font> <font id="function_return">return string </font>
- str_toLower <font id="function_arguments">(str : string) </font> <font id="function_return">return string </font>
- str_toUpper <font id="function_arguments">(str : string) </font> <font id="function_return">return string </font>
