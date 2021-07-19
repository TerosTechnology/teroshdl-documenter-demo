# Entity: axi_deltaSigma

- **File**: axi_deltaSigma.vhd
## Diagram

![Diagram](axi_deltaSigma.svg "Diagram")
## Description

***************************************************************************
***************************************************************************
Copyright 2019 (c) OscillatorIMP Digital
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

| Generic name         | Type    | Value | Description                                                                                                                                           |
| -------------------- | ------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| SLOT_WIDTH           | integer | 32    | ADD USER GENERICS BELOW THIS LINE ---------------                                                                                                     |
| C_S00_AXI_DATA_WIDTH | integer | 32    | ADD USER GENERICS ABOVE THIS LINE --------------- DO NOT EDIT BELOW THIS LINE --------------------- Bus protocol parameters, do not add to or delete  |
| C_S00_AXI_ADDR_WIDTH | integer | 4     |                                                                                                                                                       |
## Ports

| Port name          | Direction | Type                                                  | Description           |
| ------------------ | --------- | ----------------------------------------------------- | --------------------- |
| data_clk_i         | in        | std_logic                                             | Serial Data interface |
| bit_left_o         | out       | std_logic                                             |                       |
| bit_right_o        | out       | std_logic                                             |                       |
| dma_req_tx_aclk    | in        | std_logic                                             |                       |
| dma_req_tx_rstn    | in        | std_logic                                             |                       |
| dma_req_tx_davalid | in        | std_logic                                             |                       |
| dma_req_tx_datype  | in        | std_logic_vector(1 downto 0)                          |                       |
| dma_req_tx_daready | out       | std_logic                                             |                       |
| dma_req_tx_drvalid | out       | std_logic                                             |                       |
| dma_req_tx_drtype  | out       | std_logic_vector(1 downto 0)                          |                       |
| dma_req_tx_drlast  | out       | std_logic                                             |                       |
| dma_req_tx_drready | in        | std_logic                                             |                       |
| s00_axi_aclk       | in        | std_logic                                             | AXI bus interface     |
| s00_axi_aresetn    | in        | std_logic                                             |                       |
| s00_axi_awaddr     | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)     |                       |
| s00_axi_awvalid    | in        | std_logic                                             |                       |
| s00_axi_wdata      | in        | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)     |                       |
| s00_axi_wstrb      | in        | std_logic_vector((C_S00_AXI_DATA_WIDTH/8)-1 downto 0) |                       |
| s00_axi_wvalid     | in        | std_logic                                             |                       |
| s00_axi_bready     | in        | std_logic                                             |                       |
| s00_axi_araddr     | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)     |                       |
| s00_axi_arvalid    | in        | std_logic                                             |                       |
| s00_axi_rready     | in        | std_logic                                             |                       |
| s00_axi_arready    | out       | std_logic                                             |                       |
| s00_axi_rdata      | out       | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)     |                       |
| s00_axi_rresp      | out       | std_logic_vector(1 downto 0)                          |                       |
| s00_axi_rvalid     | out       | std_logic                                             |                       |
| s00_axi_wready     | out       | std_logic                                             |                       |
| s00_axi_bresp      | out       | std_logic_vector(1 downto 0)                          |                       |
| s00_axi_bvalid     | out       | std_logic                                             |                       |
| s00_axi_awready    | out       | std_logic                                             |                       |
| s00_axi_awprot     | in        | std_logic_vector(2 downto 0)                          |                       |
| s00_axi_arprot     | in        | std_logic_vector(2 downto 0)                          |                       |
## Signals

| Name                       | Type                          | Description |
| -------------------------- | ----------------------------- | ----------- |
| deltaSigma_reset           | std_logic                     |             |
| tx_fifo_reset              | std_logic                     |             |
| tx_enable                  | Boolean                       |             |
| tx_data_left               | std_logic_vector(31 downto 0) |             |
| tx_data_right              | std_logic_vector(31 downto 0) |             |
| tx_ack                     | std_logic                     |             |
| tx_stb                     | std_logic                     |             |
| const_1                    | std_logic                     |             |
| bclk_div_rate              | natural range 0 to 255        |             |
| lrclk_div_rate             | natural range 0 to 255        |             |
| DELTASIGMA_RESET_REG       | std_logic_vector(31 downto 0) |             |
| DELTASIGMA_CONTROL_REG     | std_logic_vector(31 downto 0) |             |
| DELTASIGMA_CLK_CONTROL_REG | std_logic_vector(31 downto 0) |             |
| drain_tx_dma               | std_logic                     |             |
| wr_data                    | std_logic_vector(31 downto 0) |             |
| rd_data                    | std_logic_vector(31 downto 0) |             |
| wr_addr                    | integer range 0 to 3          |             |
| rd_addr                    | integer range 0 to 3          |             |
| wr_stb                     | std_logic                     |             |
| rd_ack                     | std_logic                     |             |
| tx_fifo_stb                | std_logic                     |             |
## Constants

| Name           | Type    | Value                         | Description        |
| -------------- | ------- | ----------------------------- | ------------------ |
| FIFO_AWIDTH    | integer |  integer(ceil(log2(real(8)))) |                    |
| RAM_ADDR_WIDTH | integer |  7                            | Audio samples FIFO |
## Types

| Name     | Type | Description |
| -------- | ---- | ----------- |
| RAM_TYPE |      |             |
## Processes
- unnamed: ( rd_addr, DELTASIGMA_CONTROL_REG, DELTASIGMA_CLK_CONTROL_REG )
- unnamed: ( s00_axi_aclk )
## Instantiations

- tx_fifo: pl330_dma_fifo
- ctrl: deltaSigma_controller
- ctrlif: axi_ctrlif
