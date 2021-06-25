# Entity: fifo_ic_got
## Diagram
![Diagram](fifo_ic_got.svg "Diagram")
## Generics
| Generic name   | Type     | Value | Description |
| -------------- | -------- | ----- | ----------- |
| D_BITS         | positive |       |             |
| MIN_DEPTH      | positive |       |             |
| DATA_REG       | boolean  | false |             |
| OUTPUT_REG     | boolean  | false |             |
| ESTATE_WR_BITS | natural  | 0     |             |
| FSTATE_RD_BITS | natural  | 0     |             |
## Ports
| Port name | Direction | Type                                                 | Description |
| --------- | --------- | ---------------------------------------------------- | ----------- |
| clk_wr    | in        | std_logic                                            |             |
| rst_wr    | in        | std_logic                                            |             |
| put       | in        | std_logic                                            |             |
| din       | in        | std_logic_vector(D_BITS-1 downto 0)                  |             |
| full      | out       | std_logic                                            |             |
| estate_wr | out       | std_logic_vector(imax(ESTATE_WR_BITS-1, 0) downto 0) |             |
| clk_rd    | in        | std_logic                                            |             |
| rst_rd    | in        | std_logic                                            |             |
| got       | in        | std_logic                                            |             |
| valid     | out       | std_logic                                            |             |
| dout      | out       | std_logic_vector(D_BITS-1 downto 0)                  |             |
| fstate_rd | out       | std_logic_vector(imax(FSTATE_RD_BITS-1, 0) downto 0) |             |
## Signals
| Name | Type                                | Description |
| ---- | ----------------------------------- | ----------- |
| IP1  | std_logic_vector(AN-1 downto 0)     |             |
| IP0  | std_logic_vector(AN-1 downto 0)     |             |
| IPz  | std_logic_vector(AN-1 downto 0)     |             |
| OPs  | std_logic_vector(AN-1 downto 0)     |             |
| OPc  | std_logic_vector(AN-1 downto 0)     |             |
| Ful  | std_logic                           |             |
| OP1  | std_logic_vector(AN-1 downto 0)     |             |
| OP0  | std_logic_vector(AN-1 downto 0)     |             |
| IPs  | std_logic_vector(AN-1 downto 0)     |             |
| IPc  | std_logic_vector(AN-1 downto 0)     |             |
| Avl  | std_logic                           |             |
| Vld  | std_logic                           |             |
| wa   | unsigned(A_BITS-1 downto 0)         |             |
| di   | std_logic_vector(D_BITS-1 downto 0) |             |
| puti | std_logic                           |             |
| ra   | unsigned(A_BITS-1 downto 0)         |             |
| do   | std_logic_vector(D_BITS-1 downto 0) |             |
| geti | std_logic                           |             |
| goti | std_logic                           |             |
## Constants
| Name   | Type     | Value                  | Description |
| ------ | -------- | ---------------------- | ----------- |
| A_BITS | positive |  log2ceilnz(MIN_DEPTH) |             |
| AN     | positive |  A_BITS + 1            |             |
## Processes
- unnamed: _( clk_wr )_

- unnamed: _( clk_rd )_

