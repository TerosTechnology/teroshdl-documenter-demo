# Entity: switchReal_wb

- **File**: switchReal_wb.vhd
## Diagram

![Diagram](switchReal_wb.svg "Diagram")
## Generics

| Generic name  | Type    | Value | Description                  |
| ------------- | ------- | ----- | ---------------------------- |
| id            | natural | 1     |                              |
| DEFAULT_INPUT | natural | 1     |                              |
| wb_size       | natural | 16    |  Data port size for wishbone |
## Ports

| Port name     | Direction | Type                                  | Description      |
| ------------- | --------- | ------------------------------------- | ---------------- |
| reset         | in        | std_logic                             | Syscon signals   |
| clk           | in        | std_logic                             |                  |
| wbs_add       | in        | std_logic_vector(1 downto 0)          | Wishbone signals |
| wbs_write     | in        | std_logic                             |                  |
| wbs_writedata | in        | std_logic_vector( wb_size-1 downto 0) |                  |
| wbs_read      | in        | std_logic                             |                  |
| wbs_readdata  | out       | std_logic_vector( wb_size-1 downto 0) |                  |
| witchInput_o  | out       | std_logic                             |                  |
## Signals

| Name         | Type                                 | Description |
| ------------ | ------------------------------------ | ----------- |
| witchInput_s | std_logic                            |             |
| readdata_s   | std_logic_vector(wb_size-1 downto 0) |             |
## Constants

| Name      | Type                         | Value | Description |
| --------- | ---------------------------- | ----- | ----------- |
| REG_ID    | std_logic_vector(1 downto 0) |  "00" |             |
| REG_INPUT | std_logic_vector(1 downto 0) | "01"  |             |
## Processes
- write_bloc: ( clk )
**Description**
 manage register 
- read_bloc: ( clk )
