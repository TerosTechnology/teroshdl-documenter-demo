# Package: string_ops
## Types
| Name        | Type | Description |
| ----------- | ---- | ----------- |
| line_vector |      |             |
| lines_t     |      |             |
## Functions
- count <font id="function_arguments">(    constant s : string;
    constant substring : string;
    constant start : natural := 0;
    constant stop : natural := 0)</font> <font id="function_return">return natural</font>
- count <font id="function_arguments">(    constant s : string;
    constant char : character := ' ';
    constant start : natural := 0;
    constant stop : natural := 0)</font> <font id="function_return">return natural</font>
- find <font id="function_arguments">(    constant s : string;
    constant substring : string;
    constant start : natural := 0;
    constant stop : natural := 0)</font> <font id="function_return">return natural</font>
- find <font id="function_arguments">(    constant s : string;
    constant char : character;
    constant start : natural := 0;
    constant stop : natural := 0)</font> <font id="function_return">return natural</font>
- strip <font id="function_arguments">(    str : string;
    chars : string := " ")</font> <font id="function_return">return string</font>
- rstrip <font id="function_arguments">(    str : string;
    chars : string := " ")</font> <font id="function_return">return string</font>
- lstrip <font id="function_arguments">(    str : string;
    chars : string := " ")</font> <font id="function_return">return string</font>
- image <font id="function_arguments">(    constant data : std_logic_vector)</font> <font id="function_return">return string</font>
- hex_image <font id="function_arguments">(    constant data : std_logic_vector)</font> <font id="function_return">return string</font>
- replace <font id="function_arguments">(    constant s      : string;
    constant old_segment : character;
    constant new_segment : character;
    constant cnt : in natural := natural'high)</font> <font id="function_return">return string</font>
- replace <font id="function_arguments">(    constant s      : string;
    constant old_segment : string;
    constant new_segment : character;
    constant cnt : in natural := natural'high)</font> <font id="function_return">return string</font>
- replace <font id="function_arguments">(    constant s      : string;
    constant old_segment : character;
    constant new_segment : string;
    constant cnt : in natural := natural'high)</font> <font id="function_return">return string</font>
- replace <font id="function_arguments">(    constant s      : string;
    constant old_segment : string;
    constant new_segment : string;
    constant cnt : in natural := natural'high)</font> <font id="function_return">return string</font>
- title <font id="function_arguments">(    constant s : string)</font> <font id="function_return">return string</font>
- upper <font id="function_arguments">(    constant s : string)</font> <font id="function_return">return string</font>
- lower <font id="function_arguments">(    constant s : string)</font> <font id="function_return">return string</font>
- to_integer_string <font id="function_arguments">(    constant value : unsigned)</font> <font id="function_return">return string</font>
- to_integer_string <font id="function_arguments">(    constant value : signed)</font> <font id="function_return">return string</font>
- to_integer_string <font id="function_arguments">(    constant value : std_logic_vector)</font> <font id="function_return">return string</font>
- to_nibble_string <font id="function_arguments">(    constant value : unsigned)</font> <font id="function_return">return string</font>
- to_nibble_string <font id="function_arguments">(    constant value : std_logic_vector)</font> <font id="function_return">return string</font>
- to_nibble_string <font id="function_arguments">(    constant value : signed)</font> <font id="function_return">return string</font>
