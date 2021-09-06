# Entity: entropy_src_ack_sm

- **File**: entropy_src_ack_sm.sv
## Diagram

![Diagram](entropy_src_ack_sm.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Description: interface between a req/ack interface and a fifo


## Ports

| Port name        | Direction | Type | Description |
| ---------------- | --------- | ---- | ----------- |
| clk_i            | input     |      |             |
| rst_ni           | input     |      |             |
| enable_i         | input     |      |             |
| req_i            | input     |      |             |
| ack_o            | output    |      |             |
| fifo_not_empty_i | input     |      |             |
| fifo_pop_o       | output    |      |             |
| ack_sm_err_o     | output    |      |             |
## Signals

| Name        | Type                   | Description |
| ----------- | ---------------------- | ----------- |
| state_d     | state_e                |             |
| state_q     | state_e                |             |
| state_raw_q | logic [StateWidth-1:0] |             |
## Constants

| Name       | Type | Value | Description                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------- | ---- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| StateWidth | int  | 6     |  Encoding generated with:  $ ./util/design/sparse-fsm-encode.py -d 3 -m 4 -n 6 \       -s 1236774883 --language=sv<br>  Hamming distance histogram:<br>   0: --   1: --   2: --   3: |||||||||||||||||||| (66.67%)   4: ||||| (16.67%)   5: --   6: ||||| (16.67%)<br>  Minimum Hamming distance: 3  Maximum Hamming distance: 6  Minimum Hamming weight: 1  Maximum Hamming weight: 4<br>  |
## Types

| Name    | Type                                                                                                                                                                                                                                                                                              | Description |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| state_e | enum logic [StateWidth-1:0] {<br><span style="padding-left:20px">     Idle      = 6'b010100,<br><span style="padding-left:20px">      AckImmed  = 6'b101100,<br><span style="padding-left:20px">      AckWait   = 6'b000010,<br><span style="padding-left:20px">      Error     = 6'b101011     } |             |
## Processes
- unnamed: (  )
  - **Type:** always_comb
## Instantiations

- u_state_regs: prim_flop
**Description**
 This primitive is used to place a size-only constraint on the
 flops in order to prevent FSM state encoding optimizations.

