# Package: integer_array_pkg

- **File**: integer_array_pkg.vhd
## Constants

| Name               | Type            | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                       |
| ------------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| null_integer_array | integer_array_t |  (     length => 0,<br><span style="padding-left:20px">     width => 0,<br><span style="padding-left:20px">     height => 0,<br><span style="padding-left:20px">     depth => 0,<br><span style="padding-left:20px">     bit_width => 0,<br><span style="padding-left:20px">     is_signed => false,<br><span style="padding-left:20px">     lower_limit => integer'low,<br><span style="padding-left:20px">     upper_limit => integer'low,<br><span style="padding-left:20px">     data => null_ptr     ) | Ensure null_integer_array is the default VHDL value of the record |
## Types

| Name                | Type                                         | Description |
| ------------------- | -------------------------------------------- | ----------- |
| integer_array_t     |                                              |             |
| integer_array_vec_t | array (natural range <>) of integer_array_t  |             |
## Functions
- deallocate <font id="function_arguments">( variable arr : inout integer_array_t ) </font> <font id="function_return">return ()</font>
- set <font id="function_arguments">( arr   : integer_array_t;<br><span style="padding-left:20px"> idx   : integer;<br><span style="padding-left:20px"> value : integer ) </font> <font id="function_return">return ()</font>
- set <font id="function_arguments">( arr   : integer_array_t;<br><span style="padding-left:20px"> x,<br><span style="padding-left:20px">y   : integer;<br><span style="padding-left:20px"> value : integer ) </font> <font id="function_return">return ()</font>
- set <font id="function_arguments">( arr   : integer_array_t;<br><span style="padding-left:20px"> x,<br><span style="padding-left:20px">y,<br><span style="padding-left:20px">z : integer;<br><span style="padding-left:20px"> value : integer ) </font> <font id="function_return">return ()</font>
- append <font id="function_arguments">( variable arr : inout integer_array_t;<br><span style="padding-left:20px"> value        : integer ) </font> <font id="function_return">return ()</font>
- reshape <font id="function_arguments">( variable arr : inout integer_array_t;<br><span style="padding-left:20px"> length       : integer ) </font> <font id="function_return">return ()</font>
- reshape <font id="function_arguments">( variable arr  : inout integer_array_t;<br><span style="padding-left:20px"> width,<br><span style="padding-left:20px"> height : integer ) </font> <font id="function_return">return ()</font>
- reshape <font id="function_arguments">( variable arr         : inout integer_array_t;<br><span style="padding-left:20px"> width,<br><span style="padding-left:20px"> height,<br><span style="padding-left:20px"> depth : integer ) </font> <font id="function_return">return ()</font>
- save_csv <font id="function_arguments">( arr       : integer_array_t;<br><span style="padding-left:20px"> file_name : string ) </font> <font id="function_return">return ()</font>
- save_raw <font id="function_arguments">( arr       : integer_array_t;<br><span style="padding-left:20px"> file_name : string ) </font> <font id="function_return">return ()</font>
