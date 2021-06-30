# Package: ResolutionPkg

## Constants

| Name                     | Type           | Value  | Description |
| ------------------------ | -------------- | ------ | ----------- |
| MULTIPLE_DRIVER_SEVERITY | severity_level |  ERROR |             |
## Types

| Name                   | Type | Description                                   |
| ---------------------- | ---- | --------------------------------------------- |
| std_logic_vector_max_c |      | for non VHDL-2008                             |
| unsigned_max_c         |      | for non VHDL-2008                             |
| signed_max_c           |      | for non VHDL-2008                             |
| bit_vector_max_c       |      | for non VHDL-2008                             |
| integer_vector_max_c   |      | for non VHDL-2008                             |
| time_vector_max_c      |      | for non VHDL-2008                             |
| real_vector_max_c      |      | for non VHDL-2008                             |
| string_max_c           |      | for non VHDL-2008                             |
| boolean_vector_max_c   |      | for non VHDL-2008                             |
| integer_vector_sum_c   |      | for non VHDL-2008                             |
| time_vector_sum_c      |      | for non VHDL-2008                             |
| real_vector_sum_c      |      | for non VHDL-2008                             |
| resolved_string        |      | will change to subtype -- assert but no init  |
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
- Extend <font id="function_arguments">(A: std_logic_vector; Size : natural) </font> <font id="function_return">return std_logic_vector </font>
- Reduce <font id="function_arguments">(A: std_logic_vector; Size : natural) </font> <font id="function_return">return std_logic_vector </font>
- ToTransaction <font id="function_arguments">(A : std_logic_vector) </font> <font id="function_return">return std_logic_vector_max_c </font>
- ToTransaction <font id="function_arguments">(A : integer; Size : natural) </font> <font id="function_return">return std_logic_vector_max_c </font>
- FromTransaction <font id="function_arguments">(A: std_logic_vector_max_c) </font> <font id="function_return">return std_logic_vector </font>
- FromTransaction <font id="function_arguments">(A: std_logic_vector_max_c) </font> <font id="function_return">return integer </font>
- ToTransaction <font id="function_arguments">(A : std_logic_vector) </font> <font id="function_return">return std_logic_vector_max </font>
**Description**
ToTransaction and FromTransaction for _max provided to support a common methodology, conversions are not needed
- ToTransaction <font id="function_arguments">(A : integer; Size : natural) </font> <font id="function_return">return std_logic_vector_max </font>
- FromTransaction <font id="function_arguments">(A: std_logic_vector_max) </font> <font id="function_return">return std_logic_vector </font>
- FromTransaction <font id="function_arguments">(A: std_logic_vector_max) </font> <font id="function_return">return integer </font>
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
