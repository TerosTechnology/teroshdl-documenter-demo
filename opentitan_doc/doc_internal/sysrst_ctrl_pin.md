# Entity: sysrst_ctrl_pin

- **File**: sysrst_ctrl_pin.sv
## Diagram

![Diagram](sysrst_ctrl_pin.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Description: sysrst_ctrl pin visibility and override Module


## Ports

| Port name                 | Direction | Type                                     | Description                                       |
| ------------------------- | --------- | ---------------------------------------- | ------------------------------------------------- |
| clk_i                     | input     |                                          |                                                   |
| rst_ni                    | input     |                                          |                                                   |
| cio_pwrb_in_i             | input     |                                          |  Raw input signals (not synced to AON clock)      |
| cio_key0_in_i             | input     |                                          |                                                   |
| cio_key1_in_i             | input     |                                          |                                                   |
| cio_key2_in_i             | input     |                                          |                                                   |
| cio_ac_present_i          | input     |                                          |                                                   |
| cio_ec_rst_l_i            | input     |                                          |                                                   |
| cio_lid_open_i            | input     |                                          |                                                   |
| pwrb_out_hw_i             | input     |                                          |  Signals from autoblock (not synced to AON clock) |
| key0_out_hw_i             | input     |                                          |                                                   |
| key1_out_hw_i             | input     |                                          |                                                   |
| key2_out_hw_i             | input     |                                          |                                                   |
| aon_bat_disable_hw_i      | input     |                                          |  Generated signals, running on AON clock          |
| aon_ec_rst_l_hw_i         | input     |                                          |                                                   |
| aon_z3_wakeup_hw_i        | input     |                                          |                                                   |
| aon_pin_allowed_ctl_i     | input     | sysrst_ctrl_reg2hw_pin_allowed_ctl_reg_t |  CSRs synced to AON clock                         |
| aon_pin_out_ctl_i         | input     | sysrst_ctrl_reg2hw_pin_out_ctl_reg_t     |                                                   |
| aon_pin_out_value_i       | input     | sysrst_ctrl_reg2hw_pin_out_value_reg_t   |                                                   |
| pin_in_value_o            | output    | sysrst_ctrl_hw2reg_pin_in_value_reg_t    |  CSRs synced to bus clock                         |
| pwrb_out_int_o            | output    |                                          |  Output signals (not synced to AON clock)         |
| key0_out_int_o            | output    |                                          |                                                   |
| key1_out_int_o            | output    |                                          |                                                   |
| key2_out_int_o            | output    |                                          |                                                   |
| aon_bat_disable_out_int_o | output    |                                          |  Output signals running on AON clock              |
| aon_z3_wakeup_out_int_o   | output    |                                          |                                                   |
| aon_ec_rst_out_int_l_o    | output    |                                          |                                                   |
| aon_flash_wp_out_int_l_o  | output    |                                          |                                                   |
## Signals

| Name         | Type                   | Description |
| ------------ | ---------------------- | ----------- |
| inputs       | logic [NumSignals-1:0] |             |
| outputs      | logic [NumSignals-1:0] |             |
| aon_enabled  | logic [NumSignals-1:0] |             |
| aon_values   | logic [NumSignals-1:0] |             |
| aon_allowed0 | logic [NumSignals-1:0] |             |
| aon_allowed1 | logic [NumSignals-1:0] |             |
## Constants

| Name       | Type | Value | Description           |
| ---------- | ---- | ----- | --------------------- |
| NumSignals | int  | 8     |  Pin override logic.  |
## Instantiations

- u_cfg_ac_present_i_pin: prim_flop_2sync
**Description**
 Synchronize between GPIO and cfg(24MHz)
 Use the raw input values here (not the inverted pass through values)

