# Entity: redpitaya_converters_12_comm

- **File**: redpitaya_converters_12_comm.vhd
## Diagram

![Diagram](redpitaya_converters_12_comm.svg "Diagram")
## Generics

| Generic name        | Type    | Value | Description |
| ------------------- | ------- | ----- | ----------- |
| id                  | natural | 1     |             |
| CONF_SIZE           | integer | 14    |             |
| BUS_SIZE            | natural | 32    |             |
| INTERNAL_ADDR_WIDTH | integer | 3     |             |
## Ports

| Port name    | Direction | Type                                   | Description    |
| ------------ | --------- | -------------------------------------- | -------------- |
| reset        | in        | std_logic                              | Syscon signals |
| clk          | in        | std_logic                              |                |
| addr_i       | in        | std_logic_vector(2 downto 0)           | axi signals    |
| write_en_i   | in        | std_logic                              |                |
| writedata    | in        | std_logic_vector(BUS_SIZE-1 downto 0)  |                |
| read_en_i    | in        | std_logic                              |                |
| readdata     | out       | std_logic_vector(BUS_SIZE-1 downto 0)  |                |
| conf_o       | out       | std_logic_vector(CONF_SIZE-1 downto 0) | out signals    |
| conf_sel_o   | out       | std_logic                              |                |
| conf_en_o    | out       | std_logic                              |                |
| pll_cfg_en_o | out       | std_logic                              |                |
| pll_ok_i     | in        | std_logic                              | in signal      |
## Signals

| Name         | Type                                   | Description |
| ------------ | -------------------------------------- | ----------- |
| conf_s       | std_logic_vector(CONF_SIZE-1 downto 0) |             |
| conf_sel_s   | std_logic                              |             |
| conf_en_s    | std_logic                              |             |
| pll_cfg_en_s | std_logic                              |             |
| pll_ok_s     | std_logic                              |             |
| readdata_s   | std_logic_vector(BUS_SIZE-1 downto 0)  |             |
## Constants

| Name            | Type                         | Value  | Description |
| --------------- | ---------------------------- | ------ | ----------- |
| REG_CONF        | std_logic_vector(2 downto 0) |  "000" |             |
| REG_ADC_DAC_SEL | std_logic_vector(2 downto 0) |  "001" |             |
| REG_CONF_EN     | std_logic_vector(2 downto 0) |  "010" |             |
| REG_PLL_EN      | std_logic_vector(2 downto 0) |  "011" |             |
| REG_PLL_OK      | std_logic_vector(2 downto 0) |  "100" |             |
## Processes
- write_bloc: ( clk,reset )
</br>**Description**
 manage register 
- read_bloc: ( clk, reset )
