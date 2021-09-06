# Entity: axi_adcfifo_dma

- **File**: axi_adcfifo_dma.v
## Diagram

![Diagram](axi_adcfifo_dma.svg "Diagram")
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

| Generic name     | Type | Value | Description |
| ---------------- | ---- | ----- | ----------- |
| AXI_DATA_WIDTH   |      | 512   |             |
| DMA_DATA_WIDTH   |      | 64    |             |
| DMA_READY_ENABLE |      | 1     |             |
## Ports

| Port name       | Direction | Type                 | Description |
| --------------- | --------- | -------------------- | ----------- |
| axi_clk         | input     |                      |             |
| axi_drst        | input     |                      |             |
| axi_dvalid      | input     |                      |             |
| axi_ddata       | input     | [AXI_DATA_WIDTH-1:0] |             |
| axi_dready      | output    |                      |             |
| axi_xfer_status | input     | [ 3:0]               |             |
| dma_clk         | input     |                      |             |
| dma_wr          | output    |                      |             |
| dma_wdata       | output    | [DMA_DATA_WIDTH-1:0] |             |
| dma_wready      | input     |                      |             |
| dma_xfer_req    | input     |                      |             |
| dma_xfer_status | output    | [ 3:0]               |             |
## Signals

| Name                | Type                            | Description        |
| ------------------- | ------------------------------- | ------------------ |
| axi_waddr_rel_count | reg     [  2:0]                 |                    |
| axi_waddr_rel_t     | reg                             |                    |
| axi_waddr_rel       | reg     [AXI_ADDRESS_WIDTH-1:0] |                    |
| axi_raddr_rel_t_m   | reg     [  2:0]                 |                    |
| axi_raddr_rel       | reg     [DMA_ADDRESS_WIDTH-1:0] |                    |
| axi_addr_diff       | reg     [DMA_ADDRESS_WIDTH-1:0] |                    |
| dma_rst             | reg                             |                    |
| dma_waddr_rel_t_m   | reg     [  2:0]                 |                    |
| dma_waddr_rel       | reg     [AXI_ADDRESS_WIDTH-1:0] |                    |
| dma_rd              | reg                             |                    |
| dma_rd_d            | reg                             |                    |
| dma_rdata_d         | reg     [DMA_DATA_WIDTH-1:0]    |                    |
| dma_raddr           | reg     [DMA_ADDRESS_WIDTH-1:0] |                    |
| dma_raddr_rel_count | reg     [  2:0]                 |                    |
| dma_raddr_rel_t     | reg                             |                    |
| dma_raddr_rel       | reg     [DMA_ADDRESS_WIDTH-1:0] |                    |
| axi_addr_diff_s     | wire [DMA_ADDRESS_WIDTH:0]      |  internal signals  |
| axi_raddr_rel_t_s   | wire                            |                    |
| axi_waddr_s         | wire [DMA_ADDRESS_WIDTH-1:0]    |                    |
| dma_waddr_rel_t_s   | wire                            |                    |
| dma_waddr_rel_s     | wire [DMA_ADDRESS_WIDTH-1:0]    |                    |
| dma_wready_s        | wire                            |                    |
| dma_rd_s            | wire                            |                    |
| dma_rdata_s         | wire [DMA_DATA_WIDTH-1:0]       |                    |
## Constants

| Name              | Type | Value                           | Description |
| ----------------- | ---- | ------------------------------- | ----------- |
| DMA_MEM_RATIO     |      | AXI_DATA_WIDTH/DMA_DATA_WIDTH   |             |
| DMA_ADDRESS_WIDTH |      | 8                               |             |
| AXI_ADDRESS_WIDTH |      | reg     [AXI_ADDRESS_WIDTH-1:0] |             |
## Processes
- unnamed: ( @(posedge axi_clk) )
  - **Type:** always
**Description**
 write interface 
- unnamed: ( @(posedge axi_clk) )
  - **Type:** always
- unnamed: ( @(posedge dma_clk) )
  - **Type:** always
- unnamed: ( @(posedge dma_clk) )
  - **Type:** always
## Instantiations

- i_mem_asym: ad_mem_asym
**Description**
 instantiations

- i_axis_inf: ad_axis_inf_rx
- i_xfer_status: up_xfer_status
