# Entity: adc_ctrl

- **File**: adc_ctrl.sv
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

| Port name            | Direction | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------- | --------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| clk_i                | input     |                 | regular core clock for SW config interface                                                                                                                                                                                                                                                                                                                                                                         |
| clk_aon_i            | input     |                 | always-on slow clock for internal logic                                                                                                                                                                                                                                                                                                                                                                            |
| rst_ni               | input     |                 | power-on hardware reset                                                                                                                                                                                                                                                                                                                                                                                            |
| rst_aon_ni           | input     |                 | power-on reset for the 200KHz clock(logic)                                                                                                                                                                                                                                                                                                                                                                         |
| tl_i                 | input     |                 | Regster interface                                                                                                                                                                                                                                                                                                                                                                                                  |
| tl_o                 | output    |                 |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| alert_rx_i           | input     | [NumAlerts-1:0] |  Alerts                                                                                                                                                                                                                                                                                                                                                                                                            |
| alert_tx_o           | output    | [NumAlerts-1:0] |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| adc_o                | output    |                 |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| adc_i                | input     |                 |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| intr_debug_cable_o   | output    |                 | Inter-module IOAST interface input  [9:0] adc_d, ADC voltage level, each step is 2.148mV(2200mV/1024). It covers 0-2.2V input  adc_d_val,//Valid bit(pulse) for adc_d output logic adc_pd,//Power down ADC(used in deep sleep mode to save power) output logic [1:0] adc_chnsel, channel select for ADC; 2'b0 means stop, 2'b01 means first channel, 2'b10 means second channel, 2'b11 ilegal interrupt interface  |
| debug_cable_wakeup_o | output    |                 |  Debug cable is detected(attached or disconnected); raise the interrupt to CPUpwrmgr interface                                                                                                                                                                                                                                                                                                                     |
## Signals

| Name       | Type                  | Description |
| ---------- | --------------------- | ----------- |
| reg2hw     | adc_ctrl_reg2hw_t     |             |
| hw2reg     | adc_ctrl_hw2reg_t     |             |
| alert_test | logic [NumAlerts-1:0] |  Alerts     |
| alerts     | logic [NumAlerts-1:0] |  Alerts     |
## Instantiations

- u_reg: adc_ctrl_reg_top
**Description**
 Register module

- u_adc_ctrl_core: adc_ctrl_core
**Description**
 Instantiate DCD core module

