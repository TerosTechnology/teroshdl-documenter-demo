# Entity: clkmgr_byp

## Diagram

![Diagram](clkmgr_byp.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Handle clock manager bypass requests
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| NumDivClks   | int  | 1     |             |
## Ports

| Port name         | Direction | Type             | Description |
| ----------------- | --------- | ---------------- | ----------- |
| clk_i             | input     |                  |             |
| rst_ni            | input     |                  |             |
| en_i              | input     | lc_tx_t          |             |
| byp_req           | input     | lc_tx_t          |             |
| ast_clk_byp_req_o | output    | lc_tx_t          |             |
| ast_clk_byp_ack_i | input     | lc_tx_t          |             |
| lc_clk_byp_req_i  | input     | lc_tx_t          |             |
| lc_clk_byp_ack_o  | output    | lc_tx_t          |             |
| step_down_acks_i  | input     | [NumDivClks-1:0] |             |
| step_down_req_o   | output    | lc_tx_t          |             |
## Signals

| Name            | Type    | Description |
| --------------- | ------- | ----------- |
| reg_clk_byp_req | lc_tx_t |             |
| on_val          | lc_tx_t |             |
| ast_clk_byp_req | lc_tx_t |             |
## Processes
- unnamed: (  )
## Instantiations

- u_clk_byp_req: prim_lc_sender
- u_rcv: prim_lc_sync
- u_send: prim_lc_sender
**Description**
only ack the lc_ctrl if it made a request.

