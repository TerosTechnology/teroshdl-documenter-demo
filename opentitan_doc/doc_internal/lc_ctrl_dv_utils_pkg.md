# Package: lc_ctrl_dv_utils_pkg

- **File**: lc_ctrl_dv_utils_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name              | Type           | Description                                                                |
| ----------------- | -------------- | -------------------------------------------------------------------------- |
| VALID_NEXT_STATES | dec_lc_state_e | associative array cannot declare parameter here, so we used const instead  |
## Functions
- dec_lc_state <font id="function_arguments">(lc_state_e curr_state)</font> <font id="function_return">return (dec_lc_state_e)</font>
- encode_lc_state <font id="function_arguments">(dec_lc_state_e curr_state)</font> <font id="function_return">return (lc_state_e)</font>
- dec_lc_cnt <font id="function_arguments">(lc_cnt_e curr_cnt)</font> <font id="function_return">return (int)</font>
