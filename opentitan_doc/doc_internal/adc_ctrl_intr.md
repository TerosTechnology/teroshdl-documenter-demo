# Entity: adc_ctrl_intr

- **File**: adc_ctrl_intr.sv
## Diagram

![Diagram](adc_ctrl_intr.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Description: adc_ctrl interrupt Module


## Ports

| Port name           | Direction | Type                                  | Description |
| ------------------- | --------- | ------------------------------------- | ----------- |
| clk_i               | input     |                                       |             |
| rst_ni              | input     |                                       |             |
| aon_filter_status_i | input     | [NumAdcFilter-1:0]                    |             |
| cfg_intr_en_i       | input     | [8:0]                                 |             |
| cfg_oneshot_done_i  | input     |                                       |             |
| intr_state_i        | input     | adc_ctrl_reg2hw_intr_state_reg_t      |             |
| intr_enable_i       | input     | adc_ctrl_reg2hw_intr_enable_reg_t     |             |
| intr_test_i         | input     | adc_ctrl_reg2hw_intr_test_reg_t       |             |
| intr_state_o        | output    | adc_ctrl_hw2reg_intr_state_reg_t      |             |
| adc_intr_status_o   | output    | adc_ctrl_hw2reg_adc_intr_status_reg_t |             |
| intr_debug_cable_o  | output    |                                       |             |
## Signals

| Name               | Type                     | Description                                      |
| ------------------ | ------------------------ | ------------------------------------------------ |
| cfg_filter_status  | logic [NumAdcFilter-1:0] |  synchronize status into appropriate interrupts  |
| filter_match_event | logic [NumAdcFilter-1:0] |                                                  |
| intr_events        | logic [8:0]              | Qualify each bit with intr_en                    |
| adc_ctrl_event     | logic                    |                                                  |
## Instantiations

- i_adc_ctrl_intr_o: prim_intr_hw
**Description**
 instantiate interrupt hardware primitive

