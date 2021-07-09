# Entity: axi_usb_fx3

## Diagram

![Diagram](axi_usb_fx3.svg "Diagram")
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
 
## Ports

| Port name     | Direction | Type   | Description |
| ------------- | --------- | ------ | ----------- |
| dma_rdy       | input     |        | gpif ii     |
| dma_wmk       | input     |        |             |
| fifo_rdy      | input     | [ 3:0] |             |
| pclk          | output    |        |             |
| data          | inout     | [31:0] |             |
| addr          | output    | [ 1:0] |             |
| slcs_n        | output    |        |             |
| slrd_n        | output    |        |             |
| sloe_n        | output    |        |             |
| slwr_n        | output    |        |             |
| pktend_n      | output    |        |             |
| epswitch_n    | output    |        |             |
| irq           | output    |        | irq         |
| debug_fx32dma | output    | [74:0] | DEBUG       |
| debug_dma2fx3 | output    | [73:0] |             |
| debug_status  | output    | [14:0] |             |
| s_axis_tdata  | input     | [31:0] | s2mm        |
| s_axis_tkeep  | input     | [ 3:0] |             |
| s_axis_tlast  | input     |        |             |
| s_axis_tvalid | input     |        |             |
| s_axis_tready | output    |        |             |
| m_axis_tready | input     |        | mm2s        |
| m_axis_tdata  | output    | [31:0] |             |
| m_axis_tkeep  | output    | [ 3:0] |             |
| m_axis_tlast  | output    |        |             |
| m_axis_tvalid | output    |        |             |
| s_axi_aclk    | input     |        | axi lite    |
| s_axi_aresetn | input     |        |             |
| s_axi_awvalid | input     |        |             |
| s_axi_awaddr  | input     | [15:0] |             |
| s_axi_awprot  | input     | [ 2:0] |             |
| s_axi_awready | output    |        |             |
| s_axi_wvalid  | input     |        |             |
| s_axi_wdata   | input     | [31:0] |             |
| s_axi_wstrb   | input     | [ 3:0] |             |
| s_axi_wready  | output    |        |             |
| s_axi_bvalid  | output    |        |             |
| s_axi_bresp   | output    | [ 1:0] |             |
| s_axi_bready  | input     |        |             |
| s_axi_arvalid | input     |        |             |
| s_axi_araddr  | input     | [15:0] |             |
| s_axi_arprot  | input     | [ 2:0] |             |
| s_axi_arready | output    |        |             |
| s_axi_rvalid  | output    |        |             |
| s_axi_rresp   | output    | [ 1:0] |             |
| s_axi_rdata   | output    | [31:0] |             |
| s_axi_rready  | input     |        |             |
## Signals

| Name              | Type        | Description               |
| ----------------- | ----------- | ------------------------- |
| up_rstn           | wire        | internal clocks & resets  |
| up_clk            | wire        |                           |
| up_raddr          | wire [13:0] | internal signals          |
| up_rdata          | wire [31:0] |                           |
| up_rack           | wire        |                           |
| up_wack           | wire        |                           |
| up_wreq           | wire        |                           |
| up_waddr          | wire [13:0] |                           |
| up_wdata          | wire [31:0] |                           |
| up_rreq_s         | wire        |                           |
| fifo0_header_size | wire [ 7:0] |                           |
| fifo0_buffer_size | wire [15:0] |                           |
| fifo1_header_size | wire [ 7:0] |                           |
| fifo1_buffer_size | wire [15:0] |                           |
| fifo2_header_size | wire [ 7:0] |                           |
| fifo2_buffer_size | wire [15:0] |                           |
| fifo3_header_size | wire [ 7:0] |                           |
| fifo3_buffer_size | wire [15:0] |                           |
| fifo4_header_size | wire [ 7:0] |                           |
| fifo4_buffer_size | wire [15:0] |                           |
| fifo5_header_size | wire [ 7:0] |                           |
| fifo5_buffer_size | wire [15:0] |                           |
| fifo6_header_size | wire [ 7:0] |                           |
| fifo6_buffer_size | wire [15:0] |                           |
| fifo7_header_size | wire [ 7:0] |                           |
| fifo7_buffer_size | wire [15:0] |                           |
| fifo8_header_size | wire [ 7:0] |                           |
| fifo8_buffer_size | wire [15:0] |                           |
| fifo9_header_size | wire [ 7:0] |                           |
| fifo9_buffer_size | wire [15:0] |                           |
| fifoa_header_size | wire [ 7:0] |                           |
| fifoa_buffer_size | wire [15:0] |                           |
| fifo0_direction   | wire        |                           |
| fifo1_direction   | wire        |                           |
| fifo2_direction   | wire        |                           |
| fifo3_direction   | wire        |                           |
| fifo4_direction   | wire        |                           |
| fifo5_direction   | wire        |                           |
| fifo6_direction   | wire        |                           |
| fifo7_direction   | wire        |                           |
| fifo8_direction   | wire        |                           |
| fifo9_direction   | wire        |                           |
| fifoa_direction   | wire        |                           |
| fifo_direction    | wire [10:0] |                           |
| fx32dma_valid     | wire        |                           |
| fx32dma_ready     | wire        |                           |
| fx32dma_data      | wire [31:0] |                           |
| fx32dma_sop       | wire        |                           |
| fx32dma_eop       | wire        |                           |
| dma2fx3_ready     | wire        |                           |
| dma2fx3_valid     | wire        |                           |
| dma2fx3_data      | wire [31:0] |                           |
| dma2fx3_eop       | wire        |                           |
| test_mode_tpm     | wire [ 2:0] |                           |
| test_mode_tpg     | wire [ 2:0] |                           |
| monitor_error     | wire        |                           |
| eot_fx32dma       | wire        |                           |
| eot_dma2fx3       | wire        |                           |
| error             | wire        |                           |
| fifo_num          | wire [ 4:0] |                           |
| fifo_ready        | wire [10:0] |                           |
| length_fx32dma    | wire [31:0] |                           |
| length_dma2fx3    | wire [31:0] |                           |
| trig              | wire        |                           |
| zlp               | wire        |                           |
## Instantiations

- ep_packetizer: axi_usb_fx3_core
**Description**
packetizer, TPM/TPG and DMA interface

- fx3_registers: axi_usb_fx3_reg
**Description**
register map

- fx3_if: axi_usb_fx3_if
**Description**
GPIF II interface

- i_up_axi: up_axi
**Description**
up bus interface

