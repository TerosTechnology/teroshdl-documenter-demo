# Package: codec_builder_pkg

## Constants

| Name                         | Type     | Value                                          | Description |
| ---------------------------- | -------- | ---------------------------------------------- | ----------- |
| integer_code_length          | positive |  4                                             |             |
| boolean_code_length          | positive |  1                                             |             |
| real_code_length             | positive |  boolean_code_length + 3 * integer_code_length |             |
| std_ulogic_code_length       | positive |  1                                             |             |
| bit_code_length              | positive |  1                                             |             |
| time_code_length             | positive |  8                                             |             |
| severity_level_code_length   | positive |  1                                             |             |
| file_open_status_code_length | positive |  1                                             |             |
| file_open_kind_code_length   | positive |  1                                             |             |
| complex_code_length          | positive |  2 * real_code_length                          |             |
| complex_polar_code_length    | positive |  2 * real_code_length                          |             |
## Types

| Name             | Type                                    | Description |
| ---------------- | --------------------------------------- | ----------- |
| std_ulogic_array | array (integer range <>) of std_ulogic  |             |
## Functions
- get_simulator_resolution <font id="function_arguments">()</font> <font id="function_return">return time </font>
- to_byte_array <font id="function_arguments">( constant value : bit_vector) </font> <font id="function_return">return string </font>
- from_byte_array <font id="function_arguments">( constant byte_array : string) </font> <font id="function_return">return bit_vector </font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   integer) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   real) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   time) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   boolean) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   bit) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   std_ulogic) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   severity_level) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   file_open_status) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   file_open_kind) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   character) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   std_ulogic_array) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   string) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   bit_vector) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   std_ulogic_vector) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   complex) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   complex_polar) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   ieee.numeric_bit.unsigned) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   ieee.numeric_bit.signed) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   ieee.numeric_std.unsigned) </font> <font id="function_return">return ()</font>
- decode <font id="function_arguments">( constant code   :       string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out   ieee.numeric_std.signed) </font> <font id="function_return">return ()</font>
- encode_array_header <font id="function_arguments">( constant range_left1   : string;<br><span style="padding-left:20px"> constant range_right1  : string;<br><span style="padding-left:20px"> constant is_ascending1 : string;<br><span style="padding-left:20px"> constant range_left2   : string := "";<br><span style="padding-left:20px"> constant range_right2  : string := "";<br><span style="padding-left:20px"> constant is_ascending2 : string := "T") </font> <font id="function_return">return string </font>
