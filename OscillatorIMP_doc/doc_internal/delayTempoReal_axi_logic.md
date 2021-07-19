# Entity: delayTempoReal_axi_logic

- **File**: delayTempoReal_axi_logic.vhd
## Diagram

![Diagram](delayTempoReal_axi_logic.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DELAY_SIZE   | natural | 3     |             |
| DATA_SIZE    | natural | 18    |             |
## Ports

| Port name  | Direction | Type                                    | Description |
| ---------- | --------- | --------------------------------------- | ----------- |
| clk_i      | in        | std_logic                               |             |
| rst_i      | in        | std_logic                               |             |
| delay_i    | in        | std_logic_vector(DELAY_SIZE-1 downto 0) | ctrl        |
| data_i     | in        | std_logic_vector(DATA_SIZE-1 downto 0)  | in          |
| data_en_i  | in        | std_logic                               |             |
| data_eof_i | in        | std_logic                               |             |
| data_o     | out       | std_logic_vector(DATA_SIZE-1 downto 0)  | out         |
| data_en_o  | out       | std_logic                               |             |
| data_eof_o | out       | std_logic                               |             |
## Signals

| Name             | Type                                   | Description   |
| ---------------- | -------------------------------------- | ------------- |
| del_eq_zero_s    | std_logic                              |               |
| data_in_s        | std_logic_vector(DATA_SIZE+1 downto 0) |               |
| data_tab_s       | data_tab(MX_NB_DEL-1 downto 0)         | delay         |
|  data_tab_next_s | data_tab(MX_NB_DEL-1 downto 0)         | delay         |
| data_del_s       | std_logic_vector(DATA_SIZE+1 downto 0) | future output |
| mux_data_s       | std_logic_vector(DATA_SIZE-1 downto 0) | mux           |
| mux_data_en_s    | std_logic                              |               |
| mux_data_eof_s   | std_logic                              |               |
## Constants

| Name      | Type                                    | Value                                  | Description |
| --------- | --------------------------------------- | -------------------------------------- | ----------- |
| MX_NB_DEL | natural                                 |  2**DELAY_SIZE                         |             |
| EQ_ZERO   | std_logic_vector(DELAY_SIZE-1 downto 0) |  							(DELAY_SIZE-1 downto 0 => '0') |             |
## Types

| Name     | Type                                                                | Description |
| -------- | ------------------------------------------------------------------- | ----------- |
| data_tab | array (natural range <>) of std_logic_vector(DATA_SIZE+1 downto 0)  |             |
## Processes
- unnamed: ( clk_i )
