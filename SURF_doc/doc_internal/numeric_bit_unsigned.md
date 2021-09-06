# Package: NUMERIC_BIT_UNSIGNED

- **File**: numeric_bit_unsigned.vhdl
## Constants

| Name            | Type   | Value                                             | Description |
| --------------- | ------ | ------------------------------------------------- | ----------- |
| CopyRightNotice | STRING |       "Copyright 2008 IEEE. All rights reserved." |             |
## Functions
- find_leftmost <font id="function_arguments">(ARG : BIT_VECTOR;<br><span style="padding-left:20px"> Y : BIT) </font> <font id="function_return">return INTEGER </font>
</br>**Description**
 Result subtype: bit_vector(R'LENGTH-1 downto 0)
 Result: Computes "L mod R" where R is an UNSIGNED vector and L
         is a non-negative INTEGER.
         If NO_OF_BITS(L) > R'LENGTH, result is truncated to R'LENGTH.
============================================================================
 Id: A.39

- find_rightmost <font id="function_arguments">(ARG : BIT_VECTOR;<br><span style="padding-left:20px"> Y : BIT) </font> <font id="function_return">return INTEGER </font>
</br>**Description**
 Result subtype: INTEGER
 Result: Finds the leftmost occurrence of the value of Y in ARG.
         Returns the index of the occurrence if it exists, or -1 otherwise.
 Id: A.41

- MINIMUM <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : BIT_VECTOR) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: BOOLEAN
 Result: Computes "L /= R" where L is an UNSIGNED vector and
         R is a non-negative INTEGER.
============================================================================
 Id: C.37

- MINIMUM <font id="function_arguments">(L : NATURAL;<br><span style="padding-left:20px"> R : BIT_VECTOR) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: BIT_VECTOR
 Result: Returns the lesser of two UNSIGNED vectors that may be
         of different lengths.
 Id: C.39

- MINIMUM <font id="function_arguments">(L : BIT_VECTOR;<br><span style="padding-left:20px"> R : NATURAL) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: BIT_VECTOR
 Result: Returns the lesser of a nonnegative INTEGER, L, and
         an UNSIGNED vector, R.
 Id: C.41

- MAXIMUM <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : BIT_VECTOR) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: BIT_VECTOR
 Result: Returns the lesser of an UNSIGNED vector, L, and
         a nonnegative INTEGER, R.
============================================================================
 Id: C.43

- MAXIMUM <font id="function_arguments">(L : NATURAL;<br><span style="padding-left:20px"> R : BIT_VECTOR) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: BIT_VECTOR
 Result: Returns the greater of two UNSIGNED vectors that may be
         of different lengths.
 Id: C.45

- MAXIMUM <font id="function_arguments">(L : BIT_VECTOR;<br><span style="padding-left:20px"> R : NATURAL) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: BIT_VECTOR
 Result: Returns the greater of a nonnegative INTEGER, L, and
         an UNSIGNED vector, R.
 Id: C.47

- SHIFT_LEFT <font id="function_arguments">(ARG : BIT_VECTOR;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: BIT
 Result: Computes "L /= R" where L is an UNSIGNED vector and
         R is a nonnegative INTEGER.
============================================================================
 Shift and Rotate Functions
============================================================================
 Id: S.1

- SHIFT_RIGHT <font id="function_arguments">(ARG : BIT_VECTOR;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: bit_vector(ARG'LENGTH-1 downto 0)
 Result: Performs a shift-left on an UNSIGNED vector COUNT times.
         The vacated positions are filled with '0'.
         The COUNT leftmost elements are lost.
 Id: S.2

- ROTATE_LEFT <font id="function_arguments">(ARG : BIT_VECTOR;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: UNSIGNED(ARG'LENGTH-1 downto 0)
 Result: Performs a shift-right on an UNSIGNED vector COUNT times.
         The vacated positions are filled with '0'.
         The COUNT rightmost elements are lost.
============================================================================
 Id: S.5

- ROTATE_RIGHT <font id="function_arguments">(ARG : BIT_VECTOR;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: bit_vector(ARG'LENGTH-1 downto 0)
 Result: Performs a rotate-left of an UNSIGNED vector COUNT times.
 Id: S.6

- RESIZE <font id="function_arguments">(ARG : BIT_VECTOR;<br><span style="padding-left:20px"> NEW_SIZE : NATURAL) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: BIT_VECTOR(ARG'LENGTH-1 downto 0)
 Result: SHIFT_RIGHT(ARG, COUNT)
============================================================================
   RESIZE Functions
============================================================================
 Id: R.2

- RESIZE <font id="function_arguments">(ARG,<br><span style="padding-left:20px"> SIZE_RES : BIT_VECTOR) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: bit_vector(NEW_SIZE-1 downto 0)
 Result: Resizes the UNSIGNED vector ARG to the specified size.
         To create a larger vector, the new [leftmost] bit positions
         are filled with '0'. When truncating, the leftmost bits
         are dropped.

- TO_INTEGER <font id="function_arguments">(ARG : BIT_VECTOR) </font> <font id="function_return">return NATURAL </font>
</br>**Description**
 Result subtype: BIT_VECTOR (SIZE_RES'length-1 downto 0)
============================================================================
 Conversion Functions
============================================================================
 Id: D.1

- To_BitVector <font id="function_arguments">(ARG,<br><span style="padding-left:20px"> SIZE : NATURAL) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: NATURAL. Value cannot be negative since parameter is an
             UNSIGNED vector.
 Result: Converts the UNSIGNED vector to an INTEGER.
 Id: D.3

- To_BitVector <font id="function_arguments">(ARG : NATURAL;<br><span style="padding-left:20px"> SIZE_RES : BIT_VECTOR) </font> <font id="function_return">return BIT_VECTOR </font>
</br>**Description**
 Result subtype: bit_vector(SIZE-1 downto 0)
 Result: Converts a non-negative INTEGER to an UNSIGNED vector with
         the specified size.

