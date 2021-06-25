# Entity: neorv32_cpu_cp_muldiv
## Diagram
![Diagram](neorv32_cpu_cp_muldiv.svg "Diagram")
## Generics
| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| FAST_MUL_EN  | boolean | false |             |
| DIVISION_EN  | boolean | true  |             |
## Ports
| Port name | Direction | Type                                       | Description |
| --------- | --------- | ------------------------------------------ | ----------- |
| clk_i     | in        | std_ulogic                                 |             |
| rstn_i    | in        | std_ulogic                                 |             |
| ctrl_i    | in        | std_ulogic_vector(ctrl_width_c-1 downto 0) |             |
| start_i   | in        | std_ulogic                                 |             |
| rs1_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| rs2_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| res_o     | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| valid_o   | out       | std_ulogic                                 |             |
## Signals
| Name             | Type                                       | Description |
| ---------------- | ------------------------------------------ | ----------- |
| state            | state_t                                    |             |
| cnt              | std_ulogic_vector(4 downto 0)              |             |
| cp_op            | std_ulogic_vector(2 downto 0)              |             |
| cp_op_ff         | std_ulogic_vector(2 downto 0)              |             |
| start_div        | std_ulogic                                 |             |
| start_mul        | std_ulogic                                 |             |
| operation        | std_ulogic                                 |             |
| div_opx          | std_ulogic_vector(data_width_c-1 downto 0) |             |
| div_opy          | std_ulogic_vector(data_width_c-1 downto 0) |             |
| rs1_is_signed    | std_ulogic                                 |             |
| rs2_is_signed    | std_ulogic                                 |             |
| opy_is_zero      | std_ulogic                                 |             |
| div_res_corr     | std_ulogic                                 |             |
| valid            | std_ulogic                                 |             |
| remainder        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| quotient         | std_ulogic_vector(data_width_c-1 downto 0) |             |
| div_sub          | std_ulogic_vector(data_width_c   downto 0) |             |
| div_sign_comp_in | std_ulogic_vector(data_width_c-1 downto 0) |             |
| div_sign_comp    | std_ulogic_vector(data_width_c-1 downto 0) |             |
| div_res          | std_ulogic_vector(data_width_c-1 downto 0) |             |
| mul_product      | std_ulogic_vector(63 downto 0)             |             |
| mul_do_add       | std_ulogic_vector(data_width_c downto 0)   |             |
| mul_sign_cycle   | std_ulogic                                 |             |
| mul_p_sext       | std_ulogic                                 |             |
| mul_op_x         | signed(32 downto 0)                        |             |
| mul_op_y         | signed(32 downto 0)                        |             |
| mul_buf_ff       | signed(65 downto 0)                        |             |
## Constants
| Name           | Type                          | Value  | Description |
| -------------- | ----------------------------- | ------ | ----------- |
| cp_op_mul_c    | std_ulogic_vector(2 downto 0) |  "000" |             |
| cp_op_mulh_c   | std_ulogic_vector(2 downto 0) |  "001" |             |
| cp_op_mulhsu_c | std_ulogic_vector(2 downto 0) |  "010" |             |
| cp_op_mulhu_c  | std_ulogic_vector(2 downto 0) |  "011" |             |
| cp_op_div_c    | std_ulogic_vector(2 downto 0) |  "100" |             |
| cp_op_divu_c   | std_ulogic_vector(2 downto 0) |  "101" |             |
| cp_op_rem_c    | std_ulogic_vector(2 downto 0) |  "110" |             |
| cp_op_remu_c   | std_ulogic_vector(2 downto 0) |  "111" |             |
## Types
| Name    | Type                                                    | Description |
| ------- | ------------------------------------------------------- | ----------- |
| state_t | (IDLE, DIV_PREPROCESS, PROCESSING, FINALIZE, COMPLETED) |             |
## Processes
- coprocessor_ctrl: _( rstn_i, clk_i )_

- mul_update: _( mul_product, mul_sign_cycle, mul_p_sext, rs1_is_signed, rs1_i )_

- operation_result: _( rstn_i, clk_i )_

## State machines
![Diagram_state_machine_0]( stm_neorv32_cpu_cp_muldiv_00.svg "Diagram")