# Package: NUMERIC_STD

- **File**: numeric_std.vhdl
## Constants

| Name            | Type   | Value                        | Description |
| --------------- | ------ | ---------------------------- | ----------- |
| CopyRightNotice | STRING |  "Copyright � 2008 IEEE. All |             |
## Types

| Name                | Type                                    | Description                                                                                                                                                                                |
| ------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| UNRESOLVED_UNSIGNED | array (NATURAL range <>) of STD_ULOGIC  | ============================================================================  Numeric Array Type Definitions ============================================================================  |
| UNRESOLVED_SIGNED   | array (NATURAL range <>) of STD_ULOGIC  |                                                                                                                                                                                            |
## Functions
- find_leftmost <font id="function_arguments">(ARG : UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> Y : STD_ULOGIC) </font> <font id="function_return">return INTEGER </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED(R'LENGTH-1 downto 0)
 Result: Computes "L mod R" where L is an INTEGER and
         R is an UNRESOLVED_SIGNED vector.
         If NO_OF_BITS(L) > R'LENGTH, result is truncated to R'LENGTH.
============================================================================
 Id: A.39

- find_leftmost <font id="function_arguments">(ARG : UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> Y : STD_ULOGIC) </font> <font id="function_return">return INTEGER </font>
**Description**
 Result subtype: INTEGER
 Result: Finds the leftmost occurrence of the value of Y in ARG.
         Returns the index of the occurrence if it exists, or -1 otherwise.
 Id: A.40

- find_rightmost <font id="function_arguments">(ARG : UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> Y : STD_ULOGIC) </font> <font id="function_return">return INTEGER </font>
**Description**
 Result subtype: INTEGER
 Result: Finds the leftmost occurrence of the value of Y in ARG.
         Returns the index of the occurrence if it exists, or -1 otherwise.
 Id: A.41

- find_rightmost <font id="function_arguments">(ARG : UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> Y : STD_ULOGIC) </font> <font id="function_return">return INTEGER </font>
**Description**
 Result subtype: INTEGER
 Result: Finds the leftmost occurrence of the value of Y in ARG.
         Returns the index of the occurrence if it exists, or -1 otherwise.
 Id: A.42

- MINIMUM <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: BOOLEAN
 Result: Computes "L /= R" where L is an UNRESOLVED_SIGNED vector and
         R is an INTEGER.
============================================================================
 Id: C.37

- MINIMUM <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : UNRESOLVED_SIGNED) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED
 Result: Returns the lesser of two UNRESOLVED_UNSIGNED vectors that may be
         of different lengths.
 Id: C.38

- MINIMUM <font id="function_arguments">(L : NATURAL;<br><span style="padding-left:20px"> R : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED
 Result: Returns the lesser of two UNRESOLVED_SIGNED vectors that may be
         of different lengths.
 Id: C.39

- MINIMUM <font id="function_arguments">(L : INTEGER;<br><span style="padding-left:20px"> R : UNRESOLVED_SIGNED) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED
 Result: Returns the lesser of a nonnegative INTEGER, L, and
         an UNRESOLVED_UNSIGNED vector, R.
 Id: C.40

- MINIMUM <font id="function_arguments">(L : UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> R : NATURAL) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED
 Result: Returns the lesser of an INTEGER, L, and an UNRESOLVED_SIGNED
         vector, R.
 Id: C.41

- MINIMUM <font id="function_arguments">(L : UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> R : INTEGER) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED
 Result: Returns the lesser of an UNRESOLVED_UNSIGNED vector, L, and
         a nonnegative INTEGER, R.
 Id: C.42

- MAXIMUM <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED
 Result: Returns the lesser of an UNRESOLVED_SIGNED vector, L, and
         an INTEGER, R.
============================================================================
 Id: C.43

- MAXIMUM <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : UNRESOLVED_SIGNED) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED
 Result: Returns the greater of two UNRESOLVED_UNSIGNED vectors that may be
         of different lengths.
 Id: C.44

- MAXIMUM <font id="function_arguments">(L : NATURAL;<br><span style="padding-left:20px"> R : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED
 Result: Returns the greater of two UNRESOLVED_SIGNED vectors that may be
         of different lengths.
 Id: C.45

- MAXIMUM <font id="function_arguments">(L : INTEGER;<br><span style="padding-left:20px"> R : UNRESOLVED_SIGNED) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED
 Result: Returns the greater of a nonnegative INTEGER, L, and
         an UNRESOLVED_UNSIGNED vector, R.
 Id: C.46

- MAXIMUM <font id="function_arguments">(L : UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> R : NATURAL) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED
 Result: Returns the greater of an INTEGER, L, and an UNRESOLVED_SIGNED
         vector, R.
 Id: C.47

- MAXIMUM <font id="function_arguments">(L : UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> R : INTEGER) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED
 Result: Returns the greater of an UNRESOLVED_UNSIGNED vector, L, and
         a nonnegative INTEGER, R.
 Id: C.48

- SHIFT_LEFT <font id="function_arguments">(ARG : UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: STD_ULOGIC
 Result: Computes "L /= R" where L is an UNRESOLVED_SIGNED vector and
         R is an INTEGER.
============================================================================
 Shift and Rotate Functions
============================================================================
 Id: S.1

- SHIFT_RIGHT <font id="function_arguments">(ARG : UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED(ARG'LENGTH-1 downto 0)
 Result: Performs a shift-left on an UNRESOLVED_UNSIGNED vector COUNT times.
         The vacated positions are filled with '0'.
         The COUNT leftmost elements are lost.
 Id: S.2

- SHIFT_LEFT <font id="function_arguments">(ARG : UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED(ARG'LENGTH-1 downto 0)
 Result: Performs a shift-right on an UNRESOLVED_UNSIGNED vector COUNT times.
         The vacated positions are filled with '0'.
         The COUNT rightmost elements are lost.
 Id: S.3

- SHIFT_RIGHT <font id="function_arguments">(ARG : UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED(ARG'LENGTH-1 downto 0)
 Result: Performs a shift-left on an UNRESOLVED_SIGNED vector COUNT times.
         The vacated positions are filled with '0'.
         The COUNT leftmost elements are lost.
 Id: S.4

- ROTATE_LEFT <font id="function_arguments">(ARG : UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED(ARG'LENGTH-1 downto 0)
 Result: Performs a shift-right on an UNRESOLVED_SIGNED vector COUNT times.
         The vacated positions are filled with the leftmost
         element, ARG'LEFT. The COUNT rightmost elements are lost.
============================================================================
 Id: S.5

- ROTATE_RIGHT <font id="function_arguments">(ARG : UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED(ARG'LENGTH-1 downto 0)
 Result: Performs a rotate-left of an UNRESOLVED_UNSIGNED vector COUNT times.
 Id: S.6

- ROTATE_LEFT <font id="function_arguments">(ARG : UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED(ARG'LENGTH-1 downto 0)
 Result: Performs a rotate-right of an UNRESOLVED_UNSIGNED vector COUNT times.
 Id: S.7

- ROTATE_RIGHT <font id="function_arguments">(ARG : UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED(ARG'LENGTH-1 downto 0)
 Result: Performs a logical rotate-left of an UNRESOLVED_SIGNED
         vector COUNT times.
 Id: S.8

- RESIZE <font id="function_arguments">(ARG : UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> NEW_SIZE : NATURAL) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED(ARG'LENGTH-1 downto 0)
 Result: SHIFT_RIGHT(ARG, COUNT)
============================================================================
   RESIZE Functions
============================================================================
 Id: R.1

- RESIZE <font id="function_arguments">(ARG : UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> NEW_SIZE : NATURAL) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED(NEW_SIZE-1 downto 0)
 Result: Resizes the UNRESOLVED_SIGNED vector ARG to the specified size.
         To create a larger vector, the new [leftmost] bit positions
         are filled with the sign bit (ARG'LEFT). When truncating,
         the sign bit is retained along with the rightmost part.
 Id: R.2

- RESIZE <font id="function_arguments">(ARG,<br><span style="padding-left:20px"> SIZE_RES : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED(NEW_SIZE-1 downto 0)
 Result: Resizes the UNRESOLVED_SIGNED vector ARG to the specified size.
         To create a larger vector, the new [leftmost] bit positions
         are filled with '0'. When truncating, the leftmost bits
         are dropped.

- RESIZE <font id="function_arguments">(ARG,<br><span style="padding-left:20px"> SIZE_RES : UNRESOLVED_SIGNED) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED (SIZE_RES'length-1 downto 0)

- TO_INTEGER <font id="function_arguments">(ARG : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return NATURAL </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED (SIZE_RES'length-1 downto 0)
============================================================================
 Conversion Functions
============================================================================
 Id: D.1

- TO_INTEGER <font id="function_arguments">(ARG : UNRESOLVED_SIGNED) </font> <font id="function_return">return INTEGER </font>
**Description**
 Result subtype: NATURAL. Value cannot be negative since parameter is an
             UNRESOLVED_UNSIGNED vector.
 Result: Converts the UNRESOLVED_UNSIGNED vector to an INTEGER.
 Id: D.2

- TO_UNSIGNED <font id="function_arguments">(ARG,<br><span style="padding-left:20px"> SIZE : NATURAL) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: INTEGER
 Result: Converts an UNRESOLVED_SIGNED vector to an INTEGER.
 Id: D.3

- TO_SIGNED <font id="function_arguments">(ARG : INTEGER;<br><span style="padding-left:20px"> SIZE : NATURAL) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED(SIZE-1 downto 0)
 Result: Converts a nonnegative INTEGER to an UNRESOLVED_UNSIGNED vector with
         the specified SIZE.
 Id: D.4

- TO_UNSIGNED <font id="function_arguments">(ARG : NATURAL;<br><span style="padding-left:20px"> SIZE_RES : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED(SIZE-1 downto 0)
 Result: Converts an INTEGER to a UNRESOLVED_SIGNED vector of the specified SIZE.

- TO_SIGNED <font id="function_arguments">(ARG : INTEGER;<br><span style="padding-left:20px"> SIZE_RES : UNRESOLVED_SIGNED) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED(SIZE_RES'length-1 downto 0)

- STD_MATCH <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : STD_ULOGIC) </font> <font id="function_return">return BOOLEAN </font>
**Description**
 Result subtype: STD_ULOGIC. 
 Result: Result of xnor'ing all of the bits of the vector.
============================================================================
 Match Functions
============================================================================
 Id: M.1

- STD_MATCH <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return BOOLEAN </font>
**Description**
 Result subtype: BOOLEAN
 Result: terms compared per STD_LOGIC_1164 intent
 Id: M.2

- STD_MATCH <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : UNRESOLVED_SIGNED) </font> <font id="function_return">return BOOLEAN </font>
**Description**
 Result subtype: BOOLEAN
 Result: terms compared per STD_LOGIC_1164 intent
 Id: M.3

- STD_MATCH <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : STD_ULOGIC_VECTOR) </font> <font id="function_return">return BOOLEAN </font>
**Description**
 Result subtype: BOOLEAN
 Result: terms compared per STD_LOGIC_1164 intent
 Id: M.5

- TO_01 <font id="function_arguments">(S : UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> XMAP : STD_ULOGIC := '0') </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: BOOLEAN
 Result: terms compared per STD_LOGIC_1164 intent
============================================================================
 Translation Functions
============================================================================
 Id: T.1

- TO_01 <font id="function_arguments">(S : UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> XMAP : STD_ULOGIC := '0') </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED(S'RANGE)
 Result: Termwise, 'H' is translated to '1', and 'L' is translated
         to '0'. If a value other than '0'|'1'|'H'|'L' is found,
         the array is set to (others => XMAP), and a warning is
         issued.
 Id: T.2

- TO_X01 <font id="function_arguments">(S : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED(S'RANGE)
 Result: Termwise, 'H' is translated to '1', and 'L' is translated
         to '0'. If a value other than '0'|'1'|'H'|'L' is found,
         the array is set to (others => XMAP), and a warning is
         issued.
 Id: T.3

- TO_X01 <font id="function_arguments">(S : UNRESOLVED_SIGNED) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED(S'RANGE)
 Result: Termwise, 'H' is translated to '1', 'L' is translated to '0',
         and values other than '0'|'1'|'H'|'L' are translated to 'X'.
 Id: T.4

- TO_X01Z <font id="function_arguments">(S : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED(S'RANGE)
 Result: Termwise, 'H' is translated to '1', 'L' is translated to '0',
         and values other than '0'|'1'|'H'|'L' are translated to 'X'.
 Id: T.5

- TO_X01Z <font id="function_arguments">(S : UNRESOLVED_SIGNED) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED(S'RANGE)
 Result: Termwise, 'H' is translated to '1', 'L' is translated to '0',
         and values other than '0'|'1'|'H'|'L'|'Z' are translated to 'X'.
 Id: T.6

- TO_UX01 <font id="function_arguments">(S : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED(S'RANGE)
 Result: Termwise, 'H' is translated to '1', 'L' is translated to '0',
         and values other than '0'|'1'|'H'|'L'|'Z' are translated to 'X'.
 Id: T.7

- TO_UX01 <font id="function_arguments">(S : UNRESOLVED_SIGNED) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
 Result subtype: UNRESOLVED_UNSIGNED(S'RANGE)
 Result: Termwise, 'H' is translated to '1', 'L' is translated to '0',
         and values other than 'U'|'0'|'1'|'H'|'L' are translated to 'X'.
 Id: T.8

- IS_X <font id="function_arguments">(S : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return BOOLEAN </font>
**Description**
 Result subtype: UNRESOLVED_SIGNED(S'RANGE)
 Result: Termwise, 'H' is translated to '1', 'L' is translated to '0',
         and values other than 'U'|'0'|'1'|'H'|'L' are translated to 'X'.
 Id: T.9

- IS_X <font id="function_arguments">(S : UNRESOLVED_SIGNED) </font> <font id="function_return">return BOOLEAN </font>
**Description**
 Result subtype: BOOLEAN
 Result: TRUE if S contains a 'U'|'X'|'Z'|'W'|'-' value, FALSE otherwise.
 Id: T.10

- to_ostring <font id="function_arguments">(value : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return STRING </font>
- to_ostring <font id="function_arguments">(value : UNRESOLVED_SIGNED) </font> <font id="function_return">return STRING </font>
- to_hstring <font id="function_arguments">(value : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return STRING </font>
- to_hstring <font id="function_arguments">(value : UNRESOLVED_SIGNED) </font> <font id="function_return">return STRING </font>
- READ <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> GOOD : out BOOLEAN) </font> <font id="function_return">return ()</font>
- READ <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNRESOLVED_UNSIGNED) </font> <font id="function_return">return ()</font>
- READ <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> GOOD : out BOOLEAN) </font> <font id="function_return">return ()</font>
- READ <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNRESOLVED_SIGNED) </font> <font id="function_return">return ()</font>
- WRITE <font id="function_arguments">(L         : inout LINE;<br><span style="padding-left:20px"> VALUE : in UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> JUSTIFIED : in    SIDE := right;<br><span style="padding-left:20px"> FIELD : in WIDTH := 0) </font> <font id="function_return">return ()</font>
- WRITE <font id="function_arguments">(L         : inout LINE;<br><span style="padding-left:20px"> VALUE : in UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> JUSTIFIED : in    SIDE := right;<br><span style="padding-left:20px"> FIELD : in WIDTH := 0) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> GOOD : out BOOLEAN) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> GOOD : out BOOLEAN) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNRESOLVED_UNSIGNED) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNRESOLVED_SIGNED) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> GOOD : out BOOLEAN) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> GOOD : out BOOLEAN) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNRESOLVED_UNSIGNED) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L : inout LINE;<br><span style="padding-left:20px"> VALUE : out UNRESOLVED_SIGNED) </font> <font id="function_return">return ()</font>
- OWRITE <font id="function_arguments">(L         : inout LINE;<br><span style="padding-left:20px"> VALUE : in UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> JUSTIFIED : in    SIDE := right;<br><span style="padding-left:20px"> FIELD : in WIDTH := 0) </font> <font id="function_return">return ()</font>
- OWRITE <font id="function_arguments">(L         : inout LINE;<br><span style="padding-left:20px"> VALUE : in UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> JUSTIFIED : in    SIDE := right;<br><span style="padding-left:20px"> FIELD : in WIDTH := 0) </font> <font id="function_return">return ()</font>
- HWRITE <font id="function_arguments">(L         : inout LINE;<br><span style="padding-left:20px"> VALUE : in UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px"> JUSTIFIED : in    SIDE := right;<br><span style="padding-left:20px"> FIELD : in WIDTH := 0) </font> <font id="function_return">return ()</font>
- HWRITE <font id="function_arguments">(L         : inout LINE;<br><span style="padding-left:20px"> VALUE : in UNRESOLVED_SIGNED;<br><span style="padding-left:20px"> JUSTIFIED : in    SIDE := right;<br><span style="padding-left:20px"> FIELD : in WIDTH := 0) </font> <font id="function_return">return ()</font>
