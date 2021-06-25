# Entity: neorv32_cpu_cp_fpu
## Diagram
![Diagram](neorv32_cpu_cp_fpu.svg "Diagram")
## Ports
| Port name | Direction | Type                                       | Description |
| --------- | --------- | ------------------------------------------ | ----------- |
| clk_i     | in        | std_ulogic                                 |             |
| rstn_i    | in        | std_ulogic                                 |             |
| ctrl_i    | in        | std_ulogic_vector(ctrl_width_c-1 downto 0) |             |
| start_i   | in        | std_ulogic                                 |             |
| cmp_i     | in        | std_ulogic_vector(1 downto 0)              |             |
| rs1_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| rs2_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| res_o     | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| fflags_o  | out       | std_ulogic_vector(4 downto 0)              |             |
| valid_o   | out       | std_ulogic                                 |             |
## Signals
| Name           | Type                           | Description |
| -------------- | ------------------------------ | ----------- |
| cmd            | cmd_t                          |             |
| funct_ff       | std_ulogic_vector(2 downto 0)  |             |
| ctrl_engine    | ctrl_engine_t                  |             |
| op_data        | op_data_t                      |             |
| op_class       | op_class_t                     |             |
| fpu_operands   | fpu_operands_t                 |             |
| cmp_ff         | std_ulogic_vector(01 downto 0) |             |
| comp_equal_ff  | std_ulogic                     |             |
| comp_less_ff   | std_ulogic                     |             |
| fu_classify    | fu_interface_t                 |             |
| fu_compare     | fu_interface_t                 |             |
| fu_sign_inject | fu_interface_t                 |             |
| fu_min_max     | fu_interface_t                 |             |
| fu_conv_f2i    | fu_interface_t                 |             |
| fu_addsub      | fu_interface_t                 |             |
| fu_mul         | fu_interface_t                 |             |
| fu_core_done   | std_ulogic                     |             |
| fu_conv_i2f    | fu_i2f_interface_t             |             |
| multiplier     | multiplier_t                   |             |
| addsub         | addsub_t                       |             |
| normalizer     | normalizer_t                   |             |
## Constants
| Name        | Type                          | Value  | Description |
| ----------- | ----------------------------- | ------ | ----------- |
| op_class_c  | std_ulogic_vector(2 downto 0) |  "000" |             |
| op_comp_c   | std_ulogic_vector(2 downto 0) |  "001" |             |
| op_i2f_c    | std_ulogic_vector(2 downto 0) |  "010" |             |
| op_f2i_c    | std_ulogic_vector(2 downto 0) |  "011" |             |
| op_sgnj_c   | std_ulogic_vector(2 downto 0) |  "100" |             |
| op_minmax_c | std_ulogic_vector(2 downto 0) |  "101" |             |
| op_addsub_c | std_ulogic_vector(2 downto 0) |  "110" |             |
| op_mul_c    | std_ulogic_vector(2 downto 0) |  "111" |             |
## Types
| Name               | Type             | Description |
| ------------------ | ---------------- | ----------- |
| cmd_t              |                  |             |
| ctrl_state_t       | (S_IDLE, S_BUSY) |             |
| ctrl_engine_t      |                  |             |
| op_data_t          |                  |             |
| op_class_t         |                  |             |
| fpu_operands_t     |                  |             |
| fu_interface_t     |                  |             |
| fu_i2f_interface_t |                  |             |
| multiplier_t       |                  |             |
| addsub_t           |                  |             |
| normalizer_t       |                  |             |
## Processes
- number_classifier: _( op_data )_

- control_engine_fsm: _( rstn_i, clk_i )_

- float_comparator: _( rstn_i, clk_i )_

- float_comparison: _( fpu_operands, ctrl_i, comp_equal_ff, comp_less_ff )_

- min_max_select: _( fpu_operands, comp_less_ff, fu_compare, ctrl_i )_

- sign_injector: _( ctrl_i, fpu_operands )_

- convert_i2f: _( rstn_i, clk_i )_

- multiplier_core: _( rstn_i, clk_i )_

- multiplier_class_core: _( rstn_i, clk_i )_

- adder_subtractor_core: _( rstn_i, clk_i )_

- adder_subtractor_class_core: _( rstn_i, clk_i )_

- normalizer_input_select: _( funct_ff, addsub, multiplier, fu_conv_i2f )_

- output_gate: _( rstn_i, clk_i )_

## Instantiations
- neorv32_cpu_cp_fpu_f2i_inst: neorv32_cpu_cp_fpu_f2i
- neorv32_cpu_cp_fpu_normalizer_inst: neorv32_cpu_cp_fpu_normalizer
