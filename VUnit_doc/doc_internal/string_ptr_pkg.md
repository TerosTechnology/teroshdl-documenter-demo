# Package: string_ptr_pkg
## Constants
| Name                     | Type         | Value                | Description |
| ------------------------ | ------------ | -------------------- | ----------- |
| null_string_ptr          | string_ptr_t |  (ref => -1)         |             |
| string_ptr_t_code_length | positive     |  integer_code_length |             |
## Types
| Name         | Type | Description |
| ------------ | ---- | ----------- |
| string_ptr_t |      |             |
## Functions
- to_integer <font id="function_arguments">(    value : ptr_t
  )</font> <font id="function_return">return integer</font>
- deallocate <font id="function_arguments">(    ptr : ptr_t
  )</font> <font id="function_return">return ()</font>
- set <font id="function_arguments">(    ptr   : ptr_t;
    index : positive;
    value : val_t
  )</font> <font id="function_return">return ()</font>
- reallocate <font id="function_arguments">(    ptr    : ptr_t;
    length : natural;
    value  : val_t := val_t'low
  )</font> <font id="function_return">return ()</font>
- reallocate <font id="function_arguments">(    ptr   : ptr_t;
    value : vec_t
  )</font> <font id="function_return">return ()</font>
- resize <font id="function_arguments">(    ptr    : ptr_t;
    length : natural;
    drop   : natural := 0;
    value  : val_t   := val_t'low
  )</font> <font id="function_return">return ()</font>
- encode <font id="function_arguments">(    data : ptr_t
  )</font> <font id="function_return">return string</font>
- decode <font id="function_arguments">(    code : string
  )</font> <font id="function_return">return ptr_t</font>
- decode <font id="function_arguments">(    constant code   : string;
    variable index  : inout positive;
    variable result : out ptr_t
  )</font> <font id="function_return">return ()</font>
