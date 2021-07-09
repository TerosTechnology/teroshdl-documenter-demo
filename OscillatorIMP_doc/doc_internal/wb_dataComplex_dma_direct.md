# Entity: wb_dataComplex_dma_direct

## Diagram

![Diagram](wb_dataComplex_dma_direct.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description                 |
| ------------ | ------- | ----- | --------------------------- |
| id           | natural | 1     |                             |
| NB_SAMPLE    | natural | 10    |                             |
| wb_size      | natural | 16    | Data port size for wishbone |
## Ports

| Port name     | Direction | Type                                 | Description      |
| ------------- | --------- | ------------------------------------ | ---------------- |
| reset         | in        | std_logic                            | Syscon signals   |
| clk           | in        | std_logic                            |                  |
| wbs_add       | in        | std_logic_vector(3 downto 0)         | Wishbone signals |
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

| Name        | Type                          | Value                                                                 | Description                                     |
| ----------- | ----------------------------- | --------------------------------------------------------------------- | ----------------------------------------------- |
| REG_ID      | std_logic_vector(3 downto 0)  |  "0000"                                                               |                                                 |
| REG_START   | std_logic_vector(3 downto 0)  |  "0001"                                                               |                                                 |
| REG_SIZE    | std_logic_vector(3 downto 0)  |  "0010"                                                               |                                                 |
| CPT_SIZE    | natural                       |  natural(ceil(log2(real(NB_SAMPLE))))                                 | byte sizex2: complex, x2: two input, x2: 16bits |
| SIZE_N      | natural                       |  CPT_SIZE+1+1+1                                                       |                                                 |
| buff_size_s | unsigned(CPT_SIZE-1 downto 0) |  to_unsigned(NB_SAMPLE,<br><span style="padding-left:20px"> CPT_SIZE) |                                                 |
| plop2       | unsigned(SIZE_N-1 downto 0)   |  buff_size_s & '0' & '0' & '0'                                        |                                                 |
## Processes
- write_bloc: ( clk )
**Description**
manage register

- read_bloc: ( clk )
