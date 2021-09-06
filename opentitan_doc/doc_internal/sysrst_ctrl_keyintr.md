# Entity: sysrst_ctrl_keyintr

- **File**: sysrst_ctrl_keyintr.sv
## Diagram

![Diagram](sysrst_ctrl_keyintr.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Description: sysrst_ctrl key-triggered interrupt Module


## Ports

| Port name               | Direction | Type                                           | Description                                       |
| ----------------------- | --------- | ---------------------------------------------- | ------------------------------------------------- |
| clk_i                   | input     |                                                |                                                   |
| rst_ni                  | input     |                                                |                                                   |
| pwrb_int_i              | input     |                                                |  (Optionally) inverted input signals on AON clock |
| key0_int_i              | input     |                                                |                                                   |
| key1_int_i              | input     |                                                |                                                   |
| key2_int_i              | input     |                                                |                                                   |
| ac_present_int_i        | input     |                                                |                                                   |
| ec_rst_l_int_i          | input     |                                                |                                                   |
| key_intr_ctl_i          | input     | sysrst_ctrl_reg2hw_key_intr_ctl_reg_t          |  CSRs synced to AON clock                         |
| key_intr_debounce_ctl_i | input     | sysrst_ctrl_reg2hw_key_intr_debounce_ctl_reg_t |                                                   |
| key_intr_status_o       | output    | sysrst_ctrl_hw2reg_key_intr_status_reg_t       |                                                   |
| sysrst_ctrl_key_intr_o  | output    |                                                |  IRQ running on bus clock                         |
## Signals

| Name          | Type                   | Description |
| ------------- | ---------------------- | ----------- |
| triggers      | logic [NumKeyIntr-1:0] |             |
| l2h_en        | logic [NumKeyIntr-1:0] |             |
| h2l_en        | logic [NumKeyIntr-1:0] |             |
| l2h_met_pulse | logic [NumKeyIntr-1:0] |             |
| h2l_met_pulse | logic [NumKeyIntr-1:0] |             |
## Constants

| Name       | Type | Value | Description |
| ---------- | ---- | ----- | ----------- |
| NumKeyIntr | int  | 6     |             |
