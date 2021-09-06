# Entity: axi_adcfifo_rd

- **File**: axi_adcfifo_rd.v
## Diagram

![Diagram](axi_adcfifo_rd.svg "Diagram")
## Description

 ***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2017 (c) Analog Devices, Inc. All rights reserved.

 In this HDL repository, there are many different and unique modules, consisting
 of various HDL (Verilog or VHDL) components. The individual modules are
 developed independently, and may be accompanied by separate and unique license
 terms.

 The user should read each of these license terms, and understand the
 freedoms and responsibilities that he or she has by using this source/core.

 This core is distributed in the hope that it will be useful, but WITHOUT ANY
 WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
 A PARTICULAR PURPOSE.

 Redistribution and use of source or resulting binaries, with or without modification
 of this file, are permitted under one of the following two license terms:

   1. The GNU General Public License version 2 as published by the
      Free Software Foundation, which can be found in the top level directory
      of this repository (LICENSE_GPL2), and also online at:
      <https://www.gnu.org/licenses/old-licenses/gpl-2.0.html>

 OR

   2. An ADI specific BSD license, which can be found in the top level directory
      of this repository (LICENSE_ADIBSD), and also on-line at:
      https://github.com/analogdevicesinc/hdl/blob/master/LICENSE_ADIBSD
      This will allow to generate bit files and not release the source code,
      as long as it attaches to an ADI device.

 ***************************************************************************
 ***************************************************************************

## Generics

| Generic name      | Type | Value        | Description |
| ----------------- | ---- | ------------ | ----------- |
| AXI_DATA_WIDTH    |      | 512          |             |
| AXI_SIZE          |      | 2            |             |
| AXI_LENGTH        |      | 16           |             |
| AXI_ADDRESS       |      | 32'h00000000 |             |
| AXI_ADDRESS_LIMIT |      | 32'h00000000 |             |
## Ports

| Port name    | Direction | Type                 | Description                  |
| ------------ | --------- | -------------------- | ---------------------------- |
| dma_xfer_req | input     |                      |  request and synchronization |
| axi_rd_req   | input     |                      |  read interface              |
| axi_rd_addr  | input     | [ 31:0]              |                              |
| axi_clk      | input     |                      |  axi interface               |
| axi_resetn   | input     |                      |                              |
| axi_arvalid  | output    |                      |                              |
| axi_arid     | output    | [ 3:0]               |                              |
| axi_arburst  | output    | [ 1:0]               |                              |
| axi_arlock   | output    |                      |                              |
| axi_arcache  | output    | [ 3:0]               |                              |
| axi_arprot   | output    | [ 2:0]               |                              |
| axi_arqos    | output    | [ 3:0]               |                              |
| axi_aruser   | output    | [ 3:0]               |                              |
| axi_arlen    | output    | [ 7:0]               |                              |
| axi_arsize   | output    | [ 2:0]               |                              |
| axi_araddr   | output    | [ 31:0]              |                              |
| axi_arready  | input     |                      |                              |
| axi_rvalid   | input     |                      |                              |
| axi_rid      | input     | [ 3:0]               |                              |
| axi_ruser    | input     | [ 3:0]               |                              |
| axi_rresp    | input     | [ 1:0]               |                              |
| axi_rlast    | input     |                      |                              |
| axi_rdata    | input     | [AXI_DATA_WIDTH-1:0] |                              |
| axi_rready   | output    |                      |                              |
| axi_rerror   | output    |                      |  axi status                  |
| axi_drst     | output    |                      |  fifo interface              |
| axi_dvalid   | output    |                      |                              |
| axi_ddata    | output    | [AXI_DATA_WIDTH-1:0] |                              |
| axi_dready   | input     |                      |                              |
## Signals

| Name            | Type            | Description          |
| --------------- | --------------- | -------------------- |
| axi_rd_addr_h   | reg     [ 31:0] |  internal registers  |
| axi_rd          | reg             |                      |
| axi_rd_active   | reg             |                      |
| axi_xfer_req_m  | reg     [  2:0] |                      |
| axi_xfer_init   | reg             |                      |
| axi_xfer_enable | reg             |                      |
| axi_ready_s     | wire            |  internal signals    |
## Constants

| Name             | Type | Value                       | Description |
| ---------------- | ---- | --------------------------- | ----------- |
| AXI_BYTE_WIDTH   |      | AXI_DATA_WIDTH/8            |             |
| AXI_AWINCR       |      | AXI_LENGTH * AXI_BYTE_WIDTH |             |
| BUF_THRESHOLD_LO |      | 6'd3                        |             |
| BUF_THRESHOLD_HI |      | 6'd60                       |             |
## Processes
- unnamed: ( @(posedge axi_clk or negedge axi_resetn) )
  - **Type:** always
- unnamed: ( @(posedge axi_clk or negedge axi_resetn) )
  - **Type:** always
- unnamed: ( @(posedge axi_clk or negedge axi_resetn) )
  - **Type:** always
</br>**Description**
 read data channel 
- unnamed: ( @(posedge axi_clk or negedge axi_resetn) )
  - **Type:** always
