# Entity: arith_convert_bin2bcd
## Diagram
![Diagram](arith_convert_bin2bcd.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| BITS         | positive | 8     |             |
| DIGITS       | positive | 3     |             |
| RADIX        | positive | 2     |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| Clock     | in        | std_logic                           |             |
| Reset     | in        | std_logic                           |             |
| Start     | in        | std_logic                           |             |
| Busy      | out       | std_logic                           |             |
| Binary    | in        | std_logic_vector(BITS - 1 downto 0) |             |
| IsSigned  | in        | std_logic                           |             |
| BCDDigits | out       | T_BCD_VECTOR(DIGITS - 1 downto 0)   |             |
| Sign      | out       | std_logic                           |             |
## Signals
| Name            | Type                                       | Description |
| --------------- | ------------------------------------------ | ----------- |
| Digit_Shift_rst | std_logic                                  |             |
| Digit_Shift_en  | std_logic                                  |             |
| Digit_Shift_in  | T_CARRY_VECTOR(DIGITS downto 0)            |             |
| Binary_en       | std_logic                                  |             |
| Binary_rl       | std_logic                                  |             |
| Binary_d        | std_logic_vector(BINARY_BITS - 1 downto 0) |             |
| Sign_d          | std_logic                                  |             |
| DelayShifter    | std_logic_vector(BINARY_SHIFTS downto 0)   |             |
## Constants
| Name          | Type     | Value                       | Description |
| ------------- | -------- | --------------------------- | ----------- |
| RADIX_BITS    | positive |  log2ceil(RADIX)            |             |
| BINARY_SHIFTS | positive |  div_ceil(BITS, RADIX_BITS) |             |
| BINARY_BITS   | positive |  BINARY_SHIFTS * RADIX_BITS |             |
## Types
| Name           | Type | Description |
| -------------- | ---- | ----------- |
| T_CARRY_VECTOR |      |             |
## Functions
- nextBCD <font id="function_arguments">(Value : unsigned(4 downto 0))</font> <font id="function_return">return unsigned</font>
## Processes
- unnamed: _( Clock )_

