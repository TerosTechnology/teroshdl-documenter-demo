# Entity: sysrst_ctrl_ulpfsm

## Diagram

![Diagram](sysrst_ctrl_ulpfsm.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description sysrst_ctrl ULP FSM module
 
## Generics

| Generic name | Type         | Value | Description         |
| ------------ | ------------ | ----- | ------------------- |
| EDGE_TYPE    | bit [15:0]   | "H"   | can be LH, HL and H |
| TIMERBIT     | int unsigned | 16    |                     |
## Ports

| Port name        | Direction | Type           | Description |
| ---------------- | --------- | -------------- | ----------- |
| clk_aon_i        | input     |                |             |
| rst_aon_ni       | input     |                |             |
| trigger_i        | input     |                |             |
| cfg_timer_i      | input     | [TIMERBIT-1:0] |             |
| cfg_en_i         | input     |                |             |
| timer_cond_met_o | output    |                |             |
## Signals

| Name           | Type                 | Description |
| -------------- | -------------------- | ----------- |
| trigger_q      | logic                |             |
| trigger        | logic                |             |
| trigger_stable | logic                |             |
| timer_cnt_d    | logic [TIMERBIT-1:0] |             |
| timer_cnt_q    | logic [TIMERBIT-1:0] |             |
| timer_cnt_clr  | logic                |             |
| timer_cnt_en   | logic                |             |
| timer_state_q  | timer_state_e        |             |
| timer_state_d  | timer_state_e        |             |
## Types

| Name          | Type                                                                                                                                                                                | Description |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| timer_state_e | enum logic [1:0] {                             IDLE_ST = 2'h0,                             WAIT_ST = 2'h1,                             DONE_ST = 2'h2                             } |             |
## Processes
- i_trigger_reg: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
- i_timer_state_reg: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
- i_timer_cnt_reg: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
- timer_fsm: (  )
