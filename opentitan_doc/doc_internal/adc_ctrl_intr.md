# Entity: adc_ctrl_intr
## Diagram
![Diagram](adc_ctrl_intr.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description: adc_ctrl interrupt Module
 
## Ports
| Port name            | Direction | Type                                    | Description |
| -------------------- | --------- | --------------------------------------- | ----------- |
| clk_i                | input     |                                         |             |
| rst_ni               | input     |                                         |             |
| clk_aon_i            | input     |                                         |             |
| rst_slow_ni          | input     |                                         |             |
| cfg_wakeup_en        | input     | [NumAdcFilter-1:0]                      |             |
| cfg_intr_en          | input     | [NumAdcFilter-1:0]                      |             |
| cfg_oneshot_intr_en  | input     |                                         |             |
| adc_ctrl_match_pulse | input     | [NumAdcFilter-1:0]                      |             |
| cfg_oneshot_done     | input     |                                         |             |
| intr_state_i         | input     | adc_ctrl_reg2hw_intr_state_reg_t        |             |
| intr_enable_i        | input     | adc_ctrl_reg2hw_intr_enable_reg_t       |             |
| intr_test_i          | input     | adc_ctrl_reg2hw_intr_test_reg_t         |             |
| intr_state_o         | output    | adc_ctrl_hw2reg_intr_state_reg_t        |             |
| adc_intr_status_o    | output    | adc_ctrl_hw2reg_adc_intr_status_reg_t   |             |
| adc_wakeup_status_o  | output    | adc_ctrl_hw2reg_adc_wakeup_status_reg_t |             |
| debug_cable_wakeup_o | output    |                                         |             |
| intr_debug_cable_o   | output    |                                         |             |
## Signals
| Name                    | Type                     | Description |
| ----------------------- | ------------------------ | ----------- |
| cfg_adc_ctrl_match_done | logic [NumAdcFilter-1:0] |             |
| adc_ctrl_event          | logic                    |             |
## Instantiations
- i_cc_sink_det: prim_pulse_sync
- i_cc_1a5_sink_det: prim_pulse_sync
- i_cc_3a0_sink_det: prim_pulse_sync
- i_cc_src_det: prim_pulse_sync
- i_cc_1a5_src_det: prim_pulse_sync
- i_cc_src_det_flip: prim_pulse_sync
- i_cc_1a5_src_det_flip: prim_pulse_sync
- i_cc_discon: prim_pulse_sync
- i_adc_ctrl_intr_o: prim_intr_hw
**Description**
instantiate interrupt hardware primitive

