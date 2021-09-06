# Entity: sysrst_ctrl_combo

- **File**: sysrst_ctrl_combo.sv
## Diagram

![Diagram](sysrst_ctrl_combo.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Description: sysrst_ctrl combo Module


## Ports

| Port name                | Direction | Type                                           | Description                                       |
| ------------------------ | --------- | ---------------------------------------------- | ------------------------------------------------- |
| clk_i                    | input     |                                                |                                                   |
| rst_ni                   | input     |                                                |                                                   |
| pwrb_int_i               | input     |                                                |  (Optionally) inverted input signals on AON clock |
| key0_int_i               | input     |                                                |                                                   |
| key1_int_i               | input     |                                                |                                                   |
| key2_int_i               | input     |                                                |                                                   |
| ac_present_int_i         | input     |                                                |                                                   |
| ec_rst_l_int_i           | input     |                                                |                                                   |
| ec_rst_ctl_i             | input     | sysrst_ctrl_reg2hw_ec_rst_ctl_reg_t            |  CSRs synced to AON clock                         |
| key_intr_debounce_ctl_i  | input     | sysrst_ctrl_reg2hw_key_intr_debounce_ctl_reg_t |                                                   |
| com_sel_ctl_i            | input     | [NumCombo-1:0]                                 |                                                   |
| com_det_ctl_i            | input     | [NumCombo-1:0]                                 |                                                   |
| com_out_ctl_i            | input     | [NumCombo-1:0]                                 |                                                   |
| combo_intr_status_o      | output    | sysrst_ctrl_hw2reg_combo_intr_status_reg_t     |                                                   |
| sysrst_ctrl_combo_intr_o | output    |                                                |  Output signals on AON clock                      |
| bat_disable_hw_o         | output    |                                                |                                                   |
| rst_req_o                | output    |                                                |                                                   |
| ec_rst_l_hw_o            | output    |                                                |                                                   |
## Signals

| Name              | Type                 | Description                                                                    |
| ----------------- | -------------------- | ------------------------------------------------------------------------------ |
| combo_bat_disable | logic [NumCombo-1:0] |  There are four possible combos  Each key combo can select different triggers  |
| combo_ec_rst_l    | logic [NumCombo-1:0] |                                                                                |
| combo_rst_req     | logic [NumCombo-1:0] |                                                                                |
| combo_intr_pulse  | logic [NumCombo-1:0] |                                                                                |
| in                | logic [4:0]          |                                                                                |
