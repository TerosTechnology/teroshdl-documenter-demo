# Entity: tlul_adapter_reg

## Diagram

![Diagram](tlul_adapter_reg.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Generics

| Generic name      | Type | Value   | Description                 |
| ----------------- | ---- | ------- | --------------------------- |
| EnableDataIntgGen | bit  | 1'b0    |                             |
| RegAw             | int  | 8       |                             |
| RegDw             | int  | 32      | Shall be matched with TL_DW |
| RegBw             | int  | RegDw/8 |                             |
## Ports

| Port name | Direction | Type        | Description        |
| --------- | --------- | ----------- | ------------------ |
| clk_i     | input     |             |                    |
| rst_ni    | input     |             |                    |
| tl_i      | input     | tl_h2d_t    | TL-UL interface    |
| tl_o      | output    | tl_d2h_t    |                    |
| re_o      | output    |             | Register interface |
| we_o      | output    |             |                    |
| addr_o    | output    | [RegAw-1:0] |                    |
| wdata_o   | output    | [RegDw-1:0] |                    |
| be_o      | output    | [RegBw-1:0] |                    |
| rdata_i   | input     | [RegDw-1:0] |                    |
| error_i   | input     |             |                    |
## Signals

| Name               | Type                      | Description                             |
| ------------------ | ------------------------- | --------------------------------------- |
| outstanding        | logic                     | Indicates current request is pending    |
| a_ack              | logic                     |                                         |
| d_ack              | logic                     |                                         |
| rdata              | logic [RegDw-1:0]         |                                         |
| error              | logic                     |                                         |
| err_internal       | logic                     |                                         |
| addr_align_err     | logic                     | Size and alignment                      |
| malformed_meta_err | logic                     | User signal format error or unsupported |
| tl_err             | logic                     | Common TL-UL error checker              |
| reqid              | logic [IW-1:0]            |                                         |
| reqsz              | logic [SZW-1:0]           |                                         |
| rspop              | tl_d_op_e                 |                                         |
| rd_req             | logic                     |                                         |
| wr_req             | logic                     |                                         |
| data_intg          | logic [DataIntgWidth-1:0] |                                         |
## Constants

| Name  | Type | Value                | Description |
| ----- | ---- | -------------------- | ----------- |
| RegBw | int  | RegDw/8              |             |
| IW    | int  | $bits(tl_i.a_source) |             |
| SZW   | int  | $bits(tl_i.a_size)   |             |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
- unnamed: (  )
**Description**
addr_align_err
Raised if addr isn't aligned with the size
Read size error is checked in tlul_assert.sv
Here is it added due to the limitation of register interface.

## Instantiations

- u_err: tlul_err
**Description**
tl_err : separate checker

