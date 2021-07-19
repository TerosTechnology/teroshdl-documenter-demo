# Entity: wb_axi_to_dac

- **File**: wb_axi_to_dac.vhd
## Diagram

![Diagram](wb_axi_to_dac.svg "Diagram")
## Generics

| Generic name          | Type    | Value | Description |
| --------------------- | ------- | ----- | ----------- |
| id                    | natural | 1     |             |
| DATA_A_EN_ALWAYS_HIGH | boolean | false |             |
| DATA_B_EN_ALWAYS_HIGH | boolean | false |             |
| SYNCHRONIZE_CHAN      | boolean | false |             |
| DATA_SIZE             | natural | 16    |             |
| BUS_SIZE              | natural | 16    |             |
## Ports

| Port name               | Direction | Type                                   | Description      |
| ----------------------- | --------- | -------------------------------------- | ---------------- |
| reset                   | in        | std_logic                              | Syscon signals   |
| clk                     | in        | std_logic                              |                  |
| addr_i                  | in        | std_logic_vector(1 downto 0)           | Wishbone signals |
| wbs_write               | in        | std_logic                              |                  |
| wbs_writedata           | in        | std_logic_vector( BUS_SIZE-1 downto 0) |                  |
| wbs_read                | in        | std_logic                              |                  |
| wbs_readdata            | out       | std_logic_vector( BUS_SIZE-1 downto 0) |                  |
| data_a_en_always_high_o | out       | std_logic                              | conf             |
| data_b_en_always_high_o | out       | std_logic                              |                  |
| synchronize_chan_o      | out       | std_logic                              |                  |
| data_a_o                | out       | std_logic_vector(DATA_SIZE-1 downto 0) | data             |
| data_a_en_o             | out       | std_logic                              |                  |
| data_b_o                | out       | std_logic_vector(DATA_SIZE-1 downto 0) |                  |
| data_b_en_o             | out       | std_logic                              |                  |
## Signals

| Name                    | Type                                  | Description |
| ----------------------- | ------------------------------------- | ----------- |
| data_a_en_always_high_s | std_logic                             |             |
| data_b_en_always_high_s | std_logic                             |             |
| synchronize_chan_s      | std_logic                             |             |
| data_a_s                | std_logic_vector(BUS_SIZE-1 downto 0) |             |
| data_b_s                | std_logic_vector(BUS_SIZE-1 downto 0) |             |
| readdata_s              | std_logic_vector(BUS_SIZE-1 downto 0) |             |
| readdata_next_s         | std_logic_vector(BUS_SIZE-1 downto 0) |             |
## Constants

| Name       | Type             | Value | Description |
| ---------- | ---------------- | ----- | ----------- |
| REG_ID     | std_logic_vector |  "00" |             |
| REG_DATA_A | std_logic_vector |  "01" |             |
| REG_DATA_B | std_logic_vector |  "10" |             |
| REG_CONF   | std_logic_vector |  "11" |             |
## Functions
- bool_to_sl <font id="function_arguments">(b_val: boolean) </font> <font id="function_return">return std_logic </font>
## Processes
- write_bloc: ( clk )
**Description**
manage register

- read_async: ( addr_i, data_a_s, data_b_s,
						data_a_en_always_high_s, data_b_en_always_high_s,
						synchronize_chan_s )
- read_bloc: ( clk )
