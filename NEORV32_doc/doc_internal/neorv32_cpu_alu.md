# Entity: neorv32_cpu_alu
## Diagram
![Diagram](neorv32_cpu_alu.svg "Diagram")
## Generics
| Generic name              | Type    | Value | Description |
| ------------------------- | ------- | ----- | ----------- |
| CPU_EXTENSION_RISCV_M     | boolean | false |             |
| CPU_EXTENSION_RISCV_Zmmul | boolean | false |             |
| CPU_EXTENSION_RISCV_Zfinx | boolean | false |             |
| FAST_MUL_EN               | boolean | false |             |
| FAST_SHIFT_EN             | boolean | false |             |
## Ports
| Port name   | Direction | Type                                       | Description |
| ----------- | --------- | ------------------------------------------ | ----------- |
| clk_i       | in        | std_ulogic                                 |             |
| rstn_i      | in        | std_ulogic                                 |             |
| ctrl_i      | in        | std_ulogic_vector(ctrl_width_c-1 downto 0) |             |
| rs1_i       | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| rs2_i       | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| pc2_i       | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| imm_i       | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| csr_i       | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| cmp_i       | in        | std_ulogic_vector(1 downto 0)              |             |
| res_o       | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| add_o       | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| fpu_flags_o | out       | std_ulogic_vector(4 downto 0)              |             |
| idone_o     | out       | std_ulogic                                 |             |
## Signals
| Name       | Type                                       | Description |
| ---------- | ------------------------------------------ | ----------- |
| opa        | std_ulogic_vector(data_width_c-1 downto 0) |             |
|  opb       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| addsub_res | std_ulogic_vector(data_width_c downto 0)   |             |
| cp_res     | std_ulogic_vector(data_width_c-1 downto 0) |             |
| arith_res  | std_ulogic_vector(data_width_c-1 downto 0) |             |
| logic_res  | std_ulogic_vector(data_width_c-1 downto 0) |             |
| cp_ctrl    | cp_ctrl_t                                  |             |
| cp_start   | std_ulogic_vector(3 downto 0)              |             |
| cp_valid   | std_ulogic_vector(3 downto 0)              |             |
| cp_result  | cp_data_if_t                               |             |
## Types
| Name      | Type | Description |
| --------- | ---- | ----------- |
| cp_ctrl_t |      |             |
## Processes
- binary_arithmetic_core: _( ctrl_i, opa, opb )_

- arithmetic_core: _( ctrl_i, addsub_res )_

- cp_arbiter: _( rstn_i, clk_i )_

- alu_logic_core: _( ctrl_i, rs1_i, opb )_

- alu_function_mux: _( ctrl_i, arith_res, logic_res, csr_i, cp_res )_

## Instantiations
- neorv32_cpu_cp_shifter_inst: neorv32_cpu_cp_shifter
