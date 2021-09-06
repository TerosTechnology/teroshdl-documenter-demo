# Entity: wb_cvb

- **File**: wb_cvb.vhd
## Diagram

![Diagram](wb_cvb.svg "Diagram")
## Generics

| Generic name      | Type    | Value  | Description                  |
| ----------------- | ------- | ------ | ---------------------------- |
| ACCUM_SIZE        | natural | 8      |                              |
| ADDR_SIZE         | natural | 16     |                              |
| DFLT_START_OFFSET | natural | 500    |                              |
| DFLT_STOP_OFFSET  | natural | 1024   |                              |
| DFLT_LIMIT        | natural | 100000 |                              |
| id                | natural | 1      |                              |
| wb_size           | natural | 16     |  Data port size for wishbone |
## Ports

| Port name           | Direction | Type                                    | Description      |
| ------------------- | --------- | --------------------------------------- | ---------------- |
| reset               | in        | std_logic                               | Syscon signals   |
| clk                 | in        | std_logic                               |                  |
| wbs_add             | in        | std_logic_vector(1 downto 0)            | Wishbone signals |
| wbs_write           | in        | std_logic                               |                  |
| wbs_writedata       | in        | std_logic_vector( wb_size-1 downto 0)   |                  |
| wbs_read            | in        | std_logic                               |                  |
| wbs_readdata        | out       | std_logic_vector( wb_size-1 downto 0)   |                  |
| start_mean_offset_o | out       | std_logic_vector(ADDR_SIZE-1 downto 0)  |                  |
| max_allowed_val_o   | out       | std_logic_vector(ACCUM_SIZE-1 downto 0) |                  |
| cpt_max_o           | out       | std_logic_vector(ADDR_SIZE-1 downto 0)  |                  |
## Signals

| Name                | Type                                    | Description |
| ------------------- | --------------------------------------- | ----------- |
| readdata_s          | std_logic_vector(wb_size-1 downto 0)    |             |
| start_mean_offset_s | std_logic_vector(ADDR_SIZE-1 downto 0)  |             |
| max_allowed_val_s   | std_logic_vector(ACCUM_SIZE-1 downto 0) |             |
| cpt_max_s           | std_logic_vector(ADDR_SIZE-1 downto 0)  |             |
## Constants

| Name        | Type             | Value | Description |
| ----------- | ---------------- | ----- | ----------- |
| REG_ID      | std_logic_vector |  "00" |             |
| REG_OFFSET  | std_logic_vector | "01"  |             |
| REG_VAL_MAX | std_logic_vector | "10"  |             |
| REG_CPT_MAX | std_logic_vector | "11"  |             |
## Processes
- write_bloc: ( clk, reset )
**Description**
 manage register 
- read_bloc: ( clk, reset )
