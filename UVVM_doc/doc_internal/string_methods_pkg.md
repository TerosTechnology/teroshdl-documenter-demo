# Package: string_methods_pkg

## Functions
- bitvis_assert <font id="function_arguments">( val        : boolean; severeness : severity_level; msg        : string; scope      : string ) </font> <font id="function_return">return ()</font>
- justify <font id="function_arguments">( val       : string; width     : natural := 0; justified : side := RIGHT; format: t_format_string := AS_IS -- No defaults on 4 first param - to avoid ambiguity with std.textio ) </font> <font id="function_return">return string </font>
**Description**
DEPRECATED.Function will be removed in future versions of UVVM-Util
- justify <font id="function_arguments">( val             : string; justified       : side; width           : natural; format_spaces   : t_format_spaces; truncate        : t_truncate_string ) </font> <font id="function_return">return string </font>
**Description**
DEPRECATED.Function will be removed in future versions of UVVM-Util
- justify <font id="function_arguments">( val             : string; justified       : t_justify_center; width           : natural; format_spaces   : t_format_spaces; truncate        : t_truncate_string ) </font> <font id="function_return">return string </font>
- pos_of_leftmost <font id="function_arguments">( target              : character; vector              : string; result_if_not_found : natural := 1 ) </font> <font id="function_return">return natural </font>
- pos_of_rightmost <font id="function_arguments">( target              : character; vector              : string; result_if_not_found : natural := 1 ) </font> <font id="function_return">return natural </font>
- pos_of_leftmost_non_zero <font id="function_arguments">( vector              : string; result_if_not_found : natural := 1 ) </font> <font id="function_return">return natural </font>
- pos_of_rightmost_non_whitespace <font id="function_arguments">( vector              : string; result_if_not_found : natural := 1 ) </font> <font id="function_return">return natural </font>
- valid_length <font id="function_arguments">(    -- of string excluding trailing NULs vector              : string ) </font> <font id="function_return">return natural </font>
- get_string_between_delimiters <font id="function_arguments">( val        : string; delim_left : character; delim_right: character; start_from : SIDE;          -- search from left or right  (Only RIGHT implemented so far) occurrence  : positive := 1 -- stop on N'th occurrence of delimeter pair. Default first occurrence ) </font> <font id="function_return">return string </font>
- return_string_if_true <font id="function_arguments">( val        : string; return_val : boolean ) </font> <font id="function_return">return string </font>
- return_string1_if_true_otherwise_string2 <font id="function_arguments">( val1        : string; val2        : string; return_val : boolean ) </font> <font id="function_return">return string </font>
- to_upper <font id="function_arguments">( val  : string ) </font> <font id="function_return">return string </font>
- fill_string <font id="function_arguments">( val       : character; width     : natural ) </font> <font id="function_return">return string </font>
- pad_string <font id="function_arguments">( val   : string; char  : character; width : natural; side  : side := LEFT ) </font> <font id="function_return">return string </font>
- replace_backslash_n_with_lf <font id="function_arguments">( source : string ) </font> <font id="function_return">return string </font>
- replace_backslash_r_with_lf <font id="function_arguments">( source : string ) </font> <font id="function_return">return string </font>
- remove_initial_chars <font id="function_arguments">( source : string; num    : natural ) </font> <font id="function_return">return string </font>
- wrap_lines <font id="function_arguments">( constant text_string     : string; constant alignment_pos1  : natural;  -- Line position of first aligned character in line 1 constant alignment_pos2  : natural;  -- Line position of first aligned character in line 2, etc... constant line_width      : natural ) </font> <font id="function_return">return string </font>
- wrap_lines <font id="function_arguments">( variable text_lines      : inout line; constant alignment_pos1  : natural;  -- Line position prior to first aligned character (incl. Prefix) constant alignment_pos2  : natural; constant line_width      : natural ) </font> <font id="function_return">return ()</font>
- prefix_lines <font id="function_arguments">( variable text_lines  : inout line; constant prefix      : string := C_LOG_PREFIX ) </font> <font id="function_return">return ()</font>
- replace <font id="function_arguments">( val           : string; target_char   : character; exchange_char : character ) </font> <font id="function_return">return string </font>
- replace <font id="function_arguments">( variable text_line : inout line; target_char        : character; exchange_char      : character ) </font> <font id="function_return">return ()</font>
- to_string <font id="function_arguments">( val             : boolean; width           : natural; justified       : side; format_spaces   : t_format_spaces; truncate        : t_truncate_string := DISALLOW_TRUNCATE ) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">( val       : boolean; width     : natural; justified : side        := right; format: t_format_string := AS_IS ) </font> <font id="function_return">return string </font>
**Description**
This function has been deprecated and will be removed in the next major releaseDEPRECATED
- to_string <font id="function_arguments">( val       : integer; width     : natural; justified : side            := right; format    : t_format_string := AS_IS ) </font> <font id="function_return">return string </font>
**Description**
This function has been deprecated and will be removed in the next major releaseDEPRECATED
- to_string <font id="function_arguments">( val     : std_logic_vector; radix   : t_radix; format  : t_format_zeros := KEEP_LEADING_0;  -- | SKIP_LEADING_0 prefix  : t_radix_prefix := EXCL_RADIX -- Insert radix prefix in string? ) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">( val     : unsigned; radix   : t_radix; format  : t_format_zeros := KEEP_LEADING_0;  -- | SKIP_LEADING_0 prefix  : t_radix_prefix := EXCL_RADIX -- Insert radix prefix in string? ) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">( val     : signed; radix   : t_radix; format  : t_format_zeros := KEEP_LEADING_0;  -- | SKIP_LEADING_0 prefix  : t_radix_prefix := EXCL_RADIX -- Insert radix prefix in string? ) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">( val     : t_slv_array; radix   : t_radix        := HEX_BIN_IF_INVALID; format  : t_format_zeros := KEEP_LEADING_0;  -- | SKIP_LEADING_0 prefix  : t_radix_prefix := EXCL_RADIX -- Insert radix prefix in string? ) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">( val     : t_signed_array; radix   : t_radix        := HEX_BIN_IF_INVALID; format  : t_format_zeros := KEEP_LEADING_0;  -- | SKIP_LEADING_0 prefix  : t_radix_prefix := EXCL_RADIX -- Insert radix prefix in string? ) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">( val     : t_unsigned_array; radix   : t_radix        := HEX_BIN_IF_INVALID; format  : t_format_zeros := KEEP_LEADING_0;  -- | SKIP_LEADING_0 prefix  : t_radix_prefix := EXCL_RADIX -- Insert radix prefix in string? ) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">( val     : real_vector ) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">( val     : time_vector ) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">( val       : t_alert_level; width     : natural; justified : side    := right ) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">( val       : t_msg_id; width     : natural; justified : side    := right ) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">( val       : t_attention; width     : natural; justified : side    := right ) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">( val       : t_check_type; width     : natural; justified : side    := right ) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">( val   : t_alert_attention_counters; order : t_order := FINAL ) </font> <font id="function_return">return ()</font>
- to_string <font id="function_arguments">( val   : t_check_counters_array; order : t_order := FINAL ) </font> <font id="function_return">return ()</font>
- ascii_to_char <font id="function_arguments">( ascii_pos   : integer range 0 to 255; ascii_allow : t_ascii_allow := ALLOW_ALL ) </font> <font id="function_return">return character </font>
- char_to_ascii <font id="function_arguments">( char   : character ) </font> <font id="function_return">return integer </font>
- to_string <font id="function_arguments">( val : string ) </font> <font id="function_return">return string </font>
**Description**
return string with only valid ascii characters
- add_msg_delimiter <font id="function_arguments">( msg : string ) </font> <font id="function_return">return string </font>
- timestamp_header <font id="function_arguments">( value : time; txt   : string) </font> <font id="function_return">return string </font>
**Description**
Returns a string with a timestamp and a text. Used in report headers
