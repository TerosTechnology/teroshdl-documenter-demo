# Entity: axi_ctrlif

- **File**: axi_ctrlif.vhd
## Diagram

![Diagram](axi_ctrlif.svg "Diagram")
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

| Generic name       | Type    | Value | Description |
| ------------------ | ------- | ----- | ----------- |
| C_NUM_REG          | integer | 32    |             |
| C_S_AXI_DATA_WIDTH | integer | 32    |             |
| C_S_AXI_ADDR_WIDTH | integer | 32    |             |
## Ports

| Port name     | Direction | Type                                                | Description       |
| ------------- | --------- | --------------------------------------------------- | ----------------- |
| s_axi_aclk    | in        | std_logic                                           | AXI bus interface |
| s_axi_aresetn | in        | std_logic                                           |                   |
| s_axi_awaddr  | in        | std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0)     |                   |
| s_axi_awvalid | in        | std_logic                                           |                   |
| s_axi_wdata   | in        | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0)     |                   |
| s_axi_wstrb   | in        | std_logic_vector((C_S_AXI_DATA_WIDTH/8)-1 downto 0) |                   |
| s_axi_wvalid  | in        | std_logic                                           |                   |
| s_axi_bready  | in        | std_logic                                           |                   |
| s_axi_araddr  | in        | std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0)     |                   |
| s_axi_arvalid | in        | std_logic                                           |                   |
| s_axi_rready  | in        | std_logic                                           |                   |
| s_axi_arready | out       | std_logic                                           |                   |
| s_axi_rdata   | out       | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0)     |                   |
| s_axi_rresp   | out       | std_logic_vector(1 downto 0)                        |                   |
| s_axi_rvalid  | out       | std_logic                                           |                   |
| s_axi_wready  | out       | std_logic                                           |                   |
| s_axi_bresp   | out       | std_logic_vector(1 downto 0)                        |                   |
| s_axi_bvalid  | out       | std_logic                                           |                   |
| s_axi_awready | out       | std_logic                                           |                   |
| rd_addr       | out       | integer range 0 to C_NUM_REG - 1                    |                   |
| rd_data       | in        | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0)     |                   |
| rd_ack        | out       | std_logic                                           |                   |
| rd_stb        | in        | std_logic                                           |                   |
| wr_addr       | out       | integer range 0 to C_NUM_REG - 1                    |                   |
| wr_data       | out       | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0)     |                   |
| wr_ack        | in        | std_logic                                           |                   |
| wr_stb        | out       | std_logic                                           |                   |
## Signals

| Name     | Type       | Description |
| -------- | ---------- | ----------- |
| rd_state | state_type |             |
| wr_state | state_type |             |
## Types

| Name       | Type                                                                                       | Description |
| ---------- | ------------------------------------------------------------------------------------------ | ----------- |
| state_type | (IDLE,<br><span style="padding-left:20px"> RESP,<br><span style="padding-left:20px"> ACK)  |             |
## Processes
- unnamed: ( s_axi_aclk )
- unnamed: ( s_axi_aclk )
## State machines

![Diagram_state_machine_0]( stm_axi_ctrlif_00.svg "Diagram")![Diagram_state_machine_1]( stm_axi_ctrlif_11.svg "Diagram")