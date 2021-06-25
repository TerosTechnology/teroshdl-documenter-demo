# Entity: fifo_cc_got
## Diagram
![Diagram](fifo_cc_got.svg "Diagram")
## Generics
| Generic name   | Type     | Value | Description |
| -------------- | -------- | ----- | ----------- |
| D_BITS         | positive |       |             |
| MIN_DEPTH      | positive |       |             |
| DATA_REG       | boolean  | false |             |
| STATE_REG      | boolean  | false |             |
| OUTPUT_REG     | boolean  | false |             |
| ESTATE_WR_BITS | natural  | 0     |             |
| FSTATE_RD_BITS | natural  | 0     |             |
## Ports
| Port name | Direction | Type                                                 | Description |
| --------- | --------- | ---------------------------------------------------- | ----------- |
| rst       | in        | std_logic                                            |             |
| clk       | in        | std_logic                                            |             |
| put       | in        | std_logic                                            |             |
| din       | in        | std_logic_vector(D_BITS-1 downto 0)                  |             |
| full      | out       | std_logic                                            |             |
| estate_wr | out       | std_logic_vector(imax(0, ESTATE_WR_BITS-1) downto 0) |             |
| got       | in        | std_logic                                            |             |
| dout      | out       | std_logic_vector(D_BITS-1 downto 0)                  |             |
| valid     | out       | std_logic                                            |             |
| fstate_rd | out       | std_logic_vector(imax(0, FSTATE_RD_BITS-1) downto 0) |             |
## Signals
| Name  | Type                        | Description |
| ----- | --------------------------- | ----------- |
| IP0   | unsigned(A_BITS-1 downto 0) |             |
| OP0   | unsigned(A_BITS-1 downto 0) |             |
| IP1   | unsigned(A_BITS-1 downto 0) |             |
| OP1   | unsigned(A_BITS-1 downto 0) |             |
| wa    | unsigned(A_BITS-1 downto 0) |             |
| we    | std_logic                   |             |
| ra    | unsigned(A_BITS-1 downto 0) |             |
| re    | std_logic                   |             |
| fulli | std_logic                   |             |
| empti | std_logic                   |             |
## Constants
| Name   | Type    | Value                | Description |
| ------ | ------- | -------------------- | ----------- |
| A_BITS | natural |  log2ceil(MIN_DEPTH) |             |
## Processes
- unnamed: _( clk )_

- unnamed: _( IP0, OP0, fulli )_

