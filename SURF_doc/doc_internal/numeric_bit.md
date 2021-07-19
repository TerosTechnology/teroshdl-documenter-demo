# Package: NUMERIC_BIT

- **File**: numeric_bit.vhdl
## Constants

| Name            | Type   | Value                        | Description |
| --------------- | ------ | ---------------------------- | ----------- |
| CopyRightNotice | STRING |  "Copyright � 2008 IEEE. All |             |
## Types

| Name     | Type                             | Description |
| -------- | -------------------------------- | ----------- |
| UNSIGNED | array (NATURAL range <>) of BIT  |             |
| SIGNED   | array (NATURAL range <>) of BIT  |             |
## Functions
- find_leftmost <font id="function_arguments">(ARG : UNSIGNED;<br><span style="padding-left:20px"> Y : BIT) </font> <font id="function_return">return INTEGER </font>
**Description**
Id: A.39
- find_leftmost <font id="function_arguments">(ARG : SIGNED;<br><span style="padding-left:20px"> Y : BIT) </font> <font id="function_return">return INTEGER </font>
**Description**
Result subtype: INTEGERResult: Finds the leftmost occurrence of the value of Y in ARG.        Returns the index of the occurrence if it exists, or -1 otherwise.Id: A.40
- find_rightmost <font id="function_arguments">(ARG : UNSIGNED;<br><span style="padding-left:20px"> Y : BIT) </font> <font id="function_return">return INTEGER </font>
**Description**
Result subtype: INTEGERResult: Finds the leftmost occurrence of the value of Y in ARG.        Returns the index of the occurrence if it exists, or -1 otherwise.Id: A.41
- find_rightmost <font id="function_arguments">(ARG : SIGNED;<br><span style="padding-left:20px"> Y : BIT) </font> <font id="function_return">return INTEGER </font>
**Description**
Result subtype: INTEGERResult: Finds the leftmost occurrence of the value of Y in ARG.        Returns the index of the occurrence if it exists, or -1 otherwise.Id: A.42
- MINIMUM <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : UNSIGNED) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Id: C.37
- MINIMUM <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : SIGNED) </font> <font id="function_return">return SIGNED </font>
**Description**
Result subtype: UNSIGNEDResult: Returns the lesser of two UNSIGNED vectors that may be        of different lengths.Id: C.38
- MINIMUM <font id="function_arguments">(L : NATURAL;<br><span style="padding-left:20px"> R : UNSIGNED) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Result subtype: SIGNEDResult: Returns the lesser of two SIGNED vectors that may be        of different lengths.Id: C.39
- MINIMUM <font id="function_arguments">(L : INTEGER;<br><span style="padding-left:20px"> R : SIGNED) </font> <font id="function_return">return SIGNED </font>
**Description**
Result subtype: UNSIGNEDResult: Returns the lesser of a nonnegative INTEGER, L, and        an UNSIGNED vector, R.Id: C.40
- MINIMUM <font id="function_arguments">(L : UNSIGNED;<br><span style="padding-left:20px"> R : NATURAL) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Result subtype: SIGNEDResult: Returns the lesser of an INTEGER, L, and a SIGNED        vector, R.Id: C.41
- MINIMUM <font id="function_arguments">(L : SIGNED;<br><span style="padding-left:20px"> R : INTEGER) </font> <font id="function_return">return SIGNED </font>
**Description**
Result subtype: UNSIGNEDResult: Returns the lesser of an UNSIGNED vector, L, and        a nonnegative INTEGER, R.Id: C.42
- MAXIMUM <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : UNSIGNED) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Id: C.43
- MAXIMUM <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : SIGNED) </font> <font id="function_return">return SIGNED </font>
**Description**
Result subtype: UNSIGNEDResult: Returns the greater of two UNSIGNED vectors that may be        of different lengths.Id: C.44
- MAXIMUM <font id="function_arguments">(L : NATURAL;<br><span style="padding-left:20px"> R : UNSIGNED) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Result subtype: SIGNEDResult: Returns the greater of two SIGNED vectors that may be        of different lengths.Id: C.45
- MAXIMUM <font id="function_arguments">(L : INTEGER;<br><span style="padding-left:20px"> R : SIGNED) </font> <font id="function_return">return SIGNED </font>
**Description**
Result subtype: UNSIGNEDResult: Returns the greater of a nonnegative INTEGER, L, and        an UNSIGNED vector, R.Id: C.46
- MAXIMUM <font id="function_arguments">(L : UNSIGNED;<br><span style="padding-left:20px"> R : NATURAL) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Result subtype: SIGNEDResult: Returns the greater of an INTEGER, L, and a SIGNED        vector, R.Id: C.47
- MAXIMUM <font id="function_arguments">(L : SIGNED;<br><span style="padding-left:20px"> R : INTEGER) </font> <font id="function_return">return SIGNED </font>
**Description**
Result subtype: UNSIGNEDResult: Returns the greater of an UNSIGNED vector, L, and        a nonnegative INTEGER, R.Id: C.48
- SHIFT_LEFT <font id="function_arguments">(ARG : UNSIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Id: S.1
- SHIFT_RIGHT <font id="function_arguments">(ARG : UNSIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Result subtype: UNSIGNED(ARG'LENGTH-1 downto 0)Result: Performs a shift-left on an UNSIGNED vector COUNT times.        The vacated positions are filled with Bit '0'.        The COUNT leftmost bits are lost.Id: S.2
- SHIFT_LEFT <font id="function_arguments">(ARG : SIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return SIGNED </font>
**Description**
Result subtype: UNSIGNED(ARG'LENGTH-1 downto 0)Result: Performs a shift-right on an UNSIGNED vector COUNT times.        The vacated positions are filled with Bit '0'.        The COUNT rightmost bits are lost.Id: S.3
- SHIFT_RIGHT <font id="function_arguments">(ARG : SIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return SIGNED </font>
**Description**
Result subtype: SIGNED(ARG'LENGTH-1 downto 0)Result: Performs a shift-left on a SIGNED vector COUNT times.        The vacated positions are filled with Bit '0'.        The COUNT leftmost bits are lost.Id: S.4
- ROTATE_LEFT <font id="function_arguments">(ARG : UNSIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Id: S.5
- ROTATE_RIGHT <font id="function_arguments">(ARG : UNSIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Result subtype: UNSIGNED(ARG'LENGTH-1 downto 0)Result: Performs a rotate-left of an UNSIGNED vector COUNT times.Id: S.6
- ROTATE_LEFT <font id="function_arguments">(ARG : SIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return SIGNED </font>
**Description**
Result subtype: UNSIGNED(ARG'LENGTH-1 downto 0)Result: Performs a rotate-right of an UNSIGNED vector COUNT times.Id: S.7
- ROTATE_RIGHT <font id="function_arguments">(ARG : SIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return SIGNED </font>
**Description**
Result subtype: SIGNED(ARG'LENGTH-1 downto 0)Result: Performs a logical rotate-left of a SIGNED vector COUNT times.Id: S.8
- RESIZE <font id="function_arguments">(ARG : SIGNED;<br><span style="padding-left:20px"> NEW_SIZE : NATURAL) </font> <font id="function_return">return SIGNED </font>
**Description**
Id: R.1
- RESIZE <font id="function_arguments">(ARG : UNSIGNED;<br><span style="padding-left:20px"> NEW_SIZE : NATURAL) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Result subtype: SIGNED(NEW_SIZE-1 downto 0)Result: Resizes the SIGNED vector ARG to the specified size.        To create a larger vector, the new [leftmost] bit positions        are filled with the sign bit (ARG'LEFT). When truncating,        the sign bit is retained along with the rightmost part.Id: R.2
- RESIZE <font id="function_arguments">(ARG,<br><span style="padding-left:20px"> SIZE_RES : UNSIGNED) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Result subtype: UNSIGNED(NEW_SIZE-1 downto 0)Result: Resizes the UNSIGNED vector ARG to the specified size.        To create a larger vector, the new [leftmost] bit positions        are filled with '0'. When truncating, the leftmost bits        are dropped.
- RESIZE <font id="function_arguments">(ARG,<br><span style="padding-left:20px"> SIZE_RES : SIGNED) </font> <font id="function_return">return SIGNED </font>
**Description**
Result subtype: UNRESOLVED_UNSIGNED (SIZE_RES'length-1 downto 0)
- TO_INTEGER <font id="function_arguments">(ARG : UNSIGNED) </font> <font id="function_return">return NATURAL </font>
**Description**
Id: D.1
- TO_INTEGER <font id="function_arguments">(ARG : SIGNED) </font> <font id="function_return">return INTEGER </font>
**Description**
Result subtype: NATURAL. Value cannot be negative since parameter is an        UNSIGNED vector.Result: Converts the UNSIGNED vector to an INTEGER.Id: D.2
- TO_UNSIGNED <font id="function_arguments">(ARG,<br><span style="padding-left:20px"> SIZE : NATURAL) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Result subtype: INTEGERResult: Converts a SIGNED vector to an INTEGER.Id: D.3
- TO_SIGNED <font id="function_arguments">(ARG : INTEGER;<br><span style="padding-left:20px"> SIZE : NATURAL) </font> <font id="function_return">return SIGNED </font>
**Description**
Result subtype: UNSIGNED(SIZE-1 downto 0)Result: Converts a nonnegative INTEGER to an UNSIGNED vector with        the specified size.Id: D.4
- TO_UNSIGNED <font id="function_arguments">(ARG : NATURAL;<br><span style="padding-left:20px"> SIZE_RES : UNSIGNED) </font> <font id="function_return">return UNSIGNED </font>
**Description**
Result subtype: SIGNED(SIZE-1 downto 0)Result: Converts an INTEGER to a SIGNED vector of the specified size.
- TO_SIGNED <font id="function_arguments">(ARG : INTEGER;<br><span style="padding-left:20px"> SIZE_RES : SIGNED) </font> <font id="function_return">return SIGNED </font>
**Description**
Result subtype: UNRESOLVED_UNSIGNED(SIZE_RES'length-1 downto 0)
- to_ostring <font id="function_arguments">(value : UNSIGNED) </font> <font id="function_return">return STRING </font>
- to_ostring <font id="function_arguments">(value : SIGNED) </font> <font id="function_return">return STRING </font>
- to_hstring <font id="function_arguments">(value : UNSIGNED) </font> <font id="function_return">return STRING </font>
- to_hstring <font id="function_arguments">(value : SIGNED) </font> <font id="function_return">return STRING </font>
- READ <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNSIGNED;<br><span style="padding-left:20px"> GOOD : out BOOLEAN) </font> <font id="function_return">return ()</font>
- READ <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNSIGNED) </font> <font id="function_return">return ()</font>
- READ <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out SIGNED;<br><span style="padding-left:20px"> GOOD : out BOOLEAN) </font> <font id="function_return">return ()</font>
- READ <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out SIGNED) </font> <font id="function_return">return ()</font>
- WRITE <font id="function_arguments">(L         : inout LINE;<br><span style="padding-left:20px"> VALUE : in UNSIGNED;<br><span style="padding-left:20px"> JUSTIFIED : in    SIDE := right;<br><span style="padding-left:20px"> FIELD : in WIDTH := 0) </font> <font id="function_return">return ()</font>
- WRITE <font id="function_arguments">(L         : inout LINE;<br><span style="padding-left:20px"> VALUE : in SIGNED;<br><span style="padding-left:20px"> JUSTIFIED : in    SIDE := right;<br><span style="padding-left:20px"> FIELD : in WIDTH := 0) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNSIGNED;<br><span style="padding-left:20px"> GOOD : out BOOLEAN) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out SIGNED;<br><span style="padding-left:20px"> GOOD : out BOOLEAN) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNSIGNED) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out SIGNED) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNSIGNED;<br><span style="padding-left:20px"> GOOD : out BOOLEAN) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out SIGNED;<br><span style="padding-left:20px"> GOOD : out BOOLEAN) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNSIGNED) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out SIGNED) </font> <font id="function_return">return ()</font>
- OWRITE <font id="function_arguments">(L         : inout LINE;<br><span style="padding-left:20px"> VALUE : in UNSIGNED;<br><span style="padding-left:20px"> JUSTIFIED : in    SIDE := right;<br><span style="padding-left:20px"> FIELD : in WIDTH := 0) </font> <font id="function_return">return ()</font>
- OWRITE <font id="function_arguments">(L         : inout LINE;<br><span style="padding-left:20px"> VALUE : in SIGNED;<br><span style="padding-left:20px"> JUSTIFIED : in    SIDE := right;<br><span style="padding-left:20px"> FIELD : in WIDTH := 0) </font> <font id="function_return">return ()</font>
- HWRITE <font id="function_arguments">(L         : inout LINE;<br><span style="padding-left:20px"> VALUE : in UNSIGNED;<br><span style="padding-left:20px"> JUSTIFIED : in    SIDE := right;<br><span style="padding-left:20px"> FIELD : in WIDTH := 0) </font> <font id="function_return">return ()</font>
- HWRITE <font id="function_arguments">(L         : inout LINE;<br><span style="padding-left:20px"> VALUE : in SIGNED;<br><span style="padding-left:20px"> JUSTIFIED : in    SIDE := right;<br><span style="padding-left:20px"> FIELD : in WIDTH := 0) </font> <font id="function_return">return ()</font>
