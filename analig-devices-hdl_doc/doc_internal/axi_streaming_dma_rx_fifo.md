# Entity: axi_streaming_dma_rx_fifo

- **File**: axi_streaming_dma_rx_fifo.vhd
## Diagram

![Diagram](axi_streaming_dma_rx_fifo.svg "Diagram")
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

| Generic name   | Type    | Value | Description |
| -------------- | ------- | ----- | ----------- |
| RAM_ADDR_WIDTH | integer | 3     |             |
| FIFO_DWIDTH    | integer | 32    |             |
## Ports

| Port name     | Direction | Type                                     | Description          |
| ------------- | --------- | ---------------------------------------- | -------------------- |
| clk           | in        | std_logic                                |                      |
| resetn        | in        | std_logic                                |                      |
| fifo_reset    | in        | std_logic                                |                      |
| enable        | in        | Boolean                                  | Enable DMA interface |
| period_len    | in        | integer range 0 to 65535                 |                      |
| m_axis_aclk   | in        | std_logic                                | Read port            |
| m_axis_tready | in        | std_logic                                |                      |
| m_axis_tdata  | out       | std_logic_vector(FIFO_DWIDTH-1 downto 0) |                      |
| m_axis_tlast  | out       | std_logic                                |                      |
| m_axis_tvalid | out       | std_logic                                |                      |
| m_axis_tkeep  | out       | std_logic_vector(3 downto 0)             |                      |
| in_stb        | in        | std_logic                                | Write port           |
| in_ack        | out       | std_logic                                |                      |
| in_data       | in        | std_logic_vector(FIFO_DWIDTH-1 downto 0) |                      |
## Signals

| Name         | Type                     | Description |
| ------------ | ------------------------ | ----------- |
| out_stb      | std_logic                |             |
| period_count | integer range 0 to 65535 |             |
| last         | std_logic                |             |
## Processes
- period_counter: ( m_axis_aclk )
## Instantiations

- fifo: dma_fifo
