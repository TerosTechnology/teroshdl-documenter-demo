# Entity: nmi_gen

- **File**: nmi_gen.sv
## Diagram

![Diagram](nmi_gen.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 NMI generator. This is a simple helper unit that wraps the escalation signal
 receivers and converts them into interrupts such that they can be tested in system.
 See also alert handler documentation for more context.
 
## Generics

| Generic name | Type         | Value | Description     |
| ------------ | ------------ | ----- | --------------- |
| N_ESC_SEV    | int unsigned | 3     | leave constant  |
## Ports

| Port name     | Direction | Type            | Description            |
| ------------- | --------- | --------------- | ---------------------- |
| clk_i         | input     |                 |                        |
| rst_ni        | input     |                 |                        |
| tl_i          | input     |                 | Bus Interface (device) |
| tl_o          | output    |                 |                        |
| intr_esc0_o   | output    |                 | Interrupt Requests     |
| intr_esc1_o   | output    |                 |                        |
| intr_esc2_o   | output    |                 |                        |
| nmi_rst_req_o | output    |                 | Reset Requests         |
| esc_tx_i      | input     | [N_ESC_SEV-1:0] | Escalation outputs     |
| esc_rx_o      | output    | [N_ESC_SEV-1:0] |                        |
## Signals

| Name   | Type                              | Description |
| ------ | --------------------------------- | ----------- |
| esc_en | logic [N_ESC_SEV-1:0]             |             |
| reg2hw | nmi_gen_reg_pkg::nmi_gen_reg2hw_t |             |
| hw2reg | nmi_gen_reg_pkg::nmi_gen_hw2reg_t |             |
## Constants

| Name      | Type         | Value | Description     |
| --------- | ------------ | ----- | --------------- |
| N_ESC_SEV | int unsigned | 3     | leave constant  |
## Instantiations

- u_reg: nmi_gen_reg_top
- i_intr_esc0: prim_intr_hw
- i_intr_esc1: prim_intr_hw
- i_intr_esc2: prim_intr_hw
