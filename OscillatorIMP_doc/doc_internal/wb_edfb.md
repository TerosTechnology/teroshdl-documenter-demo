# Entity: wb_edfb

- **File**: wb_edfb.vhd
## Diagram

![Diagram](wb_edfb.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description                  |
| ------------ | ------- | ----- | ---------------------------- |
| id           | natural | 1     |                              |
| POINT_POS    | natural | 16    |                              |
| wb_size      | natural | 16    |  Data port size for wishbone |
## Ports

| Port name      | Direction | Type                                  | Description      |
| -------------- | --------- | ------------------------------------- | ---------------- |
| reset          | in        | std_logic                             | Syscon signals   |
| clk            | in        | std_logic                             |                  |
| wbs_add        | in        | std_logic_vector(1 downto 0)          | Wishbone signals |
| wbs_write      | in        | std_logic                             |                  |
| wbs_writedata  | in        | std_logic_vector( wb_size-1 downto 0) |                  |
| wbs_read       | in        | std_logic                             |                  |
| wbs_readdata   | out       | std_logic_vector( wb_size-1 downto 0) |                  |
| point_pos_en_o | out       | std_logic                             |                  |
| point_pos_o    | out       | std_logic_vector(15 downto 0)         |                  |
## Signals

| Name        | Type                                 | Description |
| ----------- | ------------------------------------ | ----------- |
| point_pos_s | std_logic_vector(15 downto 0)        |             |
| readdata_s  | std_logic_vector(wb_size-1 downto 0) |             |
## Constants

| Name          | Type             | Value | Description |
| ------------- | ---------------- | ----- | ----------- |
| REG_ID        | std_logic_vector |  "00" |             |
| REG_POINT_POS | std_logic_vector | "01"  |             |
## Processes
- write_bloc: ( clk, reset )
</br>**Description**
 manage register 
- read_bloc: ( clk, reset )
