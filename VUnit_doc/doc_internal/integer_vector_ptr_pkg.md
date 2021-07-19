# Package: integer_vector_ptr_pkg

- **File**: integer_vector_ptr_pkg.vhd
## Constants

| Name                             | Type                 | Value                | Description |
| -------------------------------- | -------------------- | -------------------- | ----------- |
| null_integer_vector_ptr          | integer_vector_ptr_t |  (ref => -1)         |             |
| integer_vector_ptr_t_code_length | positive             |  integer_code_length |             |
## Types

| Name                 | Type | Description |
| -------------------- | ---- | ----------- |
| integer_vector_ptr_t |      |             |
## Functions
- to_integer <font id="function_arguments">( value : ptr_t ) </font> <font id="function_return">return integer </font>
- deallocate <font id="function_arguments">( ptr : ptr_t ) </font> <font id="function_return">return ()</font>
- set <font id="function_arguments">( ptr   : ptr_t;<br><span style="padding-left:20px"> index : natural;<br><span style="padding-left:20px"> value : val_t ) </font> <font id="function_return">return ()</font>
- reallocate <font id="function_arguments">( ptr    : ptr_t;<br><span style="padding-left:20px"> length : natural;<br><span style="padding-left:20px"> value  : val_t := 0 ) </font> <font id="function_return">return ()</font>
- resize <font id="function_arguments">( ptr    : ptr_t;<br><span style="padding-left:20px"> length : natural;<br><span style="padding-left:20px"> drop   : natural := 0;<br><span style="padding-left:20px"> value  : val_t   := 0 ) </font> <font id="function_return">return ()</font>
- encode <font id="function_arguments">( data : ptr_t ) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( code : string ) </font> <font id="function_return">return ptr_t </font>
- decode <font id="function_arguments">( constant code   : string;<br><span style="padding-left:20px"> variable index  : inout positive;<br><span style="padding-left:20px"> variable result : out ptr_t ) </font> <font id="function_return">return ()</font>
