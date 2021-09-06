# Entity: flash_phy_rd_buffers

- **File**: flash_phy_rd_buffers.sv
## Diagram

![Diagram](flash_phy_rd_buffers.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Flash Phy Read Buffers

 This module implements the read buffers
 These buffers are straightforward flip flop storage.
 There are 3 inputs, alloc, upate and wipe.

 Alloc happens when a buffer is allocated, the state transitions to WIP.

 Update happens when a buffer has already been allocated, and is now being updated with data, the
 state transitions to VALID.

 Wipe happens when a buffer is wiped due to a program being issued to the same location, the
 state transitions to INVALID

 Basically...this is a tag ram + data ram combined into one


## Ports

| Port name  | Direction | Type                 | Description |
| ---------- | --------- | -------------------- | ----------- |
| clk_i      | input     |                      |             |
| rst_ni     | input     |                      |             |
| en_i       | input     |                      |             |
| alloc_i    | input     |                      |             |
| update_i   | input     |                      |             |
| wipe_i     | input     |                      |             |
| addr_i     | input     | [BankAddrW-1:0]      |             |
| part_i     | input     |                      |             |
| info_sel_i | input     | [InfoTypesWidth-1:0] |             |
| data_i     | input     | [DataWidth-1:0]      |             |
| out_o      | output    | rd_buf_t             |             |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
