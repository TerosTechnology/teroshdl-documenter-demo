# Entity: wb_windowReal

- **File**: wb_windowReal.vhd
## Diagram

![Diagram](wb_windowReal.svg "Diagram")
## Generics

| Generic name    | Type    | Value | Description                  |
| --------------- | ------- | ----- | ---------------------------- |
| COEFF_ADDR_SIZE | natural | 8     |                              |
| COEFF_SIZE      | natural | 16    |                              |
| id              | natural | 1     |                              |
| wb_size         | natural | 16    |  Data port size for wishbone |
## Ports

| Port name     | Direction | Type                                         | Description      |
| ------------- | --------- | -------------------------------------------- | ---------------- |
| reset         | in        | std_logic                                    | Syscon signals   |
| clk           | in        | std_logic                                    |                  |
| wbs_add       | in        | std_logic_vector(1 downto 0)                 | Wishbone signals |
| wbs_write     | in        | std_logic                                    |                  |
| wbs_writedata | in        | std_logic_vector( wb_size-1 downto 0)        |                  |
| wbs_read      | in        | std_logic                                    |                  |
| wbs_readdata  | out       | std_logic_vector( wb_size-1 downto 0)        |                  |
| coeff_en_o    | out       | std_logic                                    |                  |
| coeff_addr_o  | out       | std_logic_vector(COEFF_ADDR_SIZE-1 downto 0) |                  |
| coeff_o       | out       | std_logic_vector(COEFF_SIZE-1 downto 0)      |                  |
## Signals

| Name              | Type                                         | Description |
| ----------------- | -------------------------------------------- | ----------- |
| readdata_s        | std_logic_vector(wb_size-1 downto 0)         |             |
| coeff_en_s        | std_logic                                    |             |
| coeff_s           | std_logic_vector(COEFF_SIZE-1 downto 0)      |             |
| coeff_addr_s      | std_logic_vector(COEFF_ADDR_SIZE-1 downto 0) |             |
| coeff_next_addr_s | std_logic_vector(COEFF_ADDR_SIZE-1 downto 0) |             |
## Constants

| Name            | Type             | Value | Description |
| --------------- | ---------------- | ----- | ----------- |
| REG_ID          | std_logic_vector |  "00" |             |
| REG_COEFF       | std_logic_vector | "01"  |             |
| REG_RESET_COEFF | std_logic_vector | "10"  |             |
## Processes
- write_bloc: ( clk, reset )
**Description**
 manage register 
- read_bloc: ( clk, reset )
