# Entity: delayTempoReal_axi_comm

## Diagram

![Diagram](delayTempoReal_axi_comm.svg "Diagram")
## Generics

| Generic name       | Type    | Value | Description |
| ------------------ | ------- | ----- | ----------- |
| DEFAULT_DELAY      | natural | 0     |             |
| DELAY_ADDR_SZ      | natural | 10    |             |
| AXI_ADDR_WIDTH     | integer | 1     |             |
| C_S_AXI_DATA_WIDTH | integer | 32    |             |
## Ports

| Port name  | Direction | Type                                            | Description |
| ---------- | --------- | ----------------------------------------------- | ----------- |
| clk_i      | in        | std_logic                                       |             |
| reset      | in        | std_logic                                       |             |
| addr_i     | in        | std_logic_vector(AXI_ADDR_WIDTH-1 downto 0)     |             |
| write_en_i | in        | std_logic                                       |             |
| writedata  | in        | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0) |             |
| read_en_i  | in        | std_logic                                       |             |
| read_ack_o | out       | std_logic                                       |             |
| readdata   | out       | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0) |             |
| delay_o    | out       | std_logic_vector(DELAY_ADDR_SZ-1 downto 0)      |             |
## Signals

| Name       | Type                                            | Description |
| ---------- | ----------------------------------------------- | ----------- |
| readdata_s | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0) |             |
| delay_s    | std_logic_vector(DELAY_ADDR_SZ-1 downto 0)      |             |
## Constants

| Name      | Type                         | Value | Description |
| --------- | ---------------------------- | ----- | ----------- |
| REG_DELAY | std_logic_vector(0 downto 0) |  "0"  |             |
## Processes
- write_process: ( clk_i )
- read_process: ( clk_i )
