# Entity: prim_generic_flop_2sync

- **File**: prim_generic_flop_2sync.sv
## Diagram

![Diagram](prim_generic_flop_2sync.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Generic double-synchronizer flop
 This may need to be moved to prim_generic if libraries have a specific cell
 for synchronization

## Generics

| Generic name | Type              | Value | Description |
| ------------ | ----------------- | ----- | ----------- |
| Width        | int               | 16    |             |
| Width        | logic [Width-1:0] | '0    |             |
## Ports

| Port name | Direction | Type        | Description |
| --------- | --------- | ----------- | ----------- |
| clk_i     | input     |             |             |
| rst_ni    | input     |             |             |
| d_i       | input     | [Width-1:0] |             |
| q_o       | output    | [Width-1:0] |             |
## Signals

| Name | Type              | Description |
| ---- | ----------------- | ----------- |
| intq | logic [Width-1:0] |             |
## Instantiations

- u_sync_1: prim_flop
- u_sync_2: prim_flop
