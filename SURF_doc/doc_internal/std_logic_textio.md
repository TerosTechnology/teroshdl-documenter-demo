# Package: STD_LOGIC_TEXTIO

- **File**: std_logic_textio.vhdl
## Functions
- READ <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_ULOGIC) </font> <font id="function_return">return ()</font>
- READ <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_ULOGIC;<br><span style="padding-left:20px"> GOOD: out BOOLEAN) </font> <font id="function_return">return ()</font>
- READ <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_ULOGIC_VECTOR) </font> <font id="function_return">return ()</font>
- READ <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> GOOD: out BOOLEAN) </font> <font id="function_return">return ()</font>
- WRITE <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:in STD_ULOGIC;<br><span style="padding-left:20px"> JUSTIFIED:in SIDE := RIGHT;<br><span style="padding-left:20px"> FIELD:in WIDTH := 0) </font> <font id="function_return">return ()</font>
- WRITE <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:in STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> JUSTIFIED:in SIDE := RIGHT;<br><span style="padding-left:20px"> FIELD:in WIDTH := 0) </font> <font id="function_return">return ()</font>
- READ <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_LOGIC_VECTOR) </font> <font id="function_return">return ()</font>
**Description**
 Read and Write procedures for STD_LOGIC_VECTOR

- READ <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_LOGIC_VECTOR;<br><span style="padding-left:20px"> GOOD: out BOOLEAN) </font> <font id="function_return">return ()</font>
- WRITE <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:in STD_LOGIC_VECTOR;<br><span style="padding-left:20px"> JUSTIFIED:in SIDE := RIGHT;<br><span style="padding-left:20px"> FIELD:in WIDTH := 0) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_ULOGIC_VECTOR) </font> <font id="function_return">return ()</font>
**Description**

 Read and Write procedures for Hex and Octal values.
 The values appear in the file as a series of characters
 between 0-F (Hex), or 0-7 (Octal) respectively.

 Hex

- HREAD <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> GOOD: out BOOLEAN) </font> <font id="function_return">return ()</font>
- HWRITE <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:in STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> JUSTIFIED:in SIDE := RIGHT;<br><span style="padding-left:20px"> FIELD:in WIDTH := 0) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_LOGIC_VECTOR) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_LOGIC_VECTOR;<br><span style="padding-left:20px"> GOOD: out BOOLEAN) </font> <font id="function_return">return ()</font>
- HWRITE <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:in STD_LOGIC_VECTOR;<br><span style="padding-left:20px"> JUSTIFIED:in SIDE := RIGHT;<br><span style="padding-left:20px"> FIELD:in WIDTH := 0) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_ULOGIC_VECTOR) </font> <font id="function_return">return ()</font>
**Description**
 Octal

- OREAD <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> GOOD: out BOOLEAN) </font> <font id="function_return">return ()</font>
- OWRITE <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:in STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> JUSTIFIED:in SIDE := RIGHT;<br><span style="padding-left:20px"> FIELD:in WIDTH := 0) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_LOGIC_VECTOR) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:out STD_LOGIC_VECTOR;<br><span style="padding-left:20px"> GOOD: out BOOLEAN) </font> <font id="function_return">return ()</font>
- OWRITE <font id="function_arguments">(L:inout LINE;<br><span style="padding-left:20px"> VALUE:in STD_LOGIC_VECTOR;<br><span style="padding-left:20px"> JUSTIFIED:in SIDE := RIGHT;<br><span style="padding-left:20px"> FIELD:in WIDTH := 0) </font> <font id="function_return">return ()</font>
