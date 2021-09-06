# Entity: aes_ctrl_reg_shadowed

- **File**: aes_ctrl_reg_shadowed.sv
## Diagram

![Diagram](aes_ctrl_reg_shadowed.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 AES shadowed control register

 This module implements the AES shadowed control register. The main differences compared
 to implementing the register as part of the auto-generated aes_reg_top.sv are:

 1. The hardware can block updates to the control register from software.
    Whenever the module is busy, control register writes are ignored.
 2. Invalid values written by software are resolved to valid configurations.

## Generics

| Generic name         | Type | Value | Description |
| -------------------- | ---- | ----- | ----------- |
| AES192Enable         | bit  | 1     |             |
| SecAllowForcingMasks | bit  | 0     |             |
## Ports

| Port name          | Direction | Type                           | Description                    |
| ------------------ | --------- | ------------------------------ | ------------------------------ |
| clk_i              | input     |                                |                                |
| rst_ni             | input     |                                |                                |
| rst_shadowed_ni    | input     |                                |                                |
| qe_o               | output    |                                | software wants to write        |
| we_i               | input     |                                | hardware grants software write |
| operation_o        | output    | aes_op_e                       |                                |
| mode_o             | output    | aes_mode_e                     |                                |
| key_len_o          | output    | key_len_e                      |                                |
| manual_operation_o | output    |                                |                                |
| force_zero_masks_o | output    |                                |                                |
| err_update_o       | output    |                                |  Alerts                        |
| err_storage_o      | output    |                                |                                |
| reg2hw_ctrl_i      | input     | aes_reg2hw_ctrl_shadowed_reg_t |  Bus interface                 |
| hw2reg_ctrl_o      | output    | aes_hw2reg_ctrl_shadowed_reg_t |                                |
## Signals

| Name                         | Type       | Description      |
| ---------------------------- | ---------- | ---------------- |
| ctrl_wd                      | ctrl_reg_t |                  |
| mode                         | aes_mode_e |                  |
| key_len                      | key_len_e  |                  |
| err_update_operation         | logic      |                  |
| err_update_mode              | logic      |                  |
| err_update_key_len           | logic      |                  |
| err_update_manual_operation  | logic      |                  |
| err_update_force_zero_masks  | logic      |                  |
| err_storage_operation        | logic      |                  |
| err_storage_mode             | logic      |                  |
| err_storage_key_len          | logic      |                  |
| err_storage_manual_operation | logic      |                  |
| err_storage_force_zero_masks | logic      |                  |
| unused_force_zero_masks      | logic      |  Unused signals  |
## Processes
- mode_get: (  )
  - **Type:** always_comb
- key_len_get: (  )
  - **Type:** always_comb
## Instantiations

- u_ctrl_reg_shadowed_manual_operation: prim_subreg_shadow
- u_ctrl_reg_shadowed_force_zero_masks: prim_subreg_shadow
