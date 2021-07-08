# Package: codec_pkg

## Types

| Name    | Type                             | Description |
| ------- | -------------------------------- | ----------- |
| range_t | array (integer range <>) of bit  |             |
## Functions
- encode <font id="function_arguments">( constant data : integer) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return integer </font>
- encode <font id="function_arguments">( constant data : real) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return real </font>
- encode <font id="function_arguments">( constant data : time) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return time </font>
- encode <font id="function_arguments">( constant data : boolean) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return boolean </font>
- encode <font id="function_arguments">( constant data : bit) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return bit </font>
- encode <font id="function_arguments">( constant data : std_ulogic) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return std_ulogic </font>
- encode <font id="function_arguments">( constant data : severity_level) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return severity_level </font>
- encode <font id="function_arguments">( constant data : file_open_status) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return file_open_status </font>
- encode <font id="function_arguments">( constant data : file_open_kind) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return file_open_kind </font>
- encode <font id="function_arguments">( constant data : character) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return character </font>
- encode <font id="function_arguments">( constant data : string) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return string </font>
- encode <font id="function_arguments">( constant data : bit_vector) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return bit_vector </font>
- encode <font id="function_arguments">( constant data : std_ulogic_vector) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return std_ulogic_vector </font>
- encode <font id="function_arguments">( constant data : complex) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return complex </font>
- encode <font id="function_arguments">( constant data : complex_polar) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return complex_polar </font>
- encode <font id="function_arguments">( constant data : ieee.numeric_bit.unsigned) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return ieee.numeric_bit.unsigned </font>
- encode <font id="function_arguments">( constant data : ieee.numeric_bit.signed) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return ieee.numeric_bit.signed </font>
- encode <font id="function_arguments">( constant data : ieee.numeric_std.unsigned) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return ieee.numeric_std.unsigned </font>
- encode <font id="function_arguments">( constant data : ieee.numeric_std.signed) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( constant code : string) </font> <font id="function_return">return ieee.numeric_std.signed </font>
- get_range <font id="function_arguments">( constant code : string) </font> <font id="function_return">return range_t </font>
- encode <font id="function_arguments">( constant data : std_ulogic_array) </font> <font id="function_return">return string </font>
