# Entity: firComplex_axi

## Diagram

![Diagram](firComplex_axi.svg "Diagram")
## Generics

| Generic name       | Type    | Value    | Description              |
| ------------------ | ------- | -------- | ------------------------ |
| ID                 | natural | 1        |                          |
| coeff_format       | string  | "signed" |                          |
| COEFF_SIZE         | natural | 16       |                          |
| COEFF_ADDR_SZ      | natural | 10       |                          |
| C_S_AXI_DATA_WIDTH | integer | 32       | Width of S_AXI data bus  |
## Ports

| Port name    | Direction | Type                                            | Description |
| ------------ | --------- | ----------------------------------------------- | ----------- |
| S_AXI_ACLK   | in        | std_logic                                       |             |
| reset        | in        | std_logic                                       |             |
| addr_i       | in        | std_logic_vector(1 downto 0)                    |             |
| write_en_i   | in        | std_logic                                       |             |
| writedata    | in        | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0) |             |
| read_en_i    | in        | std_logic                                       |             |
| read_ack_o   | out       | std_logic                                       |             |
| readdata     | out       | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0) |             |
| coeff_en_o   | out       | std_logic                                       | end of test |
| coeff_val_o  | out       | std_logic_vector(COEFF_SIZE-1 downto 0)         |             |
| coeff_read_i | in        | std_logic_vector(COEFF_SIZE-1 downto 0)         |             |
| coeff_addr_o | out       | std_logic_vector(COEFF_ADDR_SZ-1 downto 0)      |             |
## Signals

| Name             | Type                                            | Description |
| ---------------- | ----------------------------------------------- | ----------- |
| readdata_s       | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0) |             |
| coeff_en_s       | std_logic                                       |             |
| coeff_val_s      | std_logic_vector(COEFF_SIZE-1 downto 0)         |             |
| coeff_addr_s     | std_logic_vector(COEFF_ADDR_SZ-1 downto 0)      |             |
| coeff_addr_uns_s | natural range 0 to 2**COEFF_ADDR_SZ-1           |             |
| rd_coeff_res_s   | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0) |             |
## Constants

| Name          | Type                         | Value | Description |
| ------------- | ---------------------------- | ----- | ----------- |
| REG_ID        | std_logic_vector(1 downto 0) |  "00" |             |
| REG_FIR_COEFF | std_logic_vector(1 downto 0) |  "01" |             |
## Processes
- write_process: ( S_AXI_ACLK )
- read_process: ( S_AXI_ACLK )
