# Package: integer_vector_ptr_pkg

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
- set <font id="function_arguments">( ptr   : ptr_t; index : natural; value : val_t ) </font> <font id="function_return">return ()</font>
- reallocate <font id="function_arguments">( ptr    : ptr_t; length : natural; value  : val_t := 0 ) </font> <font id="function_return">return ()</font>
- resize <font id="function_arguments">( ptr    : ptr_t; length : natural; drop   : natural := 0; value  : val_t   := 0 ) </font> <font id="function_return">return ()</font>
- encode <font id="function_arguments">( data : ptr_t ) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( code : string ) </font> <font id="function_return">return ptr_t </font>
- decode <font id="function_arguments">( constant code   : string; variable index  : inout positive; variable result : out ptr_t ) </font> <font id="function_return">return ()</font>
