# Package: std_logic_arith

- **File**: std_logic_arith.vhdl
## Types

| Name     | Type                                   | Description |
| -------- | -------------------------------------- | ----------- |
| UNSIGNED | array (NATURAL range <>) of STD_LOGIC  |             |
| SIGNED   | array (NATURAL range <>) of STD_LOGIC  |             |
## Functions
- SHL <font id="function_arguments">(ARG: UNSIGNED;<br><span style="padding-left:20px"> COUNT: UNSIGNED) </font> <font id="function_return">return UNSIGNED </font>
- SHL <font id="function_arguments">(ARG: SIGNED;<br><span style="padding-left:20px"> COUNT: UNSIGNED) </font> <font id="function_return">return SIGNED </font>
- SHR <font id="function_arguments">(ARG: UNSIGNED;<br><span style="padding-left:20px"> COUNT: UNSIGNED) </font> <font id="function_return">return UNSIGNED </font>
- SHR <font id="function_arguments">(ARG: SIGNED;<br><span style="padding-left:20px"> COUNT: UNSIGNED) </font> <font id="function_return">return SIGNED </font>
- CONV_INTEGER <font id="function_arguments">(ARG: INTEGER) </font> <font id="function_return">return INTEGER </font>
- CONV_INTEGER <font id="function_arguments">(ARG: UNSIGNED) </font> <font id="function_return">return INTEGER </font>
- CONV_INTEGER <font id="function_arguments">(ARG: SIGNED) </font> <font id="function_return">return INTEGER </font>
- CONV_INTEGER <font id="function_arguments">(ARG: STD_ULOGIC) </font> <font id="function_return">return SMALL_INT </font>
- CONV_UNSIGNED <font id="function_arguments">(ARG: INTEGER;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return UNSIGNED </font>
- CONV_UNSIGNED <font id="function_arguments">(ARG: UNSIGNED;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return UNSIGNED </font>
- CONV_UNSIGNED <font id="function_arguments">(ARG: SIGNED;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return UNSIGNED </font>
- CONV_UNSIGNED <font id="function_arguments">(ARG: STD_ULOGIC;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return UNSIGNED </font>
- CONV_SIGNED <font id="function_arguments">(ARG: INTEGER;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return SIGNED </font>
- CONV_SIGNED <font id="function_arguments">(ARG: UNSIGNED;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return SIGNED </font>
- CONV_SIGNED <font id="function_arguments">(ARG: SIGNED;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return SIGNED </font>
- CONV_SIGNED <font id="function_arguments">(ARG: STD_ULOGIC;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return SIGNED </font>
- CONV_STD_LOGIC_VECTOR <font id="function_arguments">(ARG: INTEGER;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return STD_LOGIC_VECTOR </font>
- CONV_STD_LOGIC_VECTOR <font id="function_arguments">(ARG: UNSIGNED;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return STD_LOGIC_VECTOR </font>
- CONV_STD_LOGIC_VECTOR <font id="function_arguments">(ARG: SIGNED;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return STD_LOGIC_VECTOR </font>
- CONV_STD_LOGIC_VECTOR <font id="function_arguments">(ARG: STD_ULOGIC;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return STD_LOGIC_VECTOR </font>
- EXT <font id="function_arguments">(ARG: STD_LOGIC_VECTOR;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return STD_LOGIC_VECTOR </font>
</br>**Description**
 zero extend STD_LOGIC_VECTOR (ARG) to SIZE, 
 SIZE < 0 is same as SIZE = 0
 returns STD_LOGIC_VECTOR(SIZE-1 downto 0)

- SXT <font id="function_arguments">(ARG: STD_LOGIC_VECTOR;<br><span style="padding-left:20px"> SIZE: INTEGER) </font> <font id="function_return">return STD_LOGIC_VECTOR </font>
</br>**Description**
 sign extend STD_LOGIC_VECTOR (ARG) to SIZE, 
 SIZE < 0 is same as SIZE = 0
 return STD_LOGIC_VECTOR(SIZE-1 downto 0)

