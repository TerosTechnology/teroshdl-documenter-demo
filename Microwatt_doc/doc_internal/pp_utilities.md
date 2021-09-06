# Package: pp_utilities

- **File**: pp_utilities.vhd
## Functions
- to_std_logic <font id="function_arguments">(input : in boolean) </font> <font id="function_return">return std_logic </font>
- is_pow2 <font id="function_arguments">(input : in natural) </font> <font id="function_return">return boolean </font>
</br>**Description**
 Checks if a number is 2^n:

- log2 <font id="function_arguments">(input : in natural) </font> <font id="function_return">return natural </font>
</br>**Description**
! Calculates log2 with integers.

- wb_get_data_sel <font id="function_arguments">(size : in std_logic_vector(1 downto 0);<br><span style="padding-left:20px"> address : in std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
</br>**Description**
 Gets the value of the sel signals to the wishbone interconnect for the specified
 operand size and address.

