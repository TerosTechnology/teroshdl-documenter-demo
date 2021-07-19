# Entity: serv_decode

- **File**: serv_decode.v
## Diagram

![Diagram](serv_decode.svg "Diagram")
## Generics

| Generic name | Type  | Value | Description |
| ------------ | ----- | ----- | ----------- |
| PRE_REGISTER | [0:0] | 1     |             |
## Ports

| Port name          | Direction | Type        | Description |
| ------------------ | --------- | ----------- | ----------- |
| clk                | input     | wire        |             |
| i_wb_rdt           | input     | wire [31:2] |             |
| i_wb_en            | input     | wire        |             |
| o_sh_right         | output    |             |             |
| o_bne_or_bge       | output    |             |             |
| o_cond_branch      | output    |             |             |
| o_e_op             | output    |             |             |
| o_ebreak           | output    |             |             |
| o_branch_op        | output    |             |             |
| o_mem_op           | output    |             |             |
| o_shift_op         | output    |             |             |
| o_slt_op           | output    |             |             |
| o_rd_op            | output    |             |             |
| o_bufreg_rs1_en    | output    |             |             |
| o_bufreg_imm_en    | output    |             |             |
| o_bufreg_clr_lsb   | output    |             |             |
| o_bufreg_sh_signed | output    |             |             |
| o_ctrl_jal_or_jalr | output    |             |             |
| o_ctrl_utype       | output    |             |             |
| o_ctrl_pc_rel      | output    |             |             |
| o_ctrl_mret        | output    |             |             |
| o_alu_sub          | output    |             |             |
| o_alu_bool_op      | output    | [1:0]       |             |
| o_alu_cmp_eq       | output    |             |             |
| o_alu_cmp_sig      | output    |             |             |
| o_alu_rd_sel       | output    | [2:0]       |             |
| o_mem_signed       | output    |             |             |
| o_mem_word         | output    |             |             |
| o_mem_half         | output    |             |             |
| o_mem_cmd          | output    |             |             |
| o_csr_en           | output    |             |             |
| o_csr_addr         | output    | [1:0]       |             |
| o_csr_mstatus_en   | output    |             |             |
| o_csr_mie_en       | output    |             |             |
| o_csr_mcause_en    | output    |             |             |
| o_csr_source       | output    | [1:0]       |             |
| o_csr_d_sel        | output    |             |             |
| o_csr_imm_en       | output    |             |             |
| o_immdec_ctrl      | output    | [3:0]       |             |
| o_immdec_en        | output    | [3:0]       |             |
| o_op_b_source      | output    |             |             |
| o_rd_csr_en        | output    |             |             |
| o_rd_alu_en        | output    |             |             |
## Signals

| Name                | Type       | Description |
| ------------------- | ---------- | ----------- |
| opcode              | reg [4:0]  |             |
| funct3              | reg [2:0]  |             |
| op20                | reg        |             |
| op21                | reg        |             |
| op22                | reg        |             |
| op26                | reg        |             |
| imm30               | reg        |             |
| op_or_opimm         | wire       |             |
| co_mem_op           | wire       |             |
| co_branch_op        | wire       |             |
| co_bufreg_rs1_en    | wire       |             |
| co_bufreg_imm_en    | wire       |             |
| co_bufreg_clr_lsb   | wire       |             |
| co_cond_branch      | wire       |             |
| co_ctrl_utype       | wire       |             |
| co_ctrl_jal_or_jalr | wire       |             |
| co_ctrl_pc_rel      | wire       |             |
| co_rd_op            | wire       |             |
| co_sh_right         | wire       |             |
| co_bne_or_bge       | wire       |             |
| co_shift_op         | wire       |             |
| co_slt_op           | wire       |             |
| csr_op              | wire       |             |
| co_ebreak           | wire       |             |
| co_ctrl_mret        | wire       |             |
| co_e_op             | wire       |             |
| co_bufreg_sh_signed | wire       |             |
| co_alu_sub          | wire       |             |
| csr_valid           | wire       |             |
| co_rd_csr_en        | wire       |             |
| co_csr_en           | wire       |             |
| co_csr_mstatus_en   | wire       |             |
| co_csr_mie_en       | wire       |             |
| co_csr_mcause_en    | wire       |             |
| co_csr_source       | wire [1:0] |             |
| co_csr_d_sel        | wire       |             |
| co_csr_imm_en       | wire       |             |
| co_csr_addr         | wire [1:0] |             |
| co_alu_cmp_eq       | wire       |             |
| co_alu_cmp_sig      | wire       |             |
| co_mem_cmd          | wire       |             |
| co_mem_signed       | wire       |             |
| co_mem_word         | wire       |             |
| co_mem_half         | wire       |             |
| co_alu_bool_op      | wire [1:0] |             |
| co_immdec_ctrl      | wire [3:0] |             |
| co_immdec_en        | wire [3:0] |             |
| co_alu_rd_sel       | wire [2:0] |             |
| co_op_b_source      | wire       |             |
| co_rd_alu_en        | wire       |             |
