# Package: ResizePkg

## Functions
- Extend <font id="function_arguments">(A: std_logic_vector;<br><span style="padding-left:20px"> Size : natural) </font> <font id="function_return">return std_logic_vector </font>
- Reduce <font id="function_arguments">(A: std_logic_vector;<br><span style="padding-left:20px"> Size : natural) </font> <font id="function_return">return std_logic_vector </font>
- ToTransaction <font id="function_arguments">(A : std_logic_vector) </font> <font id="function_return">return std_logic_vector_max_c </font>
- ToTransaction <font id="function_arguments">(A : integer;<br><span style="padding-left:20px"> Size : natural) </font> <font id="function_return">return std_logic_vector_max_c </font>
- FromTransaction <font id="function_arguments">(A: std_logic_vector_max_c) </font> <font id="function_return">return std_logic_vector </font>
- FromTransaction <font id="function_arguments">(A: std_logic_vector_max_c) </font> <font id="function_return">return integer </font>
- ToTransaction <font id="function_arguments">(A : std_logic_vector) </font> <font id="function_return">return std_logic_vector_max </font>
**Description**
ToTransaction and FromTransaction for _max provided to support a common methodology, conversions are not needed
- ToTransaction <font id="function_arguments">(A : integer;<br><span style="padding-left:20px"> Size : natural) </font> <font id="function_return">return std_logic_vector_max </font>
- FromTransaction <font id="function_arguments">(A: std_logic_vector_max) </font> <font id="function_return">return std_logic_vector </font>
- FromTransaction <font id="function_arguments">(A: std_logic_vector_max) </font> <font id="function_return">return integer </font>
