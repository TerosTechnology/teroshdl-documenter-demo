# Package: integer_array_pkg
## Constants
| Name               | Type            | Value                                                                                                                                                                                                       | Description |
| ------------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| null_integer_array | integer_array_t |  (     length => 0,     width => 0,     height => 0,     depth => 0,     bit_width => 0,     is_signed => false,     lower_limit => integer'low,     upper_limit => integer'low,     data => null_ptr     ) |             |
## Types
| Name                | Type | Description |
| ------------------- | ---- | ----------- |
| integer_array_t     |      |             |
| integer_array_vec_t |      |             |
## Functions
- deallocate <font id="function_arguments">(    variable arr : inout integer_array_t
  )</font> <font id="function_return">return ()</font>
- set <font id="function_arguments">(    arr   : integer_array_t;
    idx   : integer;
    value : integer
  )</font> <font id="function_return">return ()</font>
- set <font id="function_arguments">(    arr   : integer_array_t;
    x,y   : integer;
    value : integer
  )</font> <font id="function_return">return ()</font>
- set <font id="function_arguments">(    arr   : integer_array_t;
    x,y,z : integer;
    value : integer
  )</font> <font id="function_return">return ()</font>
- append <font id="function_arguments">(    variable arr : inout integer_array_t;
    value        : integer
  )</font> <font id="function_return">return ()</font>
- reshape <font id="function_arguments">(    variable arr : inout integer_array_t;
    length       : integer
  )</font> <font id="function_return">return ()</font>
- reshape <font id="function_arguments">(    variable arr  : inout integer_array_t;
    width, height : integer
  )</font> <font id="function_return">return ()</font>
- reshape <font id="function_arguments">(    variable arr         : inout integer_array_t;
    width, height, depth : integer
  )</font> <font id="function_return">return ()</font>
- save_csv <font id="function_arguments">(    arr       : integer_array_t;
    file_name : string
  )</font> <font id="function_return">return ()</font>
- save_raw <font id="function_arguments">(    arr       : integer_array_t;
    file_name : string
  )</font> <font id="function_return">return ()</font>
