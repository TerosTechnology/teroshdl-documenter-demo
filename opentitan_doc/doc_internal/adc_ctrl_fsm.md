# Entity: adc_ctrl_fsm

- **File**: adc_ctrl_fsm.sv
## Diagram

![Diagram](adc_ctrl_fsm.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Description adc_ctrl detection FSM module

## Ports

| Port name           | Direction | Type               | Description             |
| ------------------- | --------- | ------------------ | ----------------------- |
| clk_aon_i           | input     |                    |                         |
| rst_aon_ni          | input     |                    |                         |
| cfg_fsm_rst_i       | input     |                    |                         |
| cfg_adc_enable_i    | input     |                    |                         |
| cfg_oneshot_mode_i  | input     |                    |                         |
| cfg_lp_mode_i       | input     |                    |                         |
| cfg_pwrup_time_i    | input     | [3:0]              |                         |
| cfg_wakeup_time_i   | input     | [23:0]             |                         |
| cfg_lp_sample_cnt_i | input     | [7:0]              |                         |
| cfg_np_sample_cnt_i | input     | [15:0]             |                         |
| adc_ctrl_match_i    | input     | [NumAdcFilter-1:0] |                         |
| adc_d_i             | input     | [9:0]              |                         |
| adc_d_val_i         | input     |                    | valid bit for ADC value |
| adc_pd_o            | output    |                    |                         |
| adc_chn_sel_o       | output    | [1:0]              |                         |
| chn0_val_we_o       | output    |                    |                         |
| chn1_val_we_o       | output    |                    |                         |
| chn0_val_o          | output    | [9:0]              |                         |
| chn1_val_o          | output    | [9:0]              |                         |
| adc_ctrl_done_o     | output    |                    |                         |
| oneshot_done_o      | output    |                    |                         |
## Signals

| Name                 | Type                     | Description |
| -------------------- | ------------------------ | ----------- |
| trigger_q            | logic                    |             |
| trigger_l2h          | logic                    |             |
| trigger_h2l          | logic                    |             |
| pwrup_timer_cnt_d    | logic [3:0]              |             |
| pwrup_timer_cnt_q    | logic [3:0]              |             |
| pwrup_timer_cnt_clr  | logic                    |             |
| pwrup_timer_cnt_en   | logic                    |             |
| chn0_val_d           | logic [9:0]              |             |
| chn1_val_d           | logic [9:0]              |             |
| fsm_chn0_sel         | logic                    |             |
| fsm_chn1_sel         | logic                    |             |
| chn0_val_we_d        | logic                    |             |
| chn1_val_we_d        | logic                    |             |
| lp_sample_cnt_d      | logic [7:0]              |             |
| lp_sample_cnt_q      | logic [7:0]              |             |
| lp_sample_cnt_clr    | logic                    |             |
| lp_sample_cnt_en     | logic                    |             |
| wakeup_timer_cnt_d   | logic [23:0]             |             |
| wakeup_timer_cnt_q   | logic [23:0]             |             |
| wakeup_timer_cnt_clr | logic                    |             |
| wakeup_timer_cnt_en  | logic                    |             |
| adc_ctrl_match_q     | logic [NumAdcFilter-1:0] |             |
| fst_lp_match         | logic [NumAdcFilter-1:0] |             |
| any_fst_lp_match     | logic                    |             |
| stay_match           | logic                    |             |
| np_sample_cnt_d      | logic [15:0]             |             |
| np_sample_cnt_q      | logic [15:0]             |             |
| np_sample_cnt_clr    | logic                    |             |
| np_sample_cnt_en     | logic                    |             |
| fsm_state_q          | fsm_state_e              |             |
| fsm_state_d          | fsm_state_e              |             |
## Types

| Name        | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                             |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fsm_state_e | enum logic [3:0] {<br><span style="padding-left:20px">                             PWRDN = 4'h0,<br><span style="padding-left:20px">                             PWRUP = 4'h1,<br><span style="padding-left:20px">                             IDLE = 4'h2,<br><span style="padding-left:20px">                             ONEST_0 = 4'h3,<br><span style="padding-left:20px">                             ONEST_021 = 4'h4,<br><span style="padding-left:20px">                             ONEST_1 = 4'h5,<br><span style="padding-left:20px">                             LP_0 = 4'h6,<br><span style="padding-left:20px">                             LP_021 = 4'h7,<br><span style="padding-left:20px">                             LP_1 = 4'h8,<br><span style="padding-left:20px">                             LP_EVAL = 4'h9,<br><span style="padding-left:20px">                             LP_SLP = 4'ha,<br><span style="padding-left:20px">                             LP_PWRUP = 4'hb,<br><span style="padding-left:20px">                             NP_0 = 4'hc,<br><span style="padding-left:20px">                             NP_021 = 4'hd,<br><span style="padding-left:20px">                             NP_1 = 4'he,<br><span style="padding-left:20px">                             NP_EVAL = 4'hf                             } | FSM flow 1. PWRDN->PWRUP->IDLE->ONEST_0->ONEST_021->ONEST_1->PWRDN 2. PWRDN->PWRUP->IDLE->LP_0->LP_021->LP_1->LP_EVAL->LP_SLP->LP_PWRUP->LP0->    LP_021->LP_1->LP_EVAL->NP_0->NP_021->NP_1->NP_EVAL->NP_0...repeat 3. PWRDN->PWRUP->IDLE->NP_0->NP_021->NP_1->NP_EVAL->NP_0....repeat  |
## Processes
- unnamed: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
  - **Type:** always_ff
- adc_fsm: (  )
  - **Type:** always_comb
