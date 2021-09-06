# Entity: prim_xilinx_flop_en

- **File**: prim_xilinx_flop_en.sv
## Diagram

![Diagram](prim_xilinx_flop_en.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

## Generics

| Generic name | Type              | Value | Description |
| ------------ | ----------------- | ----- | ----------- |
| Width        | int               | 1     |             |
| Width        | logic [Width-1:0] | 0     |             |
## Ports

| Port name | Direction | Type        | Description |
| --------- | --------- | ----------- | ----------- |
| clk_i     | input     |             |             |
| rst_ni    | input     |             |             |
| en_i      | input     |             |             |
| d_i       | input     | [Width-1:0] |             |
| q_o       | output    | [Width-1:0] |             |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
