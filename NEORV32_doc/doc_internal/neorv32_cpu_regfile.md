# Entity: neorv32_cpu_regfile
## Diagram
![Diagram](neorv32_cpu_regfile.svg "Diagram")
## Generics
| Generic name          | Type    | Value | Description |
| --------------------- | ------- | ----- | ----------- |
| CPU_EXTENSION_RISCV_E | boolean | false |             |
## Ports
| Port name | Direction | Type                                       | Description |
| --------- | --------- | ------------------------------------------ | ----------- |
| clk_i     | in        | std_ulogic                                 |             |
| ctrl_i    | in        | std_ulogic_vector(ctrl_width_c-1 downto 0) |             |
| mem_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| alu_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| rs1_o     | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| rs2_o     | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| cmp_o     | out       | std_ulogic_vector(1 downto 0)              |             |
## Signals
| Name         | Type                                       | Description |
| ------------ | ------------------------------------------ | ----------- |
| reg_file     | reg_file_t                                 |             |
| reg_file_emb | reg_file_emb_t                             |             |
| rf_wdata     | std_ulogic_vector(data_width_c-1 downto 0) |             |
| rd_is_r0     | std_ulogic                                 |             |
| rf_we        | std_ulogic                                 |             |
| dst_addr     | std_ulogic_vector(4 downto 0)              |             |
| opa_addr     | std_ulogic_vector(4 downto 0)              |             |
| opb_addr     | std_ulogic_vector(4 downto 0)              |             |
| rs1          | std_ulogic_vector(data_width_c-1 downto 0) |             |
|  rs2         | std_ulogic_vector(data_width_c-1 downto 0) |             |
| cmp_opx      | std_ulogic_vector(data_width_c downto 0)   |             |
| cmp_opy      | std_ulogic_vector(data_width_c downto 0)   |             |
## Types
| Name           | Type | Description |
| -------------- | ---- | ----------- |
| reg_file_t     |      |             |
| reg_file_emb_t |      |             |
## Processes
- rf_access: _( clk_i )_

