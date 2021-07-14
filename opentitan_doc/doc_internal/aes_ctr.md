# Entity: aes_ctr

## Diagram

![Diagram](aes_ctr.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 AES counter for CTR mode
 This module uses one counter with a width of SliceSizeCtr to iteratively increment the 128-bit
 counter value.
 
## Ports

| Port name | Direction | Type               | Description |
| --------- | --------- | ------------------ | ----------- |
| clk_i     | input     |                    |             |
| rst_ni    | input     |                    |             |
| incr_i    | input     | sp2v_e             |             |
| ready_o   | output    | sp2v_e             |             |
| alert_o   | output    |                    |             |
| ctr_i     | input     | [NumSlicesCtr-1:0] |             |
| ctr_o     | output    | [NumSlicesCtr-1:0] |             |
| ctr_we_o  | output    | [NumSlicesCtr-1:0] |             |
## Signals

| Name            | Type                                        | Description                                                                                                                |
| --------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| aes_ctr_ns      | aes_ctr_e                                   |                                                                                                                            |
| aes_ctr_cs      | aes_ctr_e                                   |                                                                                                                            |
| ctr_slice_idx_d | logic                   [SliceIdxWidth-1:0] |                                                                                                                            |
| ctr_slice_idx_q | logic                   [SliceIdxWidth-1:0] |                                                                                                                            |
| ctr_carry_d     | logic                                       |                                                                                                                            |
| ctr_carry_q     | logic                                       |                                                                                                                            |
| ctr_i_rev       | logic  [NumSlicesCtr-1:0][SliceSizeCtr-1:0] | 8 times 2 bytes                                                                                                            |
| ctr_o_rev       | logic  [NumSlicesCtr-1:0][SliceSizeCtr-1:0] | 8 times 2 bytes                                                                                                            |
| ctr_we_o_rev    | sp2v_e [NumSlicesCtr-1:0]                   |                                                                                                                            |
| ctr_we          | sp2v_e                                      |                                                                                                                            |
| ctr_i_slice     | logic                    [SliceSizeCtr-1:0] |                                                                                                                            |
| ctr_o_slice     | logic                    [SliceSizeCtr-1:0] |                                                                                                                            |
| ctr_value       | logic                      [SliceSizeCtr:0] |                                                                                                                            |
| alert           | logic                                       |                                                                                                                            |
| incr            | sp2v_e                                      |                                                                                                                            |
| incr_err_d      | logic                                       |                                                                                                                            |
| incr_err_q      | logic                                       |                                                                                                                            |
| incr_raw        | logic [Sp2VWidth-1:0]                       | Check sparsely encoded incr signal.                                                                                        |
| aes_ctr_cs_raw  | logic [StateWidth-1:0]                      | This primitive is used to place a size-only constraint on the flops in order to prevent FSM state encoding optimizations.  |
## Constants

| Name          | Type         | Value                              | Description       |
| ------------- | ------------ | ---------------------------------- | ----------------- |
| SliceIdxWidth | int unsigned | prim_util_pkg::vbits(NumSlicesCtr) | Local parameters  |
| StateWidth    | int          | 5                                  |                   |
## Types

| Name      | Type                                                                                                                                                                                                           | Description |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| aes_ctr_e | enum logic [StateWidth-1:0] {<br><span style="padding-left:20px">     IDLE  = 5'b01110,<br><span style="padding-left:20px">     INCR  = 5'b11000,<br><span style="padding-left:20px">     ERROR = 5'b00001   } |             |
## Functions
- aes_rev_order_byte <font id="function_arguments">(logic [15:0][7:0])</font> <font id="function_return">return (logic [15:0][7:0])</font>
**Description**
Reverse byte order - unrelated to NumSlicesCtr and SliceSizeCtr

- aes_rev_order_sp2v <font id="function_arguments">(sp2v_e [NumSlicesCtr-1:0])</font> <font id="function_return">return (sp2v_e [NumSlicesCtr-1:0])</font>
**Description**
Reverse sp2v order

## Processes
- reg_out_ack_err: ( @(posedge clk_i or negedge rst_ni) )
**Description**
Need to register errors in incr to avoid circular loops in the main
controller related to start.

- aes_ctr_fsm: (  )
**Description**
FSM

- unnamed: ( @(posedge clk_i or negedge rst_ni) )
**Description**
Registers

- unnamed: (  )
**Description**
Combine input and counter output.

- unnamed: (  )
**Description**
Generate the sliced write enable.

## Instantiations

- u_aes_sb_en_buf_chk: aes_sel_buf_chk
- u_state_regs: prim_flop
