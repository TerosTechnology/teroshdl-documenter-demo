# Entity: keymgr_sideload_key
## Diagram
![Diagram](keymgr_sideload_key.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Key manager sideload key
 
## Ports
| Port name | Direction | Type                        | Description |
| --------- | --------- | --------------------------- | ----------- |
| clk_i     | input     |                             |             |
| rst_ni    | input     |                             |             |
| en_i      | input     |                             |             |
| set_en_i  | input     |                             |             |
| set_i     | input     |                             |             |
| clr_i     | input     |                             |             |
| entropy_i | input     | [Shares-1:0][RandWidth-1:0] |             |
| key_i     | input     | [Shares-1:0][KeyWidth-1:0]  |             |
| key_o     | output    | hw_key_req_t                |             |
## Signals
| Name    | Type                             | Description |
| ------- | -------------------------------- | ----------- |
| valid_q | logic                            |             |
| key_q   | logic [Shares-1:0][KeyWidth-1:0] |             |
## Constants
| Name          | Type | Value         | Description |
| ------------- | ---- | ------------- | ----------- |
| EntropyCopies | int  | KeyWidth / 32 |             |
## Processes
- unnamed: _( @(posedge clk_i or negedge rst_ni) )_

- unnamed: _( @(posedge clk_i) )_

