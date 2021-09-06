# Entity: sysrst_ctrl_combofsm

- **File**: sysrst_ctrl_combofsm.sv
## Diagram

![Diagram](sysrst_ctrl_combofsm.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Description sysrst_ctrl combo detection FSM module

## Generics

| Generic name | Type         | Value | Description |
| ------------ | ------------ | ----- | ----------- |
| Timer1Width  | int unsigned | 16    |             |
| Timer2Width  | int unsigned | 32    |             |
## Ports

| Port name            | Direction | Type              | Description             |
| -------------------- | --------- | ----------------- | ----------------------- |
| clk_i                | input     |                   |                         |
| rst_ni               | input     |                   |                         |
| trigger_h_i          | input     |                   | input vector is all "1" |
| trigger_l_i          | input     |                   | input vector is all "0" |
| cfg_timer1_i         | input     | [Timer1Width-1:0] | debounce                |
| cfg_timer2_i         | input     | [Timer2Width-1:0] | detection               |
| cfg_h2l_en_i         | input     |                   |                         |
| timer_h2l_cond_met_o | output    |                   |                         |
## Signals

| Name           | Type                    | Description |
| -------------- | ----------------------- | ----------- |
| trigger_h_q    | logic                   |             |
| trigger_l_q    | logic                   |             |
| trigger_h2l    | logic                   |             |
| trigger_l2h    | logic                   |             |
| trigger_l2l    | logic                   |             |
| timer1_cnt_d   | logic [Timer1Width-1:0] |             |
| timer1_cnt_q   | logic [Timer1Width-1:0] |             |
| timer1_cnt_clr | logic                   |             |
| timer1_cnt_en  | logic                   |             |
| timer2_cnt_d   | logic [Timer2Width-1:0] |             |
| timer2_cnt_q   | logic [Timer2Width-1:0] |             |
| timer2_cnt_clr | logic                   |             |
| timer2_cnt_en  | logic                   |             |
| timer_state_q  | timer_state_e           |             |
| timer_state_d  | timer_state_e           |             |
## Types

| Name          | Type                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| timer_state_e | enum logic [1:0] {<br><span style="padding-left:20px">     IDLE  = 2'h0,<br><span style="padding-left:20px">     WAIT1 = 2'h1,<br><span style="padding-left:20px">     WAIT2 = 2'h2,<br><span style="padding-left:20px">     DONE  = 2'h3   } | Four-state FSM IDLE->WAIT1->WAIT2->DONE FSM will detect a H2L transition to enter the wait1 state debounce timer defines the time for input to stablize FSM will check the input after the debounce period If the input stays at low, enter the wait2 state Detection timer defines the time for input to be held(pressed) FSM will enter the done state after the detection period  |
## Processes
- p_trigger_h_reg: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- p_trigger_l_reg: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- p_timer_state_reg: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- p_timer1_cnt_reg: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- p_timer2_cnt_reg: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- p_timer_fsm: (  )
  - **Type:** always_comb
