# Entity: rv_core_ibex_peri

- **File**: rv_core_ibex_peri.sv
## Diagram

![Diagram](rv_core_ibex_peri.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 RV core ibex peripheral
 
## Generics

| Generic name | Type                  | Value     | Description |
| ------------ | --------------------- | --------- | ----------- |
| NumAlerts    | logic [NumAlerts-1:0] | undefined |             |
## Ports

| Port name          | Direction | Type             | Description                    |
| ------------------ | --------- | ---------------- | ------------------------------ |
| clk_i              | input     |                  |                                |
| rst_ni             | input     |                  |                                |
| tl_i               | input     |                  | Bus Interface                  |
| tl_o               | output    |                  |                                |
| fatal_intg_event_i | input     | alert_event_t    | alert events from rv_core_ibex |
| fatal_core_event_i | input     | alert_event_t    |                                |
| recov_core_event_i | input     | alert_event_t    |                                |
| ibus_region_cfg_o  | output    | [NumRegions-1:0] | region configuration to ibex   |
| dbus_region_cfg_o  | output    | [NumRegions-1:0] |                                |
| alert_rx_i         | input     | [NumAlerts-1:0]  | interrupts and alerts          |
| alert_tx_o         | output    | [NumAlerts-1:0]  |                                |
## Signals

| Name           | Type                       | Description |
| -------------- | -------------------------- | ----------- |
| reg2hw         | rv_core_ibex_peri_reg2hw_t |             |
| hw2reg         | rv_core_ibex_peri_hw2reg_t |             |
| intg_err       | logic                      |             |
| fatal_intg_err | logic                      |             |
| fatal_core_err | logic                      |             |
| recov_core_err | logic                      |             |
| alert_test     | logic [NumAlerts-1:0]      |             |
| alert_events   | logic [NumAlerts-1:0]      |             |
## Constants

| Name       | Type                | Value     | Description |
| ---------- | ------------------- | --------- | ----------- |
| AlertFatal | bit [NumAlerts-1:0] | undefined |             |
## Instantiations

- u_reg: rv_core_ibex_peri_reg_top
