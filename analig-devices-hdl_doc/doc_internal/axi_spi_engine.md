# Entity: axi_spi_engine

- **File**: axi_spi_engine.v
## Diagram

![Diagram](axi_spi_engine.svg "Diagram")
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

| Generic name                   | Type   | Value | Description |
| ------------------------------ | ------ | ----- | ----------- |
| CMD_FIFO_ADDRESS_WIDTH         |        | 4     |             |
| SYNC_FIFO_ADDRESS_WIDTH        |        | 4     |             |
| SDO_FIFO_ADDRESS_WIDTH         |        | 5     |             |
| SDI_FIFO_ADDRESS_WIDTH         |        | 5     |             |
| MM_IF_TYPE                     |        | 0     |             |
| ASYNC_SPI_CLK                  |        | 0     |             |
| NUM_OFFLOAD                    |        | 0     |             |
| OFFLOAD0_CMD_MEM_ADDRESS_WIDTH |        | 4     |             |
| OFFLOAD0_SDO_MEM_ADDRESS_WIDTH |        | 4     |             |
| ID                             |        | 0     |             |
| DATA_WIDTH                     | [15:0] | 8     |             |
| NUM_OF_SDI                     | [ 7:0] | 1     |             |
## Ports

| Port name            | Direction | Type                            | Description          |
| -------------------- | --------- | ------------------------------- | -------------------- |
| s_axi_aclk           | input     |                                 | Slave AXI interface  |
| s_axi_aresetn        | input     |                                 |                      |
| s_axi_awvalid        | input     |                                 |                      |
| s_axi_awaddr         | input     | [15:0]                          |                      |
| s_axi_awready        | output    |                                 |                      |
| s_axi_awprot         | input     | [2:0]                           |                      |
| s_axi_wvalid         | input     |                                 |                      |
| s_axi_wdata          | input     | [31:0]                          |                      |
| s_axi_wstrb          | input     | [ 3:0]                          |                      |
| s_axi_wready         | output    |                                 |                      |
| s_axi_bvalid         | output    |                                 |                      |
| s_axi_bresp          | output    | [ 1:0]                          |                      |
| s_axi_bready         | input     |                                 |                      |
| s_axi_arvalid        | input     |                                 |                      |
| s_axi_araddr         | input     | [15:0]                          |                      |
| s_axi_arready        | output    |                                 |                      |
| s_axi_arprot         | input     | [2:0]                           |                      |
| s_axi_rvalid         | output    |                                 |                      |
| s_axi_rready         | input     |                                 |                      |
| s_axi_rresp          | output    | [ 1:0]                          |                      |
| s_axi_rdata          | output    | [31:0]                          |                      |
| up_clk               | input     |                                 | up interface         |
| up_rstn              | input     |                                 |                      |
| up_wreq              | input     |                                 |                      |
| up_waddr             | input     | [13:0]                          |                      |
| up_wdata             | input     | [31:0]                          |                      |
| up_wack              | output    |                                 |                      |
| up_rreq              | input     |                                 |                      |
| up_raddr             | input     | [13:0]                          |                      |
| up_rdata             | output    | [31:0]                          |                      |
| up_rack              | output    |                                 |                      |
| irq                  | output    |                                 |                      |
| spi_clk              | input     |                                 | SPI signals          |
| spi_resetn           | output    |                                 |                      |
| cmd_ready            | input     |                                 |                      |
| cmd_valid            | output    |                                 |                      |
| cmd_data             | output    | [15:0]                          |                      |
| sdo_data_ready       | input     |                                 |                      |
| sdo_data_valid       | output    |                                 |                      |
| sdo_data             | output    | [(DATA_WIDTH-1):0]              |                      |
| sdi_data_ready       | output    |                                 |                      |
| sdi_data_valid       | input     |                                 |                      |
| sdi_data             | input     | [(NUM_OF_SDI * DATA_WIDTH-1):0] |                      |
| sync_ready           | output    |                                 |                      |
| sync_valid           | input     |                                 |                      |
| sync_data            | input     | [7:0]                           |                      |
| offload0_cmd_wr_en   | output    |                                 | Offload ctrl signals |
| offload0_cmd_wr_data | output    | [15:0]                          |                      |
| offload0_sdo_wr_en   | output    |                                 |                      |
| offload0_sdo_wr_data | output    | [(DATA_WIDTH-1):0]              |                      |
| offload0_mem_reset   | output    |                                 |                      |
| offload0_enable      | output    |                                 |                      |
| offload0_enabled     | input     |                                 |                      |
| offload_sync_ready   | output    |                                 |                      |
| offload_sync_valid   | input     |                                 |                      |
| offload_sync_data    | input     | [7:0]                           |                      |
## Signals

| Name                     | Type                                 | Description       |
| ------------------------ | ------------------------------------ | ----------------- |
| clk                      | wire                                 |                   |
| rstn                     | wire                                 |                   |
| cmd_fifo_room            | wire [CMD_FIFO_ADDRESS_WIDTH-1:0]    |                   |
| cmd_fifo_almost_empty    | wire                                 |                   |
| up_cmd_fifo_almost_empty | wire                                 |                   |
| cmd_fifo_in_data         | wire [15:0]                          |                   |
| cmd_fifo_in_ready        | wire                                 |                   |
| cmd_fifo_in_valid        | wire                                 |                   |
| sdo_fifo_room            | wire [SDO_FIFO_ADDRESS_WIDTH-1:0]    |                   |
| sdo_fifo_almost_empty    | wire                                 |                   |
| up_sdo_fifo_almost_empty | wire                                 |                   |
| sdo_fifo_in_data         | wire [(DATA_WIDTH-1):0]              |                   |
| sdo_fifo_in_ready        | wire                                 |                   |
| sdo_fifo_in_valid        | wire                                 |                   |
| sdi_fifo_out_data_msb_s  | wire                                 |                   |
| sdi_fifo_level           | wire [SDI_FIFO_ADDRESS_WIDTH-1:0]    |                   |
| sdi_fifo_almost_full     | wire                                 |                   |
| up_sdi_fifo_almost_full  | wire                                 |                   |
| sdi_fifo_out_data        | wire [(NUM_OF_SDI * DATA_WIDTH-1):0] |                   |
| sdi_fifo_out_ready       | wire                                 |                   |
| sdi_fifo_out_valid       | wire                                 |                   |
| sync_fifo_data           | wire [7:0]                           |                   |
| sync_fifo_valid          | wire                                 |                   |
| offload_sync_fifo_data   | wire [7:0]                           |                   |
| offload_sync_fifo_valid  | wire                                 |                   |
| up_sw_reset              | reg                                  |                   |
| up_sw_resetn             | wire                                 |                   |
| up_rdata_ff              | reg  [31:0]                          |                   |
| up_wack_ff               | reg                                  |                   |
| up_rack_ff               | reg                                  |                   |
| up_wreq_s                | wire                                 |                   |
| up_rreq_s                | wire                                 |                   |
| up_wdata_s               | wire [31:0]                          |                   |
| up_waddr_s               | wire [13:0]                          |                   |
| up_raddr_s               | wire [13:0]                          |                   |
| up_scratch               | reg [31:0]                           | Scratch register  |
| sync_id                  | reg  [7:0]                           |                   |
| sync_id_pending          | reg                                  |                   |
| offload_sync_id          | reg  [7:0]                           |                   |
| offload_sync_id_pending  | reg                                  |                   |
| up_irq_mask              | reg [4:0]                            | IRQ handling      |
| up_irq_source            | wire [4:0]                           |                   |
| up_irq_pending           | wire [4:0]                           |                   |
| offload0_enable_reg      | reg                                  |                   |
| offload0_mem_reset_reg   | reg                                  |                   |
| offload0_enabled_s       | wire                                 |                   |
## Constants

| Name          | Type | Value    | Description |
| ------------- | ---- | -------- | ----------- |
| PCORE_VERSION |      | 'h010071 |             |
| S_AXI         |      | 0        |             |
| UP_FIFO       |      | 1        |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
the software reset should reset all the registers

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
## Instantiations

- i_cmd_fifo: util_axis_fifo
- i_sdo_fifo: util_axis_fifo
- i_sdi_fifo: util_axis_fifo
- i_offload_enable_sync: sync_bits
- i_offload_enabled_sync: sync_bits
- i_offload_mem_reset_sync: sync_bits
- i_fifo_status: sync_bits
