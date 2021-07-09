# Entity: wb_dataReal_dma_direct

## Diagram

![Diagram](wb_dataReal_dma_direct.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description              |
| ------------ | ------- | ----- | ------------------------ |
| NB_INPUT     | natural | 1     | number of 32bits to send |
| NB_SAMPLE    | natural | 10    |                          |
| wb_size      | natural | 16    |                          |
## Ports

| Port name     | Direction | Type                                 | Description      |
| ------------- | --------- | ------------------------------------ | ---------------- |
| reset         | in        | std_logic                            | CANDR            |
| clk           | in        | std_logic                            |                  |
| wbs_add       | in        | std_logic_vector(1 downto 0)         | Wishbone signals |
| wbs_writedata | in        | std_logic_vector(wb_size-1 downto 0) |                  |
| wbs_readdata  | out       | std_logic_vector(wb_size-1 downto 0) |                  |
| wbs_read      | in        | std_logic                            |                  |
| wbs_read_ack  | out       | std_logic                            |                  |
| wbs_write     | in        | std_logic                            |                  |
| busy_i        | in        | std_logic                            |                  |
| start_o       | out       | std_logic                            |                  |
## Signals

| Name       | Type                                 | Description |
| ---------- | ------------------------------------ | ----------- |
| readdata_s | std_logic_vector(wb_size-1 downto 0) |             |
| plop       | std_logic_vector(wb_size-1 downto 0) |             |
## Constants

| Name        | Type                          | Value                                                               | Description |
| ----------- | ----------------------------- | ------------------------------------------------------------------- | ----------- |
| REG_START   | std_logic_vector(1 downto 0)  |  "01"                                                               |             |
| REG_SIZE    | std_logic_vector(1 downto 0)  |  "10"                                                               |             |
| NB_BYTE     | natural                       |  NB_SAMPLE * 4                                                      | byte size   |
| CPT_SIZE    | natural                       |  natural(ceil(log2(real(NB_BYTE))))                                 |             |
| SIZE_N      | natural                       |  CPT_SIZE                                                           |             |
| buff_size_s | unsigned(CPT_SIZE-1 downto 0) |  to_unsigned(NB_BYTE,<br><span style="padding-left:20px"> CPT_SIZE) |             |
| plop2       | unsigned(SIZE_N-1 downto 0)   |  buff_size_s                                                        |             |
## Processes
- write_bloc: ( clk )
**Description**
manage register

- read_bloc: ( clk )
