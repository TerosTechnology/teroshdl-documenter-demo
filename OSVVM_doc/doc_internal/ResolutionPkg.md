# Package: ResolutionPkg

## Constants

| Name                     | Type           | Value  | Description |
| ------------------------ | -------------- | ------ | ----------- |
| MULTIPLE_DRIVER_SEVERITY | severity_level |  ERROR |             |
## Types

| Name                   | Type                                             | Description                                   |
| ---------------------- | ------------------------------------------------ | --------------------------------------------- |
| std_logic_vector_max_c | array (natural range <>) of std_logic_max        | for non VHDL-2008                             |
| unsigned_max_c         | array (natural range <>) of std_logic_max        | for non VHDL-2008                             |
| signed_max_c           | array (natural range <>) of std_logic_max        | for non VHDL-2008                             |
| bit_vector_max_c       | array (natural range <>) of bit_max              | for non VHDL-2008                             |
| integer_vector_max_c   | array (natural range <>) of integer_max          | for non VHDL-2008                             |
| time_vector_max_c      | array (natural range <>) of time_max             | for non VHDL-2008                             |
| real_vector_max_c      | array (natural range <>) of real_max             | for non VHDL-2008                             |
| string_max_c           | array (positive range <>) of character_max       | for non VHDL-2008                             |
| boolean_vector_max_c   | array (natural range <>) of boolean_max          | for non VHDL-2008                             |
| integer_vector_sum_c   | array (natural range <>) of integer_sum          | for non VHDL-2008                             |
| time_vector_sum_c      | array (natural range <>) of time_sum             | for non VHDL-2008                             |
| real_vector_sum_c      | array (natural range <>) of real_sum             | for non VHDL-2008                             |
| resolved_string        | array (positive range <>) of resolved_character  | will change to subtype -- assert but no init  |
## Functions
- resolved_max <font id="function_arguments">( s : std_ulogic_vector) </font> <font id="function_return">return std_ulogic </font>
**Description**
resolved_max  return maximum value.    No initializations required on ports, default of type'left is ok
- resolved_max <font id="function_arguments">( s : bit_vector) </font> <font id="function_return">return bit </font>
- resolved_max <font id="function_arguments">( s : integer_vector ) </font> <font id="function_return">return integer </font>
- resolved_max <font id="function_arguments">( s : time_vector ) </font> <font id="function_return">return time </font>
- resolved_max <font id="function_arguments">( s : real_vector ) </font> <font id="function_return">return real </font>
- resolved_max <font id="function_arguments">( s : string) </font> <font id="function_return">return character </font>
- resolved_max <font id="function_arguments">( s : boolean_vector) </font> <font id="function_return">return boolean </font>
- resolved_sum <font id="function_arguments">( s : integer_vector ) </font> <font id="function_return">return integer </font>
**Description**
return sum of values that /= type'leftNo initializations required on ports, default of type'left is ok
- resolved_sum <font id="function_arguments">( s : time_vector ) </font> <font id="function_return">return time </font>
- resolved_sum <font id="function_arguments">( s : real_vector ) </font> <font id="function_return">return real </font>
- resolved_weak <font id="function_arguments">(s : std_ulogic_vector) </font> <font id="function_return">return std_ulogic </font>
**Description**
no init, type'left
- resolved <font id="function_arguments">( s : integer_vector ) </font> <font id="function_return">return integer </font>
**Description**
legacy stuffrequires ports to be initialized to 0 in the appropriate type.  
- resolved <font id="function_arguments">( s : time_vector ) </font> <font id="function_return">return time </font>
- resolved <font id="function_arguments">( s : real_vector ) </font> <font id="function_return">return real </font>
- resolved <font id="function_arguments">(s : string) </font> <font id="function_return">return character </font>
**Description**
same as resolved_max
- resolved <font id="function_arguments">( s : boolean_vector) </font> <font id="function_return">return boolean </font>
