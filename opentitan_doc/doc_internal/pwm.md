# Entity: pwm
## Diagram
![Diagram](pwm.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Generics
| Generic name | Type                  | Value     | Description |
| ------------ | --------------------- | --------- | ----------- |
| NumAlerts    | logic [NumAlerts-1:0] | undefined |             |
## Ports
| Port name    | Direction | Type            | Description |
| ------------ | --------- | --------------- | ----------- |
| clk_i        | input     |                 |             |
| rst_ni       | input     |                 |             |
| clk_core_i   | input     |                 |             |
| rst_core_ni  | input     |                 |             |
| tl_i         | input     |                 |             |
| tl_o         | output    |                 |             |
| alert_rx_i   | input     | [NumAlerts-1:0] |             |
| alert_tx_o   | output    | [NumAlerts-1:0] |             |
| cio_pwm_o    | output    | [NOutputs-1:0]  |             |
| cio_pwm_en_o | output    | [NOutputs-1:0]  |             |
## Signals
| Name         | Type                      | Description                                                |
| ------------ | ------------------------- | ---------------------------------------------------------- |
| unused_regen | logic                     | TODO: Deal with Regen in this block, on TLUL clock domain  |
| reg2hw       | pwm_reg_pkg::pwm_reg2hw_t |                                                            |
| alert_test   | logic [NumAlerts-1:0]     |                                                            |
| alerts       | logic [NumAlerts-1:0]     |                                                            |
## Instantiations
- u_reg: pwm_reg_top
- u_pwm_core: pwm_core
