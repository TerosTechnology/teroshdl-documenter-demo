# Entity: otbn_mac_bignum
## Diagram
![Diagram](otbn_mac_bignum.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Ports
| Port name            | Direction | Type                   | Description |
| -------------------- | --------- | ---------------------- | ----------- |
| clk_i                | input     |                        |             |
| rst_ni               | input     |                        |             |
| operation_i          | input     | mac_bignum_operation_t |             |
| mac_en_i             | input     |                        |             |
| operation_result_o   | output    | [WLEN-1:0]             |             |
| operation_flags_o    | output    | flags_t                |             |
| operation_flags_en_o | output    | flags_t                |             |
| ispr_acc_o           | output    | [WLEN-1:0]             |             |
| ispr_acc_wr_data_i   | input     | [WLEN-1:0]             |             |
| ispr_acc_wr_en_i     | input     |                        |             |
## Signals
| Name                    | Type               | Description |
| ----------------------- | ------------------ | ----------- |
| adder_op_a              | logic [WLEN-1:0]   |             |
| adder_op_b              | logic [WLEN-1:0]   |             |
| adder_result            | logic [WLEN-1:0]   |             |
| adder_result_hw_is_zero | logic [1:0]        |             |
| mul_op_a                | logic [QWLEN-1:0]  |             |
| mul_op_b                | logic [QWLEN-1:0]  |             |
| mul_res                 | logic [WLEN/2-1:0] |             |
| mul_res_shifted         | logic [WLEN-1:0]   |             |
| acc                     | logic [WLEN-1:0]   |             |
| acc_d                   | logic [WLEN-1:0]   |             |
| acc_q                   | logic [WLEN-1:0]   |             |
| acc_en                  | logic              |             |
## Constants
| Name  | Type         | Value    | Description                                                                           |
| ----- | ------------ | -------- | ------------------------------------------------------------------------------------- |
| QWLEN | int unsigned | WLEN / 4 | The MAC operates on quarter-words, QWLEN gives the number of bits in a quarter-word.  |
## Processes
- unnamed: _(  )_
Extract QWLEN multiply operands from WLEN operand inputs based on chosen quarter word from the
instruction (operand_[a|b]_qw_sel).

**Description**
Extract QWLEN multiply operands from WLEN operand inputs based on chosen quarter word from the
instruction (operand_[a|b]_qw_sel).

- unnamed: _(  )_
Shift the QWLEN multiply result into a WLEN word before accumulating using the shift amount
supplied in the instruction (pre_acc_shift_imm).

**Description**
Shift the QWLEN multiply result into a WLEN word before accumulating using the shift amount
supplied in the instruction (pre_acc_shift_imm).

- unnamed: _( @(posedge clk_i or negedge rst_ni) )_

