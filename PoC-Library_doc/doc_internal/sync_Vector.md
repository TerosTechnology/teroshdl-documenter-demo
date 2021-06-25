# Entity: sync_Vector
## Diagram
![Diagram](sync_Vector.svg "Diagram")
## Generics
| Generic name | Type              | Value                 | Description |
| ------------ | ----------------- | --------------------- | ----------- |
| MASTER_BITS  | positive          | 8                     |             |
| SLAVE_BITS   | natural           | 0                     |             |
| INIT         | std_logic_vector  | x"00000000"           |             |
| SYNC_DEPTH   | T_MISC_SYNC_DEPTH | T_MISC_SYNC_DEPTH'low |             |
## Ports
| Port name | Direction | Type                                                      | Description |
| --------- | --------- | --------------------------------------------------------- | ----------- |
| Clock1    | in        | std_logic                                                 |             |
| Clock2    | in        | std_logic                                                 |             |
| Input     | in        | std_logic_vector((MASTER_BITS + SLAVE_BITS) - 1 downto 0) |             |
| Output    | out       | std_logic_vector((MASTER_BITS + SLAVE_BITS) - 1 downto 0) |             |
| Busy      | out       | std_logic                                                 |             |
| Changed   | out       | std_logic                                                 |             |
## Signals
| Name         | Type                                                      | Description |
| ------------ | --------------------------------------------------------- | ----------- |
| D0           | std_logic_vector((MASTER_BITS + SLAVE_BITS) - 1 downto 0) |             |
| T1           | std_logic                                                 |             |
| D2           | std_logic                                                 |             |
| D3           | std_logic                                                 |             |
| D4           | std_logic_vector((MASTER_BITS + SLAVE_BITS) - 1 downto 0) |             |
| Changed_Clk1 | std_logic                                                 |             |
| Changed_Clk2 | std_logic                                                 |             |
| Busy_i       | std_logic                                                 |             |
| syncClk1_In  | std_logic                                                 |             |
| syncClk1_Out | std_logic                                                 |             |
| syncClk2_In  | std_logic                                                 |             |
| syncClk2_Out | std_logic                                                 |             |
## Constants
| Name   | Type             | Value                                                   | Description |
| ------ | ---------------- | ------------------------------------------------------- | ----------- |
| INIT_I | std_logic_vector |  descend(INIT)((MASTER_BITS + SLAVE_BITS) - 1 downto 0) |             |
## Processes
- unnamed: _( Clock1 )_

- unnamed: _( Clock2 )_

## Instantiations
- syncClk2: PoC.sync_Bits
- syncClk1: PoC.sync_Bits
