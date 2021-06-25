# Entity: adc_ctrl_core
## Diagram
![Diagram](adc_ctrl_core.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 adc_ctrl core module
 
## Ports
| Port name             | Direction | Type                                    | Description |
| --------------------- | --------- | --------------------------------------- | ----------- |
| clk_aon_i             | input     |                                         |             |
| rst_slow_ni           | input     |                                         |             |
| clk_i                 | input     |                                         |             |
| rst_ni                | input     |                                         |             |
| adc_en_ctl_i          | input     | adc_ctrl_reg2hw_adc_en_ctl_reg_t        |             |
| adc_pd_ctl_i          | input     | adc_ctrl_reg2hw_adc_pd_ctl_reg_t        |             |
| adc_lp_sample_ctl_i   | input     | adc_ctrl_reg2hw_adc_lp_sample_ctl_reg_t |             |
| adc_sample_ctl_i      | input     | adc_ctrl_reg2hw_adc_sample_ctl_reg_t    |             |
| adc_fsm_rst_i         | input     | adc_ctrl_reg2hw_adc_fsm_rst_reg_t       |             |
| adc_chn0_filter_ctl_i | input     | [NumAdcFilter-1:0]                      |             |
| adc_chn1_filter_ctl_i | input     | [NumAdcFilter-1:0]                      |             |
| adc_wakeup_ctl_i      | input     | adc_ctrl_reg2hw_adc_wakeup_ctl_reg_t    |             |
| adc_intr_ctl_i        | input     | adc_ctrl_reg2hw_adc_intr_ctl_reg_t      |             |
| adc_chn_val_o         | output    | [NumAdcChannel-1:0]                     |             |
| intr_state_i          | input     | adc_ctrl_reg2hw_intr_state_reg_t        |             |
| intr_enable_i         | input     | adc_ctrl_reg2hw_intr_enable_reg_t       |             |
| intr_test_i           | input     | adc_ctrl_reg2hw_intr_test_reg_t         |             |
| intr_state_o          | output    | adc_ctrl_hw2reg_intr_state_reg_t        |             |
| adc_intr_status_o     | output    | adc_ctrl_hw2reg_adc_intr_status_reg_t   |             |
| adc_wakeup_status_o   | output    | adc_ctrl_hw2reg_adc_wakeup_status_reg_t |             |
| debug_cable_wakeup_o  | output    |                                         |             |
| intr_debug_cable_o    | output    |                                         |             |
| adc_i                 | input     |                                         |             |
| adc_o                 | output    |                                         |             |
## Signals
| Name                 | Type                     | Description                           |
| -------------------- | ------------------------ | ------------------------------------- |
| cfg_adc_enable       | logic                    |                                       |
| cfg_oneshot_mode     | logic                    |                                       |
| cfg_lp_mode          | logic                    |                                       |
| load_adc_ctl         | logic                    |                                       |
| load_lp_sample_cnt   | logic                    |                                       |
| load_np_sample_cnt   | logic                    |                                       |
| cfg_pwrup_time       | logic [3:0]              |                                       |
| cfg_wakeup_time      | logic [23:0]             |                                       |
| cfg_lp_sample_cnt    | logic [7:0]              |                                       |
| cfg_np_sample_cnt    | logic [15:0]             |                                       |
| cfg_fsm_rst          | logic                    |                                       |
| cfg_chn0_min_v       | logic [9:0]              |                                       |
| cfg_chn0_max_v       | logic [9:0]              |                                       |
| cfg_chn1_min_v       | logic [9:0]              |                                       |
| cfg_chn1_max_v       | logic [9:0]              |                                       |
| cfg_chn0_cond        | logic [NumAdcFilter-1:0] |                                       |
| cfg_chn1_cond        | logic [NumAdcFilter-1:0] |                                       |
| load_chn0_min_v      | logic [NumAdcFilter-1:0] |                                       |
| load_chn1_min_v      | logic [NumAdcFilter-1:0] |                                       |
| load_chn0_max_v      | logic [NumAdcFilter-1:0] |                                       |
| load_chn1_max_v      | logic [NumAdcFilter-1:0] |                                       |
| cfg_wakeup_en        | logic [NumAdcFilter-1:0] |                                       |
| cfg_intr_en          | logic [NumAdcFilter-1:0] |                                       |
| cfg_oneshot_intr_en  | logic                    |                                       |
| chn0_val_we          | logic                    |                                       |
| chn1_val_we          | logic                    |                                       |
| chn0_val             | logic [9:0]              |                                       |
| chn1_val             | logic [9:0]              |                                       |
| cfg_chn0_rvalid      | logic                    |                                       |
| cfg_chn1_rvalid      | logic                    |                                       |
| chn0_match           | logic [NumAdcFilter-1:0] |                                       |
| chn1_match           | logic [NumAdcFilter-1:0] |                                       |
| adc_ctrl_match       | logic [NumAdcFilter-1:0] |                                       |
| adc_ctrl_match_pulse | logic [NumAdcFilter-1:0] |                                       |
| adc_ctrl_done        | logic                    |                                       |
| oneshot_done         | logic                    |                                       |
| cfg_adc_ctrl_done    | logic                    |                                       |
| cfg_oneshot_done     | logic                    |                                       |
| cfg_chn_val_intr_we  | logic                    |                                       |
| unused_cond_qe       | logic [NumAdcFilter-1:0] | tieoff unused signals                 |
| unused_lp_mode_qe    | logic                    |                                       |
| adc_pd_ctl_qe        | logic                    | all qe's for a register are the same  |
## Processes
- unnamed: _( @(posedge clk_aon_i or negedge rst_slow_ni) )_

- i_cfg_lp_sample_cnt_reg: _( @(posedge clk_aon_i or negedge rst_slow_ni) )_

- i_cfg_np_sample_cnt_reg: _( @(posedge clk_aon_i or negedge rst_slow_ni) )_

## Instantiations
- i_cfg_adc_enable: prim_flop_2sync
- i_cfg_oneshot_mode: prim_flop_2sync
- i_cfg_lp_mode: prim_flop_2sync
- i_cfg_adc_pd_ctl: prim_pulse_sync
- i_cfg_lp_sample_cnt: prim_pulse_sync
- i_cfg_np_sample_cnt: prim_pulse_sync
- i_cfg_fsm_rst: prim_flop_2sync
- i_cfg_wakeup_en0: prim_flop_2sync
- i_cfg_wakeup_en1: prim_flop_2sync
- i_cfg_wakeup_en2: prim_flop_2sync
- i_cfg_wakeup_en3: prim_flop_2sync
- i_cfg_wakeup_en4: prim_flop_2sync
- i_cfg_wakeup_en5: prim_flop_2sync
- i_cfg_wakeup_en6: prim_flop_2sync
- i_cfg_wakeup_en7: prim_flop_2sync
- i_cfg_intr_en0: prim_flop_2sync
- i_cfg_intr_en1: prim_flop_2sync
- i_cfg_intr_en2: prim_flop_2sync
- i_cfg_intr_en3: prim_flop_2sync
- i_cfg_intr_en4: prim_flop_2sync
- i_cfg_intr_en5: prim_flop_2sync
- i_cfg_intr_en6: prim_flop_2sync
- i_cfg_intr_en7: prim_flop_2sync
- i_cfg_oneshot_intr_en: prim_flop_2sync
- i_oneshot_done: prim_pulse_sync
- i_adc_ctrl_done: prim_pulse_sync
- i_cfg_chn0_val: prim_pulse_sync
- i_cfg_chn1_val: prim_pulse_sync
- i_adc_ctrl_fsm: adc_ctrl_fsm
- i_adc_ctrl_intr: adc_ctrl_intr
