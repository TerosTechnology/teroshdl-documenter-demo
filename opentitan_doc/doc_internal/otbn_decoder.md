# Entity: otbn_decoder
## Diagram
![Diagram](otbn_decoder.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Ports
| Port name               | Direction | Type              | Description                    |
| ----------------------- | --------- | ----------------- | ------------------------------ |
| clk_i                   | input     |                   | For assertions only.           |
| rst_ni                  | input     |                   |                                |
| insn_fetch_resp_data_i  | input     | [31:0]            | instruction data to be decoded |
| insn_fetch_resp_valid_i | input     |                   |                                |
| insn_valid_o            | output    |                   | Decoded instruction            |
| insn_illegal_o          | output    |                   |                                |
| insn_dec_base_o         | output    | insn_dec_base_t   |                                |
| insn_dec_bignum_o       | output    | insn_dec_bignum_t |                                |
| insn_dec_shared_o       | output    | insn_dec_shared_t |                                |
## Signals
| Name                       | Type                     | Description                                                |
| -------------------------- | ------------------------ | ---------------------------------------------------------- |
| illegal_insn               | logic                    |                                                            |
| rf_we_base                 | logic                    |                                                            |
| rf_we_bignum               | logic                    |                                                            |
| insn                       | logic [31:0]             |                                                            |
| insn_alu                   | logic [31:0]             |                                                            |
| insn_rs1                   | logic [4:0]              | Source/Destination register instruction index              |
| insn_rs2                   | logic [4:0]              |                                                            |
| insn_rd                    | logic [4:0]              |                                                            |
| opcode                     | insn_opcode_e            |                                                            |
| opcode_alu                 | insn_opcode_e            |                                                            |
| unused_insn_alu_bits       | logic                    |                                                            |
| imm_b_mux_sel_base         | imm_b_sel_base_e         | immediate selection for operand b in base ISA              |
| shift_amt_mux_sel_bignum   | shamt_sel_bignum_e       | shift amount selection in bignum ISA                       |
| imm_i_type_base            | logic [31:0]             | Immediates from RV32I encoding                             |
| imm_s_type_base            | logic [31:0]             |                                                            |
| imm_b_type_base            | logic [31:0]             |                                                            |
| imm_u_type_base            | logic [31:0]             |                                                            |
| imm_j_type_base            | logic [31:0]             |                                                            |
| imm_l_type_base            | logic [31:0]             | Immediates specific to OTBN encoding                       |
| imm_x_type_base            | logic [31:0]             |                                                            |
| alu_operator_base          | alu_op_base_e            | ALU operation selection for base ISA                       |
| alu_operator_bignum        | alu_op_bignum_e          | ALU operation selection for bignum ISA                     |
| alu_op_a_mux_sel_base      | op_a_sel_e               | operand a selection for base ISA: reg value, PC or zero    |
| alu_op_b_mux_sel_base      | op_b_sel_e               | operand b selection for base ISA: reg value or immediate   |
| alu_op_b_mux_sel_bignum    | op_b_sel_e               | operand b selection for bignum ISA: reg value or immediate |
| comparison_operator_base   | comparison_op_base_e     |                                                            |
| mac_op_a_qw_sel_bignum     | logic [1:0]              |                                                            |
| mac_op_b_qw_sel_bignum     | logic [1:0]              |                                                            |
| mac_wr_hw_sel_upper_bignum | logic                    |                                                            |
| mac_pre_acc_shift_bignum   | logic [1:0]              |                                                            |
| mac_zero_acc_bignum        | logic                    |                                                            |
| mac_shift_out_bignum       | logic                    |                                                            |
| mac_en_bignum              | logic                    |                                                            |
| rf_ren_a_base              | logic                    |                                                            |
| rf_ren_b_base              | logic                    |                                                            |
| rf_ren_a_bignum            | logic                    |                                                            |
| rf_ren_b_bignum            | logic                    |                                                            |
| rf_a_indirect_bignum       | logic                    |                                                            |
| rf_b_indirect_bignum       | logic                    |                                                            |
| rf_d_indirect_bignum       | logic                    |                                                            |
| imm_i_type_bignum          | logic [WLEN-1:0]         |                                                            |
| shift_amt_a_type_bignum    | logic [$clog2(WLEN)-1:0] | Shift amount for ALU instructions other than BN.RSHI       |
| shift_amt_s_type_bignum    | logic [$clog2(WLEN)-1:0] | Shift amount for BN.RSHI                                   |
| alu_shift_right_bignum     | logic                    |                                                            |
| alu_flag_group_bignum      | flag_group_t             |                                                            |
| alu_sel_flag_bignum        | flag_e                   |                                                            |
| alu_flag_en_bignum         | logic                    |                                                            |
| mac_flag_en_bignum         | logic                    |                                                            |
| insn_subset                | insn_subset_e            |                                                            |
| rf_wdata_sel_base          | rf_wd_sel_e              |                                                            |
| rf_wdata_sel_bignum        | rf_wd_sel_e              |                                                            |
| loop_bodysize_base         | logic [11:0]             |                                                            |
| loop_immediate_base        | logic                    |                                                            |
| d_inc_bignum               | logic                    |                                                            |
| a_inc_bignum               | logic                    |                                                            |
| a_wlen_word_inc_bignum     | logic                    |                                                            |
| b_inc_bignum               | logic                    |                                                            |
| sel_insn_bignum            | logic                    |                                                            |
| ecall_insn                 | logic                    |                                                            |
| ld_insn                    | logic                    |                                                            |
| st_insn                    | logic                    |                                                            |
| branch_insn                | logic                    |                                                            |
| jump_insn                  | logic                    |                                                            |
| loop_insn                  | logic                    |                                                            |
| ispr_rd_insn               | logic                    |                                                            |
| ispr_wr_insn               | logic                    |                                                            |
| ispr_rs_insn               | logic                    |                                                            |
| imm_b_base                 | logic [31:0]             | Reduced main ALU immediate MUX for Operand B               |
| alu_shift_amt_bignum       | logic [$clog2(WLEN)-1:0] |                                                            |
| unused_clk                 | logic                    | clk_i and rst_ni are only used by assertions               |
| unused_rst_n               | logic                    |                                                            |
## Processes
- immediate_b_mux: _(  )_

- unnamed: _(  )_

- unnamed: _(  )_

- unnamed: _(  )_

