# Package: uvm_pkg

- **File**: aes_cov_if.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Implements functional coverage for AES
 

## Signals

| Name        | Type | Description |
| ----------- | ---- | ----------- |
| en_full_cov | bit  |             |
| en_intg_cov | bit  |             |
## Functions
- sample <font id="function_arguments">(bit                                 aes_op,<br><span style="padding-left:20px">)</font> <font id="function_return">return ()</font>
- cg_status_sample <font id="function_arguments">(bit [31:0])</font> <font id="function_return">return (void)</font>
- cg_trigger_sample <font id="function_arguments">(bit aes_start,<br><span style="padding-left:20px">)</font> <font id="function_return">return (void)</font>
- cg_alert_test_sample <font id="function_arguments">(bit [31:0])</font> <font id="function_return">return (void)</font>
