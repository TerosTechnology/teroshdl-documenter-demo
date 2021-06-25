# Entity: ocram_tdp_sim
## Diagram
![Diagram](ocram_tdp_sim.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| A_BITS       | positive |       |             |
| D_BITS       | positive |       |             |
| FILENAME     | string   | ""    |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| clk1      | in        | std_logic                           |             |
| clk2      | in        | std_logic                           |             |
| ce1       | in        | std_logic                           |             |
| ce2       | in        | std_logic                           |             |
| we1       | in        | std_logic                           |             |
| we2       | in        | std_logic                           |             |
| a1        | in        | unsigned(A_BITS-1 downto 0)         |             |
| a2        | in        | unsigned(A_BITS-1 downto 0)         |             |
| d1        | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| d2        | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| q1        | out       | std_logic_vector(D_BITS-1 downto 0) |             |
| q2        | out       | std_logic_vector(D_BITS-1 downto 0) |             |
## Signals
| Name   | Type  | Description |
| ------ | ----- | ----------- |
| ram    | ram_t |             |
| write1 | X01   |             |
| write2 | X01   |             |
| read1  | X01   |             |
| read2  | X01   |             |
## Constants
| Name  | Type     | Value      | Description |
| ----- | -------- | ---------- | ----------- |
| DEPTH | positive |  2**A_BITS |             |
## Types
| Name  | Type | Description |
| ----- | ---- | ----------- |
| ram_t |      |             |
## Functions
## Processes
- unnamed: _( clk1, clk2 )_

