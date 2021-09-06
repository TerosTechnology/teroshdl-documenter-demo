# Entity: rv_core_addr_trans

- **File**: rv_core_addr_trans.sv
## Diagram

![Diagram](rv_core_addr_trans.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
*

## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| AddrWidth    | int  | 32    |             |
| NumRegions   | int  | 2     |             |
## Ports

| Port name    | Direction | Type             | Description |
| ------------ | --------- | ---------------- | ----------- |
| clk_i        | input     |                  |             |
| rst_ni       | input     |                  |             |
| region_cfg_i | input     | [NumRegions-1:0] |             |
| addr_i       | input     | [AddrWidth-1:0]  |             |
| addr_o       | output    | [AddrWidth-1:0]  |             |
## Signals

| Name         | Type                                  | Description                                      |
| ------------ | ------------------------------------- | ------------------------------------------------ |
| region_ctrls | region_ctrls_t                        |                                                  |
| input_masks  | logic [NumRegions-1:0][AddrWidth-1:0] |                                                  |
| all_matches  | logic [NumRegions-1:0]                |                                                  |
| sel_match    | logic                                 |                                                  |
| sel_region   | region_ctrls_t                        |                                                  |
| unused_clk   | logic                                 |  unused clock/reset, only needed for assertions  |
| unused_rst_n | logic                                 |                                                  |
## Types

| Name           | Type                                                                                                                                                                                                         | Description |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| region_ctrls_t | struct packed {<br><span style="padding-left:20px">     logic [AddrWidth-1:0] output_mask;<br><span style="padding-left:20px">     logic [AddrWidth-1:0] remap_addr;<br><span style="padding-left:20px">   } |             |
