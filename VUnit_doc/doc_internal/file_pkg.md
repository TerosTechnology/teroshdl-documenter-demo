# Package: file_pkg

## Constants

| Name         | Type      | Value                 | Description |
| ------------ | --------- | --------------------- | ----------- |
| null_file_id | file_id_t |  (p_data => null_ptr) |             |
## Types

| Name      | Type | Description |
| --------- | ---- | ----------- |
| file_id_t |      |             |
## Functions
- to_integer <font id="function_arguments">(file_id : file_id_t) </font> <font id="function_return">return integer </font>
- file_close <font id="function_arguments">(file_id : file_id_t) </font> <font id="function_return">return ()</font>
- file_open_for_write <font id="function_arguments">(file_id : inout file_id_t; file_name : string) </font> <font id="function_return">return ()</font>
- writeline <font id="function_arguments">(file_id : file_id_t; l : inout line) </font> <font id="function_return">return ()</font>
