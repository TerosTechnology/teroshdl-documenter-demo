# Entity: clkChangeComplex

- **File**: clkChangeComplex.vhd
## Diagram

![Diagram](clkChangeComplex.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DATA_SIZE    | natural | 16    |             |
## Ports

| Port name       | Direction | Type                                         | Description       |
| --------------- | --------- | -------------------------------------------- | ----------------- |
| data_i_i        | in        | std_logic_vector(DATA_SIZE-1 downto 0)       | input             |
| data_q_i        | in        | std_logic_vector(DATA_SIZE-1 downto 0)       |                   |
| data_en_i       | in        | std_logic                                    |                   |
| data_clk_i      | in        | std_logic                                    |                   |
| data_rst_i      | in        | std_logic                                    |                   |
| data_i_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0)       | output            |
| data_q_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0)       |                   |
| data_en_o       | out       | std_logic                                    |                   |
| data_clk_o      | out       | std_logic                                    |                   |
| data_rst_o      | out       | std_logic                                    |                   |
| m00_axis_aclk   | in        | std_logic                                    | data fo FIFO      |
| m00_axis_tdata  | out       | std_logic_vector((2*DATA_SIZE)-1 downto 0)   |                   |
| m00_axis_tready | in        | std_logic                                    |                   |
| m00_axis_tvalid | out       | std_logic                                    |                   |
| m00_aclk_en     | out       | std_logic                                    |                   |
| s00_axis_aclk   | in        | std_logic                                    | from FIFO to data |
| s00_axis_reset  | in        | std_logic                                    |                   |
| s00_axis_tdata  | in        | std_logic_vector((2*DATA_SIZE) - 1 downto 0) |                   |
| s00_axis_tready | out       | std_logic                                    |                   |
| s00_axis_tvalid | in        | std_logic                                    |                   |
## Signals

| Name      | Type                                       | Description |
| --------- | ------------------------------------------ | ----------- |
| data_in_s | std_logic_vector((2*DATA_SIZE)-1 downto 0) |             |
## Processes
- unnamed: ( s00_axis_aclk )
