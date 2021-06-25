# Package: ResolutionPkg
## Constants
| Name                     | Type           | Value  | Description |
| ------------------------ | -------------- | ------ | ----------- |
| MULTIPLE_DRIVER_SEVERITY | severity_level |  ERROR |             |
## Types
| Name                   | Type | Description |
| ---------------------- | ---- | ----------- |
| std_logic_vector_max_c |      |             |
| unsigned_max_c         |      |             |
| signed_max_c           |      |             |
| bit_vector_max_c       |      |             |
| integer_vector_max_c   |      |             |
| time_vector_max_c      |      |             |
| real_vector_max_c      |      |             |
| string_max_c           |      |             |
| boolean_vector_max_c   |      |             |
| integer_vector_sum_c   |      |             |
| time_vector_sum_c      |      |             |
| real_vector_sum_c      |      |             |
| resolved_string        |      |             |
## Functions
- resolved_max <font id="function_arguments">( s : std_ulogic_vector)</font> <font id="function_return">return std_ulogic</font>
- resolved_max <font id="function_arguments">( s : bit_vector)</font> <font id="function_return">return bit</font>
- resolved_max <font id="function_arguments">( s : integer_vector )</font> <font id="function_return">return integer</font>
- resolved_max <font id="function_arguments">( s : time_vector )</font> <font id="function_return">return time</font>
- resolved_max <font id="function_arguments">( s : real_vector )</font> <font id="function_return">return real</font>
- resolved_max <font id="function_arguments">( s : string)</font> <font id="function_return">return character</font>
- resolved_max <font id="function_arguments">( s : boolean_vector)</font> <font id="function_return">return boolean</font>
- Extend <font id="function_arguments">(A: std_logic_vector; Size : natural)</font> <font id="function_return">return std_logic_vector</font>
- Reduce <font id="function_arguments">(A: std_logic_vector; Size : natural)</font> <font id="function_return">return std_logic_vector</font>
- ToTransaction <font id="function_arguments">(A : std_logic_vector)</font> <font id="function_return">return std_logic_vector_max_c</font>
- ToTransaction <font id="function_arguments">(A : integer; Size : natural)</font> <font id="function_return">return std_logic_vector_max_c</font>
- FromTransaction <font id="function_arguments">(A: std_logic_vector_max_c)</font> <font id="function_return">return std_logic_vector</font>
- FromTransaction <font id="function_arguments">(A: std_logic_vector_max_c)</font> <font id="function_return">return integer</font>
- ToTransaction <font id="function_arguments">(A : std_logic_vector)</font> <font id="function_return">return std_logic_vector_max</font>
- ToTransaction <font id="function_arguments">(A : integer; Size : natural)</font> <font id="function_return">return std_logic_vector_max</font>
- FromTransaction <font id="function_arguments">(A: std_logic_vector_max)</font> <font id="function_return">return std_logic_vector</font>
- FromTransaction <font id="function_arguments">(A: std_logic_vector_max)</font> <font id="function_return">return integer</font>
- resolved_sum <font id="function_arguments">( s : integer_vector )</font> <font id="function_return">return integer</font>
- resolved_sum <font id="function_arguments">( s : time_vector )</font> <font id="function_return">return time</font>
- resolved_sum <font id="function_arguments">( s : real_vector )</font> <font id="function_return">return real</font>
- resolved_weak <font id="function_arguments">(s : std_ulogic_vector)</font> <font id="function_return">return std_ulogic</font>
- resolved <font id="function_arguments">( s : integer_vector )</font> <font id="function_return">return integer</font>
- resolved <font id="function_arguments">( s : time_vector )</font> <font id="function_return">return time</font>
- resolved <font id="function_arguments">( s : real_vector )</font> <font id="function_return">return real</font>
- resolved <font id="function_arguments">(s : string)</font> <font id="function_return">return character</font>
- resolved <font id="function_arguments">( s : boolean_vector)</font> <font id="function_return">return boolean</font>
