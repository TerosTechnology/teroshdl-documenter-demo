# Package: string_ops

## Types

| Name        | Type                              | Description |
| ----------- | --------------------------------- | ----------- |
| line_vector | array (natural range <>) of line  |             |
| lines_t     |                                   |             |
## Functions
- count <font id="function_arguments">( constant s : string;<br><span style="padding-left:20px"> constant substring : string;<br><span style="padding-left:20px"> constant start : natural := 0;<br><span style="padding-left:20px"> constant stop : natural := 0) </font> <font id="function_return">return natural </font>
- count <font id="function_arguments">( constant s : string;<br><span style="padding-left:20px"> constant char : character := ' ';<br><span style="padding-left:20px"> constant start : natural := 0;<br><span style="padding-left:20px"> constant stop : natural := 0) </font> <font id="function_return">return natural </font>
- find <font id="function_arguments">( constant s : string;<br><span style="padding-left:20px"> constant substring : string;<br><span style="padding-left:20px"> constant start : natural := 0;<br><span style="padding-left:20px"> constant stop : natural := 0) </font> <font id="function_return">return natural </font>
- find <font id="function_arguments">( constant s : string;<br><span style="padding-left:20px"> constant char : character;<br><span style="padding-left:20px"> constant start : natural := 0;<br><span style="padding-left:20px"> constant stop : natural := 0) </font> <font id="function_return">return natural </font>
- strip <font id="function_arguments">( str : string;<br><span style="padding-left:20px"> chars : string := " ") </font> <font id="function_return">return string </font>
- rstrip <font id="function_arguments">( str : string;<br><span style="padding-left:20px"> chars : string := " ") </font> <font id="function_return">return string </font>
- lstrip <font id="function_arguments">( str : string;<br><span style="padding-left:20px"> chars : string := " ") </font> <font id="function_return">return string </font>
- image <font id="function_arguments">( constant data : std_logic_vector) </font> <font id="function_return">return string </font>
- hex_image <font id="function_arguments">( constant data : std_logic_vector) </font> <font id="function_return">return string </font>
- replace <font id="function_arguments">( constant s      : string;<br><span style="padding-left:20px"> constant old_segment : character;<br><span style="padding-left:20px"> constant new_segment : character;<br><span style="padding-left:20px"> constant cnt : in natural := natural'high) </font> <font id="function_return">return string </font>
- replace <font id="function_arguments">( constant s      : string;<br><span style="padding-left:20px"> constant old_segment : string;<br><span style="padding-left:20px"> constant new_segment : character;<br><span style="padding-left:20px"> constant cnt : in natural := natural'high) </font> <font id="function_return">return string </font>
- replace <font id="function_arguments">( constant s      : string;<br><span style="padding-left:20px"> constant old_segment : character;<br><span style="padding-left:20px"> constant new_segment : string;<br><span style="padding-left:20px"> constant cnt : in natural := natural'high) </font> <font id="function_return">return string </font>
- replace <font id="function_arguments">( constant s      : string;<br><span style="padding-left:20px"> constant old_segment : string;<br><span style="padding-left:20px"> constant new_segment : string;<br><span style="padding-left:20px"> constant cnt : in natural := natural'high) </font> <font id="function_return">return string </font>
- title <font id="function_arguments">( constant s : string) </font> <font id="function_return">return string </font>
- upper <font id="function_arguments">( constant s : string) </font> <font id="function_return">return string </font>
- lower <font id="function_arguments">( constant s : string) </font> <font id="function_return">return string </font>
- to_integer_string <font id="function_arguments">( constant value : unsigned) </font> <font id="function_return">return string </font>
- to_integer_string <font id="function_arguments">( constant value : signed) </font> <font id="function_return">return string </font>
- to_integer_string <font id="function_arguments">( constant value : std_logic_vector) </font> <font id="function_return">return string </font>
- to_nibble_string <font id="function_arguments">( constant value : unsigned) </font> <font id="function_return">return string </font>
- to_nibble_string <font id="function_arguments">( constant value : std_logic_vector) </font> <font id="function_return">return string </font>
- to_nibble_string <font id="function_arguments">( constant value : signed) </font> <font id="function_return">return string </font>
