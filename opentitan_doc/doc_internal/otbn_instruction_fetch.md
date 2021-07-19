# Entity: otbn_instruction_fetch

- **File**: otbn_instruction_fetch.sv
## Diagram

![Diagram](otbn_instruction_fetch.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Generics

| Generic name  | Type | Value                              | Description |
| ------------- | ---- | ---------------------------------- | ----------- |
| ImemSizeByte  | int  | 4096                               |             |
| ImemAddrWidth | int  | prim_util_pkg::vbits(ImemSizeByte) |             |
## Ports

| Port name               | Direction | Type                | Description                                       |
| ----------------------- | --------- | ------------------- | ------------------------------------------------- |
| clk_i                   | input     |                     |                                                   |
| rst_ni                  | input     |                     |                                                   |
| imem_req_o              | output    |                     | Instruction memory (IMEM) interface. Read-only.   |
| imem_addr_o             | output    | [ImemAddrWidth-1:0] |                                                   |
| imem_rdata_i            | input     | [31:0]              |                                                   |
| imem_rvalid_i           | input     |                     |                                                   |
| imem_rerror_i           | input     |                     |                                                   |
| insn_fetch_req_valid_i  | input     |                     | Next instruction selection (to instruction fetch) |
| insn_fetch_req_addr_i   | input     | [ImemAddrWidth-1:0] |                                                   |
| insn_fetch_resp_valid_o | output    |                     | Decoded instruction                               |
| insn_fetch_resp_addr_o  | output    | [ImemAddrWidth-1:0] |                                                   |
| insn_fetch_resp_data_o  | output    | [31:0]              |                                                   |
| insn_fetch_err_o        | output    |                     | ECC error seen in instruction fetch               |
## Signals

| Name         | Type  | Description                                                                                                                                                    |
| ------------ | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| unused_rst_n | logic | Nothing is reset in this module so rst_ni is unused. Leaving it in so adding resettable flops (or an assertion which will use the reset) is straight forward.  |
## Constants

| Name          | Type | Value                              | Description |
| ------------- | ---- | ---------------------------------- | ----------- |
| ImemAddrWidth | int  | prim_util_pkg::vbits(ImemSizeByte) |             |
## Processes
- unnamed: ( @(posedge clk_i) )
