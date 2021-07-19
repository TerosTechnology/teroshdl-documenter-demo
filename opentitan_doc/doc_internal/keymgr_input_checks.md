# Entity: keymgr_input_checks

- **File**: keymgr_input_checks.sv
## Diagram

![Diagram](keymgr_input_checks.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Key manager input checks
 Checks input data for errors
 We should also check for input validity
 
## Ports

| Port name          | Direction | Type                      | Description |
| ------------------ | --------- | ------------------------- | ----------- |
| max_key_versions_i | input     | [2**StageWidth-1:0][31:0] |             |
| stage_sel_i        | input     | keymgr_stage_e            |             |
| key_i              | input     | hw_key_req_t              |             |
| key_version_i      | input     | [31:0]                    |             |
| creator_seed_i     | input     | [KeyWidth-1:0]            |             |
| owner_seed_i       | input     | [KeyWidth-1:0]            |             |
| devid_i            | input     | [DevIdWidth-1:0]          |             |
| health_state_i     | input     | [HealthStateWidth-1:0]    |             |
| creator_seed_vld_o | output    |                           |             |
| owner_seed_vld_o   | output    |                           |             |
| devid_vld_o        | output    |                           |             |
| health_state_vld_o | output    |                           |             |
| key_version_vld_o  | output    |                           |             |
| key_vld_o          | output    |                           |             |
## Signals

| Name                | Type                             | Description         |
| ------------------- | -------------------------------- | ------------------- |
| cur_max_key_version | logic [31:0]                     |                     |
| creator_seed_padded | logic [MaxWidth-1:0]             | general data check  |
| owner_seed_padded   | logic [MaxWidth-1:0]             | general data check  |
| devid_padded        | logic [MaxWidth-1:0]             | general data check  |
| health_state_padded | logic [MaxWidth-1:0]             | general data check  |
| unused_key_vld      | logic                            | key check           |
| key_padded          | logic [Shares-1:0][MaxWidth-1:0] |                     |
| key_chk             | logic [Shares-1:0]               |                     |
## Functions
- valid_chk <font id="function_arguments">(logic [MaxWidth-1:0])</font> <font id="function_return">return (logic)</font>
**Description**
checks for all 0's or all 1's of value

## Instantiations

- u_creator_seed: prim_msb_extend
- u_owner_seed: prim_msb_extend
- u_devid: prim_msb_extend
- u_health_state: prim_msb_extend
