# Package: VITAL_Timing

- **File**: timing_p.vhdl
## Constants

| Name                   | Type                | Value                                                                                                                                                                             | Description                                                                                                                                                                                                              |
| ---------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| VitalZeroDelay         | VitalDelayType      |    0 ns                                                                                                                                                                           |  ----------------------------------------------------------------------  **********************************************************************  ----------------------------------------------------------------------  |
| VitalZeroDelay01       | VitalDelayType01    |  ( 0 ns,<br><span style="padding-left:20px"> 0 ns )                                                                                                                               |                                                                                                                                                                                                                          |
| VitalZeroDelay01Z      | VitalDelayType01Z   |  ( OTHERS => 0 ns )                                                                                                                                                               |                                                                                                                                                                                                                          |
| VitalZeroDelay01ZX     | VitalDelayType01ZX  |  ( OTHERS => 0 ns )                                                                                                                                                               |                                                                                                                                                                                                                          |
| VitalDefaultOutputMap  | VitalOutputMapType  |  "UX01ZWLH-"                                                                                                                                                                      |                                                                                                                                                                                                                          |
| VitalDefaultResultMap  | VitalResultMapType  |  ( 'U',<br><span style="padding-left:20px"> 'X',<br><span style="padding-left:20px"> '0',<br><span style="padding-left:20px"> '1' )                                               |                                                                                                                                                                                                                          |
| VitalDefaultResultZMap | VitalResultZMapType |  ( 'U',<br><span style="padding-left:20px"> 'X',<br><span style="padding-left:20px"> '0',<br><span style="padding-left:20px"> '1',<br><span style="padding-left:20px"> 'Z' )      |                                                                                                                                                                                                                          |
| VitalPeriodDataInit    | VitalPeriodDataType |  ('X',<br><span style="padding-left:20px"> 0 ns,<br><span style="padding-left:20px"> 0 ns,<br><span style="padding-left:20px"> FALSE )                                            |                                                                                                                                                                                                                          |
| VitalSkewDataInit      | VitalSkewDataType   |  ( none,<br><span style="padding-left:20px"> 0 ns,<br><span style="padding-left:20px"> 0 ns,<br><span style="padding-left:20px"> 0 ns,<br><span style="padding-left:20px"> 0 ns ) |                                                                                                                                                                                                                          |
## Types

| Name                     | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VitalTransitionType      | ( tr01,<br><span style="padding-left:20px"> tr10,<br><span style="padding-left:20px"> tr0z,<br><span style="padding-left:20px"> trz1,<br><span style="padding-left:20px"> tr1z,<br><span style="padding-left:20px"> trz0,<br><span style="padding-left:20px"> tr0X,<br><span style="padding-left:20px"> trx1,<br><span style="padding-left:20px"> tr1x,<br><span style="padding-left:20px"> trx0,<br><span style="padding-left:20px"> trxz,<br><span style="padding-left:20px"> trzx)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                      |
| VitalDelayType01         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
| VitalDelayType01Z        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
| VitalDelayType01ZX       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
| VitalDelayArrayType      | ARRAY (NATURAL RANGE <>) OF VitalDelayType                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                      |
| VitalDelayArrayType01    | ARRAY (NATURAL RANGE <>) OF VitalDelayType01                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                      |
| VitalDelayArrayType01Z   | ARRAY (NATURAL RANGE <>) OF VitalDelayType01Z                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                      |
| VitalDelayArrayType01ZX  | ARRAY (NATURAL RANGE <>) OF VitalDelayType01ZX                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                      |
| VitalOutputMapType       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  Types for strength mapping of outputs                                                                                                                                                                                                                               |
| VitalResultMapType       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
| VitalResultZMapType      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
| VitalTimeArrayT          | ARRAY (INTEGER RANGE <>) OF TIME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |  Types for fields of VitalTimingDataType                                                                                                                                                                                                                             |
| VitalTimeArrayPT         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
| VitalBoolArrayT          | ARRAY (INTEGER RANGE <>) OF BOOLEAN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                      |
| VitalBoolArrayPT         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
| VitalLogicArrayPT        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
| VitalTimingDataType      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
| VitalPeriodDataType      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  type for internal data of VitalPeriodPulseCheck                                                                                                                                                                                                                     |
| VitalGlitchKindType      | (OnEvent,<br><span style="padding-left:20px"> OnDetect,<br><span style="padding-left:20px"> VitalInertial,<br><span style="padding-left:20px"> VitalTransport)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  Type for specifying the kind of Glitch handling to use                                                                                                                                                                                                              |
| VitalGlitchDataType      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
| VitalGlitchDataArrayType | ARRAY (NATURAL RANGE <>) OF VitalGlitchDataType                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
| VitalPathType            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  PathTypes: for handling simple PathDelay info                                                                                                                                                                                                                       |
| VitalPath01Type          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
| VitalPath01ZType         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
| VitalPathArrayType       | ARRAY (NATURAL RANGE <> ) OF VitalPathType                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |  For representing multiple paths to an output                                                                                                                                                                                                                        |
| VitalPathArray01Type     | ARRAY (NATURAL RANGE <> ) OF VitalPath01Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                      |
| VitalPathArray01ZType    | ARRAY (NATURAL RANGE <> ) OF VitalPath01ZType                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                      |
| VitalTableSymbolType     | ( '/',<br><span style="padding-left:20px">      -- 0 -> 1 '\',<br><span style="padding-left:20px">      -- 1 -> 0 'P',<br><span style="padding-left:20px">      -- Union of '/' and '^' (any edge to 1) 'N',<br><span style="padding-left:20px">      -- Union of '\' and 'v' (any edge to 0) 'r',<br><span style="padding-left:20px">      -- 0 -> X 'f',<br><span style="padding-left:20px">      -- 1 -> X 'p',<br><span style="padding-left:20px">      -- Union of '/' and 'r' (any edge from 0) 'n',<br><span style="padding-left:20px">      -- Union of '\' and 'f' (any edge from 1) 'R',<br><span style="padding-left:20px">      -- Union of '^' and 'p' (any possible rising edge) 'F',<br><span style="padding-left:20px">      -- Union of 'v' and 'n' (any possible falling edge) '^',<br><span style="padding-left:20px">      -- X -> 1 'v',<br><span style="padding-left:20px">      -- X -> 0 'E',<br><span style="padding-left:20px">      -- Union of 'v' and '^' (any edge from X) 'A',<br><span style="padding-left:20px">      -- Union of 'r' and '^' (rising edge to or from 'X') 'D',<br><span style="padding-left:20px">      -- Union of 'f' and 'v' (falling edge to or from 'X') '*',<br><span style="padding-left:20px">      -- Union of 'R' and 'F' (any edge) 'X',<br><span style="padding-left:20px">      -- Unknown level '0',<br><span style="padding-left:20px">      -- low level '1',<br><span style="padding-left:20px">      -- high level 'B',<br><span style="padding-left:20px">      -- 0 or 1 'Z',<br><span style="padding-left:20px">      -- High Impedance 'S'       -- steady value )  |                                                                                                                                                                                                                                                                      |
| VitalSkewExpectedType    | (none,<br><span style="padding-left:20px"> s1r,<br><span style="padding-left:20px"> s1f,<br><span style="padding-left:20px"> s2r,<br><span style="padding-left:20px"> s2f)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |  Addition of Vital Skew Type Information   March 14, 1998  -------------------------------------------------------------------------  Procedures and Type Definitions for Defining Skews  -------------------------------------------------------------------------  |
| VitalSkewDataType        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                      |
## Functions
- VitalTimingDataInit <font id="function_arguments">()</font> <font id="function_return">RETURN VitalTimingDataType </font>
- VitalExtendToFillDelay <font id="function_arguments">( CONSTANT Delay : IN VitalDelayType ) </font> <font id="function_return">RETURN VitalDelayType01Z </font>
**Description**
 ------------------------------------------------------------------------

 Function Name:   VitalExtendToFillDelay

 Description:     A six element array of delay values of type 
                  VitalDelayType01Z is returned when a 1, 2 or 6
                  element array is given.  This function will convert
                  VitalDelayType and VitalDelayType01 delay values into
                  a VitalDelayType01Z type following these rules:

                  When a VitalDelayType is passed, all six transition
                  values are assigned the input value.  When a 
                  VitalDelayType01 is passed, the 01 transitions are
                  assigned to the 01, 0Z and Z1 transitions and the 10
                  transitions are assigned to 10, 1Z and Z0 transition
                  values.  When a VitalDelayType01Z is passed, the values
                  are kept as is.

                  The function is overloaded based on input type.

                  There is no function to fill a 12 value delay
                  type.

 Arguments:         

  IN                 Type           Description
                     Delay          A one, two or six delay value Vital-
                                    DelayType is passed and a six delay,
                                    VitalDelayType01Z, item is returned.        
                    
  INOUT
   none

  OUT
   none

  Returns              
   VitalDelayType01Z

 -------------------------------------------------------------------------

- VitalExtendToFillDelay <font id="function_arguments">( CONSTANT Delay : IN VitalDelayType01 ) </font> <font id="function_return">RETURN VitalDelayType01Z </font>
- VitalExtendToFillDelay <font id="function_arguments">( CONSTANT Delay : IN VitalDelayType01Z ) </font> <font id="function_return">RETURN VitalDelayType01Z </font>
- VitalCalcDelay <font id="function_arguments">( CONSTANT NewVal : IN std_ulogic   := 'X';<br><span style="padding-left:20px"> CONSTANT OldVal : IN std_ulogic   := 'X';<br><span style="padding-left:20px"> CONSTANT Delay  : IN VitalDelayType ) </font> <font id="function_return">RETURN TIME </font>
**Description**
 ------------------------------------------------------------------------

 Function Name:   VitalCalcDelay

 Description:     This function accepts a 1, 2 or 6 value delay and 
                  chooses the correct delay time to delay the NewVal 
                  signal.  This function is overloaded based on the
                  delay type passed. The function returns a single value
                  of time.

                  This function is provided for Level 0 models in order
                  to calculate the delay which should be applied 
                  for the passed signal. The delay selection is performed
                  using the OldVal and the NewVal to determine the 
                  transition to select.  The default value of OldVal is X.

                  This function cannot be used in a Level 1 model since
                  the VitalPathDelay routines perform the delay path
                  selection and output driving function.

 Arguments:         

  IN                 Type           Description
                      NewVal         New value of the signal to be
                                     assigned   
                      OldVal         Previous value of the signal.
                                     Default value is 'X'
                      Delay          The delay structure from which to
                                     select the appropriate delay.  The
                                     function overload is based on the
                                     type of delay passed.  In the case of
                                     the single delay, VitalDelayType, no
                                     selection is performed, since there
                                     is only one value to choose from.
                                     For the other cases, the transition
                                     from the old value to the new value
                                     decide the value returned.  
                    
  INOUT
   none 

  OUT
   none

  Returns              
   Time                              The time value selected from the
                                     Delay INPUT is returned.

 -------------------------------------------------------------------------

- VitalCalcDelay <font id="function_arguments">( CONSTANT NewVal : IN std_ulogic   := 'X';<br><span style="padding-left:20px"> CONSTANT OldVal : IN std_ulogic   := 'X';<br><span style="padding-left:20px"> CONSTANT Delay  : IN VitalDelayType01 ) </font> <font id="function_return">RETURN TIME </font>
- VitalCalcDelay <font id="function_arguments">( CONSTANT NewVal : IN std_ulogic   := 'X';<br><span style="padding-left:20px"> CONSTANT OldVal : IN std_ulogic   := 'X';<br><span style="padding-left:20px"> CONSTANT Delay  : IN VitalDelayType01Z ) </font> <font id="function_return">RETURN TIME </font>
- VitalPathDelay <font id="function_arguments">( SIGNAL   OutSignal          : OUT   std_logic;<br><span style="padding-left:20px"> VARIABLE GlitchData         : INOUT VitalGlitchDataType;<br><span style="padding-left:20px"> CONSTANT OutSignalName      : IN    string;<br><span style="padding-left:20px"> CONSTANT OutTemp            : IN    std_logic;<br><span style="padding-left:20px"> CONSTANT Paths              : IN    VitalPathArrayType;<br><span style="padding-left:20px"> CONSTANT DefaultDelay       : IN    VitalDelayType      := VitalZeroDelay;<br><span style="padding-left:20px"> CONSTANT Mode               : IN    VitalGlitchKindType := OnEvent;<br><span style="padding-left:20px"> CONSTANT XOn                : IN    BOOLEAN             := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgOn              : IN    BOOLEAN             := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgSeverity        : IN    SEVERITY_LEVEL      := WARNING;<br><span style="padding-left:20px"> CONSTANT NegPreemptOn       : IN    BOOLEAN             := FALSE;<br><span style="padding-left:20px">  --IR225 3/14/98 CONSTANT IgnoreDefaultDelay : IN    BOOLEAN             := FALSE   --IR248 3/14/98 ) </font> <font id="function_return">return ()</font>
**Description**
 ------------------------------------------------------------------------

 Function Name:   VitalPathDelay

 Description:     VitalPathDelay is the Level 1 routine used to select
                  the propagation delay path and schedule a new output 
                  value.

                  For single and dual delay values, VitalDelayType and
                  VitalDelayType01 are used.  The output value is
                  scheduled with a calculated delay without strength
                  modification.  

                  For the six delay value, VitalDelayType01Z, the output 
                  value is scheduled with a calculated delay.  The drive 
                  strength can be modified to handle weak signal strengths
                  to model tri-state devices, pull-ups and pull-downs as
                  an example.

                  The correspondence between the delay type and the
                  path delay function is as follows:

                  Delay Type                Path Type

                  VitalDelayType            VitalPathDelay
                  VitalDelayType01          VitalPathDelay01
                  VitalDelayType01Z         VitalPathDelay01Z

                  For each of these routines, the following capabilities
                  is provided:
     
                  o Transition dependent path delay selection
                  o User controlled glitch detection with the ability
                    to generate "X" on output and report the violation
                  o Control of the severity level for message generation
                  o Scheduling of the computed values on the specified
                    signal.
                  
                  Selection of the appropriate path delay begins with the
                  candidate paths.  The candidate paths are selected by
                  identifying the paths for which the PathCondition is 
                  true.  If there is a single candidate path, then that
                  delay is selected.  If there is more than one candidate
                  path, then the shortest delay is selected using 
                  transition dependent delay selection.  If there is no 
                  candidate paths, then the delay specified by the 
                  DefaultDelay parameter to the path delay is used.
                  
                  Once the delay is known, the output signal is then
                  scheduled with that delay.  In the case of 
                  VitalPathDelay01Z, an additional result mapping of
                  the output value is performed before scheduling.  The
                  result mapping is performed after transition dependent
                  delay selection but before scheduling the final output.
                      
                  In order to perform glitch detection, the user is
                  obligated to provide a variable of VitalGlitchDataType
                  for the propagation delay functions to use.  The user
                  cannot modify or use this information.

 Arguments:         

  IN             Type                   Description
   OutSignalName  string                 The name of the output signal
   OutTemp        std_logic              The new output value to be driven
   Paths          VitalPathArrayType     A list of paths of VitalPathArray
                  VitalPathArrayType01   type.  The VitalPathDelay routine
                  VitalPathArrayType01Z  is overloaded based on the type
                                         of constant passed in.  With
                                         VitalPathArrayType01Z, the
                                         resulting output strengths can be
                                         mapped.
   DefaultDelay   VitalDelayType         The default delay can be changed 
                  VitalDelayType01       from zero-delay to another set
                  VitalDelayType01Z      of values.

   IgnoreDefaultDelay BOOLEAN            If TRUE, the default delay will
                                         be used when no paths are
                                         selected.  If false, no event
                                         will be scheduled if no paths are
                                         selected.

   Mode           VitalGlitchKindType    The value of this constant
                                         selects the type of glitch
                                         detection.
                       OnEvent           Glitch on transition event
                     | OnDetect          Glitch immediate on detection
                     | VitalInertial     No glitch, use INERTIAL
                                         assignment
                     | VitalTransport    No glitch, use TRANSPORT 
                                         assignment
   XOn            BOOLEAN                Control for generation of 'X' on 
                                         glitch.  When TRUE, 'X's are
                                         scheduled for glitches, otherwise
                                         no are generated.             
   MsgOn          BOOLEAN                Control for message generation on
                                         glitch detect.  When TRUE,
                                         glitches are reported, otherwise
                                         they are not reported.      
   MsgSeverity    SEVERITY_LEVEL         The level at which the message,
                                         or assertion, will be reported. 
   IgnoreDefaultDelay BOOLEAN            Tells the VPD whether to use the
                                         default delay value in the absense
                                         of a valid delay for input conditions 3/14/98 MG

   OutputMap      VitalOutputMapType     For VitalPathDelay01Z, the output
                                         can be mapped to alternate
                                         strengths to model tri-state 
                                         devices, pull-ups and pull-downs.  
 
  INOUT
   GlitchData     VitalGlitchDataType    The internal data storage
                                         variable required to detect
                                         glitches.

  OUT
   OutSignal      std_logic              The output signal to be driven

  Returns              
   none 

 -------------------------------------------------------------------------

- VitalPathDelay01 <font id="function_arguments">( SIGNAL   OutSignal          : OUT   std_logic;<br><span style="padding-left:20px"> VARIABLE GlitchData         : INOUT VitalGlitchDataType;<br><span style="padding-left:20px"> CONSTANT OutSignalName      : IN    string;<br><span style="padding-left:20px"> CONSTANT OutTemp            : IN    std_logic;<br><span style="padding-left:20px"> CONSTANT Paths              : IN    VitalPathArray01Type;<br><span style="padding-left:20px"> CONSTANT DefaultDelay       : IN    VitalDelayType01    := VitalZeroDelay01;<br><span style="padding-left:20px"> CONSTANT Mode               : IN    VitalGlitchKindType := OnEvent;<br><span style="padding-left:20px"> CONSTANT XOn                : IN    BOOLEAN             := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgOn              : IN    BOOLEAN             := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgSeverity        : IN    SEVERITY_LEVEL      := WARNING;<br><span style="padding-left:20px"> CONSTANT NegPreemptOn       : IN    BOOLEAN             := FALSE;<br><span style="padding-left:20px">  --IR225 3/14/98 CONSTANT IgnoreDefaultDelay : IN    BOOLEAN             := FALSE;<br><span style="padding-left:20px">  --IR248 3/14/98 CONSTANT RejectFastPath     : IN    BOOLEAN             := FALSE   --IR250 ) </font> <font id="function_return">return ()</font>
- VitalPathDelay01Z <font id="function_arguments">( SIGNAL   OutSignal          : OUT   std_logic;<br><span style="padding-left:20px"> VARIABLE GlitchData         : INOUT VitalGlitchDataType;<br><span style="padding-left:20px"> CONSTANT OutSignalName      : IN    string;<br><span style="padding-left:20px"> CONSTANT OutTemp            : IN    std_logic;<br><span style="padding-left:20px"> CONSTANT Paths              : IN    VitalPathArray01ZType;<br><span style="padding-left:20px"> CONSTANT DefaultDelay       : IN    VitalDelayType01Z   := VitalZeroDelay01Z;<br><span style="padding-left:20px"> CONSTANT Mode               : IN    VitalGlitchKindType := OnEvent;<br><span style="padding-left:20px"> CONSTANT XOn                : IN    BOOLEAN             := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgOn              : IN    BOOLEAN             := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgSeverity        : IN    SEVERITY_LEVEL      := WARNING;<br><span style="padding-left:20px"> CONSTANT OutputMap          : IN    VitalOutputMapType  := VitalDefaultOutputMap;<br><span style="padding-left:20px"> CONSTANT NegPreemptOn       : IN    BOOLEAN             := FALSE;<br><span style="padding-left:20px">  --IR225 3/14/98 CONSTANT IgnoreDefaultDelay : IN    BOOLEAN             := FALSE;<br><span style="padding-left:20px">  --IR248 3/14/98 CONSTANT RejectFastPath     : IN    BOOLEAN             := FALSE   --IR250 ) </font> <font id="function_return">return ()</font>
- VitalWireDelay <font id="function_arguments">( SIGNAL   OutSig     : OUT   std_ulogic;<br><span style="padding-left:20px"> SIGNAL   InSig      : IN    std_ulogic;<br><span style="padding-left:20px"> CONSTANT twire      : IN    VitalDelayType ) </font> <font id="function_return">return ()</font>
**Description**
 ------------------------------------------------------------------------

 Function Name:   VitalWireDelay

 Description:     VitalWireDelay is used to delay an input signal.
                  The delay is selected from the input parameter passed.
                  The function is useful for back annotation of actual
                  net delays.  
                  
                  The function is overloaded to permit passing a delay
                  value for twire for VitalDelayType, VitalDelayType01
                  and VitalDelayType01Z.  twire is a generic which can
                  be back annotated and must be constructed to follow
                  the SDF to generic mapping rules.       
                  
 Arguments:         

  IN          Type                  Description         
   InSig       std_ulogic            The input signal (port) to be
                                     delayed.
   twire       VitalDelayType        The delay value for which the input 
               VitalDelayType01      signal should be delayed.  For Vital-
               VitalDelayType01Z     DelayType, the value is single value 
                                     passed.  For VitalDelayType01 and
                                     VitalDelayType01Z, the appropriate
                                     delay value is selected by VitalCalc-
                                     Delay.

  INOUT
   none 

  OUT
   OutSig      std_ulogic            The internal delayed signal

  Returns              
   none 

 -------------------------------------------------------------------------

- VitalWireDelay <font id="function_arguments">( SIGNAL   OutSig     : OUT   std_ulogic;<br><span style="padding-left:20px"> SIGNAL   InSig      : IN    std_ulogic;<br><span style="padding-left:20px"> CONSTANT twire      : IN    VitalDelayType01 ) </font> <font id="function_return">return ()</font>
- VitalWireDelay <font id="function_arguments">( SIGNAL   OutSig     : OUT   std_ulogic;<br><span style="padding-left:20px"> SIGNAL   InSig      : IN    std_ulogic;<br><span style="padding-left:20px"> CONSTANT twire      : IN    VitalDelayType01Z ) </font> <font id="function_return">return ()</font>
- VitalSignalDelay <font id="function_arguments">( SIGNAL   OutSig     : OUT   std_ulogic;<br><span style="padding-left:20px"> SIGNAL   InSig      : IN    std_ulogic;<br><span style="padding-left:20px"> CONSTANT dly        : IN   TIME ) </font> <font id="function_return">return ()</font>
**Description**
 ------------------------------------------------------------------------

 Function Name:   VitalSignalDelay

 Description:     The VitalSignalDelay procedure is called in a signal
                  delay block in the architecture to delay the 
                  appropriate test or reference signal in order to 
                  accommodate negative constraint checks.

                  The amount of delay is of type TIME and is a constant.

 Arguments:         

  IN                Type            Description         
   InSig             std_ulogic      The signal to be delayed.
   dly               TIME            The amount of time the signal is
                                     delayed.

  INOUT
   none

  OUT
   OutSig            std_ulogic      The delayed signal

  Returns              
   none

 -------------------------------------------------------------------------

- VitalSetupHoldCheck <font id="function_arguments">( VARIABLE Violation     : OUT    X01;<br><span style="padding-left:20px"> VARIABLE TimingData    : INOUT  VitalTimingDataType;<br><span style="padding-left:20px"> SIGNAL   TestSignal    : IN     std_ulogic;<br><span style="padding-left:20px"> CONSTANT TestSignalName: IN     STRING := "";<br><span style="padding-left:20px"> CONSTANT TestDelay     : IN     TIME := 0 ns;<br><span style="padding-left:20px"> SIGNAL   RefSignal     : IN     std_ulogic;<br><span style="padding-left:20px"> CONSTANT RefSignalName : IN     STRING := "";<br><span style="padding-left:20px"> CONSTANT RefDelay      : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT SetupHigh     : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT SetupLow      : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT HoldHigh      : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT HoldLow       : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT CheckEnabled  : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT RefTransition : IN     VitalEdgeSymbolType;<br><span style="padding-left:20px"> CONSTANT HeaderMsg     : IN     STRING := " ";<br><span style="padding-left:20px"> CONSTANT XOn           : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgOn         : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgSeverity   : IN     SEVERITY_LEVEL := WARNING;<br><span style="padding-left:20px"> CONSTANT EnableSetupOnTest : IN BOOLEAN := TRUE;<br><span style="padding-left:20px">	--IR252 3/23/98 CONSTANT EnableSetupOnRef  : IN BOOLEAN := TRUE;<br><span style="padding-left:20px">	--IR252 3/23/98 CONSTANT EnableHoldOnRef   : IN BOOLEAN := TRUE;<br><span style="padding-left:20px">    --IR252 3/23/98 CONSTANT EnableHoldOnTest  : IN BOOLEAN := TRUE	    --IR252 3/23/98 ) </font> <font id="function_return">return ()</font>
**Description**
 ------------------------------------------------------------------------

 Function Name:  VitalSetupHoldCheck

 Description:    The VitalSetupHoldCheck procedure detects a setup or a 
                 hold violation on the input test signal with respect
                 to the corresponding input reference signal.  The timing 
                 constraints are specified through parameters 
                 representing the high and low values for the setup and
                 hold values for the setup and hold times.  This 
                 procedure assumes non-negative values for setup and hold 
                 timing constraints. 

                 It is assumed that negative timing constraints
                 are handled by internally delaying the test or
                 reference signals.  Negative setup times result in
                 a delayed reference signal.  Negative hold times
                 result in a delayed test signal.  Furthermore, the
                 delays and constraints associated with these and
                 other signals may need to be appropriately
                 adjusted so that all constraint intervals overlap
                 the delayed reference signals and all constraint
                 values (with respect to the delayed signals) are
                 non-negative.

                 This function is overloaded based on the input
                 TestSignal.  A vector and scalar form are provided.
                  
 TestSignal XXXXXXXXXXXX____________________________XXXXXXXXXXXXXXXXXXXXXX
            :
            :        -->|       error region       |<--
            :
            _______________________________
 RefSignal                                 \______________________________
            :           |                  |       |
            :           |               -->|       |<-- thold
            :        -->|     tsetup       |<--

 Arguments:         

  IN                 Type           Description    
   TestSignal         std_ulogic     Value of test signal
                      std_logic_vector
   TestSignalName     STRING         Name of test signal
   TestDelay          TIME           Model's internal delay associated
                                     with TestSignal
   RefSignal          std_ulogic     Value of reference signal
   RefSignalName      STRING         Name of reference signal
   RefDelay           TIME           Model's internal delay associated
                                     with RefSignal
   SetupHigh          TIME           Absolute minimum time duration before
                                     the transition of RefSignal for which
                                     transitions of TestSignal are allowed
                                     to proceed to the "1" state without
                                     causing a setup violation.      
   SetupLow           TIME           Absolute minimum time duration before 
                                     the transition of RefSignal for which
                                     transitions of TestSignal are allowed
                                     to proceed to the "0" state without
                                     causing a setup violation.      
   HoldHigh           TIME           Absolute minimum time duration after
                                     the transition of RefSignal for which
                                     transitions of TestSignal are allowed
                                     to proceed to the "1" state without
                                     causing a hold violation.      
   HoldLow            TIME           Absolute minimum time duration after 
                                     the transition of RefSignal for which
                                     transitions of TestSignal are allowed
                                     to proceed to the "0" state without
                                     causing a hold violation.      
   CheckEnabled       BOOLEAN        Check performed if TRUE.
   RefTransition      VitalEdgeSymbolType
                                     Reference edge specified. Events on
                                     the RefSignal which match the edge
                                     spec. are used as reference edges.      
   HeaderMsg          STRING         String that will accompany any
                                     assertion messages produced.
   XOn                BOOLEAN         If TRUE, Violation output parameter
                                     is set to "X". Otherwise, Violation
                                     is always set to "0".
   MsgOn              BOOLEAN        If TRUE, set and hold violation 
                                     message will be generated.
                                     Otherwise, no messages are generated,
                                     even upon violations.
   MsgSeverity        SEVERITY_LEVEL Severity level for the assertion.      
   EnableSetupOnTest  BOOLEAN        If FALSE at the time that the 
                                     TestSignal signal changes, 
                                     no setup check will be performed.
   EnableSetupOnRef   BOOLEAN        If FALSE at the time that the 
                                     RefSignal signal changes, 
                                     no setup check will be performed.
   EnableHoldOnRef    BOOLEAN        If FALSE at the time that the 
                                     RefSignal signal changes, 
                                     no hold check will be performed.
   EnableHoldOnTest   BOOLEAN        If FALSE at the time that the 
                                     TestSignal signal changes, 
                                     no hold check will be performed.
              
  INOUT
   TimingData         VitalTimingDataType  
                                     VitalSetupHoldCheck information
                                     storage area.  This is used
                                     internally to detect reference edges
                                     and record the time of the last edge.

  OUT
   Violation   X01                   This is the violation flag returned. 

  Returns              
   none    

 -------------------------------------------------------------------------

- VitalSetupHoldCheck <font id="function_arguments">( VARIABLE Violation     : OUT    X01;<br><span style="padding-left:20px"> VARIABLE TimingData    : INOUT  VitalTimingDataType;<br><span style="padding-left:20px"> SIGNAL   TestSignal    : IN     std_logic_vector;<br><span style="padding-left:20px"> CONSTANT TestSignalName: IN     STRING := "";<br><span style="padding-left:20px"> CONSTANT TestDelay     : IN     TIME := 0 ns;<br><span style="padding-left:20px"> SIGNAL   RefSignal     : IN     std_ulogic;<br><span style="padding-left:20px"> CONSTANT RefSignalName : IN     STRING := "";<br><span style="padding-left:20px"> CONSTANT RefDelay      : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT SetupHigh     : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT SetupLow      : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT HoldHigh      : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT HoldLow       : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT CheckEnabled  : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT RefTransition : IN     VitalEdgeSymbolType;<br><span style="padding-left:20px"> CONSTANT HeaderMsg     : IN     STRING := " ";<br><span style="padding-left:20px"> CONSTANT XOn           : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgOn         : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgSeverity   : IN     SEVERITY_LEVEL := WARNING;<br><span style="padding-left:20px"> CONSTANT EnableSetupOnTest : IN BOOLEAN := TRUE;<br><span style="padding-left:20px">	--IR252 3/23/98 CONSTANT EnableSetupOnRef  : IN BOOLEAN := TRUE;<br><span style="padding-left:20px">	--IR252 3/23/98 CONSTANT EnableHoldOnRef   : IN BOOLEAN := TRUE;<br><span style="padding-left:20px">    --IR252 3/23/98 CONSTANT EnableHoldOnTest  : IN BOOLEAN := TRUE	    --IR252 3/23/98 ) </font> <font id="function_return">return ()</font>
- VitalRecoveryRemovalCheck <font id="function_arguments">( VARIABLE Violation     : OUT    X01;<br><span style="padding-left:20px"> VARIABLE TimingData    : INOUT  VitalTimingDataType;<br><span style="padding-left:20px"> SIGNAL   TestSignal    : IN     std_ulogic;<br><span style="padding-left:20px"> CONSTANT TestSignalName: IN     STRING := "";<br><span style="padding-left:20px"> CONSTANT TestDelay     : IN     TIME := 0 ns;<br><span style="padding-left:20px"> SIGNAL   RefSignal     : IN     std_ulogic;<br><span style="padding-left:20px"> CONSTANT RefSignalName : IN     STRING := "";<br><span style="padding-left:20px"> CONSTANT RefDelay      : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT Recovery      : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT Removal       : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT ActiveLow     : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT CheckEnabled  : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT RefTransition : IN     VitalEdgeSymbolType;<br><span style="padding-left:20px"> CONSTANT HeaderMsg     : IN     STRING := " ";<br><span style="padding-left:20px"> CONSTANT XOn           : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgOn         : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgSeverity   : IN     SEVERITY_LEVEL := WARNING;<br><span style="padding-left:20px"> CONSTANT EnableRecOnTest : IN   BOOLEAN := TRUE;<br><span style="padding-left:20px">	--IR252 3/23/98 CONSTANT EnableRecOnRef  : IN   BOOLEAN := TRUE;<br><span style="padding-left:20px">	--IR252 3/23/98 CONSTANT EnableRemOnRef  : IN   BOOLEAN := TRUE;<br><span style="padding-left:20px">	--IR252 3/23/98 CONSTANT EnableRemOnTest : IN   BOOLEAN := TRUE		--IR252 3/23/98 ) </font> <font id="function_return">return ()</font>
**Description**
 ------------------------------------------------------------------------

 Function Name:   VitalRecoveryRemovalCheck

 Description:     The VitalRecoveryRemovalCheck detects the presence of
                  a recovery or removal violation on the input test 
                  signal with respect to the corresponding input reference
                  signal.  It assumes non-negative values of setup and
                  hold timing constraints.  The timing constraint is 
                  specified through parameters representing the recovery
                  and removal times associated with a reference edge of 
                  the reference signal.  A flag indicates whether a test
                  signal is asserted when it is high or when it is low.
                  
                  It is assumed that negative timing constraints 
                  are handled by internally delaying the test or 
                  reference signals.  Negative recovery times result in 
                  a delayed reference signal.  Negative removal times 
                  result in a delayed test signal.  Furthermore, the 
                  delays and constraints associated with these and
                  other signals may need to be appropriately
                  adjusted so that all constraint intervals overlap 
                  the delayed reference signals and all constraint
                  values (with respect to the delayed signals) are
                  non-negative.
                  
 Arguments:         

  IN               Type             Description
   TestSignal       std_ulogic       Value of TestSignal.  The routine is
   TestSignalName   STRING           Name of TestSignal 
   TestDelay        TIME             Model internal delay associated with
                                     the TestSignal
   RefSignal        std_ulogic       Value of RefSignal
   RefSignalName    STRING           Name of RefSignal
   RefDelay         TIME             Model internal delay associated with
                                     the RefSignal
   Recovery         TIME             A change to an unasserted value on
                                     the asynchronous TestSignal must
                                     precede reference edge (on RefSignal)
                                     by at least this time.
   Removal          TIME             An asserted condition must be present
                                     on the asynchronous TestSignal for at
                                     least the removal time following a
                                     reference edge on RefSignal.
   ActiveLow        BOOLEAN          A flag which indicates if TestSignal
                                     is asserted when it is low - "0."
                                     FALSE indicate that TestSignal is
                                     asserted when it has a value "1."
   CheckEnabled     BOOLEAN          The check in enabled when the value
                                     is TRUE, otherwise the constraints 
                                     are not checked.
   RefTransition    VitalEdgeSymbolType  
                                     Reference edge specifier.  Events on
                                     RefSignal will match the edge
                                     specified.
   HeaderMsg         STRING          A header message that will accompany
                                     any assertion message.
   XOn               BOOLEAN         When TRUE, the output Violation is
                                     set to "X."  When FALSE, it is always 
                                     "0."
   MsgOn             BOOLEAN         When TRUE, violation messages are
                                     output.  When FALSE, no messages are
                                     generated.
   MsgSeverity       SEVERITY_LEVEL  Severity level of the asserted
                                     message.
   EnableRecOnTest   BOOLEAN         If FALSE at the time that the 
                                     TestSignal signal changes, 
                                     no recovery check will be performed.
   EnableRecOnRef    BOOLEAN         If FALSE at the time that the 
                                     RefSignal signal changes, 
                                     no recovery check will be performed.
   EnableRemOnRef    BOOLEAN         If FALSE at the time that the 
                                     RefSignal signal changes, 
                                     no removal check will be performed.
   EnableRemOnTest   BOOLEAN         If FALSE at the time that the 
                                     TestSignal signal changes, 
                                     no removal check will be performed.
                             
   INOUT
    TimingData       VitalTimingDataType 
                                     VitalRecoveryRemovalCheck information
                                     storage area.  This is used
                                     internally to detect reference edges
                                     and record the time of the last edge.
   OUT
    Violation        X01             This is the violation flag returned.

   Returns              
           none

 -------------------------------------------------------------------------

- VitalPeriodPulseCheck <font id="function_arguments">( VARIABLE Violation      : OUT    X01;<br><span style="padding-left:20px"> VARIABLE PeriodData     : INOUT  VitalPeriodDataType;<br><span style="padding-left:20px"> SIGNAL   TestSignal     : IN     std_ulogic;<br><span style="padding-left:20px"> CONSTANT TestSignalName : IN     STRING := "";<br><span style="padding-left:20px"> CONSTANT TestDelay      : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT Period         : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT PulseWidthHigh : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT PulseWidthLow  : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT CheckEnabled   : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT HeaderMsg      : IN     STRING := " ";<br><span style="padding-left:20px"> CONSTANT XOn           : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgOn         : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgSeverity   : IN     SEVERITY_LEVEL := WARNING ) </font> <font id="function_return">return ()</font>
**Description**
 ------------------------------------------------------------------------

 Function Name:  VitalPeriodPulseCheck

 Description:    VitalPeriodPulseCheck checks for minimum
                 periodicity and pulse width for "1" and "0" values of
                 the input test signal.  The timing constraint is 
                 specified through parameters representing the minimal
                 period between successive rising and falling edges of
                 the input test signal and the minimum pulse widths 
                 associated with high and low values.  
                 
                 VitalPeriodCheck's accepts rising and falling edges
                 from 1 and 0 as well as transitions to and from 'X.'
                 
                    _______________         __________
       ____________|               |_______|

                   |<--- pw_hi --->|
                   |<-------- period ----->|
                                -->| pw_lo |<--
                 
 Arguments:
  IN                 Type           Description
    TestSignal        std_ulogic     Value of test signal  
    TestSignalName    STRING         Name of the test signal
    TestDelay         TIME           Model's internal delay associated
                                     with TestSignal
    Period            TIME           Minimum period allowed between
                                     consecutive rising ('P') or 
                                     falling ('F') transitions.
    PulseWidthHigh    TIME           Minimum time allowed for a high
                                     pulse ('1' or 'H')
    PulseWidthLow     TIME           Minimum time allowed for a low
                                     pulse ('0' or 'L')
    CheckEnabled      BOOLEAN        Check performed if TRUE.
    HeaderMsg         STRING         String that will accompany any
                                     assertion messages produced.   
    XOn               BOOLEAN        If TRUE, Violation output parameter
                                     is set to "X". Otherwise, Violation
                                     is always set to "0".
                                     XOnChecks is a global that allows for
                                     only timing checks to be turned on. 
    MsgOn             BOOLEAN        If TRUE, period/pulse violation
                                     message will be generated.
                                     Otherwise, no messages are generated,
                                     even though a violation is detected.
                                     MsgOnChecks allows for only timing
                                     check messages to be turned on. 
    MsgSeverity       SEVERITY_LEVEL Severity level for the assertion.
         
   INOUT
    PeriodData        VitalPeriodDataType 
                                     VitalPeriodPulseCheck information
                                     storage area.  This is used
                                     internally to detect reference edges
                                     and record the pulse and period
                                     times.
   OUT
    Violation         X01            This is the violation flag returned. 

   Returns              
    none

 ------------------------------------------------------------------------

- VitalInPhaseSkewCheck <font id="function_arguments">( VARIABLE Violation         : OUT    X01;<br><span style="padding-left:20px"> VARIABLE SkewData          : INOUT  VitalSkewDataType;<br><span style="padding-left:20px"> SIGNAL   Signal1           : IN     std_ulogic;<br><span style="padding-left:20px"> CONSTANT Signal1Name       : IN     STRING := "";<br><span style="padding-left:20px"> CONSTANT Signal1Delay      : IN     TIME := 0 ns;<br><span style="padding-left:20px"> SIGNAL   Signal2           : IN     std_ulogic;<br><span style="padding-left:20px"> CONSTANT Signal2Name       : IN     STRING := "";<br><span style="padding-left:20px"> CONSTANT Signal2Delay      : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT SkewS1S2RiseRise  : IN     TIME := TIME'HIGH;<br><span style="padding-left:20px"> CONSTANT SkewS2S1RiseRise  : IN     TIME := TIME'HIGH;<br><span style="padding-left:20px"> CONSTANT SkewS1S2FallFall  : IN     TIME := TIME'HIGH;<br><span style="padding-left:20px"> CONSTANT SkewS2S1FallFall  : IN     TIME := TIME'HIGH;<br><span style="padding-left:20px"> CONSTANT CheckEnabled      : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT XOn               : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgOn             : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgSeverity       : IN     SEVERITY_LEVEL := WARNING;<br><span style="padding-left:20px"> CONSTANT HeaderMsg         : IN     STRING  := "";<br><span style="padding-left:20px"> SIGNAL   Trigger           : INOUT  std_ulogic ) </font> <font id="function_return">return ()</font>
**Description**
 ------------------------------------------------------------------------

 Function Name:  VitalInPhaseSkewCheck

 Description:    The VitalInPhaseSkewCheck procedure detects an in-phase
                 skew violation between input signals Signal1 and Signal2.
                 This is a timer based skew check in which a
                 violation is detected if Signal1 and Signal2 are in
                 different logic states longer than the specified skew 
                 interval.

                 The timing constraints are specified through parameters
                 representing the skew values for the different states
                 of Signal1 and Signal2.


 Signal2    XXXXXXXXXXXX___________________________XXXXXXXXXXXXXXXXXXXXXX
            :
            :        -->|                         |<--
            :      Signal2 should go low in this region
            :

            ____________
 Signal1                \_________________________________________________
            :           |                         |
            :           |<-------- tskew -------->|

 Arguments:

  IN                 Type           Description
   Signal1            std_ulogic     Value of first signal
   Signal1Name        STRING         Name of first signal
   Signal1Delay       TIME           Model's internal delay associated
                                     with Signal1
   Signal2            std_ulogic     Value of second signal
   Signal2Name        STRING         Name of second signal
   Signal2Delay       TIME           Model's internal delay associated
                                     with Signal2
   SkewS1S2RiseRise   TIME           Absolute maximum time duration for
                                     which Signal2 can remain at "0"
                                     after Signal1 goes to the "1" state,
                                     without causing a skew violation.
   SkewS2S1RiseRise   TIME           Absolute maximum time duration for
                                     which Signal1 can remain at "0"
                                     after Signal2 goes to the "1" state,
                                     without causing a skew violation.
   SkewS1S2FallFall   TIME           Absolute maximum time duration for
                                     which Signal2 can remain at "1"
                                     after Signal1 goes to the "0" state,
                                     without causing a skew violation.
   SkewS2S1FallFall   TIME           Absolute maximum time duration for
                                     which Signal1 can remain at "1"
                                     after Signal2 goes to the "0" state,
                                     without causing a skew violation.
   CheckEnabled       BOOLEAN        Check performed if TRUE.
   HeaderMsg          STRING         String that will accompany any
                                     assertion messages produced.
   XOn                BOOLEAN        If TRUE, Violation output parameter
                                     is set to "X". Otherwise, Violation
                                     is always set to "0."      
   MsgOn              BOOLEAN        If TRUE, skew timing violation 
                                     messages will be generated.
                                     Otherwise, no messages are generated,
                                     even upon violations.      
   MsgSeverity        SEVERITY_LEVEL Severity level for the assertion.

  INOUT
   SkewData           VitalSkewDataType
                                     VitalInPhaseSkewCheck information
                                     storage area.  This is used
                                     internally to detect signal edges
                                     and record the time of the last edge.
 

   Trigger            std_ulogic     This signal is used to trigger the
                                     process in which the timing check
                                     occurs upon expiry of the skew
                                     interval.

  OUT
   Violation   X01                   This is the violation flag returned.

  Returns
   none

 -------------------------------------------------------------------------

- VitalOutPhaseSkewCheck <font id="function_arguments">( VARIABLE Violation         : OUT    X01;<br><span style="padding-left:20px"> VARIABLE SkewData          : INOUT  VitalSkewDataType;<br><span style="padding-left:20px"> SIGNAL   Signal1           : IN     std_ulogic;<br><span style="padding-left:20px"> CONSTANT Signal1Name       : IN     STRING := "";<br><span style="padding-left:20px"> CONSTANT Signal1Delay      : IN     TIME := 0 ns;<br><span style="padding-left:20px"> SIGNAL   Signal2           : IN     std_ulogic;<br><span style="padding-left:20px"> CONSTANT Signal2Name       : IN     STRING := "";<br><span style="padding-left:20px"> CONSTANT Signal2Delay      : IN     TIME := 0 ns;<br><span style="padding-left:20px"> CONSTANT SkewS1S2RiseFall  : IN     TIME := TIME'HIGH;<br><span style="padding-left:20px"> CONSTANT SkewS2S1RiseFall  : IN     TIME := TIME'HIGH;<br><span style="padding-left:20px"> CONSTANT SkewS1S2FallRise  : IN     TIME := TIME'HIGH;<br><span style="padding-left:20px"> CONSTANT SkewS2S1FallRise  : IN     TIME := TIME'HIGH;<br><span style="padding-left:20px"> CONSTANT CheckEnabled      : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT XOn               : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgOn             : IN     BOOLEAN := TRUE;<br><span style="padding-left:20px"> CONSTANT MsgSeverity       : IN     SEVERITY_LEVEL := WARNING;<br><span style="padding-left:20px"> CONSTANT HeaderMsg         : IN     STRING  := "";<br><span style="padding-left:20px"> SIGNAL   Trigger           : INOUT  std_ulogic ) </font> <font id="function_return">return ()</font>
**Description**
 ------------------------------------------------------------------------

 Function Name:  VitalOutPhaseSkewCheck

 Description:    The VitalOutPhaseSkewCheck procedure detects an 
                 out-of-phase skew violation between input signals Signal1
                 and Signal2. This is a timer based skew check in
                 which a violation is detected if Signal1 and Signal2 are
                 in the same logic state longer than the specified skew
                 interval.  

                 The timing constraints are specified through parameters
                 representing the skew values for the different states
                 of Signal1 and Signal2.


 Signal2    XXXXXXXXXXXX___________________________XXXXXXXXXXXXXXXXXXXXXX
            :
            :        -->|                         |<--
            :     Signal2 should go high in this region
            :

            ____________
 Signal1                \_________________________________________________  
            :           |                         |
            :           |<-------- tskew -------->|

 Arguments:

  IN                 Type           Description
   Signal1            std_ulogic     Value of first signal
   Signal1Name        STRING         Name of first signal
   Signal1Delay       TIME           Model's internal delay associated
                                     with Signal1
   Signal2            std_ulogic     Value of second signal
   Signal2Name        STRING         Name of second signal
   Signal2Delay       TIME           Model's internal delay associated
                                     with Signal2
   SkewS1S2RiseFall   TIME           Absolute maximum time duration for
                                     which Signal2 can remain at "1"
                                     after Signal1 goes to the "1" state,
                                     without causing a skew violation.
   SkewS2S1RiseFall   TIME           Absolute maximum time duration for
                                     which Signal1 can remain at "1"
                                     after Signal2 goes to the "1" state,
                                     without causing a skew violation.
   SkewS1S2FallRise   TIME           Absolute maximum time duration for
                                     which Signal2 can remain at "0"
                                     after Signal1 goes to the "0" state,
                                     without causing a skew violation.
   SkewS2S1FallRise   TIME           Absolute maximum time duration for
                                     which Signal1 can remain at "0"
                                     after Signal2 goes to the "0" state,
                                     without causing a skew violation.
   CheckEnabled       BOOLEAN        Check performed if TRUE.
   HeaderMsg          STRING         String that will accompany any
                                     assertion messages produced.
   XOn                BOOLEAN        If TRUE, Violation output parameter
                                     is set to "X". Otherwise, Violation
                                     is always set to "0."
   MsgOn              BOOLEAN        If TRUE, skew timing violation
                                     messages will be generated.
                                     Otherwise, no messages are generated,
                                     even upon violations.
   MsgSeverity        SEVERITY_LEVEL Severity level for the assertion.

  INOUT
   SkewData           VitalSkewDataType
                                     VitalInPhaseSkewCheck information
                                     storage area.  This is used
                                     internally to detect signal edges
                                     and record the time of the last edge.

   Trigger            std_ulogic     This signal is used to trigger the
                                     process in which the timing check
                                     occurs upon expiry of the skew
                                     interval.

  OUT
   Violation   X01                   This is the violation flag returned.

  Returns
   none

 ------------------------------------------------------------------------- 

