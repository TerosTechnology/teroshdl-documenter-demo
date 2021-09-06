# Entity: sysrst_ctrl_autoblock

- **File**: sysrst_ctrl_autoblock.sv
## Diagram

![Diagram](sysrst_ctrl_autoblock.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Description sysrst_ctrl PWRB autoblock module

## Ports

| Port name                     | Direction | Type                                             | Description                                                     |
| ----------------------------- | --------- | ------------------------------------------------ | --------------------------------------------------------------- |
| clk_aon_i                     | input     |                                                  |                                                                 |
| rst_aon_ni                    | input     |                                                  |                                                                 |
| aon_pwrb_int_i                | input     |                                                  |  (Optionally) inverted input signals on AON clock               |
| pwrb_int_i                    | input     |                                                  |  (Optionally) inverted input signals (not synced to AON clock)  |
| key0_int_i                    | input     |                                                  |                                                                 |
| key1_int_i                    | input     |                                                  |                                                                 |
| key2_int_i                    | input     |                                                  |                                                                 |
| aon_auto_block_debounce_ctl_i | input     | sysrst_ctrl_reg2hw_auto_block_debounce_ctl_reg_t |  CSRs synced to AON clock                                       |
| aon_auto_block_out_ctl_i      | input     | sysrst_ctrl_reg2hw_auto_block_out_ctl_reg_t      |                                                                 |
| pwrb_out_hw_o                 | output    |                                                  |  Output signals to pin override logic (not synced to AON clock) |
| key0_out_hw_o                 | output    |                                                  |                                                                 |
| key1_out_hw_o                 | output    |                                                  |                                                                 |
| key2_out_hw_o                 | output    |                                                  |                                                                 |
## Signals

| Name            | Type  | Description |
| --------------- | ----- | ----------- |
| aon_ab_cond_met | logic |             |
## Instantiations

- u_ab_fsm: sysrst_ctrl_timerfsm
