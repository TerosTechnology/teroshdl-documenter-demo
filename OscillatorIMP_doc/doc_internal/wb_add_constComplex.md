# Entity: wb_add_constComplex

## Diagram

![Diagram](wb_add_constComplex.svg "Diagram")
## Generics

| Generic name   | Type    | Value    | Description                 |
| -------------- | ------- | -------- | --------------------------- |
| DEFAULT_OFFSET | natural | 0        |                             |
| FORMAT         | string  | "signed" |                             |
| DATA_SIZE      | natural | 16       |                             |
| id             | natural | 1        |                             |
| wb_size        | natural | 16       | Data port size for wishbone |
## Ports

| Port name     | Direction | Type                                   | Description      |
| ------------- | --------- | -------------------------------------- | ---------------- |
| reset         | in        | std_logic                              | Syscon signals   |
| clk           | in        | std_logic                              |                  |
| wbs_add       | in        | std_logic_vector(1 downto 0)           | Wishbone signals |
| wbs_write     | in        | std_logic                              |                  |
| wbs_writedata | in        | std_logic_vector(wb_size-1 downto 0)   |                  |
| wbs_read      | in        | std_logic                              |                  |
| wbs_readdata  | out       | std_logic_vector(wb_size-1 downto 0)   |                  |
| offset_o      | out       | std_logic_vector(DATA_SIZE-1 downto 0) |                  |
## Signals

| Name       | Type                                     | Description |
| ---------- | ---------------------------------------- | ----------- |
| offset_l_s | std_logic_vector(wb_size-1 downto 0)     |             |
| offset_s   | std_logic_vector((2*wb_size)-1 downto 0) |             |
| readdata_s | std_logic_vector(wb_size-1 downto 0)     |             |
| off_read_s | std_logic_vector(wb_size-1 downto 0)     |             |
## Constants

| Name         | Type             | Value | Description |
| ------------ | ---------------- | ----- | ----------- |
| REG_ID       | std_logic_vector |  "00" |             |
| REG_OFFSET_L | std_logic_vector |  "01" |             |
| REG_OFFSET_H | std_logic_vector |  "10" |             |
## Processes
- write_bloc: ( clk, reset )
**Description**
manage register

- read_bloc: ( clk, reset )
