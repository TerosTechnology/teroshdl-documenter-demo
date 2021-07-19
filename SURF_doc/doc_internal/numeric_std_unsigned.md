# Package: NUMERIC_STD_UNSIGNED

- **File**: numeric_std_unsigned.vhdl
## Constants

| Name            | Type   | Value                                             | Description |
| --------------- | ------ | ------------------------------------------------- | ----------- |
| CopyRightNotice | STRING |       "Copyright 2008 IEEE. All rights reserved." |             |
## Functions
- find_leftmost <font id="function_arguments">(ARG : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> Y : STD_ULOGIC) </font> <font id="function_return">return INTEGER </font>
**Description**
Id: A.39
- find_rightmost <font id="function_arguments">(ARG : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> Y : STD_ULOGIC) </font> <font id="function_return">return INTEGER </font>
**Description**
Result subtype: INTEGERResult: Finds the leftmost occurrence of the value of Y in ARG.        Returns the index of the occurrence if it exists, or -1 otherwise.Id: A.41
- MINIMUM <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : STD_ULOGIC_VECTOR) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Id: C.37
- MINIMUM <font id="function_arguments">(L : NATURAL;<br><span style="padding-left:20px"> R : STD_ULOGIC_VECTOR) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Result subtype: STD_ULOGIC_VECTORResult: Returns the lesser of two UNSIGNED vectors that may be        of different lengths.Id: C.39
- MINIMUM <font id="function_arguments">(L : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> R : NATURAL) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Result subtype: STD_ULOGIC_VECTORResult: Returns the lesser of a nonnegative INTEGER, L, and        an UNSIGNED vector, R.Id: C.41
- MAXIMUM <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : STD_ULOGIC_VECTOR) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Id: C.43
- MAXIMUM <font id="function_arguments">(L : NATURAL;<br><span style="padding-left:20px"> R : STD_ULOGIC_VECTOR) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Result subtype: STD_ULOGIC_VECTORResult: Returns the greater of two UNSIGNED vectors that may be        of different lengths.Id: C.45
- MAXIMUM <font id="function_arguments">(L : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> R : NATURAL) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Result subtype: STD_ULOGIC_VECTORResult: Returns the greater of a nonnegative INTEGER, L, and        an UNSIGNED vector, R.Id: C.47
- SHIFT_LEFT <font id="function_arguments">(ARG : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Id: S.1
- SHIFT_RIGHT <font id="function_arguments">(ARG : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Result subtype: STD_ULOGIC_VECTOR(ARG'LENGTH-1 downto 0)Result: Performs a shift-left on an UNSIGNED vector COUNT times.        The vacated positions are filled with '0'.        The COUNT leftmost elements are lost.Id: S.2
- ROTATE_LEFT <font id="function_arguments">(ARG : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Id: S.5
- ROTATE_RIGHT <font id="function_arguments">(ARG : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Result subtype: STD_ULOGIC_VECTOR(ARG'LENGTH-1 downto 0)Result: Performs a rotate-left of an UNSIGNED vector COUNT times.Id: S.6
- RESIZE <font id="function_arguments">(ARG : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> NEW_SIZE : NATURAL) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Id: R.2
- RESIZE <font id="function_arguments">(ARG,<br><span style="padding-left:20px"> SIZE_RES : STD_ULOGIC_VECTOR) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Result subtype: STD_ULOGIC_VECTOR(NEW_SIZE-1 downto 0)Result: Resizes the UNSIGNED vector ARG to the specified size.        To create a larger vector, the new [leftmost] bit positions        are filled with '0'. When truncating, the leftmost bits        are dropped.
- TO_INTEGER <font id="function_arguments">(ARG : STD_ULOGIC_VECTOR) </font> <font id="function_return">return NATURAL </font>
**Description**
Id: D.1
- To_StdLogicVector <font id="function_arguments">(ARG,<br><span style="padding-left:20px"> SIZE : NATURAL) </font> <font id="function_return">return STD_LOGIC_VECTOR </font>
**Description**
Result subtype: NATURAL. Value cannot be negative since parameter is an            UNSIGNED vector.Result: Converts the UNSIGNED vector to an INTEGER.Id: D.3
- To_StdLogicVector <font id="function_arguments">(ARG : NATURAL;<br><span style="padding-left:20px"> SIZE_RES : STD_ULOGIC_VECTOR) </font> <font id="function_return">return STD_LOGIC_VECTOR </font>
**Description**
Result subtype: STD_LOGIC_VECTOR(SIZE-1 downto 0)Result: Converts a non-negative INTEGER to an UNSIGNED vector with        the specified SIZE.
- To_StdULogicVector <font id="function_arguments">(ARG,<br><span style="padding-left:20px"> SIZE : NATURAL) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Id: D.5
- To_StdULogicVector <font id="function_arguments">(ARG : NATURAL;<br><span style="padding-left:20px"> SIZE_RES : STD_ULOGIC_VECTOR) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
**Description**
Result subtype: STD_ULOGIC_VECTOR(SIZE-1 downto 0)Result: Converts a non-negative INTEGER to an UNSIGNED vector with        the specified SIZE.
