# Package: keymgr_env_pkg

- **File**: keymgr_env_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name   | Type   | Description |
| ------ | ------ | ----------- |
| msg_id | string |             |
## Constants

| Name                  | Type   | Value                                                                                                              | Description           |
| --------------------- | ------ | ------------------------------------------------------------------------------------------------------------------ | --------------------- |
| LIST_OF_ALERTS        | string | {<br><span style="padding-left:20px">"fatal_fault_err",<br><span style="padding-left:20px"> "recov_operation_err"} | parameters and types  |
| uint                  | uint   | 2                                                                                                                  |                       |
| DIGEST_SHARE_WORD_NUM | uint   | keymgr_pkg::KeyWidth / TL_DW                                                                                       |                       |
## Types

| Name          | Type                                                                                                                 | Description |
| ------------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| keymgr_vif    | virtual keymgr_if                                                                                                    |             |
| key_shares_t  | bit [keymgr_pkg::Shares-1:0][keymgr_pkg::KeyWidth-1:0]                                                               |             |
| keymgr_intr_e | enum {<br><span style="padding-left:20px">     IntrOpDone,<br><span style="padding-left:20px">     NumKeyMgrIntr   } |             |
## Functions
- get_next_state <font id="function_arguments">(keymgr_pkg::keymgr_working_state_e current_state)</font> <font id="function_return">return (keymgr_pkg::keymgr_working_state_e)</font>
**Description**
functions
state is incremental, if it's not in defined enum, consider as StDisabled

