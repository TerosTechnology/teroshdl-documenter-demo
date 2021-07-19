# Entity: prim_keccak_fpv

- **File**: prim_keccak_fpv.sv
## Diagram

![Diagram](prim_keccak_fpv.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Testbench module for prim_keccak. Intended to be used with a formal tool.
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| Width        | int  | 1600  |             |
## Ports

| Port name | Direction | Type        | Description |
| --------- | --------- | ----------- | ----------- |
| clk_i     | input     |             |             |
| rst_ni    | input     |             |             |
| valid_i   | input     |             |             |
| state_i   | input     | [Width-1:0] |             |
| done_o    | output    |             |             |
| state_o   | output    | [Width-1:0] |             |
## Signals

| Name     | Type              | Description        |
| -------- | ----------------- | ------------------ |
| round    | logic [RndW-1:0]  |                    |
| active   | logic             |                    |
| state    | logic [Width-1:0] |                    |
| state_d  | logic [Width-1:0] |                    |
| data_0   | logic [1599:0]    | Test with value 0  |
| digest_0 | logic [255:0]     |                    |
## Constants

| Name     | Type | Value              | Description   |
| -------- | ---- | ------------------ | ------------- |
| W        | int  | Width/25           |               |
| L        | int  | $clog2(W)          |               |
| NumRound | int  | 12 + 2*L           | Keccak-f only |
| RndW     | int  | $clog2(NumRound+1) |               |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
- unnamed: (  )
## Instantiations

- u_keccak: prim_keccak
