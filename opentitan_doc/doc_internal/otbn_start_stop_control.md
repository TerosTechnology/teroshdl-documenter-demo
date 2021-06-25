# Entity: otbn_start_stop_control
## Diagram
![Diagram](otbn_start_stop_control.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Generics
| Generic name  | Type | Value                              | Description                               |
| ------------- | ---- | ---------------------------------- | ----------------------------------------- |
| ImemSizeByte  | int  | 4096                               | Size of the instruction memory, in bytes  |
| ImemAddrWidth | int  | prim_util_pkg::vbits(ImemSizeByte) |                                           |
## Ports
| Port name               | Direction | Type                | Description |
| ----------------------- | --------- | ------------------- | ----------- |
| clk_i                   | input     |                     |             |
| rst_ni                  | input     |                     |             |
| start_i                 | input     |                     |             |
| start_addr_i            | input     | [ImemAddrWidth-1:0] |             |
| controller_start_o      | output    |                     |             |
| controller_start_addr_o | output    | [ImemAddrWidth-1:0] |             |
| controller_done_i       | input     |                     |             |
| urnd_reseed_req_o       | output    |                     |             |
| urnd_reseed_busy_i      | input     |                     |             |
| urnd_advance_o          | output    |                     |             |
| ispr_init_o             | output    |                     |             |
| insn_cnt_reset_o        | output    |                     |             |
## Signals
| Name          | Type                      | Description |
| ------------- | ------------------------- | ----------- |
| state_q       | otbn_start_stop_state_e   |             |
| state_d       | otbn_start_stop_state_e   |             |
| start_addr_q  | logic [ImemAddrWidth-1:0] |             |
| start_addr_en | logic                     |             |
## Constants
| Name          | Type | Value                              | Description |
| ------------- | ---- | ---------------------------------- | ----------- |
| ImemAddrWidth | int  | prim_util_pkg::vbits(ImemSizeByte) |             |
## Processes
- unnamed: _( @(posedge clk_i or negedge rst_ni) )_

- unnamed: _( @(posedge clk_i) )_

- unnamed: _(  )_

