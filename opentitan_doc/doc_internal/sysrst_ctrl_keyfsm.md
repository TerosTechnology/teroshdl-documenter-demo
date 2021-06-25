# Entity: sysrst_ctrl_keyfsm
## Diagram
![Diagram](sysrst_ctrl_keyfsm.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description sysrst_ctrl key press and release FSM module
 
## Generics
| Generic name | Type         | Value | Description |
| ------------ | ------------ | ----- | ----------- |
| TIMERBIT     | int unsigned | 16    |             |
## Ports
| Port name          | Direction | Type           | Description |
| ------------------ | --------- | -------------- | ----------- |
| clk_aon_i          | input     |                |             |
| rst_aon_ni         | input     |                |             |
| trigger_i          | input     |                |             |
| cfg_timer_i        | input     | [TIMERBIT-1:0] |             |
| cfg_l2h_en_i       | input     |                |             |
| cfg_h2l_en_i       | input     |                |             |
| timer_l2h_cond_met | output    |                |             |
| timer_h2l_cond_met | output    |                |             |
## Signals
| Name          | Type                 | Description |
| ------------- | -------------------- | ----------- |
| trigger_q     | logic                |             |
| trigger_h2l   | logic                |             |
| trigger_l2h   | logic                |             |
| trigger_l2l   | logic                |             |
| trigger_h2h   | logic                |             |
| timer_cnt_d   | logic [TIMERBIT-1:0] |             |
| timer_cnt_q   | logic [TIMERBIT-1:0] |             |
| timer_cnt_clr | logic                |             |
| timer_cnt_en  | logic                |             |
| timer_state_q | timer_state_e        |             |
| timer_state_d | timer_state_e        |             |
## Types
| Name          | Type                                                                                                                                                                                                                                                                     | Description |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| timer_state_e | enum logic [2:0] {                             IDLE = 3'h0,                             WAITL2H = 3'h1,                             WAITH2L = 3'h2,                             DONEL2H = 3'h3,                             DONEH2L = 3'h4                             } |             |
## Processes
- i_trigger_reg: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_timer_state_reg: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_timer_cnt_reg: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- timer_fsm: _(  )_

