# Entity: axi_spdif_rx

- **File**: axi_spdif_rx.vhd
## Diagram

![Diagram](axi_spdif_rx.svg "Diagram")
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

| Generic name       | Type    | Value | Description |
| ------------------ | ------- | ----- | ----------- |
| C_S_AXI_DATA_WIDTH | integer | 32    |             |
| C_S_AXI_ADDR_WIDTH | integer | 32    |             |
| C_DMA_TYPE         | integer | 0     |             |
## Ports

| Port name       | Direction | Type                                                | Description           |
| --------------- | --------- | --------------------------------------------------- | --------------------- |
| rx_int_o        | out       | std_logic                                           | PDIF ports            |
| spdif_rx_i      | in        | std_logic                                           |                       |
| spdif_rx_i_dbg  | out       | std_logic                                           |                       |
| s_axi_aclk      | in        | std_logic                                           | XI Lite inter    face |
| s_axi_aresetn   | in        | std_logic                                           |                       |
| s_axi_awaddr    | in        | std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0)     |                       |
| s_axi_awvalid   | in        | std_logic                                           |                       |
| s_axi_wdata     | in        | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0)     |                       |
| s_axi_wstrb     | in        | std_logic_vector((C_S_AXI_DATA_WIDTH/8)-1 downto 0) |                       |
| s_axi_wvalid    | in        | std_logic                                           |                       |
| s_axi_bready    | in        | std_logic                                           |                       |
| s_axi_araddr    | in        | std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0)     |                       |
| s_axi_arvalid   | in        | std_logic                                           |                       |
| s_axi_rready    | in        | std_logic                                           |                       |
| s_axi_arready   | out       | std_logic                                           |                       |
| s_axi_rdata     | out       | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0)     |                       |
| s_axi_rresp     | out       | std_logic_vector(1 downto 0)                        |                       |
| s_axi_rvalid    | out       | std_logic                                           |                       |
| s_axi_wready    | out       | std_logic                                           |                       |
| s_axi_bresp     | out       | std_logic_vector(1 downto 0)                        |                       |
| s_axi_bvalid    | out       | std_logic                                           |                       |
| s_axi_awready   | out       | std_logic                                           |                       |
| s_axi_awprot    | in        | std_logic_vector(2 downto 0)                        |                       |
| s_axi_arprot    | in        | std_logic_vector(2 downto 0)                        |                       |
| m_axis_aclk     | in        | std_logic                                           | XI STREAM interface   |
| m_axis_tready   | in        | std_logic                                           |                       |
| m_axis_tdata    | out       | std_logic_vector(31 downto 0)                       |                       |
| m_axis_tlast    | out       | std_logic                                           |                       |
| m_axis_tvalid   | out       | std_logic                                           |                       |
| m_axis_tkeep    | out       | std_logic_vector(3 downto 0)                        |                       |
| dma_req_aclk    | in        | std_logic                                           | L330 DMA interface    |
| dma_req_rstn    | in        | std_logic                                           |                       |
| dma_req_davalid | in        | std_logic                                           |                       |
| dma_req_datype  | in        | std_logic_vector(1 downto 0)                        |                       |
| dma_req_daready | out       | std_logic                                           |                       |
| dma_req_drvalid | out       | std_logic                                           |                       |
| dma_req_drtype  | out       | std_logic_vector(1 downto 0)                        |                       |
| dma_req_drlast  | out       | std_logic                                           |                       |
| dma_req_drready | in        | std_logic                                           |                       |
## Signals

| Name           | Type                                              | Description |
| -------------- | ------------------------------------------------- | ----------- |
| wr_data        | std_logic_vector(31 downto 0)                     |             |
| rd_data        | std_logic_vector(31 downto 0)                     |             |
| wr_addr        | integer range 0 to 3                              |             |
| rd_addr        | integer range 0 to 3                              |             |
| wr_stb         | std_logic                                         |             |
| rd_ack         | std_logic                                         |             |
| version_reg    | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0)   |             |
| control_reg    | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0)   |             |
| chstatus_reg   | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0)   |             |
| sampled_data   | std_logic_vector(31 downto 0)                     |             |
| sample_ack     | std_logic                                         |             |
| sample_din     | std_logic_vector(31 downto 0)                     |             |
| sample_wr      | std_logic                                         |             |
| conf_rxen      | std_logic                                         |             |
| conf_sample    | std_logic                                         |             |
| conf_chas      | std_logic                                         |             |
| conf_valid     | std_logic                                         |             |
| conf_blken     | std_logic                                         |             |
| conf_valen     | std_logic                                         |             |
| conf_useren    | std_logic                                         |             |
| conf_staten    | std_logic                                         |             |
| conf_paren     | std_logic                                         |             |
| config_rd      | std_logic                                         |             |
| config_wr      | std_logic                                         |             |
| conf_mode      | std_logic_vector(3 downto 0)                      |             |
| conf_bits      | std_logic_vector(C_S_AXI_DATA_WIDTH - 1 downto 0) |             |
| conf_dout      | std_logic_vector(C_S_AXI_DATA_WIDTH - 1 downto 0) |             |
| fifo_data_out  | std_logic_vector(31 downto 0)                     |             |
| fifo_data_ack  | std_logic                                         |             |
| fifo_reset     | std_logic                                         |             |
| tx_fifo_stb    | std_logic                                         |             |
| enable         | boolean                                           |             |
| lock           | std_logic                                         |             |
| rx_data        | std_logic                                         |             |
| rx_data_en     | std_logic                                         |             |
| rx_block_start | std_logic                                         |             |
| rx_channel_a   | std_logic                                         |             |
| rx_error       | std_logic                                         |             |
| lock_evt       | std_logic                                         |             |
| ud_a_en        | std_logic                                         |             |
| ud_b_en        | std_logic                                         |             |
| cs_a_en        | std_logic                                         |             |
| cs_b_en        | std_logic                                         |             |
| rx_frame_start | std_logic                                         |             |
| istat_lsbf     | std_logic                                         |             |
| istat_hsbf     | std_logic                                         |             |
| istat_paritya  | std_logic                                         |             |
| istat_parityb  | std_logic                                         |             |
| sbuf_wr_adr    | std_logic_vector(C_S_AXI_ADDR_WIDTH - 2 downto 0) |             |
## Processes
- unnamed: ( s_axi_aclk )
- unnamed: ( rd_addr, version_reg, control_reg, chstatus_reg, sampled_data )
## Instantiations

- STAT: rx_status_reg
**Description**
------------------------------------------------------------------------------
 Status Register
------------------------------------------------------------------------------

- PDET: rx_phase_det
**Description**
------------------------------------------------------------------------------
------------------------------------------------------------------------------
 Phase decoder
------------------------------------------------------------------------------

- FDEC: rx_decode
**Description**
------------------------------------------------------------------------------
------------------------------------------------------------------------------
 Rx Decoder
------------------------------------------------------------------------------

- ctrlif: axi_ctrlif
