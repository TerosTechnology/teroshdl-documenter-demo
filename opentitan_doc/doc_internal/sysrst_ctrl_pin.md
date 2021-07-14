# Entity: sysrst_ctrl_pin

## Diagram

![Diagram](sysrst_ctrl_pin.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description: sysrst_ctrl pin visibility and override Module
 
## Ports

| Port name          | Direction | Type                                     | Description |
| ------------------ | --------- | ---------------------------------------- | ----------- |
| clk_aon_i          | input     |                                          |             |
| rst_aon_ni         | input     |                                          |             |
| clk_i              | input     |                                          |             |
| rst_ni             | input     |                                          |             |
| cio_pwrb_in_i      | input     |                                          |             |
| cio_key0_in_i      | input     |                                          |             |
| cio_key1_in_i      | input     |                                          |             |
| cio_key2_in_i      | input     |                                          |             |
| cio_ac_present_i   | input     |                                          |             |
| cio_ec_rst_in_l_i  | input     |                                          |             |
| cio_lid_open_i     | input     |                                          |             |
| pwrb_out_hw        | input     |                                          |             |
| key0_out_hw        | input     |                                          |             |
| key1_out_hw        | input     |                                          |             |
| key2_out_hw        | input     |                                          |             |
| bat_disable_hw     | input     |                                          |             |
| ec_rst_l_hw        | input     |                                          |             |
| z3_wakeup_hw       | input     |                                          |             |
| pin_allowed_ctl_i  | input     | sysrst_ctrl_reg2hw_pin_allowed_ctl_reg_t |             |
| pin_out_ctl_i      | input     | sysrst_ctrl_reg2hw_pin_out_ctl_reg_t     |             |
| pin_out_value_i    | input     | sysrst_ctrl_reg2hw_pin_out_value_reg_t   |             |
| pin_in_value_o     | output    | sysrst_ctrl_hw2reg_pin_in_value_reg_t    |             |
| pwrb_out_int       | output    |                                          |             |
| key0_out_int       | output    |                                          |             |
| key1_out_int       | output    |                                          |             |
| key2_out_int       | output    |                                          |             |
| bat_disable_int    | output    |                                          |             |
| z3_wakeup_int      | output    |                                          |             |
| cio_ec_rst_out_l_o | output    |                                          |             |
## Signals

| Name                    | Type  | Description |
| ----------------------- | ----- | ----------- |
| cfg_ac_present_i_pin    | logic |             |
| cfg_ec_rst_l_i_pin      | logic |             |
| cfg_pwrb_in_i_pin       | logic |             |
| cfg_key0_in_i_pin       | logic |             |
| cfg_key1_in_i_pin       | logic |             |
| cfg_key2_in_i_pin       | logic |             |
| cfg_lid_open_i_pin      | logic |             |
| cfg_bat_disable_0_allow | logic |             |
| cfg_ec_rst_l_0_allow    | logic |             |
| cfg_pwrb_out_0_allow    | logic |             |
| cfg_key0_out_0_allow    | logic |             |
| cfg_key1_out_0_allow    | logic |             |
| cfg_key2_out_0_allow    | logic |             |
| cfg_z3_wakeup_0_allow   | logic |             |
| cfg_bat_disable_1_allow | logic |             |
| cfg_ec_rst_l_1_allow    | logic |             |
| cfg_pwrb_out_1_allow    | logic |             |
| cfg_key0_out_1_allow    | logic |             |
| cfg_key1_out_1_allow    | logic |             |
| cfg_key2_out_1_allow    | logic |             |
| cfg_z3_wakeup_1_allow   | logic |             |
| cfg_bat_disable_ov      | logic |             |
| cfg_ec_rst_l_ov         | logic |             |
| cfg_pwrb_out_ov         | logic |             |
| cfg_key0_out_ov         | logic |             |
| cfg_key1_out_ov         | logic |             |
| cfg_key2_out_ov         | logic |             |
| cfg_z3_wakeup_ov        | logic |             |
| cfg_bat_disable_q       | logic |             |
| cfg_ec_rst_l_q          | logic |             |
| cfg_pwrb_out_q          | logic |             |
| cfg_key0_out_q          | logic |             |
| cfg_key1_out_q          | logic |             |
| cfg_key2_out_q          | logic |             |
| cfg_z3_wakeup_q         | logic |             |
## Instantiations

- i_cfg_ac_present_i_pin: prim_flop_2sync
- i_cfg_ec_rst_l_i_pin: prim_flop_2sync
- i_cfg_pwrb_in_i_pin: prim_flop_2sync
- i_cfg_key0_in_i_pin: prim_flop_2sync
- i_cfg_key1_in_i_pin: prim_flop_2sync
- i_cfg_key2_in_i_pin: prim_flop_2sync
- i_cfg_lid_open_i_pin: prim_flop_2sync
- i_cfg_bat_disable_0_allow: prim_flop_2sync
- i_cfg_ec_rst_l_0_allow: prim_flop_2sync
- i_cfg_pwrb_out_0_allow: prim_flop_2sync
- i_cfg_key0_out_0_allow: prim_flop_2sync
- i_cfg_key1_out_0_allow: prim_flop_2sync
- i_cfg_key2_out_0_allow: prim_flop_2sync
- i_cfg_z3_wakeup_0_allow: prim_flop_2sync
- i_cfg_bat_disable_1_allow: prim_flop_2sync
- i_cfg_ec_rst_l_1_allow: prim_flop_2sync
- i_cfg_pwrb_out_1_allow: prim_flop_2sync
- i_cfg_key0_out_1_allow: prim_flop_2sync
- i_cfg_key1_out_1_allow: prim_flop_2sync
- i_cfg_key2_out_1_allow: prim_flop_2sync
- i_cfg_z3_wakeup_1_allow: prim_flop_2sync
- i_cfg_bat_disable_ov: prim_flop_2sync
- i_cfg_ec_rst_l_ov: prim_flop_2sync
- i_cfg_pwrb_out_ov: prim_flop_2sync
- i_cfg_key0_out_ov: prim_flop_2sync
- i_cfg_key1_out_ov: prim_flop_2sync
- i_cfg_key2_out_ov: prim_flop_2sync
- i_cfg_z3_wakeup_ov: prim_flop_2sync
- i_cfg_bat_disable_q: prim_flop_2sync
- i_cfg_ec_rst_l_q: prim_flop_2sync
- i_cfg_pwrb_out_q: prim_flop_2sync
- i_cfg_key0_out_q: prim_flop_2sync
- i_cfg_key1_out_q: prim_flop_2sync
- i_cfg_key2_out_q: prim_flop_2sync
- i_cfg_z3_wakeup_q: prim_flop_2sync
