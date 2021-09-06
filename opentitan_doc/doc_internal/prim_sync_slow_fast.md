# Entity: prim_sync_slow_fast

- **File**: prim_sync_slow_fast.sv
## Diagram

![Diagram](prim_sync_slow_fast.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Slow to fast clock synchronizer
 This module is designed to be used for efficient sampling of signals from a slow clock to a much
 faster clock.

 The data is captured into flops on the negative edge of the slow clock (when the data should be
 stable). Because the slow clock passes through a two-flop synchronizer, the ratio of clock speeds
 needs to be high to guarantee that the data will be stable when sampled.

 A ratio of at-least 10:1 in clock speeds is recommended.

## Generics

| Generic name | Type         | Value | Description |
| ------------ | ------------ | ----- | ----------- |
| Width        | int unsigned | 32    |             |
## Ports

| Port name   | Direction | Type        | Description |
| ----------- | --------- | ----------- | ----------- |
| clk_slow_i  | input     |             |             |
| clk_fast_i  | input     |             |             |
| rst_fast_ni | input     |             |             |
| wdata_i     | input     | [Width-1:0] | Slow domain |
| rdata_o     | output    | [Width-1:0] | Fast domain |
## Signals

| Name            | Type              | Description |
| --------------- | ----------------- | ----------- |
| sync_clk_slow   | logic             |             |
| sync_clk_slow_q | logic             |             |
| wdata_en        | logic             |             |
| wdata_q         | logic [Width-1:0] |             |
## Processes
- unnamed: ( @(posedge clk_fast_i or negedge rst_fast_ni) )
  - **Type:** always_ff
**Description**
 Register the synchronized clk 
- unnamed: ( @(posedge clk_fast_i or negedge rst_fast_ni) )
  - **Type:** always_ff
**Description**
 Sample the slow data on the negative edge 
## Instantiations

- sync_slow_clk: prim_flop_2sync
**Description**
 Synchronize the slow clock to the fast domain

