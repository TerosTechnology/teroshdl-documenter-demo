# Entity: util_adcfifo

- **File**: util_adcfifo.v
## Diagram

![Diagram](util_adcfifo.svg "Diagram")
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

| Generic name      | Type | Value | Description |
| ----------------- | ---- | ----- | ----------- |
| FPGA_TECHNOLOGY   |      | 0     |             |
| ADC_DATA_WIDTH    |      | 256   |             |
| DMA_DATA_WIDTH    |      | 64    |             |
| DMA_READY_ENABLE  |      | 1     |             |
| DMA_ADDRESS_WIDTH |      | 10    |             |
## Ports

| Port name       | Direction | Type                 | Description    |
| --------------- | --------- | -------------------- | -------------- |
| adc_rst         | input     |                      | fifo interface |
| adc_clk         | input     |                      |                |
| adc_wr          | input     |                      |                |
| adc_wdata       | input     | [ADC_DATA_WIDTH-1:0] |                |
| adc_wovf        | output    |                      |                |
| dma_clk         | input     |                      | dma interface  |
| dma_wr          | output    |                      |                |
| dma_wdata       | output    | [DMA_DATA_WIDTH-1:0] |                |
| dma_wready      | input     |                      |                |
| dma_xfer_req    | input     |                      |                |
| dma_xfer_status | output    | [ 3:0]               |                |
## Signals

| Name                 | Type                                | Description         |
| -------------------- | ----------------------------------- | ------------------- |
| adc_xfer_req_m       | reg         [ 2:0]                  | internal registers  |
| adc_xfer_init        | reg                                 |                     |
| adc_xfer_enable      | reg                                 |                     |
| adc_wr_int           | reg                                 |                     |
| adc_wdata_int        | reg         [ADC_DATA_WIDTH-1:0]    |                     |
| adc_waddr_int        | reg         [ADC_ADDRESS_WIDTH-1:0] |                     |
| adc_capture_arm      | reg                                 |                     |
| dma_rd               | reg                                 |                     |
| dma_rd_d             | reg                                 |                     |
| dma_rdata_d          | reg         [DMA_DATA_WIDTH-1:0]    |                     |
| dma_raddr            | reg         [DMA_ADDRESS_WIDTH:0]   |                     |
| dma_waddr_int        | reg         [DMA_ADDRESS_WIDTH-1:0] |                     |
| dma_endof_read       | reg                                 |                     |
| adc_rst_s            | wire                                | internal signals    |
| dma_wready_s         | wire                                |                     |
| dma_rdata_s          | wire [DMA_DATA_WIDTH-1:0]           |                     |
| dma_read_rst_s       | wire                                |                     |
| dma_wr_int_s         | wire                                |                     |
| dma_waddr_int_s      | wire [ADC_ADDRESS_WIDTH-1:0]        |                     |
| adc_end_of_capture_s | wire                                |                     |
| adc_waddr_int_s      | wire [ADC_ADDRESS_WIDTH-1:0]        |                     |
## Constants

| Name                  | Type | Value                                     | Description |
| --------------------- | ---- | ----------------------------------------- | ----------- |
| DMA_MEM_RATIO         |      | ADC_DATA_WIDTH/DMA_DATA_WIDTH             |             |
| ADDRESS_PADDING_WIDTH |      | 3                                         |             |
| ADC_ADDRESS_WIDTH     |      | DMA_ADDRESS_WIDTH - ADDRESS_PADDING_WIDTH |             |
| ADC_ADDR_LIMIT        |      | (2**ADC_ADDRESS_WIDTH)-1                  |             |
| DMA_ADDR_LIMIT        |      | (2**DMA_ADDRESS_WIDTH)-1                  |             |
## Processes
- unnamed: ( @(posedge adc_clk) )
**Description**
optional capture synchronization

- unnamed: ( @(posedge adc_clk) )
- unnamed: ( @(posedge adc_clk) )
- unnamed: ( @(posedge adc_clk) )
- unnamed: ( @(posedge dma_clk) )
- unnamed: ( @(posedge dma_clk) )
## Instantiations

- i_adc_rst_sync: ad_rst
**Description**
synchronize the adc_rst to the adc_clk clock domain

- i_dma_waddr_sync: sync_gray
**Description**
write address synchronization

- i_axis_inf: ad_axis_inf_rx
