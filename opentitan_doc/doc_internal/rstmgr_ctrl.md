# Entity: rstmgr_ctrl

## Diagram

![Diagram](rstmgr_ctrl.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 This module implements generic reset controls
 
## Ports

| Port name     | Direction | Type               | Description  |
| ------------- | --------- | ------------------ | ------------ |
| clk_i         | input     |                    |              |
| rst_ni        | input     |                    |              |
| rst_req_i     | input     | [PowerDomains-1:0] |              |
| rst_parent_ni | input     | [PowerDomains-1:0] | parent reset |
| rst_no        | output    | [PowerDomains-1:0] |              |
| scanmode_i    | input     |                    |              |
| scan_rst_ni   | input     |                    |              |
## Signals

| Name              | Type                     | Description                                                                                              |
| ----------------- | ------------------------ | -------------------------------------------------------------------------------------------------------- |
| rst_aon_n_premux  | logic                    | the always on root reset                                                                                 |
| rst_aon_n         | logic                    | the always on root reset                                                                                 |
| rst_pd_nd         | logic [OffDomains-1:0]   | the remaining resets                                                                                     |
| rst_pd_nq         | logic [OffDomains-1:0]   | the remaining resets                                                                                     |
| rst_parent_synced | logic [PowerDomains-1:0] | Parent resets may assert asynchronously, so we need to sync before using it as part of the control path  |
## Constants

| Name             | Type | Value            | Description |
| ---------------- | ---- | ---------------- | ----------- |
| DomainPdStartIdx | int  | DomainAonSel + 1 |             |
## Instantiations

- u_lc: prim_flop_2sync
- u_aon_rst: prim_flop
**Description**
always on handling

- u_rst_aon_mux: prim_clock_mux2
