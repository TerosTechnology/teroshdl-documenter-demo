# Package: com_debug_codec_builder_pkg
## Functions
- open_group <font id="function_arguments">(    variable l : inout line)</font> <font id="function_return">return ()</font>
- append_group <font id="function_arguments">(    variable l       : inout line;
    constant element : in    string)</font> <font id="function_return">return ()</font>
- close_group <font id="function_arguments">(    variable l      : inout line;
    variable code   : out   string;
    variable length : out   natural)</font> <font id="function_return">return ()</font>
- create_group <font id="function_arguments">(    constant num_of_elements : natural range 0 to 10;
    constant element1        : string := "";
    constant element2        : string := "";
    constant element3        : string := "";
    constant element4        : string := "";
    constant element5        : string := "";
    constant element6        : string := "";
    constant element7        : string := "";
    constant element8        : string := "";
    constant element9        : string := "";
    constant element10       : string := "")</font> <font id="function_return">return string</font>
- create_array_group <font id="function_arguments">(    constant arr           : string;
    constant range_left1   : string;
    constant range_right1  : string;
    constant is_ascending1 : boolean;
    constant range_left2   : string  := "";
    constant range_right2  : string  := "";
    constant is_ascending2 : boolean := true)</font> <font id="function_return">return string</font>
- escape_special_characters <font id="function_arguments">(    constant data : string)</font> <font id="function_return">return string</font>
- split_group <font id="function_arguments">(    constant grp                 : in    string;
    variable elements            : inout lines_t;
    constant max_num_of_elements : in    natural;
    variable length              : inout natural)</font> <font id="function_return">return ()</font>
- get_element <font id="function_arguments">(    constant grp      : in string;
    constant position : in natural)</font> <font id="function_return">return string</font>
- get_first_element <font id="function_arguments">(    constant grp : string)</font> <font id="function_return">return string</font>
- deallocate_elements <font id="function_arguments">(    variable elements : inout lines_t)</font> <font id="function_return">return ()</font>
- unescape_special_characters <font id="function_arguments">(    constant code : string)</font> <font id="function_return">return string</font>
