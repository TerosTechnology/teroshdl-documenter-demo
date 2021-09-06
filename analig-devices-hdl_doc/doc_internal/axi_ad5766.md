# Entity: axi_ad5766

- **File**: axi_ad5766.v
## Diagram

![Diagram](axi_ad5766.svg "Diagram")
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

| Generic name          | Type | Value | Description |
| --------------------- | ---- | ----- | ----------- |
| FPGA_TECHNOLOGY       |      | 0     |             |
| FPGA_FAMILY           |      | 0     |             |
| SPEED_GRADE           |      | 0     |             |
| DEV_PACKAGE           |      | 0     |             |
| ASYNC_SPI_CLK         |      | 0     |             |
| CMD_MEM_ADDRESS_WIDTH |      | 4     |             |
| SDO_MEM_ADDRESS_WIDTH |      | 4     |             |
## Ports

| Port name        | Direction | Type   | Description                                           |
| ---------------- | --------- | ------ | ----------------------------------------------------- |
| s_axi_aclk       | input     |        |  Slave AXI interface                                  |
| s_axi_aresetn    | input     |        |                                                       |
| s_axi_awvalid    | input     |        |                                                       |
| s_axi_awaddr     | input     | [15:0] |                                                       |
| s_axi_awready    | output    |        |                                                       |
| s_axi_awprot     | input     | [ 2:0] |                                                       |
| s_axi_wvalid     | input     |        |                                                       |
| s_axi_wdata      | input     | [31:0] |                                                       |
| s_axi_wstrb      | input     | [ 3:0] |                                                       |
| s_axi_wready     | output    |        |                                                       |
| s_axi_bvalid     | output    |        |                                                       |
| s_axi_bresp      | output    | [ 1:0] |                                                       |
| s_axi_bready     | input     |        |                                                       |
| s_axi_arvalid    | input     |        |                                                       |
| s_axi_araddr     | input     | [15:0] |                                                       |
| s_axi_arready    | output    |        |                                                       |
| s_axi_arprot     | input     | [ 2:0] |                                                       |
| s_axi_rvalid     | output    |        |                                                       |
| s_axi_rready     | input     |        |                                                       |
| s_axi_rresp      | output    | [ 1:0] |                                                       |
| s_axi_rdata      | output    | [31:0] |                                                       |
| dma_clk          | output    |        |  FIFO transmit                                        |
| dma_valid        | output    |        |                                                       |
| dma_enable       | input     |        |                                                       |
| dma_data         | input     | [15:0] |                                                       |
| dma_xfer_req     | input     |        |                                                       |
| dma_underflow    | input     |        |                                                       |
| spi_clk          | input     |        | should be connected to up_clk                         |
| spi_resetn       | input     |        |                                                       |
| cmd_ready        | input     |        |                                                       |
| cmd_valid        | output    |        |                                                       |
| cmd_data         | output    | [15:0] |                                                       |
| sdo_data_ready   | input     |        |                                                       |
| sdo_data_valid   | output    |        |                                                       |
| sdo_data         | output    | [ 7:0] |                                                       |
| sdi_data_ready   | output    |        |                                                       |
| sdi_data_valid   | input     |        |                                                       |
| sdi_data         | input     | [ 7:0] |                                                       |
| sync_ready       | output    |        |                                                       |
| sync_valid       | input     |        |                                                       |
| sync_data        | input     | [ 7:0] |                                                       |
| ctrl_clk         | input     |        |  SPI engine offload interface (to the AXI SPI engine) |
| ctrl_cmd_wr_en   | input     |        |                                                       |
| ctrl_cmd_wr_data | input     | [15:0] |                                                       |
| ctrl_enable      | input     |        |                                                       |
| ctrl_enabled     | output    |        |                                                       |
| ctrl_mem_reset   | input     |        |                                                       |
## Signals

| Name                 | Type                             | Description      |
| -------------------- | -------------------------------- | ---------------- |
| up_wreq_s            | wire                             |  internal wires  |
| up_waddr_s           | wire [13:0]                      |                  |
| up_wdata_s           | wire [31:0]                      |                  |
| up_rreq_s            | wire                             |                  |
| up_raddr_s           | wire [13:0]                      |                  |
| up_rdata_s           | wire [31:0]                      |                  |
| up_rack_s            | wire                             |                  |
| up_wack_s            | wire                             |                  |
| trigger_s            | wire                             |                  |
| pulse_period_s       | wire [31:0]                      |                  |
| dac_datarate_s       | wire [15:0]                      |                  |
| spi_reset            | wire                             |                  |
| spi_enable_s         | wire                             |                  |
| sequencer            | wire [ 3:0]                      |                  |
| cmd_bits             | wire [ 3:0]                      |                  |
| end_of_sequence      | wire [ 3:0]                      |                  |
| spi_mem_reset_s      | wire                             |                  |
| sequence_valid_s     | wire                             |                  |
| sequence_data_s      | wire [ 7:0]                      |                  |
| dac_rst_s            | wire                             |                  |
| dac_rstn_s           | wire                             |                  |
| spi_cmd_rd_addr_next | wire [CMD_MEM_ADDRESS_WIDTH-1:0] |                  |
| up_rdata             | reg         [31:0]               |  registers       |
| up_rack              | reg                              |                  |
| up_wack              | reg                              |                  |
| cmd_mem              | reg         [15:0]               |                  |
| sdo_mem              | reg         [ 7:0]               |                  |
| ctrl_cmd_wr_addr     | reg [CMD_MEM_ADDRESS_WIDTH-1:0]  |                  |
| spi_cmd_rd_addr      | reg [CMD_MEM_ADDRESS_WIDTH-1:0]  |                  |
| ctrl_sdo_wr_addr     | reg [SDO_MEM_ADDRESS_WIDTH-1:0]  |                  |
| spi_sdo_rd_addr      | reg [SDO_MEM_ADDRESS_WIDTH-1:0]  |                  |
| spi_active           | reg                              |                  |
## Processes
- unnamed: ( @(posedge spi_clk) )
  - **Type:** always
- unnamed: ( @(posedge spi_clk) )
  - **Type:** always
- unnamed: ( @(posedge spi_clk) )
  - **Type:** always
- unnamed: ( @(posedge ctrl_clk) )
  - **Type:** always
- unnamed: ( @(posedge ctrl_clk) )
  - **Type:** always
- unnamed: ( @(posedge dma_clk) )
  - **Type:** always
**Description**
 request data from the DMA at the desired rate 
- unnamed: ( @(negedge up_rstn or posedge spi_clk) )
  - **Type:** always
**Description**
 offset of the sequencer registers are 8'h40 
## Instantiations

- i_trigger_gen: util_pulse_gen
- i_sequencer: up_ad5766_sequencer
- i_dac_common: up_dac_common
- i_up_axi: up_axi
**Description**
 AXI wrapper

