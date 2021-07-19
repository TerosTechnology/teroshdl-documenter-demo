# Entity: util_dacfifo

- **File**: util_dacfifo.v
## Diagram

![Diagram](util_dacfifo.svg "Diagram")
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

| Generic name  | Type | Value | Description |
| ------------- | ---- | ----- | ----------- |
| ADDRESS_WIDTH |      | 6     |             |
| DATA_WIDTH    |      | 128   |             |
## Ports

| Port name     | Direction | Type               | Description   |
| ------------- | --------- | ------------------ | ------------- |
| dma_clk       | input     |                    | DMA interface |
| dma_rst       | input     |                    |               |
| dma_valid     | input     |                    |               |
| dma_data      | input     | [(DATA_WIDTH-1):0] |               |
| dma_ready     | output    |                    |               |
| dma_xfer_req  | input     |                    |               |
| dma_xfer_last | input     |                    |               |
| dac_clk       | input     |                    | DAC interface |
| dac_rst       | input     |                    |               |
| dac_valid     | input     |                    |               |
| dac_data      | output    | [(DATA_WIDTH-1):0] |               |
| dac_dunf      | output    |                    |               |
| dac_xfer_out  | output    |                    |               |
| bypass        | input     |                    |               |
## Signals

| Name                 | Type                          | Description         |
| -------------------- | ----------------------------- | ------------------- |
| dma_init             | reg                           | internal registers  |
| dma_waddr            | reg     [(ADDRESS_WIDTH-1):0] |                     |
| dma_waddr_g          | reg     [(ADDRESS_WIDTH-1):0] |                     |
| dma_lastaddr_g       | reg     [(ADDRESS_WIDTH-1):0] |                     |
| dma_bypass           | reg                           |                     |
| dma_bypass_m1        | reg                           |                     |
| dma_xfer_req_d1      | reg                           |                     |
| dma_xfer_req_d2      | reg                           |                     |
| dma_xfer_out_fifo    | reg                           |                     |
| dac_raddr            | reg     [(ADDRESS_WIDTH-1):0] |                     |
| dac_waddr            | reg     [(ADDRESS_WIDTH-1):0] |                     |
| dac_waddr_m1         | reg     [(ADDRESS_WIDTH-1):0] |                     |
| dac_waddr_m2         | reg     [(ADDRESS_WIDTH-1):0] |                     |
| dac_addr_diff        | reg     [(ADDRESS_WIDTH-1):0] |                     |
| dac_lastaddr_m1      | reg     [(ADDRESS_WIDTH-1):0] |                     |
| dac_lastaddr_m2      | reg     [(ADDRESS_WIDTH-1):0] |                     |
| dac_lastaddr         | reg     [(ADDRESS_WIDTH-1):0] |                     |
| dac_mem_ready        | reg                           |                     |
| dac_xfer_req_m1      | reg                           |                     |
| dac_xfer_req         | reg                           |                     |
| dac_xfer_req_d       | reg                           |                     |
| dac_xfer_out_fifo    | reg                           |                     |
| dac_xfer_out_fifo_m1 | reg                           |                     |
| dac_xfer_out_fifo_d  | reg                           |                     |
| dac_bypass           | reg                           |                     |
| dac_bypass_m1        | reg                           |                     |
| dma_rst_int_s        | wire                          | internal wires      |
| dma_wren_s           | wire                          |                     |
| dma_xfer_posedge_s   | wire                          |                     |
| dma_ready_bypass_s   | wire                          |                     |
| dac_data_fifo_s      | wire [(DATA_WIDTH-1):0]       |                     |
| dac_data_bypass_s    | wire [(DATA_WIDTH-1):0]       |                     |
| dac_addr_diff_s      | wire [ADDRESS_WIDTH:0]        |                     |
| dma_waddr_b2g_s      | wire [(ADDRESS_WIDTH-1):0]    |                     |
| dac_waddr_g2b_s      | wire [(ADDRESS_WIDTH-1):0]    |                     |
| dac_lastaddr_g2b_s   | wire [(ADDRESS_WIDTH-1):0]    |                     |
| dac_mem_ren_s        | wire                          |                     |
| dac_xfer_posedge_s   | wire                          |                     |
| dac_rst_int_s        | wire                          |                     |
## Constants

| Name              | Type | Value | Description |
| ----------------- | ---- | ----- | ----------- |
| FIFO_THRESHOLD_HI |      | - 4   |             |
## Processes
- unnamed: ( @(posedge dma_clk) )
**Description**
internal reset generation

- unnamed: ( @(posedge dma_clk) )
**Description**
status register indicating that the module is in initialization phase

- unnamed: ( @(posedge dma_clk) )
- unnamed: ( @(posedge dma_clk) )
**Description**
save the last write address

- unnamed: ( @(posedge dac_clk) )
**Description**
DAC / Read interface

- unnamed: ( @(posedge dac_clk) )
**Description**
The memory module is ready if it's not empty

- unnamed: ( @(posedge dac_clk) )
**Description**
sync lastaddr to dac clock domain

- unnamed: ( @(posedge dac_clk) )
- unnamed: ( @(posedge dac_clk) )
**Description**
define underflow
underflow make sense just if bypass is enabled

- unnamed: ( @(posedge dma_clk) )
- unnamed: ( @(posedge dac_clk) )
- unnamed: ( @(posedge dma_clk) )
**Description**
the util_dacfifo is always ready for the DMA

- unnamed: ( @(posedge dac_clk) )
## Instantiations

- i_dma_waddr_b2g: ad_b2g
- i_dac_waddr_g2b: ad_g2b
- i_dac_lastaddr_g2b: ad_g2b
- i_mem_fifo: ad_mem
**Description**
memory instantiation

- i_dacfifo_bypass: util_dacfifo_bypass
**Description**
bypass logic

