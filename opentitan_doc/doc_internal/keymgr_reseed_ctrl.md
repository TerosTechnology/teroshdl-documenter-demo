# Entity: keymgr_reseed_ctrl

- **File**: keymgr_reseed_ctrl.sv
## Diagram

![Diagram](keymgr_reseed_ctrl.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Key manager entropy reseed controls


## Ports

| Port name         | Direction | Type            | Description               |
| ----------------- | --------- | --------------- | ------------------------- |
| clk_i             | input     |                 |                           |
| rst_ni            | input     |                 |                           |
| clk_edn_i         | input     |                 |                           |
| rst_edn_ni        | input     |                 |                           |
| reseed_req_i      | input     |                 |  interface to keymgr_ctrl |
| reseed_ack_o      | output    |                 |                           |
| reseed_interval_i | input     | [15:0]          |  interface to software    |
| edn_o             | output    |                 |  interface to edn         |
| edn_i             | input     |                 |                           |
| seed_en_o         | output    |                 |  interface to lfsr        |
| seed_o            | output    | [LfsrWidth-1:0] |                           |
## Signals

| Name         | Type                    | Description                             |
| ------------ | ----------------------- | --------------------------------------- |
| edn_cnt      | logic [EdnCntWidth-1:0] |  counter to track number of edn rounds  |
| edn_txn_done | logic                   |                                         |
| edn_done     | logic                   |                                         |
| edn_req      | logic                   |                                         |
| edn_ack      | logic                   |                                         |
| edn_data     | logic [EdnWidth-1:0]    |                                         |
| unused_fips  | logic                   |                                         |
## Constants

| Name         | Type         | Value                           | Description |
| ------------ | ------------ | ------------------------------- | ----------- |
| EdnRounds    | int unsigned | LfsrWidth / EdnWidth            |             |
| EdnCntWidth  | int unsigned | prim_util_pkg::vbits(EdnRounds) |             |
| LastEdnRound | int unsigned | EdnRounds - 1                   |             |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk_edn_i) )
  - **Type:** always_ff
</br>**Description**
 capture the data on edn domain since the ack interface  finishes before the source domain is able to see it 
## Instantiations

- u_reqack: prim_sync_reqack
</br>**Description**
req/ack interface to edn

