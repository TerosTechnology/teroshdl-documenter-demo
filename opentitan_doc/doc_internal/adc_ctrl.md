# Entity: adc_ctrl
## Diagram
![Diagram](adc_ctrl.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 adc_ctrl module
 
## Generics
| Generic name | Type                  | Value     | Description |
| ------------ | --------------------- | --------- | ----------- |
| NumAlerts    | logic [NumAlerts-1:0] | undefined |             |
## Ports
| Port name            | Direction | Type            | Description |
| -------------------- | --------- | --------------- | ----------- |
| clk_i                | input     |                 |             |
| clk_aon_i            | input     |                 |             |
| rst_ni               | input     |                 |             |
| rst_slow_ni          | input     |                 |             |
| tl_i                 | input     |                 |             |
| tl_o                 | output    |                 |             |
| alert_rx_i           | input     | [NumAlerts-1:0] | Alerts      |
| alert_tx_o           | output    | [NumAlerts-1:0] |             |
| adc_o                | output    |                 |             |
| adc_i                | input     |                 |             |
| intr_debug_cable_o   | output    |                 |             |
| debug_cable_wakeup_o | output    |                 |             |
## Signals
| Name       | Type                  | Description |
| ---------- | --------------------- | ----------- |
| reg2hw     | adc_ctrl_reg2hw_t     |             |
| hw2reg     | adc_ctrl_hw2reg_t     |             |
| alert_test | logic [NumAlerts-1:0] | Alerts      |
| alerts     | logic [NumAlerts-1:0] | Alerts      |
## Instantiations
- u_reg: adc_ctrl_reg_top
**Description**
Register module

- i_adc_ctrl_core: adc_ctrl_core
**Description**
Instantiate DCD core module

