# Package: dict_pkg

- **File**: dict_pkg.vhd
## Constants

| Name      | Type   | Value                 | Description |
| --------- | ------ | --------------------- | ----------- |
| null_dict | dict_t |  (others => null_ptr) |             |
## Types

| Name   | Type | Description |
| ------ | ---- | ----------- |
| dict_t |      |             |
## Functions
- deallocate <font id="function_arguments">( variable dict : inout dict_t ) </font> <font id="function_return">return ()</font>
- set <font id="function_arguments">( dict       : dict_t;<br><span style="padding-left:20px"> key,<br><span style="padding-left:20px"> value : string ) </font> <font id="function_return">return ()</font>
- remove <font id="function_arguments">( dict : dict_t;<br><span style="padding-left:20px"> key  : string ) </font> <font id="function_return">return ()</font>
