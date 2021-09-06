# Entity: otbn_alu_base

- **File**: otbn_alu_base.sv
## Diagram

![Diagram](otbn_alu_base.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
*

## Ports

| Port name           | Direction | Type                  | Description                                               |
| ------------------- | --------- | --------------------- | --------------------------------------------------------- |
| clk_i               | input     |                       |  Block is combinatorial; clk/rst are for assertions only. |
| rst_ni              | input     |                       |                                                           |
| operation_i         | input     | alu_base_operation_t  |                                                           |
| comparison_i        | input     | alu_base_comparison_t |                                                           |
| operation_result_o  | output    | [31:0]                |                                                           |
| comparison_result_o | output    |                       |                                                           |
## Signals

| Name                        | Type                | Description                                                                                                                                         |
| --------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| adder_op_a                  | logic [32:0]        |                                                                                                                                                     |
| adder_op_b                  | logic [32:0]        |                                                                                                                                                     |
| adder_op_b_negate           | logic               |                                                                                                                                                     |
| adder_result                | logic [32:0]        |                                                                                                                                                     |
| and_result                  | logic [31:0]        |                                                                                                                                                     |
| or_result                   | logic [31:0]        |                                                                                                                                                     |
| xor_result                  | logic [31:0]        |                                                                                                                                                     |
| not_result                  | logic [31:0]        |                                                                                                                                                     |
| is_equal                    | logic               |                                                                                                                                                     |
| shift_in                    | logic [32:0]        | ///////////  Shifter // ///////////                                                                                                                 |
| shift_amt                   | logic [4:0]         |                                                                                                                                                     |
| operand_a_reverse           | logic [31:0]        |                                                                                                                                                     |
| shift_out                   | logic [32:0]        |                                                                                                                                                     |
| shift_out_reverse           | logic [31:0]        |                                                                                                                                                     |
| shift_in_signed             | logic signed [32:0] |                                                                                                                                                     |
| unused_adder_result_bit     | logic               |  The bottom bit of adder_result is discarded. It simply corresponds to the carry in used to  produce twos complement subtraction from an addition.  |
| unused_shift_out_result_bit | logic               |  The top bit of shift_out is discarded. shift_in contains an extra bit to deal with sign  extension which isn't needed in the shift_out result.     |
| unused_clk                  | logic               |  clk_i, rst_ni are only used by assertions                                                                                                          |
| unused_rst_n                | logic               |                                                                                                                                                     |
## Processes
- unnamed: (  )
  - **Type:** always_comb
</br>**Description**
//////////////  Output Mux // ////////////// 
