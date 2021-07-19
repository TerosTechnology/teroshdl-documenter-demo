# Package: uvm_pkg

- **File**: rom_ctrl_cov_if.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Implements functional coverage for rom_ctrl
 

## Signals

| Name             | Type                   | Description                                                 |
| ---------------- | ---------------------- | ----------------------------------------------------------- |
| en_full_cov      | bit                    |                                                             |
| en_intg_cov      | bit                    |                                                             |
| rom_ctrl_kmac_cg | covergroup             |                                                             |
| name             | option                 |                                                             |
| comment          | option                 |                                                             |
| per_instance     | option                 |                                                             |
| zero_delay_5     | cp_kmac_ready          | Cover some basic stalling behavior on the kmac ready input  |
| stall_1          | bins                   |                                                             |
| stall_long       | bins                   |                                                             |
| name             | option                 |                                                             |
| comment          | option                 |                                                             |
| per_instance     | option                 |                                                             |
| a_valid          | cp_rom_req_check       | Cover rom requests around the time of check completion      |
| req_before_done  | cp_rom_req_check       | Cover rom requests around the time of check completion      |
| req_and_done     | bins                   |                                                             |
| req_after_done   | bins                   |                                                             |
| name             | option                 |                                                             |
| comment          | option                 |                                                             |
| per_instance     | option                 |                                                             |
| check_pass       | cp_rom_check_condition | Cover the check pass and fail case                          |
| check_fail       | bins                   |                                                             |
