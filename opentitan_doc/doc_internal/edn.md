# Entity: edn

- **File**: edn.sv
## Diagram

![Diagram](edn.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description: edn top level wrapper file
 
## Generics

| Generic name | Type                  | Value         | Description |
| ------------ | --------------------- | ------------- | ----------- |
| NumEndPoints | int                   | 7             |             |
| NumAlerts    | logic [NumAlerts-1:0] | undefined     |             |
| BootInsCmd   | int                   | 32'h0000_0001 |             |
| BootGenCmd   | int                   | 32'h00ff_f003 |             |
## Ports

| Port name               | Direction | Type               | Description                 |
| ----------------------- | --------- | ------------------ | --------------------------- |
| clk_i                   | input     |                    |                             |
| rst_ni                  | input     |                    |                             |
| tl_i                    | input     |                    | Tilelink Bus registers      |
| tl_o                    | output    |                    |                             |
| edn_i                   | input     | [NumEndPoints-1:0] | EDN interfaces              |
| edn_o                   | output    | [NumEndPoints-1:0] |                             |
| csrng_cmd_o             | output    |                    | CSRNG Application Interface |
| csrng_cmd_i             | input     |                    |                             |
| alert_rx_i              | input     | [NumAlerts-1:0]    | Alerts                      |
| alert_tx_o              | output    | [NumAlerts-1:0]    |                             |
| intr_edn_cmd_req_done_o | output    |                    | Interrupts                  |
| intr_edn_fatal_err_o    | output    |                    |                             |
## Signals

| Name           | Type         | Description |
| -------------- | ------------ | ----------- |
| reg2hw         | edn_reg2hw_t |             |
| hw2reg         | edn_hw2reg_t |             |
| alert          | logic        |             |
| alert_test     | logic        |             |
| intg_err_alert | logic        |             |
## Instantiations

- u_reg: edn_reg_top
- u_edn_core: edn_core
- u_prim_alert_sender: prim_alert_sender
