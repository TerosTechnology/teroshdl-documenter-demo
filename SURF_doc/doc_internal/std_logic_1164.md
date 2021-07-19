# Package: std_logic_1164

- **File**: std_logic_1164.vhdl
## Types

| Name              | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| std_ulogic        | ('U',<br><span style="padding-left:20px">  --  Uninitialized,<br><span style="padding-left:20px"> this is also the default value. 'X',<br><span style="padding-left:20px">  --  Unknown / conflict value (forcing level). '0',<br><span style="padding-left:20px">  --  0 (forcing level). '1',<br><span style="padding-left:20px">  --  1 (forcing level). 'Z',<br><span style="padding-left:20px">  --  High impedance. 'W',<br><span style="padding-left:20px">  --  Unknown / conflict (weak level). 'L',<br><span style="padding-left:20px">  --  0 (weak level). 'H',<br><span style="padding-left:20px">  --  1 (weak level). )  |                         |
| std_ulogic_vector | array (natural range <>) of std_ulogic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |  Vector of logic state. |
| std_logic_vector  | array (natural range <>) of std_logic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  Vector of std_logic.   |
## Functions
- resolved <font id="function_arguments">(s : std_ulogic_vector) </font> <font id="function_return">return std_ulogic </font>
**Description**
 Resolution function. If S is empty, returns 'Z'. If S has one element, return the element. Otherwise, 'U' is the strongest.      then  'X'      then  '0' and '1'      then  'W'      then  'H' and 'L'      then  'Z'.
- to_bit <font id="function_arguments">(s : std_ulogic;<br><span style="padding-left:20px"> xmap : bit := '0') </font> <font id="function_return">return bit </font>
**Description**
 Conversion functions. The result range (for vectors) is S'Length - 1 downto 0. XMAP is return for values not in '0', '1', 'L', 'H'.
- to_bitvector <font id="function_arguments">(s : std_logic_vector;<br><span style="padding-left:20px"> xmap : bit := '0') </font> <font id="function_return">return bit_vector </font>
- to_bitvector <font id="function_arguments">(s : std_ulogic_vector;<br><span style="padding-left:20px"> xmap : bit := '0') </font> <font id="function_return">return bit_vector </font>
- to_stdulogic <font id="function_arguments">(b : bit) </font> <font id="function_return">return std_ulogic </font>
- to_stdlogicvector <font id="function_arguments">(b : bit_vector) </font> <font id="function_return">return std_logic_vector </font>
- to_stdlogicvector <font id="function_arguments">(s : std_ulogic_vector) </font> <font id="function_return">return std_logic_vector </font>
- to_stdulogicvector <font id="function_arguments">(b : bit_vector) </font> <font id="function_return">return std_ulogic_vector </font>
- to_stdulogicvector <font id="function_arguments">(s : std_logic_vector) </font> <font id="function_return">return std_ulogic_vector </font>
- to_X01 <font id="function_arguments">(s : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
**Description**
 Normalization. The result range (for vectors) is 1 to S'Length.
- to_X01 <font id="function_arguments">(s : std_ulogic_vector) </font> <font id="function_return">return std_ulogic_vector </font>
- to_X01 <font id="function_arguments">(s : std_ulogic) </font> <font id="function_return">return X01 </font>
- to_X01 <font id="function_arguments">(b : bit_vector) </font> <font id="function_return">return std_logic_vector </font>
- to_X01 <font id="function_arguments">(b : bit_vector) </font> <font id="function_return">return std_ulogic_vector </font>
- to_X01 <font id="function_arguments">(b : bit) </font> <font id="function_return">return X01 </font>
- to_X01Z <font id="function_arguments">(s : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
- to_X01Z <font id="function_arguments">(s : std_ulogic_vector) </font> <font id="function_return">return std_ulogic_vector </font>
- to_X01Z <font id="function_arguments">(s : std_ulogic) </font> <font id="function_return">return X01Z </font>
- to_X01Z <font id="function_arguments">(b : bit_vector) </font> <font id="function_return">return std_logic_vector </font>
- to_X01Z <font id="function_arguments">(b : bit_vector) </font> <font id="function_return">return std_ulogic_vector </font>
- to_X01Z <font id="function_arguments">(b : bit) </font> <font id="function_return">return X01Z </font>
- to_UX01 <font id="function_arguments">(s : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
- to_UX01 <font id="function_arguments">(s : std_ulogic_vector) </font> <font id="function_return">return std_ulogic_vector </font>
- to_UX01 <font id="function_arguments">(s : std_ulogic) </font> <font id="function_return">return UX01 </font>
- to_UX01 <font id="function_arguments">(b : bit_vector) </font> <font id="function_return">return std_logic_vector </font>
- to_UX01 <font id="function_arguments">(b : bit_vector) </font> <font id="function_return">return std_ulogic_vector </font>
- to_UX01 <font id="function_arguments">(b : bit) </font> <font id="function_return">return UX01 </font>
- rising_edge <font id="function_arguments">(signal s : std_ulogic) </font> <font id="function_return">return boolean </font>
**Description**
 Edge detection. An edge is detected in case of event on s, and X01 normalized value rises from 0 to 1 or falls from 1 to 0.
- falling_edge <font id="function_arguments">(signal s : std_ulogic) </font> <font id="function_return">return boolean </font>
- is_X <font id="function_arguments">(s : std_ulogic_vector) </font> <font id="function_return">return boolean </font>
**Description**
 Test for unknown.  Only 0, 1, L and H are known values.
- is_X <font id="function_arguments">(s : std_logic_vector) </font> <font id="function_return">return boolean </font>
- is_X <font id="function_arguments">(s : std_ulogic) </font> <font id="function_return">return boolean </font>
