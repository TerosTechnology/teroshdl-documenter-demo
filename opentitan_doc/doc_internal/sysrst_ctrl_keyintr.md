# Entity: sysrst_ctrl_keyintr
## Diagram
![Diagram](sysrst_ctrl_keyintr.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description: sysrst_ctrl key-triggered interrupt Module
 
## Ports
| Port name               | Direction | Type                                           | Description |
| ----------------------- | --------- | ---------------------------------------------- | ----------- |
| clk_aon_i               | input     |                                                |             |
| rst_aon_ni              | input     |                                                |             |
| clk_i                   | input     |                                                |             |
| rst_ni                  | input     |                                                |             |
| pwrb_int                | input     |                                                |             |
| key0_int                | input     |                                                |             |
| key1_int                | input     |                                                |             |
| key2_int                | input     |                                                |             |
| ac_present_int          | input     |                                                |             |
| cio_ec_rst_in_l_i       | input     |                                                |             |
| key_intr_ctl_i          | input     | sysrst_ctrl_reg2hw_key_intr_ctl_reg_t          |             |
| key_intr_debounce_ctl_i | input     | sysrst_ctrl_reg2hw_key_intr_debounce_ctl_reg_t |             |
| key_intr_status_o       | output    | sysrst_ctrl_hw2reg_key_intr_status_reg_t       |             |
| sysrst_ctrl_key_intr    | output    |                                                |             |
## Signals
| Name                      | Type         | Description |
| ------------------------- | ------------ | ----------- |
| cfg_pwrb_in_h2l           | logic        |             |
| cfg_key0_in_h2l           | logic        |             |
| cfg_key1_in_h2l           | logic        |             |
| cfg_key2_in_h2l           | logic        |             |
| cfg_ac_present_h2l        | logic        |             |
| cfg_ec_rst_l_h2l          | logic        |             |
| cfg_pwrb_in_l2h           | logic        |             |
| cfg_key0_in_l2h           | logic        |             |
| cfg_key1_in_l2h           | logic        |             |
| cfg_key2_in_l2h           | logic        |             |
| cfg_ac_present_l2h        | logic        |             |
| cfg_ec_rst_l_l2h          | logic        |             |
| cfg_key_intr_timer        | logic [15:0] |             |
| load_key_intr_timer       | logic        |             |
| cfg_key_intr_timer_d      | logic [15:0] |             |
| pwrb_int_i                | logic        |             |
| key0_int_i                | logic        |             |
| key1_int_i                | logic        |             |
| key2_int_i                | logic        |             |
| ac_present_int_i          | logic        |             |
| ec_rst_l_int_i            | logic        |             |
| pwrb_intr_h2l_det         | logic        |             |
| pwrb_intr_h2l_det_q       | logic        |             |
| pwrb_intr_h2l_pulse       | logic        |             |
| pwrb_intr_l2h_det         | logic        |             |
| pwrb_intr_l2h_det_q       | logic        |             |
| pwrb_intr_l2h_pulse       | logic        |             |
| key0_intr_h2l_det         | logic        |             |
| key0_intr_h2l_det_q       | logic        |             |
| key0_intr_h2l_pulse       | logic        |             |
| key0_intr_l2h_det         | logic        |             |
| key0_intr_l2h_det_q       | logic        |             |
| key0_intr_l2h_pulse       | logic        |             |
| key1_intr_h2l_det         | logic        |             |
| key1_intr_h2l_det_q       | logic        |             |
| key1_intr_h2l_pulse       | logic        |             |
| key1_intr_l2h_det         | logic        |             |
| key1_intr_l2h_det_q       | logic        |             |
| key1_intr_l2h_pulse       | logic        |             |
| key2_intr_h2l_det         | logic        |             |
| key2_intr_h2l_det_q       | logic        |             |
| key2_intr_h2l_pulse       | logic        |             |
| key2_intr_l2h_det         | logic        |             |
| key2_intr_l2h_det_q       | logic        |             |
| key2_intr_l2h_pulse       | logic        |             |
| ac_present_intr_h2l_det   | logic        |             |
| ac_present_intr_h2l_det_q | logic        |             |
| ac_present_intr_h2l_pulse | logic        |             |
| ac_present_intr_l2h_det   | logic        |             |
| ac_present_intr_l2h_det_q | logic        |             |
| ac_present_intr_l2h_pulse | logic        |             |
| ec_rst_l_intr_h2l_det     | logic        |             |
| ec_rst_l_intr_h2l_det_q   | logic        |             |
| ec_rst_l_intr_h2l_pulse   | logic        |             |
| ec_rst_l_intr_l2h_det     | logic        |             |
| ec_rst_l_intr_l2h_det_q   | logic        |             |
| ec_rst_l_intr_l2h_pulse   | logic        |             |
| pwrb_h2l_intr             | logic        |             |
| pwrb_l2h_intr             | logic        |             |
| key0_in_h2l_intr          | logic        |             |
| key0_in_l2h_intr          | logic        |             |
| key1_in_h2l_intr          | logic        |             |
| key1_in_l2h_intr          | logic        |             |
| key2_in_h2l_intr          | logic        |             |
| key2_in_l2h_intr          | logic        |             |
| ac_present_h2l_intr       | logic        |             |
| ac_present_l2h_intr       | logic        |             |
| ec_rst_l_h2l_intr         | logic        |             |
| ec_rst_l_l2h_intr         | logic        |             |
## Processes
- i_cfg_key_intr_timer_reg: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_pwrb_intr_h2l_det: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_pwrb_intr_l2h_det: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_key0_intr_h2l_det: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_key0_intr_l2h_det: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_key1_intr_h2l_det: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_key1_intr_l2h_det: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_key2_intr_h2l_det: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_key2_intr_l2h_det: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_ac_present_intr_h2l_det: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_ac_present_intr_l2h_det: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_ec_rst_l_intr_h2l_det: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

- i_ec_rst_l_intr_l2h_det: _( @(posedge clk_aon_i or negedge rst_aon_ni) )_

## Instantiations
- i_cfg_pwrb_in_h2l: prim_flop_2sync
- i_cfg_key0_in_h2l: prim_flop_2sync
- i_cfg_key1_in_h2l: prim_flop_2sync
- i_cfg_key2_in_h2l: prim_flop_2sync
- i_cfg_ac_present_h2l: prim_flop_2sync
- i_cfg_ec_rst_l_h2l: prim_flop_2sync
- i_cfg_pwrb_in_l2h: prim_flop_2sync
- i_cfg_key0_in_l2h: prim_flop_2sync
- i_cfg_key1_in_l2h: prim_flop_2sync
- i_cfg_key2_in_l2h: prim_flop_2sync
- i_cfg_ac_present_l2h: prim_flop_2sync
- i_cfg_ec_rst_l_l2h: prim_flop_2sync
- i_cfg_key_intr_timer: prim_fifo_async
- i_pwrb_int_i: prim_flop_2sync
- i_key0_int_i: prim_flop_2sync
- i_key1_int_i: prim_flop_2sync
- i_key2_int_i: prim_flop_2sync
- i_ac_present_int_i: prim_flop_2sync
- i_ec_rst_l_int_i: prim_flop_2sync
- i_pwrbintr_fsm: sysrst_ctrl_keyfsm
- i_key0intr_fsm: sysrst_ctrl_keyfsm
- i_key1intr_fsm: sysrst_ctrl_keyfsm
- i_key2intr_fsm: sysrst_ctrl_keyfsm
- i_ac_presentintr_fsm: sysrst_ctrl_keyfsm
- i_ec_rst_lintr_fsm: sysrst_ctrl_keyfsm
- i_pwrb_h2l: prim_pulse_sync
- i_pwrb_l2h: prim_pulse_sync
- i_key0_in_h2l: prim_pulse_sync
- i_key0_in_l2h: prim_pulse_sync
- i_key1_in_h2l: prim_pulse_sync
- i_key1_in_l2h: prim_pulse_sync
- i_key2_in_h2l: prim_pulse_sync
- i_key2_in_l2h: prim_pulse_sync
- i_ac_present_h2l: prim_pulse_sync
- i_ac_present_l2h: prim_pulse_sync
- i_ec_rst_l_h2l: prim_pulse_sync
- i_ec_rst_l_l2h: prim_pulse_sync
