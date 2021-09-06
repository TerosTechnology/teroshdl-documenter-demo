# Package: VITAL_Primitives

- **File**: vital_primitives.vhdl
## Types

| Name                | Type                                                                                                      | Description |
| ------------------- | --------------------------------------------------------------------------------------------------------- | ----------- |
| VitalTruthTableType | ARRAY ( NATURAL RANGE <>,<br><span style="padding-left:20px"> NATURAL RANGE <> ) OF VitalTruthSymbolType  |             |
| VitalStateTableType | ARRAY ( NATURAL RANGE <>,<br><span style="padding-left:20px"> NATURAL RANGE <> ) OF VitalStateSymbolType  |             |
## Functions
- VitalAND <font id="function_arguments">( CONSTANT      Data : IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT ResultMap : IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
**Description**
 ------------------------------------------------------------------------
 VITAL Primitives
 
   The primitives packages contains a collections of common gates, 
 including AND, OR, XOR, NAND, NOR, XNOR, BUF, INV, MUX and DECODER 
 functions.  In addition, for sequential devices, a STATE TABLE construct
 is provided.  For complex functions a modeler may wish to use either
 a collection of connected VITAL primitives, or a TRUTH TABLE construct.

   For each primitive a Function and Procedure is provided.  The primitive
 functions are provided to support behavioral modeling styles.  The 
 primitive procedures are provided to support structural modeling styles.

   The procedures wait internally for an event on an input signal, compute
 the new result, perform glitch handling, schedule transaction on the
 output signals, and wait for future input events.  All of the functional 
 (logic) input or output parameters of the primitive procedures are
 signals.  All the other parameters are constants.

   The procedure primitives are parameterized for separate path delays 
 from each input signal.  All path delays default to 0 ns.
 
   The sequential primitive functions compute the defined function and 
 return a value of type std_ulogic or std_logic_vector.  All parameters
 of the primitive functions are constants of mode IN.

   The primitives are based on 1164 operators. The user may also elect to
   express functions using the 1164 operators as well.  These styles are
   all equally acceptable methods for device modeling.

 ------------------------------------------------------------------------

 Sequential 
 Primitive
 Function Name:   N-input logic device function calls:
                    VitalAND  VitalOR  VitalXOR 
                    VitalNAND VitalNOR VitalXNOR             

 Description:     The function calls return the evaluated logic function
                  corresponding to the function name.

 Arguments:         

  IN                Type                  Description
   Data              std_logic_vector      The input signals for the n-bit
                                           wide logic functions.
   ResultMap         VitalResultMapType    The output signal strength
                                           result map to modify default
                                           result mapping.  
                    
  INOUT
   none

  OUT
   none

  Returns              
                      std_ulogic           The evaluated logic function of
                                           the n-bit wide primitives.

 -------------------------------------------------------------------------

- VitalOR <font id="function_arguments">( CONSTANT      Data : IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT ResultMap : IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalXOR <font id="function_arguments">( CONSTANT      Data : IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT ResultMap : IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalNAND <font id="function_arguments">( CONSTANT      Data : IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT ResultMap : IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalNOR <font id="function_arguments">( CONSTANT      Data : IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT ResultMap : IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalXNOR <font id="function_arguments">( CONSTANT      Data : IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT ResultMap : IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalAND <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Data :  IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT tpd_data_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
**Description**
 -------------------------------------------------------------------------

 Concurrent
 Primitive
 Procedure Name:  N-input logic device concurrent procedure calls.
                         VitalAND  VitalOR  VitalXOR 
                         VitalNAND VitalNOR VitalXNOR             

 Description:     The procedure calls return the evaluated logic function
                  corresponding to the function name as a parameter to the
                  procedure.  Propagation delay form data to q is a
                  a parameter to the procedure.  A vector of delay values
                  for inputs to output are provided.  It is noted that
                  limitations in SDF make the back annotation of the delay
                  array difficult.

 Arguments:         

  IN                  Type                  Description
   Data               std_logic_vector       The input signals for the n-
                                             bit wide logic functions.
   tpd_data_q         VitalDelayArrayType01  The propagation delay from
                                             the data inputs to the output
                                             q.

  INOUT
   none 

  OUT
   q                  std_ulogic             The output signal of the 
                                             evaluated logic function.

  Returns  
   none            

 -------------------------------------------------------------------------

- VitalOR <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Data :  IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT tpd_data_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalXOR <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Data :  IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT tpd_data_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalNAND <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Data :  IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT tpd_data_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalNOR <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Data :  IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT tpd_data_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalXNOR <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Data :  IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT tpd_data_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalAND2 <font id="function_arguments">( CONSTANT       a,<br><span style="padding-left:20px"> b :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
**Description**
 -------------------------------------------------------------------------

 Sequential 
 Primitive
 Function Name:   2,3 and 4 input logic device function calls.
 
                    VitalAND2    VitalOR2    VitalXOR2 
                    VitalAND3    VitalOR3    VitalXOR3             
                    VitalAND4    VitalOR4    VitalXOR4
 
                    VitalNAND2   VitalNOR2   VitalXNOR2             
                    VitalNAND3   VitalNOR3   VitalXNOR3 
                    VitalNAND4   VitalNOR4   VitalXNOR4             

 Description:     The function calls return the evaluated 2, 3 or 4 input
                  logic function corresponding to the function name.

 Arguments:         

  IN             Type               Description
   a, b, c, d     std_ulogic         2 input devices have a and b as 
                                     inputs.  3 input devices have a, b
                                     and c as inputs.  4 input devices 
                                     have a, b, c and d as inputs.
   ResultMap      VitalResultMapType The output signal strength result map
                                     to modify default result mapping.   
                    
  INOUT
   none  

  OUT
   none 

  Returns              
                   std_ulogic        The result of the evaluated logic
                                     function.

 -------------------------------------------------------------------------

- VitalOR2 <font id="function_arguments">( CONSTANT       a,<br><span style="padding-left:20px"> b :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalXOR2 <font id="function_arguments">( CONSTANT       a,<br><span style="padding-left:20px"> b :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalNAND2 <font id="function_arguments">( CONSTANT       a,<br><span style="padding-left:20px"> b :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalNOR2 <font id="function_arguments">( CONSTANT       a,<br><span style="padding-left:20px"> b :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalXNOR2 <font id="function_arguments">( CONSTANT       a,<br><span style="padding-left:20px"> b :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalAND3 <font id="function_arguments">( CONSTANT    a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalOR3 <font id="function_arguments">( CONSTANT    a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalXOR3 <font id="function_arguments">( CONSTANT    a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalNAND3 <font id="function_arguments">( CONSTANT    a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalNOR3 <font id="function_arguments">( CONSTANT    a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalXNOR3 <font id="function_arguments">( CONSTANT    a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalAND4 <font id="function_arguments">( CONSTANT a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c,<br><span style="padding-left:20px"> d :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalOR4 <font id="function_arguments">( CONSTANT a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c,<br><span style="padding-left:20px"> d :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalXOR4 <font id="function_arguments">( CONSTANT a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c,<br><span style="padding-left:20px"> d :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalNAND4 <font id="function_arguments">( CONSTANT a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c,<br><span style="padding-left:20px"> d :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalNOR4 <font id="function_arguments">( CONSTANT a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c,<br><span style="padding-left:20px"> d :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalXNOR4 <font id="function_arguments">( CONSTANT a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c,<br><span style="padding-left:20px"> d :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalAND2 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         a,<br><span style="padding-left:20px"> b :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
**Description**
 -------------------------------------------------------------------------

 Concurrent
 Primitive
 Procedure Name:  2, 3 and 4 input logic device concurrent procedure
                  calls.

                    VitalAND2    VitalOR2    VitalXOR2 
                    VitalAND3    VitalOR3    VitalXOR3             
                    VitalAND4    VitalOR4    VitalXOR4
 
                    VitalNAND2   VitalNOR2   VitalXNOR2             
                    VitalNAND3   VitalNOR3   VitalXNOR3 
                    VitalNAND4   VitalNOR4   VitalXNOR4             

 Description:     The procedure calls return the evaluated logic function
                  corresponding to the function name as a parameter to the
                  procedure.  Propagation delays from a and b to q are 
                  a parameter to the procedure.  The default propagation
                  delay is 0 ns.  

 Arguments:         

  IN             Type               Description
   a, b, c, d     std_ulogic         2 input devices have a and b as 
                                     inputs.  3 input devices have a, b
                                     and c as inputs.  4 input devices 
                                     have a, b, c and d as inputs.
   tpd_a_q        VitalDelayType01   The propagation delay from the a
                                     input to output q for 2, 3 and 4 
                                     input devices.
   tpd_b_q        VitalDelayType01   The propagation delay from the b
                                     input to output q for 2, 3 and 4 
                                     input devices.
   tpd_c_q        VitalDelayType01   The propagation delay from the c
                                     input to output q for 3 and 4 input 
                                     devices.
   tpd_d_q        VitalDelayType01   The propagation delay from the d
                                     input to output q for 4 input 
                                     devices.
   ResultMap      VitalResultMapType The output signal strength result map
                                     to modify default result mapping.  

  INOUT
   none 

  OUT
   q              std_ulogic         The output signal of the evaluated
                                     logic function.

  Returns              
   none
 -------------------------------------------------------------------------

- VitalOR2 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         a,<br><span style="padding-left:20px"> b :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalXOR2 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         a,<br><span style="padding-left:20px"> b :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalNAND2 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         a,<br><span style="padding-left:20px"> b :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalNOR2 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         a,<br><span style="padding-left:20px"> b :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalXNOR2 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         a,<br><span style="padding-left:20px"> b :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalAND3 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL      a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_c_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalOR3 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL      a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_c_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalXOR3 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL      a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_c_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalNAND3 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL      a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_c_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalNOR3 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL      a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_c_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalXNOR3 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL      a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_c_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalAND4 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL   a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c,<br><span style="padding-left:20px"> d :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_c_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_d_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalOR4 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL   a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c,<br><span style="padding-left:20px"> d :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_c_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_d_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalXOR4 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL   a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c,<br><span style="padding-left:20px"> d :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_c_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_d_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalNAND4 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL   a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c,<br><span style="padding-left:20px"> d :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_c_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_d_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalNOR4 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL   a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c,<br><span style="padding-left:20px"> d :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_c_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_d_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalXNOR4 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL   a,<br><span style="padding-left:20px"> b,<br><span style="padding-left:20px"> c,<br><span style="padding-left:20px"> d :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_b_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_c_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    tpd_d_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalBUF <font id="function_arguments">( CONSTANT         Data :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
**Description**
 ------------------------------------------------------------------------

 Sequential 
 Primitive
 Function Name:   Buffer logic device concurrent procedure calls.

 Description:     Four buffer sequential primitive function calls are
                  provided.  One is a simple buffer and the others 
                  offer high and low enables and the four permits
                  propagation of Z as shown below:
 
                     VitalBUF     Standard non-inverting buffer
                     VitalBUFIF0  Non-inverting buffer with Enable low
                     VitalBUFIF1  Non-inverting buffer with Enable high
                     VitalIDENT   Pass buffer capable of propagating Z

 Arguments:         

  IN            Type                Description
   Data          std_ulogic          Input to the buffers
   Enable        std_ulogic          Enable for the enable high and low
                                     buffers.
   ResultMap     VitalResultMapType  The output signal strength result map
                                     to modify default result mapping for
                                     simple buffer.  
                 VitalResultZMapType The output signal strength result map
                                     to modify default result mapping
                                     which has high impedance capability
                                     for the enable high, enable low and
                                     identity buffers.
                    
  INOUT
   none

  OUT
   none

  Returns              
                  std_ulogic        The output signal of the evaluated 
                                    buffer function.

 -------------------------------------------------------------------------

- VitalBUFIF0 <font id="function_arguments">( CONSTANT Data,<br><span style="padding-left:20px"> Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultZMapType := VitalDefaultResultZMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalBUFIF1 <font id="function_arguments">( CONSTANT Data,<br><span style="padding-left:20px"> Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultZMapType := VitalDefaultResultZMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalIDENT <font id="function_arguments">( CONSTANT         Data :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultZMapType := VitalDefaultResultZMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalBUF <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL            a :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
**Description**
 -------------------------------------------------------------------------

 Concurrent
 Primitive
 Procedure Name:  Buffer device procedure calls. 

 Description:     Four buffer concurrent primitive procedure calls are
                  provided.  One is a simple buffer and the others 
                  offer high and low enables and the fourth permits
                  propagation of Z as shown below:
 
                     VitalBUF     Standard non-inverting buffer
                     VitalBUFIF0  Non-inverting buffer with Enable low
                     VitalBUFIF1  Non-inverting buffer with Enable high
                     VitalIDENT   Pass buffer capable of propagating Z

 Arguments:         

  IN            Type                Description
   a             std_ulogic          Input signal to the buffers
   Enable        std_ulogic          Enable signal for the enable high and 
                                     low buffers.
   tpd_a_q       VitalDelayType01    Propagation delay from input to 
                                     output for the simple buffer.
                 VitalDelayType01Z   Propagation delay from input to 
                                     to output for the enable high and low
                                     and identity buffers.
   tpd_enable_q  VitalDelayType01Z   Propagation delay from enable to
                                     output for the enable high and low
                                     buffers.
   ResultMap     VitalResultMapType  The output signal strength result map
                                     to modify default result mapping for
                                     simple buffer.  
                 VitalResultZMapType The output signal strength result map
                                     to modify default result mapping
                                     which has high impedance capability
                                     for the enable high, enable low and
                                     identity buffers.
                    
 INOUT
  none   

 OUT
  q              std_ulogic          Output of the buffers.   

 Returns 
  none             

 -------------------------------------------------------------------------

- VitalBUFIF0 <font id="function_arguments">( SIGNAL              q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL           Data :  IN std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT   tpd_data_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT tpd_enable_q :  IN VitalDelayType01Z   := VitalDefDelay01Z;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultZMapType := VitalDefaultResultZMap) </font> <font id="function_return">return ()</font>
- VitalBUFIF1 <font id="function_arguments">( SIGNAL              q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL           Data :  IN std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT   tpd_data_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT tpd_enable_q :  IN VitalDelayType01Z   := VitalDefDelay01Z;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultZMapType := VitalDefaultResultZMap) </font> <font id="function_return">return ()</font>
- VitalIDENT <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL            a :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01Z   := VitalDefDelay01Z;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultZMapType := VitalDefaultResultZMap ) </font> <font id="function_return">return ()</font>
- VitalINV <font id="function_arguments">( CONSTANT         Data :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
**Description**
 ------------------------------------------------------------------------

 Sequential 
 Primitive
 Function Name:   VitalINV, VitalINVIF0, VitalINVIF1

 Description:     Inverter functions which return the inverted signal
                  value.  Inverters with enable low and high are provided
                  which can drive high impedance when inactive.

 Arguments:         

  IN            Type                Description
   Data          std_ulogic          Input to the inverter
   Enable        std_ulogic          Enable to the enable high and low
                                     inverters.
   ResultMap     VitalResultMap      The output signal strength result map
                                     to modify default result mapping for
                                     simple inverter.
                 VitalResultZMapType The output signal strength result map
                                     to modify default result mapping
                                     which has high impedance capability
                                     for the enable high, enable low
                                     inverters.

  INOUT
   none

  OUT
   none

  Returns              
                 std_ulogic          Output of the inverter

 -------------------------------------------------------------------------

- VitalINVIF0 <font id="function_arguments">( CONSTANT Data,<br><span style="padding-left:20px"> Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultZMapType := VitalDefaultResultZMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalINVIF1 <font id="function_arguments">( CONSTANT Data,<br><span style="padding-left:20px"> Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultZMapType := VitalDefaultResultZMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalINV <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL            a :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    tpd_a_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
**Description**
 -------------------------------------------------------------------------

 Concurrent
 Primitive
 Procedure Name:  VitalINV, VitalINVIF0, VitalINVIF1

 Description:     The concurrent primitive procedure calls implement a 
                  signal inversion function.  The output is a parameter to
                  the procedure.  The path delay information is passed as
                  a parameter to the call.
                  
 Arguments:         

  IN            Type                Description
   a             std_ulogic          Input signal for the simple inverter
   Data          std_ulogic          Input signal for the enable high and
                                     low inverters.
   Enable        std_ulogic          Enable signal for the enable high and 
                                     low inverters.
   tpd_a_q       VitalDelayType01    Propagation delay from input a to
                                     output q for the simple inverter.
   tpd_data_q    VitalDelayType01    Propagation delay from input data to
                                     output q for the enable high and low
                                     inverters.
   tpd_enable_q  VitalDelayType01Z   Propagation delay from input enable
                                     to output q for the enable high and 
                                     low inverters.
   ResultMap     VitalResultMapType  The output signal strength result map
                                     to modify default result mapping for
                                     simple inverter. 
                 VitalResultZMapType The output signal strength result map
                                     to modify default result mapping
                                     which has high impedance capability
                                     for the enable high, enable low
                                     inverters.
                
  INOUT
   none

  OUT
   q               std_ulogic        Output signal of the inverter.

  Returns              
   none

 -------------------------------------------------------------------------

- VitalINVIF0 <font id="function_arguments">( SIGNAL              q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL           Data :  IN std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT   tpd_data_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT tpd_enable_q :  IN VitalDelayType01Z   := VitalDefDelay01Z;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultZMapType := VitalDefaultResultZMap) </font> <font id="function_return">return ()</font>
- VitalINVIF1 <font id="function_arguments">( SIGNAL              q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL           Data :  IN std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT   tpd_data_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT tpd_enable_q :  IN VitalDelayType01Z   := VitalDefDelay01Z;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultZMapType := VitalDefaultResultZMap) </font> <font id="function_return">return ()</font>
- VitalMUX <font id="function_arguments">( CONSTANT       Data :  IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT    dSelect :  IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
**Description**
 ------------------------------------------------------------------------

 Sequential 
 Primitive
 Function Name:   VitalMUX, VitalMUX2, VitalMUX4, VitalMUX8

 Description:     The VitalMUX functions return the selected data bit 
                  based on the value of dSelect.  For MUX2, the function
                  returns data0 when dselect is 0 and returns data1 when
                  dselect is 1.  When dselect is X, result is X for MUX2
                  when data0 /= data1.  X propagation is reduced when the
                  dselect signal is X and both data signals are identical.
                  When this is the case, the result returned is the value
                  of the data signals.

                  For the N input device:
 
                       N must equal 2**(bits of dSelect)  

 Arguments:         

  IN            Type                Description
   Data           std_logic_vector   Input signal for the N-bit, 4-bit and 
                                     8-bit mux.
   Data1,Data0    std_ulogic         Input signals for the 2-bit mux.
   dSelect        std_ulogic         Select signal for 2-bit mux
                  std_logic_vector2  Select signal for 4-bit mux
                  std_logic_vector3  Select signal for 8-bit mux
                  std_logic_vector   Select signal for N-Bit mux
   ResultMap      VitalResultMapType The output signal strength result map
                                     to modify default result mapping for
                                     all muxes. 

  INOUT
   none

  OUT
   none

  Returns              
                  std_ulogic         The value of the selected bit is 
                                     returned.

 -------------------------------------------------------------------------

- VitalMUX2 <font id="function_arguments">( CONSTANT Data1,<br><span style="padding-left:20px"> Data0 :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT      dSelect :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalMUX4 <font id="function_arguments">( CONSTANT       Data :  IN std_logic_vector4;<br><span style="padding-left:20px"> CONSTANT    dSelect :  IN std_logic_vector2;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalMUX8 <font id="function_arguments">( CONSTANT       Data :  IN std_logic_vector8;<br><span style="padding-left:20px"> CONSTANT    dSelect :  IN std_logic_vector3;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_ulogic </font>
- VitalMUX <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Data :  IN std_logic_vector;<br><span style="padding-left:20px"> SIGNAL         dSel :  IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT tpd_data_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT tpd_dsel_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
**Description**
 -------------------------------------------------------------------------

 Concurrent
 Primitive
 Procedure Name:  VitalMUX, VitalMUX2, VitalMUX4, VitalMUX8

 Description:     The VitalMUX concurrent primitive procedures calls
                  return in the output q the value of the selected data
                  bit based on the value of dsel.  For the two bit mux,
                  the data returned is either d0 or d1, the data input.
                  For 4, 8 and N-bit functions, data is the input and is
                  of type std_logic_vector.  For the 2-bit mux, if d0 or
                  d1 are X, the output is X only when d0 do not equal d1.
                  When d0 and d1 are equal, the return value is this value
                  to reduce X propagation.

                  Propagation delay information is passed as a parameter
                  to the procedure call for delays from data to output and
                  select to output.  For 2-bit muxes, the propagation
                  delays from data are provided for d0 and d1 to output.
                  

 Arguments:         

  IN            Type                   Description
   d1,d0          std_ulogic            Input signals for the 2-bit mux.
   Data           std_logic_vector4     Input signals for the 4-bit mux.
                  std_logic_vector8     Input signals for the 8-bit mux.
                  std_logic_vector      Input signals for the N-bit mux.
   dsel           std_ulogic            Select signal for the 2-bit mux.
                  std_logic_vector2     Select signals for the 4-bit mux.
                  std_logic_vector3     Select signals for the 8-bit mux.
                  std_logic_vector      Select signals for the N-bit mux.
   tpd_d1_q       VitalDelayType01      Propagation delay from input d1 to
                                        output q for 2-bit mux.
   tpd_d0_q       VitalDelayType01      Propagation delay from input d0 to
                                        output q for 2-bit mux.
   tpd_data_q     VitalDelayArrayType01 Propagation delay from input data
                                        to output q for 4-bit, 8-bit and
                                        N-bit muxes.
   tpd_dsel_q     VitalDelayType01      Propagation delay from input dsel
                                        to output q for 2-bit mux.
                  VitalDelayArrayType01 Propagation delay from input dsel
                                        to output q for 4-bit, 8-bit and
                                        N-bit muxes.
   ResultMap      VitalResultMapType    The output signal strength result
                                        map to modify default result
                                        mapping for all muxes.

  INOUT
   none

  OUT
   q              std_ulogic            The value of the selected signal.

  Returns              
   none

 -------------------------------------------------------------------------

- VitalMUX2 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL       d1,<br><span style="padding-left:20px"> d0 :  IN std_ulogic;<br><span style="padding-left:20px"> SIGNAL         dSel :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT   tpd_d1_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT   tpd_d0_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT tpd_dsel_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalMUX4 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Data :  IN std_logic_vector4;<br><span style="padding-left:20px"> SIGNAL         dSel :  IN std_logic_vector2;<br><span style="padding-left:20px"> CONSTANT tpd_data_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT tpd_dsel_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalMUX8 <font id="function_arguments">( SIGNAL            q : OUT std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Data :  IN std_logic_vector8;<br><span style="padding-left:20px"> SIGNAL         dSel :  IN std_logic_vector3;<br><span style="padding-left:20px"> CONSTANT tpd_data_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT tpd_dsel_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalDECODER <font id="function_arguments">( CONSTANT       Data :  IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT     Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_logic_vector </font>
**Description**
 ------------------------------------------------------------------------

 Sequential 
 Primitive
 Function Name:   VitalDECODER, VitalDECODER2, VitalDECODER4,
                  VitalDECODER8

 Description:     The VitalDECODER functions are the sequential primitive
                  calls for decoder logic.  The functions are provided
                  for N, 2, 4 and 8-bit outputs.  

                  The N-bit decoder is (2**(bits of data)) wide.

                  The VitalDECODER returns 0 if enable is 0.
                  The VitalDECODER returns the result bit set to 1 if 
                  enable is 1.  All other bits of returned result are 
                  set to 0.

                  The returned array is in descending order: 
                  (n-1 downto 0).
   
 Arguments:         

  IN            Type                Description
   Data          std_ulogic          Input signal for 2-bit decoder.
                 std_logic_vector2   Input signals for 4-bit decoder.
                 std_logic_vector3   Input signals for 8-bit decoder.
                 std_logic_vector    Input signals for N-bit decoder.
   Enable        std_ulogic          Enable input signal.  The result is
                                     output when enable is high.
   ResultMap     VitalResultMapType  The output signal strength result map
                                     to modify default result mapping for
                                     all output signals of the decoders. 

  INOUT
   none

  OUT
   none

  Returns              
                 std_logic_vector2  The output of the 2-bit decoder.
                 std_logic_vector4  The output of the 4-bit decoder.
                 std_logic_vector8  The output of the 8-bit decoder.   
                 std_logic_vector   The output of the n-bit decoder.

 -------------------------------------------------------------------------

- VitalDECODER2 <font id="function_arguments">( CONSTANT       Data :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT     Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_logic_vector2 </font>
- VitalDECODER4 <font id="function_arguments">( CONSTANT       Data :  IN std_logic_vector2;<br><span style="padding-left:20px"> CONSTANT     Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_logic_vector4 </font>
- VitalDECODER8 <font id="function_arguments">( CONSTANT       Data :  IN std_logic_vector3;<br><span style="padding-left:20px"> CONSTANT     Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT  ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">RETURN std_logic_vector8 </font>
- VitalDECODER <font id="function_arguments">( SIGNAL              q : OUT std_logic_vector;<br><span style="padding-left:20px"> SIGNAL           Data :  IN std_logic_vector;<br><span style="padding-left:20px"> SIGNAL         Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT   tpd_data_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT tpd_enable_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
**Description**
 -------------------------------------------------------------------------

 Concurrent
 Primitive
 Procedure Name:  VitalDECODER, VitalDECODER2, VitalDECODER4,
                  VitalDECODER8

 Description:     The VitalDECODER procedures are the concurrent primitive 
                  procedure calls for decoder functions.  The procedures 
                  are provided for N, 2, 4 and 8 outputs.  

                  The N-bit decoder is (2**(bits of data)) wide.

                  The procedural form of the decoder is used for
                  distributed delay modeling.  The delay information for
                  each path is passed as an argument to the procedure.

                  Result is set to 0 if enable is 0.
                  The result bit represented by data is set to 1 if 
                  enable is 1.  All other bits of result are set to 0.

                  The result array is in descending order: (n-1 downto 0).
   
                  For the N-bit decoder, the delay path is a vector of
                  delays from inputs to outputs.  

 Arguments:         

  IN            Type                  Description
   Data          std_ulogic            Input signal for 2-bit decoder.
                 std_logic_vector2     Input signals for 4-bit decoder.
                 std_logic_vector3     Input signals for 8-bit decoder.
                 std_logic_vector      Input signals for N-bit decoder.
   enable        std_ulogic            Enable input signal.  The result is
                                       output when enable is high. 
   tpd_data_q    VitalDelayType01      Propagation delay from input data
                                       to output q for 2-bit decoder.
                 VitalDelayArrayType01 Propagation delay from input data
                                       to output q for 4, 8 and n-bit
                                       decoders.
   tpd_enable_q  VitalDelayType01      Propagation delay from input enable
                                       to output q for 2, 4, 8 and n-bit
                                       decoders.

 INOUT
  none

 OUT
  q              std_logic_vector2     Output signals for 2-bit decoder. 
                 std_logic_vector4     Output signals for 4-bit decoder.
                 std_logic_vector8     Output signals for 8-bit decoder.
                 std_logic_vector      Output signals for n-bit decoder.
                        
 Returns              
  none

 -------------------------------------------------------------------------    

- VitalDECODER2 <font id="function_arguments">( SIGNAL              q : OUT std_logic_vector2;<br><span style="padding-left:20px"> SIGNAL           Data :  IN std_ulogic;<br><span style="padding-left:20px"> SIGNAL         Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT   tpd_data_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT tpd_enable_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalDECODER4 <font id="function_arguments">( SIGNAL              q : OUT std_logic_vector4;<br><span style="padding-left:20px"> SIGNAL           Data :  IN std_logic_vector2;<br><span style="padding-left:20px"> SIGNAL         Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT   tpd_data_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT tpd_enable_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalDECODER8 <font id="function_arguments">( SIGNAL              q : OUT std_logic_vector8;<br><span style="padding-left:20px"> SIGNAL           Data :  IN std_logic_vector3;<br><span style="padding-left:20px"> SIGNAL         Enable :  IN std_ulogic;<br><span style="padding-left:20px"> CONSTANT   tpd_data_q :  IN VitalDelayArrayType01;<br><span style="padding-left:20px"> CONSTANT tpd_enable_q :  IN VitalDelayType01    := VitalDefDelay01;<br><span style="padding-left:20px"> CONSTANT    ResultMap :  IN VitalResultMapType := VitalDefaultResultMap ) </font> <font id="function_return">return ()</font>
- VitalTruthTable <font id="function_arguments">( CONSTANT TruthTable   : IN VitalTruthTableType;<br><span style="padding-left:20px"> CONSTANT DataIn       : IN std_logic_vector ) </font> <font id="function_return">RETURN std_logic_vector </font>
**Description**
 -------------------------------------------------------------------------
 Function Name:   VitalTruthTable

 Description:     VitalTruthTable implements a truth table.  Given
                  a set of inputs, a sequential search is performed
                  to match the input.  If a match is found, the output
                  is set based on the contents of the CONSTANT TruthTable.
                  If there is no match, all X's are returned.  There is
                  no limit to the size of the table.

                  There is a procedure and function for VitalTruthTable.
                  For each of these, a single value output (std_logic) and
                  a multi-value output (std_logic_vector) are provided.

                  The first dimension of the table is for number of
                  entries in the truth table and second dimension is for
                  the number of elements in a row. The number of inputs
                  in the row should be Data'LENGTH plus result'LENGTH.

                  Elements is a row will be interpreted as
                  Input(NumInputs - 1),.., Input(0),
                    Result(NumOutputs - 1),.., Result(0)

                  All inputs will be mapped to the X01 subtype

                  If the value of Result is not in the range 'X' to 'Z'
                  then an error will be reported. Also, the Result is
                  always given either as a 0, 1, X or Z value.

 Arguments:         

  IN            Type               Description
                 TruthTable         The input constant which defines the
                                    behavior in truth table form.
                 DataIn             The inputs to the truth table used to
                                    perform input match to select
                                    output(s) to value(s) to drive.

  INOUT
   none                 

  OUT
   Result         std_logic         Concurrent procedure version scalar
                                    output.
                  std_logic_vector  Concurrent procedure version vector
                                    output.

  Returns              
   Result         std_logic         Function version scalar output.
                  std_logic_vector  Function version vector output.

 -------------------------------------------------------------------------

- VitalTruthTable <font id="function_arguments">( CONSTANT TruthTable   : IN VitalTruthTableType;<br><span style="padding-left:20px"> CONSTANT DataIn       : IN std_logic_vector ) </font> <font id="function_return">RETURN std_logic </font>
- VitalTruthTable <font id="function_arguments">( SIGNAL   Result       : OUT std_logic_vector;<br><span style="padding-left:20px"> CONSTANT TruthTable   : IN VitalTruthTableType;<br><span style="padding-left:20px"> CONSTANT DataIn       : IN std_logic_vector ) </font> <font id="function_return">return ()</font>
- VitalTruthTable <font id="function_arguments">( SIGNAL   Result       : OUT std_logic;<br><span style="padding-left:20px"> CONSTANT TruthTable   : IN VitalTruthTableType;<br><span style="padding-left:20px"> CONSTANT DataIn       : IN std_logic_vector ) </font> <font id="function_return">return ()</font>
- VitalStateTable <font id="function_arguments">( VARIABLE Result         : INOUT std_logic_vector;<br><span style="padding-left:20px"> VARIABLE PreviousDataIn : INOUT std_logic_vector;<br><span style="padding-left:20px"> CONSTANT StateTable     : IN VitalStateTableType;<br><span style="padding-left:20px"> CONSTANT DataIn         : IN  std_logic_vector;<br><span style="padding-left:20px"> CONSTANT NumStates      : IN NATURAL ) </font> <font id="function_return">return ()</font>
**Description**
 -------------------------------------------------------------------------

 Function Name:   VitalStateTable

 Description:     VitalStateTable is a non-concurrent implementation of a
                  state machine (Moore Machine).  It is used to model
                  sequential devices and devices with internal states.

                  The procedure takes the value of the state table
                  data set and performs a sequential search of the 
                  CONSTANT StateTable until a match is found.  Once a 
                  match is found, the result of that match is applied
                  to Result.  If there is no match, all X's are returned.
                  The resultant output becomes the input for the next 
                  state.

                  The first dimension of the table is the number of
                  entries in the state table and second dimension is the
                  number of elements in a row of the table. The number of
                  inputs in the row should be DataIn'LENGTH. Result should
                  contain the current state (which will become the next
                  state) as well as the outputs

                  Elements is a row of the table will be interpreted as
                  Input(NumInputs-1),.., Input(0), State(NumStates-1),
                   ..., State(0),Output(NumOutputs-1),.., Output(0)
 
                  where State(numStates-1) DOWNTO State(0) represent the
                  present state and Output(NumOutputs - 1) DOWNTO
                  Outputs(NumOutputs - NumStates) represent the new
                  values of the state variables (i.e. the next state).
                  Also, Output(NumOutputs - NumStates - 1)

                  This procedure returns the next state and the new
                  outputs when a match is made between the present state
                  and present inputs and the state table.  A search is
                  made starting at the top of the state table and
                  terminates with the first match.  If no match is found
                  then the next state and new outputs are set to all 'X's.

                  (Asynchronous inputs (i.e. resets and clears) must be
                  handled by placing the corresponding entries at the top
                  of the table. )

                  All inputs will be mapped to the X01 subtype.

                  NOTE:  Edge transitions should not be used as values
                         for the state variables in the present state
                         portion of the state table.  The only valid
                         values that can be used for the present state
                         portion of the state table are:
                         'X', '0', '1', 'B', '-'

 Arguments:         

  IN             Type                 Description      
   StateTable     VitalStateTableType  The input constant which defines
                                       the behavior in state table form.
   DataIn         std_logic_vector     The current state inputs to the
                                       state table used to perform input
                                       matches and transition
                                       calculations.
   NumStates      NATURAL              Number of state variables
                    
  INOUT
   Result         std_logic            Output signal for scalar version of
                                       the concurrent procedure call.
                  std_logic_vector     Output signals for vector version
                                       of the concurrent procedure call.
   PreviousDataIn std_logic_vector     The previous inputs and states used
                                       in transition calculations and to 
                                       set outputs for steady state cases. 

  OUT
   none

  Returns  
   none            

 -------------------------------------------------------------------------

- VitalStateTable <font id="function_arguments">( VARIABLE Result         : INOUT std_logic;<br><span style="padding-left:20px"> VARIABLE PreviousDataIn : INOUT std_logic_vector;<br><span style="padding-left:20px"> CONSTANT StateTable     : IN VitalStateTableType;<br><span style="padding-left:20px"> CONSTANT DataIn         : IN  std_logic_vector ) </font> <font id="function_return">return ()</font>
- VitalStateTable <font id="function_arguments">( SIGNAL   Result     : INOUT std_logic_vector;<br><span style="padding-left:20px"> CONSTANT StateTable : IN VitalStateTableType;<br><span style="padding-left:20px"> SIGNAL   DataIn     : IN std_logic_vector;<br><span style="padding-left:20px"> CONSTANT NumStates  : IN NATURAL ) </font> <font id="function_return">return ()</font>
- VitalStateTable <font id="function_arguments">( SIGNAL   Result     : INOUT std_logic;<br><span style="padding-left:20px"> CONSTANT StateTable : IN VitalStateTableType;<br><span style="padding-left:20px"> SIGNAL   DataIn     : IN std_logic_vector ) </font> <font id="function_return">return ()</font>
- VitalResolve <font id="function_arguments">( SIGNAL              q : OUT std_ulogic;<br><span style="padding-left:20px"> CONSTANT         Data :  IN std_logic_vector) </font> <font id="function_return">return ()</font>
**Description**
 -------------------------------------------------------------------------

 Function Name:   VitalResolve

 Description:     VitalResolve takes a vector of signals and resolves
                  them to a std_ulogic value.  This procedure can be used
                  to resolve multiple drivers in a single model.  
                  
 Arguments:         

  IN           Type               Description
   Data         std_logic_vector   Set of input signals which drive a
                                   common signal.
                    
  INOUT
   none

  OUT
   q            std_ulogic         Output signal which is the resolved 
                                   value being driven by the collection of
                                   input signals.

  Returns              
   none
                    
 -------------------------------------------------------------------------

