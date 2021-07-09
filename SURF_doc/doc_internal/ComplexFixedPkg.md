# Package: ComplexFixedPkg

## Types

| Name         | Type                                | Description |
| ------------ | ----------------------------------- | ----------- |
| cfixed       |                                     |             |
| sfixedArray  | array(natural range <>) of sfixed   |             |
| cfixedArray  | array(natural range<>)  of cfixed   |             |
| realArray    | array(natural range<>) of real      |             |
| complexArray | array(natural range <>) of complex  |             |
## Functions
- to_cfixed <font id="function_arguments">(R,<br><span style="padding-left:20px"> I : REAL;<br><span style="padding-left:20px"> CTYP : cfixed) </font> <font id="function_return">return cfixed </font>
- to_cfixed <font id="function_arguments">(CIN : COMPLEX;<br><span style="padding-left:20px"> CTYP : cfixed) </font> <font id="function_return">return cfixed </font>
- to_cfixed <font id="function_arguments">(R,<br><span style="padding-left:20px"> I : sfixed) </font> <font id="function_return">return cfixed </font>
- to_cfixedArray <font id="function_arguments">( CIN : complexArray;<br><span style="padding-left:20px"> CTYP : cfixed ) </font> <font id="function_return">return cfixedArray </font>
- to_sfixedArray <font id="function_arguments">( SIN : realArray;<br><span style="padding-left:20px"> STYP : sfixed) </font> <font id="function_return">return sfixedArray </font>
- resize <font id="function_arguments">(CIN  : cfixed;<br><span style="padding-left:20px"> CTYP : cfixed;<br><span style="padding-left:20px"> constant overflow_style : fixed_overflow_style_type;<br><span style="padding-left:20px"> constant round_style    : fixed_round_style_type) </font> <font id="function_return">return cfixed </font>
- to_slv <font id="function_arguments">(ARG : cfixed) </font> <font id="function_return">return std_logic_vector </font>
- to_cfixed <font id="function_arguments">(VEC : std_logic_vector;<br><span style="padding-left:20px"> CTYP : cfixed) </font> <font id="function_return">return cfixed </font>
- conj <font id="function_arguments">(ARG : cfixed) </font> <font id="function_return">return cfixed </font>
- swap <font id="function_arguments">(ARG : cfixed) </font> <font id="function_return">return cfixed </font>
