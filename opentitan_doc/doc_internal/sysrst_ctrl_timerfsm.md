# Entity: sysrst_ctrl_timerfsm

- **File**: sysrst_ctrl_timerfsm.sv
## Diagram

![Diagram](sysrst_ctrl_timerfsm.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Description sysrst_ctrl timer-based FSM module

## Generics

| Generic name | Type         | Value | Description |
| ------------ | ------------ | ----- | ----------- |
| TimerWidth   | int unsigned | 16    |             |
## Ports

| Port name          | Direction | Type             | Description |
| ------------------ | --------- | ---------------- | ----------- |
| clk_i              | input     |                  |             |
| rst_ni             | input     |                  |             |
| trigger_i          | input     |                  |             |
| cfg_timer_i        | input     | [TimerWidth-1:0] |             |
| cfg_l2h_en_i       | input     |                  |             |
| cfg_h2l_en_i       | input     |                  |             |
| timer_l2h_cond_met | output    |                  |             |
| timer_h2l_cond_met | output    |                  |             |
## Signals

| Name          | Type                   | Description                      |
| ------------- | ---------------------- | -------------------------------- |
| trigger_q     | logic                  |                                  |
| trigger_h2l   | logic                  |                                  |
| trigger_l2h   | logic                  |                                  |
| trigger_h2h   | logic                  |                                  |
| trigger_l2l   | logic                  |                                  |
| timer_cnt_d   | logic [TimerWidth-1:0] | logic trigger_tgl, trigger_sty;  |
| timer_cnt_q   | logic [TimerWidth-1:0] | logic trigger_tgl, trigger_sty;  |
| timer_cnt_clr | logic                  |                                  |
| timer_cnt_en  | logic                  |                                  |
| timer_state_q | timer_state_e          |                                  |
| timer_state_d | timer_state_e          |                                  |
## Types

| Name          | Type                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| timer_state_e | enum logic [2:0] {<br><span style="padding-left:20px">     IDLE    = 3'h0,<br><span style="padding-left:20px">     WAITL2H = 3'h1,<br><span style="padding-left:20px">     WAITH2L = 3'h2,<br><span style="padding-left:20px">     DONEL2H = 3'h3,<br><span style="padding-left:20px">     DONEH2L = 3'h4   } | assign trigger_tgl = trigger_q != trigger_i; assign trigger_sty = trigger_q == trigger_i; three-state FSM IDLE->WAITL2H->DONEL2H or IDLE->WAITH2L->DONEH2L The input signals can be inverted. Hence, both paths FSM will detect a L2H or H2L transition to enter the wait state debounce timer defines the time to wait for input to stablize FSM will check the input after the debounce period  |
## Processes
- p_trigger_reg: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- p_timer_state_reg: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- p_timer_cnt_reg: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- p_timer_fsm: (  )
  - **Type:** always_comb
