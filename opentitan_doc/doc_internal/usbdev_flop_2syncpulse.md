# Entity: usbdev_flop_2syncpulse
## Diagram
![Diagram](usbdev_flop_2syncpulse.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Generic double-synchronizer flop followed by pulse generation
 
## Generics
| Generic name | Type         | Value | Description |
| ------------ | ------------ | ----- | ----------- |
| Width        | int unsigned | 16    |             |
## Ports
| Port name | Direction | Type        | Description   |
| --------- | --------- | ----------- | ------------- |
| clk_i     | input     |             | receive clock |
| rst_ni    | input     |             |               |
| d_i       | input     | [Width-1:0] |               |
| q_o       | output    | [Width-1:0] |               |
## Signals
| Name     | Type              | Description                    |
| -------- | ----------------- | ------------------------------ |
| d_sync   | logic [Width-1:0] | double-flop synchronizer cell  |
| d_sync_q | logic [Width-1:0] | delay d_sync by 1 cycle        |
## Processes
- unnamed: _( @(posedge clk_i or negedge rst_ni) )_

## Instantiations
- prim_flop_2sync: prim_flop_2sync
