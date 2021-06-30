# Package: queue_pkg

## Constants

| Name       | Type    | Value                                          | Description |
| ---------- | ------- | ---------------------------------------------- | ----------- |
| null_queue | queue_t |  (p_meta => null_ptr, data => null_string_ptr) |             |
## Types

| Name                 | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| queue_t              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |             |
| queue_vec_t          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |             |
| queue_element_type_t | ( vhdl_character, vhdl_integer, vunit_byte, vhdl_string, vhdl_boolean, vhdl_real, vhdl_bit, ieee_std_ulogic, vhdl_severity_level, vhdl_file_open_status, vhdl_file_open_kind, vhdl_bit_vector, vhdl_std_ulogic_vector, ieee_complex, ieee_complex_polar, ieee_numeric_bit_unsigned, ieee_numeric_bit_signed, ieee_numeric_std_unsigned, ieee_numeric_std_signed, vhdl_time, vunit_integer_vector_ptr_t, vunit_string_ptr_t, vunit_queue_t, vunit_integer_array_t, vhdl_boolean_vector, vhdl_integer_vector, vhdl_real_vector, vhdl_time_vector, ieee_ufixed, ieee_sfixed, ieee_float )  | Private     |
## Functions
- flush <font id="function_arguments">( queue : queue_t ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : integer ) </font> <font id="function_return">return ()</font>
- push_byte <font id="function_arguments">( queue : queue_t; value : natural range 0 to 255 ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : character ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : boolean ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : real ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : bit ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : std_ulogic ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : severity_level ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : file_open_status ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : file_open_kind ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : bit_vector ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : std_ulogic_vector ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : complex ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : complex_polar ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : ieee.numeric_bit.unsigned ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : ieee.numeric_bit.signed ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : ieee.numeric_std.unsigned ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : ieee.numeric_std.signed ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : string ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; value : time ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; variable value : inout integer_vector_ptr_t ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; variable value : inout string_ptr_t ) </font> <font id="function_return">return ()</font>
- push <font id="function_arguments">( queue : queue_t; variable value : inout queue_t ) </font> <font id="function_return">return ()</font>
- push_ref <font id="function_arguments">( constant queue : queue_t; value : inout integer_array_t ) </font> <font id="function_return">return ()</font>
- encode <font id="function_arguments">( data : queue_t ) </font> <font id="function_return">return string </font>
- decode <font id="function_arguments">( code : string ) </font> <font id="function_return">return queue_t </font>
- decode <font id="function_arguments">( constant code   : string; variable index  : inout positive; variable result : out queue_t ) </font> <font id="function_return">return ()</font>
- push_type <font id="function_arguments">( queue        : queue_t; element_type : queue_element_type_t ) </font> <font id="function_return">return ()</font>
- check_type <font id="function_arguments">( queue        : queue_t; element_type : queue_element_type_t ) </font> <font id="function_return">return ()</font>
- unsafe_push <font id="function_arguments">( queue : queue_t; value : character ) </font> <font id="function_return">return ()</font>
- push_variable_string <font id="function_arguments">( queue : queue_t; value : string ) </font> <font id="function_return">return ()</font>
- push_fix_string <font id="function_arguments">( queue : queue_t; value : string ) </font> <font id="function_return">return ()</font>
