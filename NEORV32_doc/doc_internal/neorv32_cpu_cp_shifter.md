# Entity: neorv32_cpu_cp_shifter
## Diagram
![Diagram](neorv32_cpu_cp_shifter.svg "Diagram")
## Generics
| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| FAST_SHIFT_EN | boolean | false |             |
## Ports
| Port name | Direction | Type                                       | Description |
| --------- | --------- | ------------------------------------------ | ----------- |
| clk_i     | in        | std_ulogic                                 |             |
| rstn_i    | in        | std_ulogic                                 |             |
| ctrl_i    | in        | std_ulogic_vector(ctrl_width_c-1 downto 0) |             |
| start_i   | in        | std_ulogic                                 |             |
| rs1_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| rs2_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| imm_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| res_o     | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| valid_o   | out       | std_ulogic                                 |             |
## Signals
| Name         | Type                                                     | Description |
| ------------ | -------------------------------------------------------- | ----------- |
| shift_amount | std_ulogic_vector(index_size_f(data_width_c)-1 downto 0) |             |
| shifter      | shifter_t                                                |             |
| bs_level     | bs_level_t                                               |             |
| bs_result    | std_ulogic_vector(data_width_c-1 downto 0)               |             |
## Types
| Name       | Type | Description |
| ---------- | ---- | ----------- |
| shifter_t  |      |             |
| bs_level_t |      |             |
