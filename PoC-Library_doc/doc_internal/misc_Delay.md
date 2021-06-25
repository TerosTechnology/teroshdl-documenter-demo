# Entity: misc_Delay
## Diagram
![Diagram](misc_Delay.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| BITS         | positive |       |             |
| TAPS         | T_NATVEC |       |             |
## Ports
| Port name | Direction | Type                                               | Description |
| --------- | --------- | -------------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                          |             |
| Reset     | in        | std_logic                                          |             |
| Enable    | in        | std_logic                                          |             |
| DataIn    | in        | std_logic_vector(BITS - 1 downto 0)                |             |
| DataOut   | out       | T_SLM(TAPS'length - 1 downto 0, BITS - 1 downto 0) |             |
## Signals
| Name        | Type                                               | Description |
| ----------- | -------------------------------------------------- | ----------- |
| Shifter_nxt | T_DELAY_VECTOR(MAX_DELAY downto 0)                 |             |
| Shifter_d   | T_DELAY_VECTOR(MAX_DELAY - 1 downto 0)             |             |
| DataOut_i   | T_SLM(TAPS'length - 1 downto 0, BITS - 1 downto 0) |             |
## Constants
| Name      | Type    | Value       | Description |
| --------- | ------- | ----------- | ----------- |
| MAX_DELAY | natural |  imax(TAPS) |             |
## Types
| Name           | Type | Description |
| -------------- | ---- | ----------- |
| T_DELAY_VECTOR |      |             |
## Processes
- unnamed: _( Clock )_

