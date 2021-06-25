# Entity: rv_plic_gateway
## Diagram
![Diagram](rv_plic_gateway.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 RISC-V Platform-Level Interrupt Gateways module
 
## Generics
| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| N_SOURCE     | int  | 32    |             |
## Ports
| Port name  | Direction | Type           | Description          |
| ---------- | --------- | -------------- | -------------------- |
| clk_i      | input     |                |                      |
| rst_ni     | input     |                |                      |
| src_i      | input     | [N_SOURCE-1:0] |                      |
| le_i       | input     | [N_SOURCE-1:0] | Level0 Edge1         |
| claim_i    | input     | [N_SOURCE-1:0] | $onehot0(claim_i)    |
| complete_i | input     | [N_SOURCE-1:0] | $onehot0(complete_i) |
| ip_o       | output    | [N_SOURCE-1:0] |                      |
## Signals
| Name  | Type                 | Description                            |
| ----- | -------------------- | -------------------------------------- |
| ia    | logic [N_SOURCE-1:0] | Interrupt Active                       |
| set   | logic [N_SOURCE-1:0] | Set: (le_i) ? src_i & ~src_q : src_i ; |
| src_q | logic [N_SOURCE-1:0] |                                        |
## Processes
- unnamed: _( @(posedge clk_i or negedge rst_ni) )_

- unnamed: _(  )_

- unnamed: _( @(posedge clk_i or negedge rst_ni) )_
Interrupt pending is set by source (depends on le_i), cleared by claim_i.
Until interrupt is claimed, set doesn't affect ip_o.
RISC-V PLIC spec mentioned it can have counter for edge triggered
But skipped the feature as counter consumes substantial logic size.

**Description**
Interrupt pending is set by source (depends on le_i), cleared by claim_i.
Until interrupt is claimed, set doesn't affect ip_o.
RISC-V PLIC spec mentioned it can have counter for edge triggered
But skipped the feature as counter consumes substantial logic size.

- unnamed: _( @(posedge clk_i or negedge rst_ni) )_
Interrupt active is to control ip_o. If ip_o is set then until completed
by target, ip_o shouldn't be set by source even claim_i can clear ip_o.
ia can be cleared only when ia was set. If `set` and `complete_i` happen
at the same time, always `set` wins.

**Description**
Interrupt active is to control ip_o. If ip_o is set then until completed
by target, ip_o shouldn't be set by source even claim_i can clear ip_o.
ia can be cleared only when ia was set. If `set` and `complete_i` happen
at the same time, always `set` wins.

