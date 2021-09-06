# Entity: tlul_adapter_host

- **File**: tlul_adapter_host.sv
## Diagram

![Diagram](tlul_adapter_host.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 tlul_adapter (Host adapter) converts basic req/grant/rvalid into TL-UL interface. If
 MAX_REQS == 1 it is purely combinational logic. If MAX_REQS > 1 flops are required.

 The host driving the adapter is responsible for ensuring it doesn't have more requests in flight
 than the specified MAX_REQS.

 The outgoing address is always word aligned. The access size is always the word size (as
 specified by TL_DW). For write accesses that occupy all lanes the operation is PutFullData,
 otherwise it is PutPartialData, mask is generated from be_i. For reads all lanes are enabled as
 required by TL-UL (every bit in mask set).

 When MAX_REQS > 1 tlul_adapter_host does not do anything to order responses from the TL-UL
 interface which could return them out of order. It is the host's responsibility to either only
 have outstanding requests to an address space it knows will return responses in order or to not
 care about out of order responses (note that if read data is returned out of order there is no
 way to determine this).

## Generics

| Generic name      | Type         | Value | Description                                                             |
| ----------------- | ------------ | ----- | ----------------------------------------------------------------------- |
| MAX_REQS          | int unsigned | 2     |                                                                         |
| EnableDataIntgGen | bit          | 1     |  TODO(#7966) disable data intgrity overwrite once dv support available  |
## Ports

| Port name    | Direction | Type                  | Description |
| ------------ | --------- | --------------------- | ----------- |
| clk_i        | input     |                       |             |
| rst_ni       | input     |                       |             |
| req_i        | input     |                       |             |
| gnt_o        | output    |                       |             |
| addr_i       | input     | [top_pkg::TL_AW-1:0]  |             |
| we_i         | input     |                       |             |
| wdata_i      | input     | [top_pkg::TL_DW-1:0]  |             |
| wdata_intg_i | input     | [DataIntgWidth-1:0]   |             |
| be_i         | input     | [top_pkg::TL_DBW-1:0] |             |
| type_i       | input     | tl_type_e             |             |
| valid_o      | output    |                       |             |
| rdata_o      | output    | [top_pkg::TL_DW-1:0]  |             |
| rdata_intg_o | output    | [DataIntgWidth-1:0]   |             |
| err_o        | output    |                       |             |
| intg_err_o   | output    |                       |             |
| tl_o         | output    | tl_h2d_t              |             |
| tl_i         | input     | tl_d2h_t              |             |
## Signals

| Name                    | Type                           | Description                                                                 |
| ----------------------- | ------------------------------ | --------------------------------------------------------------------------- |
| tl_source               | logic [top_pkg::TL_AIW-1:0]    |                                                                             |
| tl_be                   | logic [top_pkg::TL_DBW-1:0]    |                                                                             |
| tl_out                  | tl_h2d_t                       |                                                                             |
| intg_err                | logic                          |                                                                             |
| intg_err_q              | logic                          |                                                                             |
| unused_addr_bottom_bits | logic                          |  Addresses are assumed to be word-aligned, and the bottom bits are ignored  |
| unused_tl_i_fields      | logic                          |  Explicitly ignore unused fields of tl_i                                    |
| outstanding_reqs_q      | logic [OutstandingReqCntW-1:0] |                                                                             |
| outstanding_reqs_d      | logic [OutstandingReqCntW-1:0] |                                                                             |
## Constants

| Name               | Type | Value                   | Description |
| ------------------ | ---- | ----------------------- | ----------- |
| WordSize           | int  | $clog2(top_pkg::TL_DBW) |             |
| OutstandingReqCntW | int  | $clog2(MAX_REQS) + 1    |             |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- unnamed: (  )
  - **Type:** always_comb
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
## Instantiations

- u_cmd_intg_gen: tlul_cmd_intg_gen
**Description**
 TODO #7966 disable data intgrity overwrite once dv support available

- u_rsp_chk: tlul_rsp_intg_chk
