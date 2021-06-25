# Entity: gpio
## Diagram
![Diagram](gpio.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 General Purpose Input/Output module
 
## Generics
| Generic name | Type                  | Value     | Description |
| ------------ | --------------------- | --------- | ----------- |
| NumAlerts    | logic [NumAlerts-1:0] | undefined |             |
## Ports
| Port name     | Direction | Type            | Description   |
| ------------- | --------- | --------------- | ------------- |
| clk_i         | input     |                 |               |
| rst_ni        | input     |                 |               |
| tl_i          | input     |                 | Bus interface |
| tl_o          | output    |                 |               |
| intr_gpio_o   | output    | [31:0]          | Interrupts    |
| alert_rx_i    | input     | [NumAlerts-1:0] | Alerts        |
| alert_tx_o    | output    | [NumAlerts-1:0] |               |
| cio_gpio_i    | input     | [31:0]          | GPIOs         |
| cio_gpio_o    | output    | [31:0]          |               |
| cio_gpio_en_o | output    | [31:0]          |               |
## Signals
| Name                | Type                  | Description                                                  |
| ------------------- | --------------------- | ------------------------------------------------------------ |
| reg2hw              | gpio_reg2hw_t         |                                                              |
| hw2reg              | gpio_hw2reg_t         |                                                              |
| cio_gpio_q          | logic [31:0]          |                                                              |
| cio_gpio_en_q       | logic [31:0]          |                                                              |
| data_in_d           | logic [31:0]          | possibly filter the input based upon register configuration  |
| else                | end                   |                                                              |
| assign              | end                   |                                                              |
| cio_gpio_en_q       | hw2reg                |                                                              |
| else                | end                   |                                                              |
| logic [31:0]        | end                   |                                                              |
| event_intr_rise     | logic [31:0]          |                                                              |
| event_intr_fall     | logic [31:0]          |                                                              |
| event_intr_actlow   | logic [31:0]          |                                                              |
| event_intr_acthigh  | logic [31:0]          |                                                              |
| event_intr_combined | logic [31:0]          |                                                              |
| alert_test          | logic [NumAlerts-1:0] | Alerts                                                       |
| alerts              | logic [NumAlerts-1:0] | Alerts                                                       |
## Processes
- unnamed: _( @(posedge clk_i) )_

## Instantiations
- intr_hw: prim_intr_hw
**Description**
instantiate interrupt hardware primitive

- u_reg: gpio_reg_top
**Description**
Register module

