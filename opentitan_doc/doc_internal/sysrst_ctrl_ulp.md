# Entity: sysrst_ctrl_ulp

## Diagram

![Diagram](sysrst_ctrl_ulp.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description sysrst_ctrl ULP module
 
## Ports

| Port name               | Direction | Type                                           | Description |
| ----------------------- | --------- | ---------------------------------------------- | ----------- |
| clk_aon_i               | input     |                                                |             |
| rst_aon_ni              | input     |                                                |             |
| clk_i                   | input     |                                                |             |
| rst_ni                  | input     |                                                |             |
| lid_open_int            | input     |                                                |             |
| ac_present_int          | input     |                                                |             |
| pwrb_int                | input     |                                                |             |
| ulp_ac_debounce_ctl_i   | input     | sysrst_ctrl_reg2hw_ulp_ac_debounce_ctl_reg_t   |             |
| ulp_lid_debounce_ctl_i  | input     | sysrst_ctrl_reg2hw_ulp_lid_debounce_ctl_reg_t  |             |
| ulp_pwrb_debounce_ctl_i | input     | sysrst_ctrl_reg2hw_ulp_pwrb_debounce_ctl_reg_t |             |
| ulp_ctl_i               | input     | sysrst_ctrl_reg2hw_ulp_ctl_reg_t               |             |
| ulp_status_o            | output    | sysrst_ctrl_hw2reg_ulp_status_reg_t            |             |
| ulp_wakeup_o            | output    |                                                |             |
| z3_wakeup_hw            | output    |                                                |             |
## Signals

| Name                     | Type         | Description |
| ------------------------ | ------------ | ----------- |
| cfg_ulp_en               | logic        |             |
| load_ulp_ac_timer        | logic        |             |
| cfg_ulp_ac_timer         | logic [15:0] |             |
| cfg_ulp_ac_timer_d       | logic [15:0] |             |
| load_ulp_lid_timer       | logic        |             |
| cfg_ulp_lid_timer        | logic [15:0] |             |
| cfg_ulp_lid_timer_d      | logic [15:0] |             |
| load_ulp_pwrb_timer      | logic        |             |
| cfg_ulp_pwrb_timer       | logic [15:0] |             |
| cfg_ulp_pwrb_timer_d     | logic [15:0] |             |
| pwrb_cond_met            | logic        |             |
| pwrb_cond_met_q          | logic        |             |
| lid_open_cond_met        | logic        |             |
| lid_open_cond_met_q      | logic        |             |
| ac_present_cond_met      | logic        |             |
| ac_present_cond_met_q    | logic        |             |
| pwrb_int_i               | logic        |             |
| lid_open_int_i           | logic        |             |
| ac_present_int_i         | logic        |             |
| pwrb_det_pulse           | logic        |             |
| lid_open_det_pulse       | logic        |             |
| ac_present_det_pulse     | logic        |             |
| cfg_pwrb_det_pulse       | logic        |             |
| cfg_lid_open_det_pulse   | logic        |             |
| cfg_ac_present_det_pulse | logic        |             |
## Processes
- i_cfg_ulp_ac_timer_reg: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
- i_cfg_ulp_lid_timer_reg: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
- i_cfg_ulp_pwrb_timer_reg: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
- i_ulp_cond_met: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
## Instantiations

- i_cfg_ulp_en: prim_flop_2sync
- i_cfg_ulp_ac_timer: prim_fifo_async
- i_cfg_ulp_lid_timer: prim_fifo_async
- i_cfg_ulp_pwrb_timer: prim_fifo_async
- i_pwrb_in_i: prim_flop_2sync
- i_lid_open_in_i: prim_flop_2sync
- i_ac_present_in_i: prim_flop_2sync
- i_pwrb_ulpfsm: sysrst_ctrl_ulpfsm
- i_lid_open_ulpfsm: sysrst_ctrl_ulpfsm
- i_ac_present_ulpfsm: sysrst_ctrl_ulpfsm
- i_pwrb_det_pulse: prim_pulse_sync
- i_lid_open_det_pulse: prim_pulse_sync
- i_ac_present_det_pulse: prim_pulse_sync
