# Entity: remote_terminal_control
## Diagram
![Diagram](remote_terminal_control.svg "Diagram")
## Generics
| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| RESET_COUNT   | natural |       |             |
| PULSE_COUNT   | natural |       |             |
| SWITCH_COUNT  | natural |       |             |
| LIGHT_COUNT   | natural |       |             |
| DIGIT_COUNT   | natural |       |             |
| COUNT_DECIMAL | boolean | true  |             |
## Ports
| Port name | Direction | Type                                                | Description |
| --------- | --------- | --------------------------------------------------- | ----------- |
| clk       | in        | std_logic                                           |             |
| rst       | in        | std_logic                                           |             |
| idat      | in        | std_logic_vector(6 downto 0)                        |             |
| istb      | in        | std_logic                                           |             |
| odat      | out       | std_logic_vector(6 downto 0)                        |             |
| ordy      | in        | std_logic                                           |             |
| oput      | out       | std_logic                                           |             |
| resets    | out       | std_logic_vector(imax(RESET_COUNT -1, 0) downto 0)  |             |
| pulses    | out       | std_logic_vector(imax(PULSE_COUNT -1, 0) downto 0)  |             |
| switches  | out       | std_logic_vector(imax(SWITCH_COUNT-1, 0) downto 0)  |             |
| lights    | in        | std_logic_vector(imax(  LIGHT_COUNT-1, 0) downto 0) |             |
| digits    | in        | std_logic_vector(imax(4*DIGIT_COUNT-1, 0) downto 0) |             |
## Signals
| Name   | Type                              | Description |
| ------ | --------------------------------- | ----------- |
| BufVld | std_logic                         |             |
| BufCmd | std_logic_vector(4 downto 0)      |             |
| BufCnt | unsigned(CNT_BITS-1 downto 0)     |             |
| BufEco | std_logic_vector(0 to ECO_BITS-1) |             |
| BufAck | std_logic                         |             |
## Constants
| Name       | Type                     | Value                                                                                                                                        | Description |
| ---------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| COUNTS     | tCounts                  |  (0,                                  RESET_COUNT,   PULSE_COUNT, SWITCH_COUNT,                                  LIGHT_COUNT, 4*DIGIT_COUNT) |             |
| PAR_BITS   | natural                  |  max_count(COUNTS(tInput))                                                                                                                   |             |
| RES_BITS   | natural                  |  max_count(COUNTS(tActual))                                                                                                                  |             |
| ECO_BITS   | natural                  |  4*((RES_BITS+3)/4)                                                                                                                          |             |
| CNT_BITS   | positive                 |  makeCntBits                                                                                                                                 |             |
| OUT_COUNTS | tOutCounts(COUNTS'range) |  makeOutCounts                                                                                                                               |             |
| CODES      | tCodes(tActual)          |  ("10010", "10000", "10011", "01100", "00100")                                                                                               |             |
| STROBES    | tStrobes(tInput)         |  (true, true, false)                                                                                                                         |             |
## Types
| Name       | Type                                                                                                             | Description |
| ---------- | ---------------------------------------------------------------------------------------------------------------- | ----------- |
| tKind      | (KIND_NONE,                     KIND_RESET, KIND_PULSE, KIND_SWITCH,                     KIND_LIGHT, KIND_DIGIT) |             |
| tCounts    |                                                                                                                  |             |
| tOutCounts |                                                                                                                  |             |
| tCodes     |                                                                                                                  |             |
| tStrobes   |                                                                                                                  |             |
## Functions
- max_count <font id="function_arguments">(arr : tCounts)</font> <font id="function_return">return natural</font>
- log10ceil <font id="function_arguments">(x : natural)</font> <font id="function_return">return positive</font>
- makeCntBits <font id="function_arguments">()</font> <font id="function_return">return positive</font>
- makeOutCounts <font id="function_arguments">()</font> <font id="function_return">return tOutCounts</font>
