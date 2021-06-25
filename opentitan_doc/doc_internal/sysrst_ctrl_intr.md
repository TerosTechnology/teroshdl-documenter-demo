# Entity: sysrst_ctrl_intr
## Diagram
![Diagram](sysrst_ctrl_intr.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description: sysrst_ctrl interrupt Module
 
## Ports
| Port name              | Direction | Type                                 | Description |
| ---------------------- | --------- | ------------------------------------ | ----------- |
| clk_i                  | input     |                                      |             |
| rst_ni                 | input     |                                      |             |
| sysrst_ctrl_combo_intr | input     |                                      |             |
| sysrst_ctrl_key_intr   | input     |                                      |             |
| intr_state_i           | input     | sysrst_ctrl_reg2hw_intr_state_reg_t  |             |
| intr_enable_i          | input     | sysrst_ctrl_reg2hw_intr_enable_reg_t |             |
| intr_test_i            | input     | sysrst_ctrl_reg2hw_intr_test_reg_t   |             |
| intr_state_o           | output    | sysrst_ctrl_hw2reg_intr_state_reg_t  |             |
| sysrst_ctrl_intr_o     | output    |                                      |             |
## Signals
| Name              | Type  | Description |
| ----------------- | ----- | ----------- |
| sysrst_ctrl_event | logic |             |
## Instantiations
- i_sysrst_ctrl_intr_o: prim_intr_hw
**Description**
instantiate interrupt hardware primitive

