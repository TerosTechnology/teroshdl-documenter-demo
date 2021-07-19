# Package: fixed_generic_pkg

- **File**: fixed_generic_pkg.vhdl
## Constants

| Name            | Type   | Value                                               | Description |
| --------------- | ------ | --------------------------------------------------- | ----------- |
| CopyRightNotice | STRING |      "Copyright 2008 by IEEE. All rights reserved." |             |
## Types

| Name              | Type                                    | Description                                              |
| ----------------- | --------------------------------------- | -------------------------------------------------------- |
| UNRESOLVED_ufixed | array (INTEGER range <>) of STD_ULOGIC  | base Unsigned fixed point type, downto direction assumed |
| UNRESOLVED_sfixed | array (INTEGER range <>) of STD_ULOGIC  | base Signed fixed point type, downto direction assumed   |
## Functions
- divide <font id="function_arguments">( l,<br><span style="padding-left:20px"> r                 : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> constant round_style : fixed_round_style_type := fixed_round_style;<br><span style="padding-left:20px"> constant guard_bits  : NATURAL                := fixed_guard_bits) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
This version of divide gives the user more controlufixed(a downto b) / ufixed(c downto d) = ufixed(a-d downto b-c-1)
- divide <font id="function_arguments">( l,<br><span style="padding-left:20px"> r                 : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> constant round_style : fixed_round_style_type := fixed_round_style;<br><span style="padding-left:20px"> constant guard_bits  : NATURAL                := fixed_guard_bits) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
**Description**
This version of divide gives the user more controlsfixed(a downto b) / sfixed(c downto d) = sfixed(a-d+1 downto b-c)
- reciprocal <font id="function_arguments">( arg                  : UNRESOLVED_ufixed;<br><span style="padding-left:20px">  -- fixed point input constant round_style : fixed_round_style_type := fixed_round_style;<br><span style="padding-left:20px"> constant guard_bits  : NATURAL                := fixed_guard_bits) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
These functions return 1/X1 / ufixed(a downto b) = ufixed(-b downto -a-1)
- reciprocal <font id="function_arguments">( arg                  : UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- fixed point input constant round_style : fixed_round_style_type := fixed_round_style;<br><span style="padding-left:20px"> constant guard_bits  : NATURAL                := fixed_guard_bits) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
**Description**
1 / sfixed(a downto b) = sfixed(-b+1 downto -a)
- remainder <font id="function_arguments">( l,<br><span style="padding-left:20px"> r                 : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> constant round_style : fixed_round_style_type := fixed_round_style;<br><span style="padding-left:20px"> constant guard_bits  : NATURAL                := fixed_guard_bits) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
REM functionufixed (a downto b) rem ufixed (c downto d)  = ufixed (minimum(a,c) downto minimum(b,d))
- remainder <font id="function_arguments">( l,<br><span style="padding-left:20px"> r                 : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> constant round_style : fixed_round_style_type := fixed_round_style;<br><span style="padding-left:20px"> constant guard_bits  : NATURAL                := fixed_guard_bits) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
**Description**
sfixed (a downto b) rem sfixed (c downto d)  = sfixed (minimum(a,c) downto minimum(b,d))
- modulo <font id="function_arguments">( l,<br><span style="padding-left:20px"> r                 : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> constant round_style : fixed_round_style_type := fixed_round_style;<br><span style="padding-left:20px"> constant guard_bits  : NATURAL                := fixed_guard_bits) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
mod functionufixed (a downto b) mod ufixed (c downto d)       = ufixed (minimum(a,c) downto minimum(b, d))
- modulo <font id="function_arguments">( l,<br><span style="padding-left:20px"> r                    : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style;<br><span style="padding-left:20px"> constant guard_bits     : NATURAL                   := fixed_guard_bits) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
**Description**
sfixed (a downto b) mod sfixed (c downto d)       = sfixed (c downto minimum(b, d))
- add_carry <font id="function_arguments">( L,<br><span style="padding-left:20px"> R   : in  UNRESOLVED_ufixed;<br><span style="padding-left:20px"> c_in   : in  STD_ULOGIC;<br><span style="padding-left:20px"> result : out UNRESOLVED_ufixed;<br><span style="padding-left:20px"> c_out  : out STD_ULOGIC) </font> <font id="function_return">return ()</font>
**Description**
Procedure for those who need an "accumulator" function.add_carry (ufixed(a downto b), ufixed (c downto d))        = ufixed (maximum(a,c) downto minimum(b,d))
- add_carry <font id="function_arguments">( L,<br><span style="padding-left:20px"> R   : in  UNRESOLVED_sfixed;<br><span style="padding-left:20px"> c_in   : in  STD_ULOGIC;<br><span style="padding-left:20px"> result : out UNRESOLVED_sfixed;<br><span style="padding-left:20px"> c_out  : out STD_ULOGIC) </font> <font id="function_return">return ()</font>
**Description**
add_carry (sfixed(a downto b), sfixed (c downto d))        = sfixed (maximum(a,c) downto minimum(b,d))
- scalb <font id="function_arguments">(y : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> N : INTEGER) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
Scales the result by a power of 2.  Width of input = width of output withthe binary point moved.
- scalb <font id="function_arguments">(y : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> N : UNRESOLVED_SIGNED) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- scalb <font id="function_arguments">(y : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> N : INTEGER) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- scalb <font id="function_arguments">(y : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> N : UNRESOLVED_SIGNED) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- Is_Negative <font id="function_arguments">(arg : UNRESOLVED_sfixed) </font> <font id="function_return">return BOOLEAN </font>
- std_match <font id="function_arguments">(l,<br><span style="padding-left:20px"> r : UNRESOLVED_ufixed) </font> <font id="function_return">return BOOLEAN </font>
- std_match <font id="function_arguments">(l,<br><span style="padding-left:20px"> r : UNRESOLVED_sfixed) </font> <font id="function_return">return BOOLEAN </font>
- maximum <font id="function_arguments">(l,<br><span style="padding-left:20px"> r : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
Overloads the default "maximum" and "minimum" function
- minimum <font id="function_arguments">(l,<br><span style="padding-left:20px"> r : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- maximum <font id="function_arguments">(l,<br><span style="padding-left:20px"> r : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- minimum <font id="function_arguments">(l,<br><span style="padding-left:20px"> r : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- maximum <font id="function_arguments">(l : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> r : NATURAL) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- minimum <font id="function_arguments">(l : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> r : NATURAL) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- maximum <font id="function_arguments">(l : NATURAL;<br><span style="padding-left:20px"> r : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- minimum <font id="function_arguments">(l : NATURAL;<br><span style="padding-left:20px"> r : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- maximum <font id="function_arguments">(l : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> r : REAL) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- maximum <font id="function_arguments">(l : REAL;<br><span style="padding-left:20px"> r : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- minimum <font id="function_arguments">(l : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> r : REAL) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- minimum <font id="function_arguments">(l : REAL;<br><span style="padding-left:20px"> r : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- maximum <font id="function_arguments">(l : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> r : INTEGER) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- maximum <font id="function_arguments">(l : INTEGER;<br><span style="padding-left:20px"> r : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- minimum <font id="function_arguments">(l : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> r : INTEGER) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- minimum <font id="function_arguments">(l : INTEGER;<br><span style="padding-left:20px"> r : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- maximum <font id="function_arguments">(l : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> r : REAL) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- maximum <font id="function_arguments">(l : REAL;<br><span style="padding-left:20px"> r : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- minimum <font id="function_arguments">(l : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> r : REAL) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- minimum <font id="function_arguments">(l : REAL;<br><span style="padding-left:20px"> r : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- SHIFT_LEFT <font id="function_arguments">(ARG : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- SHIFT_RIGHT <font id="function_arguments">(ARG : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- SHIFT_LEFT <font id="function_arguments">(ARG : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- SHIFT_RIGHT <font id="function_arguments">(ARG : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> COUNT : NATURAL) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- find_leftmost <font id="function_arguments">(arg : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> y : STD_ULOGIC) </font> <font id="function_return">return INTEGER </font>
**Description**
returns arg'low-1 if not found
- find_leftmost <font id="function_arguments">(arg : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> y : STD_ULOGIC) </font> <font id="function_return">return INTEGER </font>
- find_rightmost <font id="function_arguments">(arg : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> y : STD_ULOGIC) </font> <font id="function_return">return INTEGER </font>
**Description**
returns arg'high+1 if not found
- find_rightmost <font id="function_arguments">(arg : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> y : STD_ULOGIC) </font> <font id="function_return">return INTEGER </font>
- resize <font id="function_arguments">( arg                     : UNRESOLVED_ufixed;<br><span style="padding-left:20px">  -- input constant left_index     : INTEGER;<br><span style="padding-left:20px">  -- integer portion constant right_index    : INTEGER;<br><span style="padding-left:20px">  -- size of fraction constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
resizes the number (larger or smaller)The returned result will be ufixed (left_index downto right_index)If "round_style" is fixed_round, then the result will be rounded.If the MSB of the remainder is a "1" AND the LSB of the unrounded resultis a '1' or the lower bits of the remainder include a '1' then the resultwill be increased by the smallest representable number for that type."overflow_style" can be fixed_saturate or fixed_wrap.In saturate mode, if the number overflows then the largest possiblerepresentable number is returned.  If wrap mode, then the upper bitsof the number are truncated.
- resize <font id="function_arguments">( arg                     : UNRESOLVED_ufixed;<br><span style="padding-left:20px">  -- input size_res                : UNRESOLVED_ufixed;<br><span style="padding-left:20px">  -- for size only constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
"size_res" functions create the size of the output from the indicesof the "size_res" input.  The actual value of "size_res" is not used.
- resize <font id="function_arguments">( arg                     : UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- input constant left_index     : INTEGER;<br><span style="padding-left:20px">            -- integer portion constant right_index    : INTEGER;<br><span style="padding-left:20px">            -- size of fraction constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
**Description**
Note that in "wrap" mode the sign bit is not replicated.  Thus theresize of a negative number can have a positive result in wrap mode.
- resize <font id="function_arguments">( arg                     : UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- input size_res                : UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- for size only constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- to_ufixed <font id="function_arguments">( arg                     : NATURAL;<br><span style="padding-left:20px">  -- integer constant left_index     : INTEGER;<br><span style="padding-left:20px">  -- left index (high index) constant right_index    : INTEGER                   := 0;<br><span style="padding-left:20px">  -- right index constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
integer (natural) to unsigned fixed point.arguments are the upper and lower bounds of the number, thusufixed (7 downto -3) <= to_ufixed (int, 7, -3);
- to_ufixed <font id="function_arguments">( arg                     : NATURAL;<br><span style="padding-left:20px">            -- integer size_res                : UNRESOLVED_ufixed;<br><span style="padding-left:20px">  -- for size only constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- to_ufixed <font id="function_arguments">( arg                     : REAL;<br><span style="padding-left:20px">     -- real constant left_index     : INTEGER;<br><span style="padding-left:20px">  -- left index (high index) constant right_index    : INTEGER;<br><span style="padding-left:20px">  -- right index constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style;<br><span style="padding-left:20px"> constant guard_bits     : NATURAL                   := fixed_guard_bits) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
real to unsigned fixed point
- to_ufixed <font id="function_arguments">( arg                     : REAL;<br><span style="padding-left:20px">     -- real size_res                : UNRESOLVED_ufixed;<br><span style="padding-left:20px">  -- for size only constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style;<br><span style="padding-left:20px"> constant guard_bits     : NATURAL                   := fixed_guard_bits) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- to_ufixed <font id="function_arguments">( arg                     : UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px">             -- unsigned constant left_index     : INTEGER;<br><span style="padding-left:20px">  -- left index (high index) constant right_index    : INTEGER                   := 0;<br><span style="padding-left:20px">  -- right index constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
unsigned to unsigned fixed point
- to_ufixed <font id="function_arguments">( arg                     : UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px">           -- unsigned size_res                : UNRESOLVED_ufixed;<br><span style="padding-left:20px">  -- for size only constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- to_ufixed <font id="function_arguments">( arg : UNRESOLVED_UNSIGNED) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
Performs a conversion.  ufixed (arg'range) is returned
- to_unsigned <font id="function_arguments">( arg                     : UNRESOLVED_ufixed;<br><span style="padding-left:20px">  -- fixed point input constant size           : NATURAL;<br><span style="padding-left:20px">            -- length of output constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
unsigned fixed point to unsigned
- to_unsigned <font id="function_arguments">( arg                     : UNRESOLVED_ufixed;<br><span style="padding-left:20px">    -- fixed point input size_res                : UNRESOLVED_UNSIGNED;<br><span style="padding-left:20px">  -- used for length of output constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_UNSIGNED </font>
**Description**
unsigned fixed point to unsigned
- to_real <font id="function_arguments">( arg : UNRESOLVED_ufixed) </font> <font id="function_return">return REAL </font>
**Description**
unsigned fixed point to real
- to_integer <font id="function_arguments">( arg                     : UNRESOLVED_ufixed;<br><span style="padding-left:20px">  -- fixed point input constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return NATURAL </font>
**Description**
unsigned fixed point to integer
- to_sfixed <font id="function_arguments">( arg                     : INTEGER;<br><span style="padding-left:20px">   -- integer constant left_index     : INTEGER;<br><span style="padding-left:20px">   -- left index (high index) constant right_index    : INTEGER                   := 0;<br><span style="padding-left:20px">  -- right index constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
**Description**
Integer to UNRESOLVED_sfixed
- to_sfixed <font id="function_arguments">( arg                     : INTEGER;<br><span style="padding-left:20px">            -- integer size_res                : UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- for size only constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- to_sfixed <font id="function_arguments">( arg                     : REAL;<br><span style="padding-left:20px">     -- real constant left_index     : INTEGER;<br><span style="padding-left:20px">  -- left index (high index) constant right_index    : INTEGER;<br><span style="padding-left:20px">  -- right index constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style;<br><span style="padding-left:20px"> constant guard_bits     : NATURAL                   := fixed_guard_bits) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
**Description**
Real to sfixed
- to_sfixed <font id="function_arguments">( arg                     : REAL;<br><span style="padding-left:20px">     -- real size_res                : UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- for size only constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style;<br><span style="padding-left:20px"> constant guard_bits     : NATURAL                   := fixed_guard_bits) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- to_sfixed <font id="function_arguments">( arg                     : UNRESOLVED_SIGNED;<br><span style="padding-left:20px">               -- signed constant left_index     : INTEGER;<br><span style="padding-left:20px">  -- left index (high index) constant right_index    : INTEGER                   := 0;<br><span style="padding-left:20px">  -- right index constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
**Description**
signed to sfixed
- to_sfixed <font id="function_arguments">( arg                     : UNRESOLVED_SIGNED;<br><span style="padding-left:20px">  -- signed size_res                : UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- for size only constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- to_sfixed <font id="function_arguments">( arg : UNRESOLVED_SIGNED) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
**Description**
signed to sfixed (output assumed to be size of signed input)
- to_sfixed <font id="function_arguments">( arg : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
**Description**
Conversion from ufixed to sfixed
- to_signed <font id="function_arguments">( arg                     : UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- fixed point input constant size           : NATURAL;<br><span style="padding-left:20px">            -- length of output constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
signed fixed point to signed
- to_signed <font id="function_arguments">( arg                     : UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- fixed point input size_res                : UNRESOLVED_SIGNED;<br><span style="padding-left:20px">  -- used for length of output constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return UNRESOLVED_SIGNED </font>
**Description**
signed fixed point to signed
- to_real <font id="function_arguments">( arg : UNRESOLVED_sfixed) </font> <font id="function_return">return REAL </font>
**Description**
signed fixed point to real
- to_integer <font id="function_arguments">( arg                     : UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- fixed point input constant overflow_style : fixed_overflow_style_type := fixed_overflow_style;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type    := fixed_round_style) </font> <font id="function_return">return INTEGER </font>
**Description**
signed fixed point to integer
- ufixed_high <font id="function_arguments">(left_index,<br><span style="padding-left:20px"> right_index   : INTEGER;<br><span style="padding-left:20px"> operation                 : CHARACTER := 'X';<br><span style="padding-left:20px"> left_index2,<br><span style="padding-left:20px"> right_index2 : INTEGER   := 0) </font> <font id="function_return">return INTEGER </font>
**Description**
Because of the fairly complicated sizing rules in the fixed pointpackages these functions are provided to compute the result rangesExample:signal uf1 : ufixed (3 downto -3);signal uf2 : ufixed (4 downto -2);signal uf1multuf2 : ufixed (ufixed_high (3, -3, '*', 4, -2) downto                            ufixed_low (3, -3, '*', 4, -2));uf1multuf2 <= uf1 * uf2;Valid characters: '+', '-', '*', '/', 'r' or 'R' (rem), 'm' or 'M' (mod),                  '1' (reciprocal), 'a' or 'A' (abs), 'n' or 'N' (unary -)
- ufixed_low <font id="function_arguments">(left_index,<br><span style="padding-left:20px"> right_index   : INTEGER;<br><span style="padding-left:20px"> operation                 : CHARACTER := 'X';<br><span style="padding-left:20px"> left_index2,<br><span style="padding-left:20px"> right_index2 : INTEGER   := 0) </font> <font id="function_return">return INTEGER </font>
- sfixed_high <font id="function_arguments">(left_index,<br><span style="padding-left:20px"> right_index   : INTEGER;<br><span style="padding-left:20px"> operation                 : CHARACTER := 'X';<br><span style="padding-left:20px"> left_index2,<br><span style="padding-left:20px"> right_index2 : INTEGER   := 0) </font> <font id="function_return">return INTEGER </font>
- sfixed_low <font id="function_arguments">(left_index,<br><span style="padding-left:20px"> right_index   : INTEGER;<br><span style="padding-left:20px"> operation                 : CHARACTER := 'X';<br><span style="padding-left:20px"> left_index2,<br><span style="padding-left:20px"> right_index2 : INTEGER   := 0) </font> <font id="function_return">return INTEGER </font>
- ufixed_high <font id="function_arguments">(size_res  : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> operation : CHARACTER := 'X';<br><span style="padding-left:20px"> size_res2 : UNRESOLVED_ufixed) </font> <font id="function_return">return INTEGER </font>
**Description**
Same as above, but using the "size_res" input only for their ranges:signal uf1multuf2 : ufixed (ufixed_high (uf1, '*', uf2) downto                            ufixed_low (uf1, '*', uf2));uf1multuf2 <= uf1 * uf2;
- ufixed_low <font id="function_arguments">(size_res  : UNRESOLVED_ufixed;<br><span style="padding-left:20px"> operation : CHARACTER := 'X';<br><span style="padding-left:20px"> size_res2 : UNRESOLVED_ufixed) </font> <font id="function_return">return INTEGER </font>
- sfixed_high <font id="function_arguments">(size_res  : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> operation : CHARACTER := 'X';<br><span style="padding-left:20px"> size_res2 : UNRESOLVED_sfixed) </font> <font id="function_return">return INTEGER </font>
- sfixed_low <font id="function_arguments">(size_res  : UNRESOLVED_sfixed;<br><span style="padding-left:20px"> operation : CHARACTER := 'X';<br><span style="padding-left:20px"> size_res2 : UNRESOLVED_sfixed) </font> <font id="function_return">return INTEGER </font>
- saturate <font id="function_arguments">( constant left_index  : INTEGER;<br><span style="padding-left:20px"> constant right_index : INTEGER) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
purpose: returns a saturated number
- saturate <font id="function_arguments">( constant left_index  : INTEGER;<br><span style="padding-left:20px"> constant right_index : INTEGER) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
**Description**
purpose: returns a saturated number
- saturate <font id="function_arguments">( size_res : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- saturate <font id="function_arguments">( size_res : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- to_01 <font id="function_arguments">( s             : UNRESOLVED_ufixed;<br><span style="padding-left:20px">  -- fixed point input constant XMAP : STD_ULOGIC := '0') </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
maps meta-logical values
- to_01 <font id="function_arguments">( s             : UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- fixed point input constant XMAP : STD_ULOGIC := '0') </font> <font id="function_return">return UNRESOLVED_sfixed </font>
**Description**
maps meta-logical values
- Is_X <font id="function_arguments">(arg : UNRESOLVED_ufixed) </font> <font id="function_return">return BOOLEAN </font>
- Is_X <font id="function_arguments">(arg : UNRESOLVED_sfixed) </font> <font id="function_return">return BOOLEAN </font>
- to_X01 <font id="function_arguments">(arg : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- to_X01 <font id="function_arguments">(arg : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- to_X01Z <font id="function_arguments">(arg : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- to_X01Z <font id="function_arguments">(arg : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- to_UX01 <font id="function_arguments">(arg : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- to_UX01 <font id="function_arguments">(arg : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- to_slv <font id="function_arguments">( arg : UNRESOLVED_ufixed) </font> <font id="function_return">return STD_LOGIC_VECTOR </font>
**Description**
straight vector conversion routines, needed for synthesis.These functions are here so that a std_logic_vector can beconverted to and from sfixed and ufixed.  Note that you cannot convert these vectors because of their negative index.
- to_slv <font id="function_arguments">( arg : UNRESOLVED_sfixed) </font> <font id="function_return">return STD_LOGIC_VECTOR </font>
- to_sulv <font id="function_arguments">( arg : UNRESOLVED_ufixed) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
- to_sulv <font id="function_arguments">( arg : UNRESOLVED_sfixed) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
- to_ufixed <font id="function_arguments">( arg                  : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px">  -- shifted vector constant left_index  : INTEGER;<br><span style="padding-left:20px"> constant right_index : INTEGER) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- to_ufixed <font id="function_arguments">( arg      : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px">       -- shifted vector size_res : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- to_sfixed <font id="function_arguments">( arg                  : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px">  -- shifted vector constant left_index  : INTEGER;<br><span style="padding-left:20px"> constant right_index : INTEGER) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- to_sfixed <font id="function_arguments">( arg      : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px">       -- shifted vector size_res : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- to_UFix <font id="function_arguments">( arg      : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> width    : NATURAL;<br><span style="padding-left:20px">                 -- width of vector fraction : NATURAL) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
As a concession to those who use a graphical DSP environment,these functions take parameters in those tools format and createfixed point numbers.  These functions are designed to convert froma std_logic_vector to the VHDL fixed point format using the conventionsof these packages.  In a pure VHDL environment you should use the"to_ufixed" and "to_sfixed" routines.unsigned fixed point
- to_SFix <font id="function_arguments">( arg      : STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> width    : NATURAL;<br><span style="padding-left:20px">                 -- width of vector fraction : NATURAL) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
**Description**
signed fixed point
- UFix_high <font id="function_arguments">(width,<br><span style="padding-left:20px"> fraction   : NATURAL;<br><span style="padding-left:20px"> operation         : CHARACTER := 'X';<br><span style="padding-left:20px"> width2,<br><span style="padding-left:20px"> fraction2 : NATURAL   := 0) </font> <font id="function_return">return INTEGER </font>
**Description**
finding the bounds of a number.  These functions can be used like this:signal xxx : ufixed (7 downto -3);-- Which is the same as "ufixed (UFix_high (11,3) downto UFix_low(11,3))"signal yyy : ufixed (UFix_high (11, 3, "+", 11, 3)              downto UFix_low(11, 3, "+", 11, 3));Where "11" is the width of xxx (xxx'length),and 3 is the lower bound (abs (xxx'low))In a pure VHDL environment use "ufixed_high" and "ufixed_low"
- UFix_low <font id="function_arguments">(width,<br><span style="padding-left:20px"> fraction   : NATURAL;<br><span style="padding-left:20px"> operation         : CHARACTER := 'X';<br><span style="padding-left:20px"> width2,<br><span style="padding-left:20px"> fraction2 : NATURAL   := 0) </font> <font id="function_return">return INTEGER </font>
- SFix_high <font id="function_arguments">(width,<br><span style="padding-left:20px"> fraction   : NATURAL;<br><span style="padding-left:20px"> operation         : CHARACTER := 'X';<br><span style="padding-left:20px"> width2,<br><span style="padding-left:20px"> fraction2 : NATURAL   := 0) </font> <font id="function_return">return INTEGER </font>
**Description**
Same as above but for signed fixed point.  Note that the widthof a signed fixed point number ignores the sign bit, thuswidth = sxxx'length-1
- SFix_low <font id="function_arguments">(width,<br><span style="padding-left:20px"> fraction   : NATURAL;<br><span style="padding-left:20px"> operation         : CHARACTER := 'X';<br><span style="padding-left:20px"> width2,<br><span style="padding-left:20px"> fraction2 : NATURAL   := 0) </font> <font id="function_return">return INTEGER </font>
- WRITE <font id="function_arguments">( L         : inout LINE;<br><span style="padding-left:20px">               -- input line VALUE     : in    UNRESOLVED_ufixed;<br><span style="padding-left:20px">  -- fixed point input JUSTIFIED : in    SIDE  := right;<br><span style="padding-left:20px"> FIELD     : in    WIDTH := 0) </font> <font id="function_return">return ()</font>
**Description**
purpose: writes fixed point into a line
- WRITE <font id="function_arguments">( L         : inout LINE;<br><span style="padding-left:20px">               -- input line VALUE     : in    UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- fixed point input JUSTIFIED : in    SIDE  := right;<br><span style="padding-left:20px"> FIELD     : in    WIDTH := 0) </font> <font id="function_return">return ()</font>
**Description**
purpose: writes fixed point into a line
- READ <font id="function_arguments">(L     : inout LINE;<br><span style="padding-left:20px"> VALUE : out   UNRESOLVED_ufixed) </font> <font id="function_return">return ()</font>
- READ <font id="function_arguments">(L     : inout LINE;<br><span style="padding-left:20px"> VALUE : out   UNRESOLVED_ufixed;<br><span style="padding-left:20px"> GOOD  : out   BOOLEAN) </font> <font id="function_return">return ()</font>
- READ <font id="function_arguments">(L     : inout LINE;<br><span style="padding-left:20px"> VALUE : out   UNRESOLVED_sfixed) </font> <font id="function_return">return ()</font>
- READ <font id="function_arguments">(L     : inout LINE;<br><span style="padding-left:20px"> VALUE : out   UNRESOLVED_sfixed;<br><span style="padding-left:20px"> GOOD  : out   BOOLEAN) </font> <font id="function_return">return ()</font>
- OWRITE <font id="function_arguments">( L         : inout LINE;<br><span style="padding-left:20px">               -- input line VALUE     : in    UNRESOLVED_ufixed;<br><span style="padding-left:20px">  -- fixed point input JUSTIFIED : in    SIDE  := right;<br><span style="padding-left:20px"> FIELD     : in    WIDTH := 0) </font> <font id="function_return">return ()</font>
**Description**
octal read and write
- OWRITE <font id="function_arguments">( L         : inout LINE;<br><span style="padding-left:20px">               -- input line VALUE     : in    UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- fixed point input JUSTIFIED : in    SIDE  := right;<br><span style="padding-left:20px"> FIELD     : in    WIDTH := 0) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L     : inout LINE;<br><span style="padding-left:20px"> VALUE : out   UNRESOLVED_ufixed) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L     : inout LINE;<br><span style="padding-left:20px"> VALUE : out   UNRESOLVED_ufixed;<br><span style="padding-left:20px"> GOOD  : out   BOOLEAN) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L     : inout LINE;<br><span style="padding-left:20px"> VALUE : out   UNRESOLVED_sfixed) </font> <font id="function_return">return ()</font>
- OREAD <font id="function_arguments">(L     : inout LINE;<br><span style="padding-left:20px"> VALUE : out   UNRESOLVED_sfixed;<br><span style="padding-left:20px"> GOOD  : out   BOOLEAN) </font> <font id="function_return">return ()</font>
- HWRITE <font id="function_arguments">( L         : inout LINE;<br><span style="padding-left:20px">               -- input line VALUE     : in    UNRESOLVED_ufixed;<br><span style="padding-left:20px">  -- fixed point input JUSTIFIED : in    SIDE  := right;<br><span style="padding-left:20px"> FIELD     : in    WIDTH := 0) </font> <font id="function_return">return ()</font>
**Description**
hex read and write
- HWRITE <font id="function_arguments">( L         : inout LINE;<br><span style="padding-left:20px">               -- input line VALUE     : in    UNRESOLVED_sfixed;<br><span style="padding-left:20px">  -- fixed point input JUSTIFIED : in    SIDE  := right;<br><span style="padding-left:20px"> FIELD     : in    WIDTH := 0) </font> <font id="function_return">return ()</font>
**Description**
purpose: writes fixed point into a line
- HREAD <font id="function_arguments">(L     : inout LINE;<br><span style="padding-left:20px"> VALUE : out   UNRESOLVED_ufixed) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L     : inout LINE;<br><span style="padding-left:20px"> VALUE : out   UNRESOLVED_ufixed;<br><span style="padding-left:20px"> GOOD  : out   BOOLEAN) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L     : inout LINE;<br><span style="padding-left:20px"> VALUE : out   UNRESOLVED_sfixed) </font> <font id="function_return">return ()</font>
- HREAD <font id="function_arguments">(L     : inout LINE;<br><span style="padding-left:20px"> VALUE : out   UNRESOLVED_sfixed;<br><span style="padding-left:20px"> GOOD  : out   BOOLEAN) </font> <font id="function_return">return ()</font>
- to_string <font id="function_arguments">(value : UNRESOLVED_ufixed) </font> <font id="function_return">return STRING </font>
**Description**
returns a string, useful for:assert (x = y) report "error found " & to_string(x) severity error;
- to_ostring <font id="function_arguments">(value : UNRESOLVED_ufixed) </font> <font id="function_return">return STRING </font>
- to_hstring <font id="function_arguments">(value : UNRESOLVED_ufixed) </font> <font id="function_return">return STRING </font>
- to_string <font id="function_arguments">(value : UNRESOLVED_sfixed) </font> <font id="function_return">return STRING </font>
- to_ostring <font id="function_arguments">(value : UNRESOLVED_sfixed) </font> <font id="function_return">return STRING </font>
- to_hstring <font id="function_arguments">(value : UNRESOLVED_sfixed) </font> <font id="function_return">return STRING </font>
- from_string <font id="function_arguments">( bstring              : STRING;<br><span style="padding-left:20px">      -- binary string constant left_index  : INTEGER;<br><span style="padding-left:20px"> constant right_index : INTEGER) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
From string functions allow you to convert a string into a fixedpoint number.  Example: signal uf1 : ufixed (3 downto -3); uf1 <= from_string ("0110.100", uf1'high, uf1'low); -- 6.5The "." is optional in this syntax, however it exist and isin the wrong location an error is produced.  Overflow willresult in saturation.
- from_ostring <font id="function_arguments">( ostring              : STRING;<br><span style="padding-left:20px">      -- Octal string constant left_index  : INTEGER;<br><span style="padding-left:20px"> constant right_index : INTEGER) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
Octal and hex conversions work as follows:uf1 <= from_hstring ("6.8", 3, -3); -- 6.5 (bottom zeros dropped)uf1 <= from_ostring ("06.4", 3, -3); -- 6.5 (top zeros dropped)
- from_hstring <font id="function_arguments">( hstring              : STRING;<br><span style="padding-left:20px">      -- hex string constant left_index  : INTEGER;<br><span style="padding-left:20px"> constant right_index : INTEGER) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- from_string <font id="function_arguments">( bstring              : STRING;<br><span style="padding-left:20px">      -- binary string constant left_index  : INTEGER;<br><span style="padding-left:20px"> constant right_index : INTEGER) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- from_ostring <font id="function_arguments">( ostring              : STRING;<br><span style="padding-left:20px">      -- Octal string constant left_index  : INTEGER;<br><span style="padding-left:20px"> constant right_index : INTEGER) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- from_hstring <font id="function_arguments">( hstring              : STRING;<br><span style="padding-left:20px">      -- hex string constant left_index  : INTEGER;<br><span style="padding-left:20px"> constant right_index : INTEGER) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- from_string <font id="function_arguments">( bstring  : STRING;<br><span style="padding-left:20px">                  -- binary string size_res : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
Same as above, "size_res" is used for it's range only.
- from_ostring <font id="function_arguments">( ostring  : STRING;<br><span style="padding-left:20px">                  -- Octal string size_res : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- from_hstring <font id="function_arguments">( hstring  : STRING;<br><span style="padding-left:20px">                  -- hex string size_res : UNRESOLVED_ufixed) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- from_string <font id="function_arguments">( bstring  : STRING;<br><span style="padding-left:20px">                  -- binary string size_res : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- from_ostring <font id="function_arguments">( ostring  : STRING;<br><span style="padding-left:20px">                  -- Octal string size_res : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- from_hstring <font id="function_arguments">( hstring  : STRING;<br><span style="padding-left:20px">                  -- hex string size_res : UNRESOLVED_sfixed) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- from_string <font id="function_arguments">( bstring : STRING) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
Direct conversion functions.  Example: signal uf1 : ufixed (3 downto -3); uf1 <= from_string ("0110.100"); -- 6.5In this case the "." is not optional, and the size ofthe output must match exactly.
- from_ostring <font id="function_arguments">( ostring : STRING) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
**Description**
Direct octal and hex conversion functions.  In this casethe string lengths must match.  Example:signal sf1 := sfixed (5 downto -3);sf1 <= from_ostring ("71.4") -- -6.5
- from_hstring <font id="function_arguments">( hstring : STRING) </font> <font id="function_return">return UNRESOLVED_ufixed </font>
- from_string <font id="function_arguments">( bstring : STRING) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- from_ostring <font id="function_arguments">( ostring : STRING) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
- from_hstring <font id="function_arguments">( hstring : STRING) </font> <font id="function_return">return UNRESOLVED_sfixed </font>
