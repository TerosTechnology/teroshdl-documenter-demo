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
- to_integer <font id="function_arguments">( value : ptr_t ) </font> <font id="function_return">return integer </font>
- deallocate <font id="function_arguments">( ptr : ptr_t ) </font> <font id="function_return">return ()</font>
- set <font id="function_arguments">( ptr   : ptr_t;<br><span style="padding-left:20px"> index : positive;<br><span style="padding-left:20px"> value : val_t ) </font> <font id="function_return">return ()</font>
- reallocate <font id="function_arguments">( ptr    : ptr_t;<br><span style="padding-left:20px"> length : natural;<br><span style="padding-left:20px"> value  : val_t := val_t'low ) </font> <font id="function_return">return ()</font>
- reallocate <font id="function_arguments">( ptr   : ptr_t;<br><span style="padding-left:20px"> value : vec_t ) </font> <font id="function_return">return ()</font>
- resize <font id="function_arguments">( ptr    : ptr_t;<br><span style="padding-left:20px"> length : natural;<br><span style="padding-left:20px"> drop   : natural := 0;<br><span style="padding-left:20px"> value  : val_t   := val_t'low ) </font> <font id="function_return">return ()</font>
- encode <font id="function_arguments">( data : ptr_t ) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( code : string ) </font> <font id="function_return">return ptr_t </font>
- decode <font id="function_arguments">( constant code   : string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out ptr_t ) </font> <font id="function_return">return ()</font>
