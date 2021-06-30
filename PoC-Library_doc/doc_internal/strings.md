# Package: strings

## Constants

| Name      | Type      | Value                                                                                                                                                                                                                            | Description |
| --------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_POC_NUL | character |  ite((SYNTHESIS_TOOL /= SYNTHESIS_TOOL_ALTERA_QUARTUS2), NUL, '`');  	-- Type declarations 	-- =========================================================================== 	subtype T_RAWCHAR				is std_logic_vector(7 downto 0) |             |
## Types

| Name        | Type | Description |
| ----------- | ---- | ----------- |
| T_RAWSTRING |      |             |
## Functions
- to_IPStyle <font id="function_arguments">(str : string) </font> <font id="function_return">return T_IPSTYLE </font>
**Description**
testing area:===========================================================================
- to_char <font id="function_arguments">(Value : std_logic) </font> <font id="function_return">return character </font>
**Description**
to_char
- to_char <font id="function_arguments">(rawchar : T_RAWCHAR) </font> <font id="function_return">return character </font>
- to_HexChar <font id="function_arguments">(Value : natural) </font> <font id="function_return">return character </font>
- to_HexChar <font id="function_arguments">(Value : unsigned) </font> <font id="function_return">return character </font>
- chr_isDigit <font id="function_arguments">(chr : character) </font> <font id="function_return">return boolean </font>
**Description**
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
**Description**
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
- str_format <font id="function_arguments">(Value : REAL; precision : natural := 3) </font> <font id="function_return">return string </font>
**Description**
str_format_* functions
- to_string <font id="function_arguments">(Value : boolean) </font> <font id="function_return">return string </font>
**Description**
to_string
- to_string <font id="function_arguments">(Value : integer; base : positive := 10) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">(slv : std_logic_vector; format : character; Length : natural := 0; fill : character := '0') </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">(rawstring : T_RAWSTRING) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">(Value : T_BCD_VECTOR) </font> <font id="function_return">return string </font>
- to_slv <font id="function_arguments">(rawstring : T_RAWSTRING) </font> <font id="function_return">return std_logic_vector </font>
**Description**
to_slv
- to_digit_bin <font id="function_arguments">(chr : character) </font> <font id="function_return">return T_DIGIT_BIN </font>
**Description**
to_digit*
- to_digit_oct <font id="function_arguments">(chr : character) </font> <font id="function_return">return T_DIGIT_OCT </font>
- to_digit_dec <font id="function_arguments">(chr : character) </font> <font id="function_return">return T_DIGIT_DEC </font>
- to_digit_hex <font id="function_arguments">(chr : character) </font> <font id="function_return">return T_DIGIT_HEX </font>
- to_digit <font id="function_arguments">(chr : character; base : character := 'd') </font> <font id="function_return">return integer </font>
- to_natural_bin <font id="function_arguments">(str : string) </font> <font id="function_return">return integer </font>
**Description**
to_natural*
- to_natural_oct <font id="function_arguments">(str : string) </font> <font id="function_return">return integer </font>
- to_natural_dec <font id="function_arguments">(str : string) </font> <font id="function_return">return integer </font>
- to_natural_hex <font id="function_arguments">(str : string) </font> <font id="function_return">return integer </font>
- to_natural <font id="function_arguments">(str : string; base : character := 'd') </font> <font id="function_return">return integer </font>
- to_RawChar <font id="function_arguments">(char : character) </font> <font id="function_return">return T_RAWCHAR </font>
**Description**
to_raw*
- to_RawString <font id="function_arguments">(str : string) </font> <font id="function_return">return T_RAWSTRING </font>
- resize <font id="function_arguments">(str : string; size : positive; FillChar : character := C_POC_NUL) </font> <font id="function_return">return string </font>
**Description**
resize
- chr_toLower <font id="function_arguments">(chr : character) </font> <font id="function_return">return character </font>
**Description**
Character functions
- chr_toUpper <font id="function_arguments">(chr : character) </font> <font id="function_return">return character </font>
- str_length <font id="function_arguments">(str : string) </font> <font id="function_return">return natural </font>
**Description**
String functions
- str_equal <font id="function_arguments">(str1 : string; str2 : string) </font> <font id="function_return">return boolean </font>
- str_match <font id="function_arguments">(str1 : string; str2 : string) </font> <font id="function_return">return boolean </font>
- str_imatch <font id="function_arguments">(str1 : string; str2 : string) </font> <font id="function_return">return boolean </font>
- str_pos <font id="function_arguments">(str : string; chr : character; start : natural := 0) </font> <font id="function_return">return integer </font>
- str_pos <font id="function_arguments">(str : string; pattern : string; start : natural := 0) </font> <font id="function_return">return integer </font>
- str_ipos <font id="function_arguments">(str : string; chr : character; start : natural := 0) </font> <font id="function_return">return integer </font>
- str_ipos <font id="function_arguments">(str : string; pattern : string; start : natural := 0) </font> <font id="function_return">return integer </font>
- str_find <font id="function_arguments">(str : string; chr : character) </font> <font id="function_return">return boolean </font>
- str_find <font id="function_arguments">(str : string; pattern : string) </font> <font id="function_return">return boolean </font>
- str_ifind <font id="function_arguments">(str : string; chr : character) </font> <font id="function_return">return boolean </font>
- str_ifind <font id="function_arguments">(str : string; pattern : string) </font> <font id="function_return">return boolean </font>
- str_replace <font id="function_arguments">(str : string; pattern : string; replace : string) </font> <font id="function_return">return string </font>
- str_substr <font id="function_arguments">(str : string; start : integer := 0; Length : integer := 0) </font> <font id="function_return">return string </font>
- str_ltrim <font id="function_arguments">(str : string; char : character := ' ') </font> <font id="function_return">return string </font>
- str_rtrim <font id="function_arguments">(str : string; char : character := ' ') </font> <font id="function_return">return string </font>
- str_trim <font id="function_arguments">(str : string) </font> <font id="function_return">return string </font>
- str_calign <font id="function_arguments">(str : string; Length : natural; FillChar : character := ' ') </font> <font id="function_return">return string </font>
- str_lalign <font id="function_arguments">(str : string; Length : natural; FillChar : character := ' ') </font> <font id="function_return">return string </font>
- str_ralign <font id="function_arguments">(str : string; Length : natural; FillChar : character := ' ') </font> <font id="function_return">return string </font>
- str_toLower <font id="function_arguments">(str : string) </font> <font id="function_return">return string </font>
- str_toUpper <font id="function_arguments">(str : string) </font> <font id="function_return">return string </font>
