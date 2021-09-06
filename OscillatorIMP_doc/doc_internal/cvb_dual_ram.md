# Entity: cvb_dual_ram

- **File**: cvb_dual_ram.vhd
## Diagram

![Diagram](cvb_dual_ram.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DATA         | integer | 72    |             |
| ADDR         | integer | 10    |             |
## Ports

| Port name  | Direction | Type                              | Description |
| ---------- | --------- | --------------------------------- | ----------- |
| clk_i      | in        | std_logic                         |             |
| rst_i      | in        | std_logic                         |             |
| w_switch_i | in        | std_logic                         |             |
| w_en_i     | in        | std_logic                         |             |
| w_addr_i   | in        | std_logic_vector(ADDR-1 downto 0) |             |
| w_din_i    | in        | std_logic_vector(DATA-1 downto 0) |             |
| r_switch_i | in        | std_logic                         |             |
| r_addr_i   | in        | std_logic_vector(ADDR-1 downto 0) |             |
| r_dout_o   | out       | std_logic_vector(DATA-1 downto 0) |             |
## Signals

| Name       | Type                                | Description |
| ---------- | ----------------------------------- | ----------- |
| r_select_s | std_logic                           |  read       |
| r_data_s   | data_tab(NB_RAM-1 downto 0)         |             |
| w_select_s | std_logic                           |  write      |
| we_s       | std_logic_vector(NB_RAM-1 downto 0) |             |
## Constants

| Name   | Type    | Value | Description |
| ------ | ------- | ----- | ----------- |
| NB_RAM | natural |  2    |             |
## Types

| Name     | Type                                                           | Description |
| -------- | -------------------------------------------------------------- | ----------- |
| data_tab | array (natural range <>) of std_logic_vector(DATA-1 downto 0)  |             |
## Processes
- unnamed: ( clk_i )
