# Package: std_logic_misc

- **File**: std_logic_misc.vhdl
## Description

library SYNOPSYS;
use SYNOPSYS.attributes.all;

## Types

| Name     | Type                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description             |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| STRENGTH | (strn_X01,<br><span style="padding-left:20px"> strn_X0H,<br><span style="padding-left:20px"> strn_XL1,<br><span style="padding-left:20px"> strn_X0Z,<br><span style="padding-left:20px"> strn_XZ1,<br><span style="padding-left:20px"> strn_WLH,<br><span style="padding-left:20px"> strn_WLZ,<br><span style="padding-left:20px"> strn_WZH,<br><span style="padding-left:20px"> strn_W0H,<br><span style="padding-left:20px"> strn_WL1)  |                         |
| MINOMAX  |                                                                                                                                                                                                                                                                                                                                                                                                                                           | synopsys synthesis_off  |
## Functions
- strength_map <font id="function_arguments">(input: STD_ULOGIC;<br><span style="padding-left:20px"> strn: STRENGTH) </font> <font id="function_return">return STD_LOGIC </font>
**Description**
-------------------------------------------------------------------

 functions for mapping the STD_(U)LOGIC according to STRENGTH

-------------------------------------------------------------------

- strength_map_z <font id="function_arguments">(input:STD_ULOGIC;<br><span style="padding-left:20px"> strn:STRENGTH) </font> <font id="function_return">return STD_LOGIC </font>
- Drive <font id="function_arguments">(V: STD_ULOGIC_VECTOR) </font> <font id="function_return">return STD_LOGIC_VECTOR </font>
**Description**
-------------------------------------------------------------------

 conversion functions for STD_ULOGIC_VECTOR and STD_LOGIC_VECTOR

-------------------------------------------------------------------
synopsys synthesis_on

- Drive <font id="function_arguments">(V: STD_LOGIC_VECTOR) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
- Sense <font id="function_arguments">(V: STD_ULOGIC;<br><span style="padding-left:20px"> vZ,<br><span style="padding-left:20px"> vU,<br><span style="padding-left:20px"> vDC: STD_ULOGIC) </font> <font id="function_return">return STD_LOGIC </font>
**Description**
synopsys synthesis_off
attribute CLOSELY_RELATED_TCF of Drive: function is TRUE;
-------------------------------------------------------------------

 conversion functions for sensing various types
 (the second argument allows the user to specify the value to
  be returned when the network is undriven)

-------------------------------------------------------------------

- Sense <font id="function_arguments">(V: STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> vZ,<br><span style="padding-left:20px"> vU,<br><span style="padding-left:20px"> vDC: STD_ULOGIC) </font> <font id="function_return">return STD_LOGIC_VECTOR </font>
- Sense <font id="function_arguments">(V: STD_ULOGIC_VECTOR;<br><span style="padding-left:20px"> vZ,<br><span style="padding-left:20px"> vU,<br><span style="padding-left:20px"> vDC: STD_ULOGIC) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
- Sense <font id="function_arguments">(V: STD_LOGIC_VECTOR;<br><span style="padding-left:20px"> vZ,<br><span style="padding-left:20px"> vU,<br><span style="padding-left:20px"> vDC: STD_ULOGIC) </font> <font id="function_return">return STD_LOGIC_VECTOR </font>
- Sense <font id="function_arguments">(V: STD_LOGIC_VECTOR;<br><span style="padding-left:20px"> vZ,<br><span style="padding-left:20px"> vU,<br><span style="padding-left:20px"> vDC: STD_ULOGIC) </font> <font id="function_return">return STD_ULOGIC_VECTOR </font>
- STD_LOGIC_VECTORtoBIT_VECTOR <font id="function_arguments">(V: STD_LOGIC_VECTOR ;<br><span style="padding-left:20px"> vX,<br><span style="padding-left:20px"> vZ,<br><span style="padding-left:20px"> vU,<br><span style="padding-left:20px"> vDC: BIT := '0';<br><span style="padding-left:20px"> Xflag,<br><span style="padding-left:20px"> Zflag,<br><span style="padding-left:20px"> Uflag,<br><span style="padding-left:20px"> DCflag: BOOLEAN := FALSE ) </font> <font id="function_return">return BIT_VECTOR </font>
**Description**
synopsys synthesis_on
-------------------------------------------------------------------

	Function: STD_LOGIC_VECTORtoBIT_VECTOR STD_ULOGIC_VECTORtoBIT_VECTOR

	Purpose: Conversion fun. from STD_(U)LOGIC_VECTOR to BIT_VECTOR

	Mapping:	0, L --> 0
			1, H --> 1
			X, W --> vX if Xflag is TRUE
			X, W --> 0  if Xflag is FALSE
			Z --> vZ if Zflag is TRUE
			Z --> 0  if Zflag is FALSE
			U --> vU if Uflag is TRUE
			U --> 0  if Uflag is FALSE
			- --> vDC if DCflag is TRUE
			- --> 0  if DCflag is FALSE

-------------------------------------------------------------------

- STD_ULOGIC_VECTORtoBIT_VECTOR <font id="function_arguments">(V: STD_ULOGIC_VECTOR ;<br><span style="padding-left:20px"> vX,<br><span style="padding-left:20px"> vZ,<br><span style="padding-left:20px"> vU,<br><span style="padding-left:20px"> vDC: BIT := '0';<br><span style="padding-left:20px"> Xflag,<br><span style="padding-left:20px"> Zflag,<br><span style="padding-left:20px"> Uflag,<br><span style="padding-left:20px"> DCflag: BOOLEAN := FALSE ) </font> <font id="function_return">return BIT_VECTOR </font>
- STD_ULOGICtoBIT <font id="function_arguments">(V: STD_ULOGIC ;<br><span style="padding-left:20px"> vX,<br><span style="padding-left:20px"> vZ,<br><span style="padding-left:20px"> vU,<br><span style="padding-left:20px"> vDC: BIT := '0';<br><span style="padding-left:20px"> Xflag,<br><span style="padding-left:20px"> Zflag,<br><span style="padding-left:20px"> Uflag,<br><span style="padding-left:20px"> DCflag: BOOLEAN := FALSE ) </font> <font id="function_return">return BIT </font>
**Description**
-------------------------------------------------------------------

	Function: STD_ULOGICtoBIT

	Purpose: Conversion function from STD_(U)LOGIC to BIT

	Mapping:	0, L --> 0
			1, H --> 1
			X, W --> vX if Xflag is TRUE
			X, W --> 0  if Xflag is FALSE
			Z --> vZ if Zflag is TRUE
			Z --> 0  if Zflag is FALSE
			U --> vU if Uflag is TRUE
			U --> 0  if Uflag is FALSE
			- --> vDC if DCflag is TRUE
			- --> 0  if DCflag is FALSE

-------------------------------------------------------------------

- AND_REDUCE <font id="function_arguments">(ARG: STD_LOGIC_VECTOR) </font> <font id="function_return">return UX01 </font>
**Description**
------------------------------------------------------------------

- NAND_REDUCE <font id="function_arguments">(ARG: STD_LOGIC_VECTOR) </font> <font id="function_return">return UX01 </font>
- OR_REDUCE <font id="function_arguments">(ARG: STD_LOGIC_VECTOR) </font> <font id="function_return">return UX01 </font>
- NOR_REDUCE <font id="function_arguments">(ARG: STD_LOGIC_VECTOR) </font> <font id="function_return">return UX01 </font>
- XOR_REDUCE <font id="function_arguments">(ARG: STD_LOGIC_VECTOR) </font> <font id="function_return">return UX01 </font>
- XNOR_REDUCE <font id="function_arguments">(ARG: STD_LOGIC_VECTOR) </font> <font id="function_return">return UX01 </font>
- AND_REDUCE <font id="function_arguments">(ARG: STD_ULOGIC_VECTOR) </font> <font id="function_return">return UX01 </font>
- NAND_REDUCE <font id="function_arguments">(ARG: STD_ULOGIC_VECTOR) </font> <font id="function_return">return UX01 </font>
- OR_REDUCE <font id="function_arguments">(ARG: STD_ULOGIC_VECTOR) </font> <font id="function_return">return UX01 </font>
- NOR_REDUCE <font id="function_arguments">(ARG: STD_ULOGIC_VECTOR) </font> <font id="function_return">return UX01 </font>
- XOR_REDUCE <font id="function_arguments">(ARG: STD_ULOGIC_VECTOR) </font> <font id="function_return">return UX01 </font>
- XNOR_REDUCE <font id="function_arguments">(ARG: STD_ULOGIC_VECTOR) </font> <font id="function_return">return UX01 </font>
- fun_BUF3S <font id="function_arguments">(Input,<br><span style="padding-left:20px"> Enable: UX01;<br><span style="padding-left:20px"> Strn: STRENGTH) </font> <font id="function_return">return STD_LOGIC </font>
**Description**
synopsys synthesis_off

- fun_BUF3SL <font id="function_arguments">(Input,<br><span style="padding-left:20px"> Enable: UX01;<br><span style="padding-left:20px"> Strn: STRENGTH) </font> <font id="function_return">return STD_LOGIC </font>
- fun_MUX2x1 <font id="function_arguments">(Input0,<br><span style="padding-left:20px"> Input1,<br><span style="padding-left:20px"> Sel: UX01) </font> <font id="function_return">return UX01 </font>
- fun_MAJ23 <font id="function_arguments">(Input0,<br><span style="padding-left:20px"> Input1,<br><span style="padding-left:20px"> Input2: UX01) </font> <font id="function_return">return UX01 </font>
- fun_WiredX <font id="function_arguments">(Input0,<br><span style="padding-left:20px"> Input1: std_ulogic) </font> <font id="function_return">return STD_LOGIC </font>
