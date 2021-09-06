# Entity: adc_ctrl_core

- **File**: adc_ctrl_core.sv
## Diagram

![Diagram](adc_ctrl_core.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 adc_ctrl core module

## Ports

| Port name            | Direction | Type                                  | Description                                |
| -------------------- | --------- | ------------------------------------- | ------------------------------------------ |
| clk_aon_i            | input     |                                       | Always-on 200KHz clock(logic)              |
| rst_aon_ni           | input     |                                       | power-on reset for the 200KHz clock(logic) |
| clk_i                | input     |                                       | regular core clock for SW config interface |
| rst_ni               | input     |                                       | power-on hardware reset                    |
| reg2hw_i             | input     | adc_ctrl_reg2hw_t                     |  register interface inputs                 |
| intr_state_o         | output    | adc_ctrl_hw2reg_intr_state_reg_t      |  register interface outputs                |
| adc_chn_val_o        | output    | [NumAdcChannel-1:0]                   |                                            |
| adc_intr_status_o    | output    | adc_ctrl_hw2reg_adc_intr_status_reg_t |                                            |
| aon_filter_status_o  | output    | adc_ctrl_hw2reg_filter_status_reg_t   |                                            |
| debug_cable_wakeup_o | output    |                                       |  interrupt and wakeup outputs              |
| intr_debug_cable_o   | output    |                                       |                                            |
| adc_i                | input     |                                       |  adc interface                             |
| adc_o                | output    |                                       |                                            |
## Signals

| Name             | Type                                               | Description                                                                                                                                                                                 |
| ---------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| chn0_val_we      | logic                                              | write enable for the latest ADC sample                                                                                                                                                      |
| chn1_val_we      | logic                                              | write enable for the latest ADC sample                                                                                                                                                      |
| chn0_val         | logic [9:0]                                        |                                                                                                                                                                                             |
| chn1_val         | logic [9:0]                                        |                                                                                                                                                                                             |
| chn0_match       | logic [NumAdcFilter-1:0]                           |                                                                                                                                                                                             |
| chn1_match       | logic [NumAdcFilter-1:0]                           |                                                                                                                                                                                             |
| match            | logic [NumAdcFilter-1:0]                           |                                                                                                                                                                                             |
| match_pulse      | logic [NumAdcFilter-1:0]                           |                                                                                                                                                                                             |
| adc_ctrl_done    | logic                                              | write enable for the ADC sample when the interrupt is triggered                                                                                                                             |
| oneshot_done     | logic                                              | write enable for the ADC sample when the interrupt is triggered                                                                                                                             |
| aon_filter_ctl   | filter_ctl_t [NumAdcChannel-1:0][NumAdcFilter-1:0] |                                                                                                                                                                                             |
| chn_val_intr_we  | logic                                              |  Interrupt based adc channel values  The value of the adc is captured whenever an interrupt triggers.  There are two cases:  completion of one shot mode  match detection from the filters  |
| cfg_oneshot_done | logic                                              |  synchronzie from clk_aon into cfg domain                                                                                                                                                   |
| unused_cfgs      | logic                                              |  unused register inputs                                                                                                                                                                     |
## Types

| Name         | Type                                                                                                                                                                                                                                                                                | Description                          |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| filter_ctl_t | struct packed {<br><span style="padding-left:20px">     logic [9:0] min_v;<br><span style="padding-left:20px">     logic [9:0] max_v;<br><span style="padding-left:20px">     logic cond;<br><span style="padding-left:20px">     logic en;<br><span style="padding-left:20px">   } |  Pack channel 0/1 into one variable  |
## Instantiations

- u_adc_ctrl_fsm: adc_ctrl_fsm
**Description**
instantiate the main state machine

- u_oneshot_done_sync: prim_pulse_sync
- u_adc_ctrl_intr: adc_ctrl_intr
**Description**
Instantiate the interrupt module

