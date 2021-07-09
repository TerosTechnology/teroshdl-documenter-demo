# Entity: avl_dacfifo

## Diagram

![Diagram](avl_dacfifo.svg "Diagram")
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

| Generic name          | Type | Value        | Description |
| --------------------- | ---- | ------------ | ----------- |
| DAC_DATA_WIDTH        |      | 64           |             |
| DAC_MEM_ADDRESS_WIDTH |      | 8            |             |
| DMA_DATA_WIDTH        |      | 64           |             |
| DMA_MEM_ADDRESS_WIDTH |      | 10           |             |
| AVL_DATA_WIDTH        |      | 512          |             |
| AVL_ADDRESS_WIDTH     |      | 25           |             |
| AVL_BURST_LENGTH      |      | 127          |             |
| AVL_BASE_ADDRESS      |      | 32'h00000000 |             |
| AVL_ADDRESS_LIMIT     |      | 32'h1fffffff |             |
## Ports

| Port name          | Direction | Type                      | Description      |
| ------------------ | --------- | ------------------------- | ---------------- |
| dma_clk            | input     |                           | dma interface    |
| dma_rst            | input     |                           |                  |
| dma_valid          | input     |                           |                  |
| dma_data           | input     | [(DMA_DATA_WIDTH-1):0]    |                  |
| dma_ready          | output    |                           |                  |
| dma_xfer_req       | input     |                           |                  |
| dma_xfer_last      | input     |                           |                  |
| dac_clk            | input     |                           | dac interface    |
| dac_rst            | input     |                           |                  |
| dac_valid          | input     |                           |                  |
| dac_data           | output    | [(DAC_DATA_WIDTH-1):0]    |                  |
| dac_dunf           | output    |                           |                  |
| dac_xfer_out       | output    |                           |                  |
| bypass             | input     |                           |                  |
| avl_clk            | input     |                           | avalon interface |
| avl_reset          | input     |                           |                  |
| avl_address        | output    | [(AVL_ADDRESS_WIDTH-1):0] |                  |
| avl_burstcount     | output    | [  6:0]                   |                  |
| avl_byteenable     | output    | [ 63:0]                   |                  |
| avl_read           | output    |                           |                  |
| avl_readdata       | input     | [(AVL_DATA_WIDTH-1):0]    |                  |
| avl_readdata_valid | input     |                           |                  |
| avl_ready          | input     |                           |                  |
| avl_write          | output    |                           |                  |
| avl_writedata      | output    | [(AVL_DATA_WIDTH-1):0]    |                  |
## Signals

| Name                  | Type                        | Description       |
| --------------------- | --------------------------- | ----------------- |
| dma_bypass            | reg                         |                   |
| dac_bypass_m1         | reg                         |                   |
| dac_bypass            | reg                         |                   |
| dac_xfer_out_m1       | reg                         |                   |
| dac_xfer_out_bypass   | reg                         |                   |
| dma_ready_wr_s        | wire                        | internal signals  |
| dma_ready_bypass_s    | wire                        |                   |
| avl_read_s            | wire                        |                   |
| avl_write_s           | wire                        |                   |
| avl_wr_address_s      | wire [ 24:0]                |                   |
| avl_rd_address_s      | wire [ 24:0]                |                   |
| avl_last_address_s    | wire [ 24:0]                |                   |
| avl_last_burstcount_s | wire [  6:0]                |                   |
| dma_last_beats_s      | wire [  7:0]                |                   |
| avl_wr_burstcount_s   | wire [  6:0]                |                   |
| avl_rd_burstcount_s   | wire [  6:0]                |                   |
| avl_wr_byteenable_s   | wire [ 63:0]                |                   |
| avl_rd_byteenable_s   | wire [ 63:0]                |                   |
| avl_xfer_wren_s       | wire                        |                   |
| avl_xfer_out_s        | wire                        |                   |
| avl_xfer_in_s         | wire                        |                   |
| dac_data_fifo_s       | wire [(DAC_DATA_WIDTH-1):0] |                   |
| dac_data_bypass_s     | wire [(DAC_DATA_WIDTH-1):0] |                   |
| dac_xfer_fifo_out_s   | wire                        |                   |
| dac_dunf_fifo_s       | wire                        |                   |
| dac_dunf_bypass_s     | wire                        |                   |
## Constants

| Name        | Type | Value | Description |
| ----------- | ---- | ----- | ----------- |
| FIFO_BYPASS |      | 1'b0  |             |
## Processes
- unnamed: ( @(posedge avl_clk) )
## Instantiations

- i_wr: avl_dacfifo_wr
- i_rd: avl_dacfifo_rd
