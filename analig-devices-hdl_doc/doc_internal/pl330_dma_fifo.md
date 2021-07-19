# Entity: pl330_dma_fifo

- **File**: pl330_dma_fifo.vhd
## Diagram

![Diagram](pl330_dma_fifo.svg "Diagram")
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

| Generic name   | Type    | Value | Description                   |
| -------------- | ------- | ----- | ----------------------------- |
| RAM_ADDR_WIDTH | integer | 3     |                               |
| FIFO_DWIDTH    | integer | 32    |                               |
| FIFO_DIRECTION | integer | 0     | 0 = write FIFO, 1 = read FIFO |
## Ports

| Port name  | Direction | Type                                     | Description          |
| ---------- | --------- | ---------------------------------------- | -------------------- |
| clk        | in        | std_logic                                |                      |
| resetn     | in        | std_logic                                |                      |
| fifo_reset | in        | std_logic                                |                      |
| enable     | in        | Boolean                                  | Enable DMA interface |
| in_stb     | in        | std_logic                                | Write port           |
| in_ack     | out       | std_logic                                |                      |
| in_data    | in        | std_logic_vector(FIFO_DWIDTH-1 downto 0) |                      |
| out_stb    | out       | std_logic                                | Read port            |
| out_ack    | in        | std_logic                                |                      |
| out_data   | out       | std_logic_vector(FIFO_DWIDTH-1 downto 0) |                      |
| dclk       | in        | std_logic                                | PL330 DMA interface  |
| dresetn    | in        | std_logic                                |                      |
| davalid    | in        | std_logic                                |                      |
| daready    | out       | std_logic                                |                      |
| datype     | in        | std_logic_vector(1 downto 0)             |                      |
| drvalid    | out       | std_logic                                |                      |
| drready    | in        | std_logic                                |                      |
| drtype     | out       | std_logic_vector(1 downto 0)             |                      |
| drlast     | out       | std_logic                                |                      |
| DBG        | out       | std_logic_vector(7 downto 0)             |                      |
## Signals

| Name         | Type       | Description |
| ------------ | ---------- | ----------- |
| request_data | Boolean    |             |
| state        | state_type |             |
| i_in_ack     | std_logic  |             |
| i_out_stb    | std_logic  |             |
## Types

| Name       | Type                                                                                                                                         | Description |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| state_type | (IDLE,<br><span style="padding-left:20px"> REQUEST,<br><span style="padding-left:20px"> WAITING,<br><span style="padding-left:20px"> FLUSH)  |             |
## Processes
- unnamed: ( state )
- pl330_req_fsm: ( dclk )
## Instantiations

- fifo: dma_fifo
## State machines

![Diagram_state_machine_0]( stm_pl330_dma_fifo_00.svg "Diagram")