# Entity: axi_spdif_tx

## Diagram

![Diagram](axi_spdif_tx.svg "Diagram")
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

| Generic name        | Type    | Value     | Description |
| ------------------- | ------- | --------- | ----------- |
| S_AXI_DATA_WIDTH    | integer | 32        |             |
| S_AXI_ADDRESS_WIDTH | integer | 32        |             |
| DEVICE_FAMILY       | string  | "virtex6" |             |
| DMA_TYPE            | integer | 0         |             |
## Ports

| Port name       | Direction | Type                                              | Description |
| --------------- | --------- | ------------------------------------------------- | ----------- |
| spdif_data_clk  | in        | std_logic                                         |             |
| spdif_tx_o      | out       | std_logic                                         |             |
| s_axi_aclk      | in        | std_logic                                         |             |
| s_axi_aresetn   | in        | std_logic                                         |             |
| s_axi_awaddr    | in        | std_logic_vector(S_AXI_ADDRESS_WIDTH-1 downto 0)  |             |
| s_axi_awprot    | in        | std_logic_vector(2 downto 0)                      |             |
| s_axi_awvalid   | in        | std_logic                                         |             |
| s_axi_wdata     | in        | std_logic_vector(S_AXI_DATA_WIDTH-1 downto 0)     |             |
| s_axi_wstrb     | in        | std_logic_vector((S_AXI_DATA_WIDTH/8)-1 downto 0) |             |
| s_axi_wvalid    | in        | std_logic                                         |             |
| s_axi_bready    | in        | std_logic                                         |             |
| s_axi_araddr    | in        | std_logic_vector(S_AXI_ADDRESS_WIDTH-1 downto 0)  |             |
| s_axi_arprot    | in        | std_logic_vector(2 downto 0)                      |             |
| s_axi_arvalid   | in        | std_logic                                         |             |
| s_axi_rready    | in        | std_logic                                         |             |
| s_axi_arready   | out       | std_logic                                         |             |
| s_axi_rdata     | out       | std_logic_vector(S_AXI_DATA_WIDTH-1 downto 0)     |             |
| s_axi_rresp     | out       | std_logic_vector(1 downto 0)                      |             |
| s_axi_rvalid    | out       | std_logic                                         |             |
| s_axi_wready    | out       | std_logic                                         |             |
| s_axi_bresp     | out       | std_logic_vector(1 downto 0)                      |             |
| s_axi_bvalid    | out       | std_logic                                         |             |
| s_axi_awready   | out       | std_logic                                         |             |
| s_axis_aclk     | in        | std_logic                                         |             |
| s_axis_aresetn  | in        | std_logic                                         |             |
| s_axis_tready   | out       | std_logic                                         |             |
| s_axis_tdata    | in        | std_logic_vector(31 downto 0)                     |             |
| s_axis_tlast    | in        | std_logic                                         |             |
| s_axis_tvalid   | in        | std_logic                                         |             |
| dma_req_aclk    | in        | std_logic                                         |             |
| dma_req_rstn    | in        | std_logic                                         |             |
| dma_req_davalid | in        | std_logic                                         |             |
| dma_req_datype  | in        | std_logic_vector(1 downto 0)                      |             |
| dma_req_daready | out       | std_logic                                         |             |
| dma_req_drvalid | out       | std_logic                                         |             |
| dma_req_drtype  | out       | std_logic_vector(1 downto 0)                      |             |
| dma_req_drlast  | out       | std_logic                                         |             |
| dma_req_drready | in        | std_logic                                         |             |
## Signals

| Name            | Type                                          | Description     |
| --------------- | --------------------------------------------- | --------------- |
| config_reg      | std_logic_vector(S_AXI_DATA_WIDTH-1 downto 0) |                 |
| chstatus_reg    | std_logic_vector(S_AXI_DATA_WIDTH-1 downto 0) |                 |
| chstat_freq     | std_logic_vector(1 downto 0)                  |                 |
| chstat_gstat    | std_logic                                     |                 |
|  chstat_preem   | std_logic                                     |                 |
|  chstat_copy    | std_logic                                     |                 |
|  chstat_audio   | std_logic                                     |                 |
| sample_data_ack | std_logic                                     |                 |
| sample_data     | std_logic_vector(15 downto 0)                 |                 |
| conf_mode       | std_logic_vector(3 downto 0)                  |                 |
| conf_ratio      | std_logic_vector(7 downto 0)                  |                 |
| conf_tinten     | std_logic                                     |                 |
|  conf_txdata    | std_logic                                     |                 |
|  conf_txen      | std_logic                                     |                 |
| channel         | std_logic                                     |                 |
| enable          | boolean                                       |                 |
| fifo_data_out   | std_logic_vector(31 downto 0)                 |                 |
| fifo_data_ack   | std_logic                                     |                 |
| fifo_reset      | std_logic                                     |                 |
| tx_fifo_stb     | std_logic                                     |                 |
| wr_data         | std_logic_vector(31 downto 0)                 | Register access |
| rd_data         | std_logic_vector(31 downto 0)                 |                 |
| wr_addr         | integer range 0 to 3                          |                 |
| rd_addr         | integer range 0 to 3                          |                 |
| wr_stb          | std_logic                                     |                 |
| rd_ack          | std_logic                                     |                 |
## Processes
- sample_data_mux: ( fifo_data_out, channel )
- unnamed: ( s_axi_aclk )
- unnamed: ( rd_addr, config_reg, chstatus_reg )
## Instantiations

- TENC: tx_encoder
**Description**
Transmit encoder

- ctrlif: axi_ctrlif
