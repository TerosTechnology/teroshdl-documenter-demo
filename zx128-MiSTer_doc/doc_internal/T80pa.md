# Entity: T80pa
## Diagram
![Diagram](T80pa.svg "Diagram")
## Generics
| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| Mode         | integer | 0     |             |
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| RESET_n   | in        | std_logic                      |             |
| CLK       | in        | std_logic                      |             |
| CEN_p     | in        | std_logic                      |             |
| CEN_n     | in        | std_logic                      |             |
| WAIT_n    | in        | std_logic                      |             |
| INT_n     | in        | std_logic                      |             |
| NMI_n     | in        | std_logic                      |             |
| BUSRQ_n   | in        | std_logic                      |             |
| M1_n      | out       | std_logic                      |             |
| MREQ_n    | out       | std_logic                      |             |
| IORQ_n    | out       | std_logic                      |             |
| RD_n      | out       | std_logic                      |             |
| WR_n      | out       | std_logic                      |             |
| RFSH_n    | out       | std_logic                      |             |
| HALT_n    | out       | std_logic                      |             |
| BUSAK_n   | out       | std_logic                      |             |
| OUT0      | in        | std_logic                      |             |
| A         | out       | std_logic_vector(15 downto 0)  |             |
| DI        | in        | std_logic_vector(7 downto 0)   |             |
| DO        | out       | std_logic_vector(7 downto 0)   |             |
| REG       | out       | std_logic_vector(211 downto 0) |             |
| DIRSet    | in        | std_logic                      |             |
| DIR       | in        | std_logic_vector(211 downto 0) |             |
## Signals
| Name        | Type                          | Description |
| ----------- | ----------------------------- | ----------- |
| IntCycle_n  | std_logic                     |             |
| IntCycleD_n | std_logic_vector(1 downto 0)  |             |
| IORQ        | std_logic                     |             |
| NoRead      | std_logic                     |             |
| Write       | std_logic                     |             |
| BUSAK       | std_logic                     |             |
| DI_Reg      | std_logic_vector (7 downto 0) |             |
| MCycle      | std_logic_vector(2 downto 0)  |             |
| TState      | std_logic_vector(2 downto 0)  |             |
| CEN_pol     | std_logic                     |             |
| CEN         | std_logic                     |             |
## Processes
- unnamed: _( CLK )_

## Instantiations
- u0: T80
