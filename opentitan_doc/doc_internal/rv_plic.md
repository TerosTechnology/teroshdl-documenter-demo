# Entity: rv_plic

## Diagram

![Diagram](rv_plic.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 RISC-V Platform-Level Interrupt Controller compliant INTC
   Current version doesn't support MSI interrupt but it is easy to add
   the feature. Create one external register and connect qe signal to the
   gateway module (as edge-triggered)
   Consider to set MAX_PRIO as small number as possible. It is main factor
   of area increase if edge-triggered counter isn't implemented.
 Verilog parameter
   MAX_PRIO: Maximum value of interrupt priority
 
## Generics

| Generic name | Type                  | Value          | Description        |
| ------------ | --------------------- | -------------- | ------------------ |
| NumAlerts    | logic [NumAlerts-1:0] | undefined      |                    |
| SRCW         | int                   | $clog2(NumSrc) | derived parameter  |
## Ports

| Port name  | Direction | Type            | Description                       |
| ---------- | --------- | --------------- | --------------------------------- |
| clk_i      | input     |                 |                                   |
| rst_ni     | input     |                 |                                   |
| tl_i       | input     |                 | Bus Interface (device)            |
| tl_o       | output    |                 |                                   |
| intr_src_i | input     | [NumSrc-1:0]    | Interrupt Sources                 |
| alert_rx_i | input     | [NumAlerts-1:0] | Alerts                            |
| alert_tx_o | output    | [NumAlerts-1:0] |                                   |
| irq_o      | output    | [NumTarget-1:0] | Interrupt notification to targets |
| irq_id_o   | output    | [SRCW-1:0]      |                                   |
| msip_o     | output    | [NumTarget-1:0] |                                   |
## Signals

| Name        | Type                  | Description                            |
| ----------- | --------------------- | -------------------------------------- |
| reg2hw      | rv_plic_reg2hw_t      |                                        |
| hw2reg      | rv_plic_hw2reg_t      |                                        |
| le          | logic [NumSrc-1:0]    | 0:level 1:edge                         |
| ip          | logic [NumSrc-1:0]    |                                        |
| ie          | logic [NumSrc-1:0]    |                                        |
| claim_re    | logic [NumTarget-1:0] | Target read indicator                  |
| claim_id    | logic [SRCW-1:0]      |                                        |
| claim       | logic [NumSrc-1:0]    | Converted from claim_re/claim_id       |
| complete_we | logic [NumTarget-1:0] | Target write indicator                 |
| complete_id | logic [SRCW-1:0]      |                                        |
| complete    | logic [NumSrc-1:0]    | Converted from complete_re/complete_id |
| cc_id       | logic [SRCW-1:0]      | Write ID                               |
| prio        | logic [PRIOW-1:0]     |                                        |
| threshold   | logic [PRIOW-1:0]     |                                        |
| alert_test  | logic [NumAlerts-1:0] |                                        |
| alerts      | logic [NumAlerts-1:0] |                                        |
## Constants

| Name     | Type | Value              | Description        |
| -------- | ---- | ------------------ | ------------------ |
| SRCW     | int  | $clog2(NumSrc)     | derived parameter  |
| MAX_PRIO | int  | 7                  |                    |
| PRIOW    | int  | $clog2(MAX_PRIO+1) |                    |
## Processes
- unnamed: (  )
- unnamed: (  )
## Instantiations

- u_gateway: rv_plic_gateway
- u_reg: rv_plic_reg_top
**Description**
Limitation of register tool prevents the module from having flexibility to parameters
So, signals are manually tied at the top.

