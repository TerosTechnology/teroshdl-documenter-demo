# Entity: sysrst_ctrl_combo

## Diagram

![Diagram](sysrst_ctrl_combo.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description: sysrst_ctrl combo Module
 
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
| ec_rst_ctl_i            | input     | sysrst_ctrl_reg2hw_ec_rst_ctl_reg_t            |             |
| key_intr_debounce_ctl_i | input     | sysrst_ctrl_reg2hw_key_intr_debounce_ctl_reg_t |             |
| com_sel_ctl_i           | input     | [NumCombo-1:0]                                 |             |
| com_det_ctl_i           | input     | [NumCombo-1:0]                                 |             |
| com_out_ctl_i           | input     | [NumCombo-1:0]                                 |             |
| combo_intr_status_o     | output    | sysrst_ctrl_hw2reg_combo_intr_status_reg_t     |             |
| sysrst_ctrl_combo_intr  | output    |                                                |             |
| bat_disable_hw          | output    |                                                |             |
| gsc_rst_o               | output    |                                                |             |
| ec_rst_l_hw             | output    |                                                |             |
## Signals

| Name                   | Type                 | Description |
| ---------------------- | -------------------- | ----------- |
| cfg_key0_in_sel_com    | logic [NumCombo-1:0] |             |
| cfg_key1_in_sel_com    | logic [NumCombo-1:0] |             |
| cfg_key2_in_sel_com    | logic [NumCombo-1:0] |             |
| cfg_pwrb_in_sel_com    | logic [NumCombo-1:0] |             |
| cfg_ac_present_sel_com | logic [NumCombo-1:0] |             |
| cfg_combo_timer        | logic [31:0]         |             |
| cfg_debounce_timer     | logic [15:0]         |             |
| load_combo_timer       | logic [NumCombo-1:0] |             |
| load_debounce_timer    | logic                |             |
| cfg_combo_timer_d      | logic [31:0]         |             |
| cfg_debounce_timer_d   | logic [15:0]         |             |
| cfg_bat_disable_com    | logic [NumCombo-1:0] |             |
| cfg_intr_com           | logic [NumCombo-1:0] |             |
| cfg_ec_rst_com         | logic [NumCombo-1:0] |             |
| cfg_gsc_rst_com        | logic [NumCombo-1:0] |             |
| pwrb_int_i             | logic                |             |
| key0_int_i             | logic                |             |
| key1_int_i             | logic                |             |
| key2_int_i             | logic                |             |
| ac_present_int_i       | logic                |             |
| trigger_h              | logic [NumCombo-1:0] |             |
| trigger_l              | logic [NumCombo-1:0] |             |
| cfg_combo_en           | logic [NumCombo-1:0] |             |
| combo_det              | logic [NumCombo-1:0] |             |
| combo_bat_disable      | logic [NumCombo-1:0] |             |
| combo_intr_pulse       | logic [NumCombo-1:0] |             |
| combo_ec_rst_l         | logic [NumCombo-1:0] |             |
| combo_gsc_rst          | logic [NumCombo-1:0] |             |
| ec_rst_l_int_i         | logic                |             |
| combo0_h2l_intr        | logic                |             |
| combo1_h2l_intr        | logic                |             |
| combo2_h2l_intr        | logic                |             |
| combo3_h2l_intr        | logic                |             |
## Processes
- i_cfg_debounce_timer_reg: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
## Instantiations

- i_ec_rst_l_int_i: prim_flop_2sync
- i_cfg_debounce_timer: prim_fifo_async
- i_pwrb_int_i: prim_flop_2sync
- i_key0_int_i: prim_flop_2sync
- i_key1_int_i: prim_flop_2sync
- i_key2_int_i: prim_flop_2sync
- i_ac_present_int_i: prim_flop_2sync
- i_combo0_intr: prim_pulse_sync
- i_combo1_intr: prim_pulse_sync
- i_combo2_intr: prim_pulse_sync
- i_combo3_intr: prim_pulse_sync
