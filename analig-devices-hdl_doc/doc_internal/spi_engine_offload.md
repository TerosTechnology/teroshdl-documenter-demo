# Entity: spi_engine_offload

- **File**: spi_engine_offload.v
## Diagram

![Diagram](spi_engine_offload.svg "Diagram")
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

| Generic name          | Type | Value | Description                             |
| --------------------- | ---- | ----- | --------------------------------------- |
| ASYNC_SPI_CLK         |      | 0     |                                         |
| ASYNC_TRIG            |      | 0     |                                         |
| CMD_MEM_ADDRESS_WIDTH |      | 4     |                                         |
| SDO_MEM_ADDRESS_WIDTH |      | 4     |                                         |
| DATA_WIDTH            |      | 8     | Valid data widths values are 8/16/24/32 |
| NUM_OF_SDI            |      | 1     |                                         |
## Ports

| Port name         | Direction | Type                            | Description |
| ----------------- | --------- | ------------------------------- | ----------- |
| ctrl_clk          | input     |                                 |             |
| ctrl_cmd_wr_en    | input     |                                 |             |
| ctrl_cmd_wr_data  | input     | [15:0]                          |             |
| ctrl_sdo_wr_en    | input     |                                 |             |
| ctrl_sdo_wr_data  | input     | [(DATA_WIDTH-1):0]              |             |
| ctrl_enable       | input     |                                 |             |
| ctrl_enabled      | output    |                                 |             |
| ctrl_mem_reset    | input     |                                 |             |
| status_sync_valid | output    |                                 |             |
| status_sync_ready | input     |                                 |             |
| status_sync_data  | output    | [7:0]                           |             |
| spi_clk           | input     |                                 |             |
| spi_resetn        | input     |                                 |             |
| trigger           | input     |                                 |             |
| cmd_valid         | output    |                                 |             |
| cmd_ready         | input     |                                 |             |
| cmd               | output    | [15:0]                          |             |
| sdo_data_valid    | output    |                                 |             |
| sdo_data_ready    | input     |                                 |             |
| sdo_data          | output    | [(DATA_WIDTH-1):0]              |             |
| sdi_data_valid    | input     |                                 |             |
| sdi_data_ready    | output    |                                 |             |
| sdi_data          | input     | [(NUM_OF_SDI * DATA_WIDTH-1):0] |             |
| sync_valid        | input     |                                 |             |
| sync_ready        | output    |                                 |             |
| sync_data         | input     | [7:0]                           |             |
| offload_sdi_valid | output    |                                 |             |
| offload_sdi_ready | input     |                                 |             |
| offload_sdi_data  | output    | [(NUM_OF_SDI * DATA_WIDTH-1):0] |             |
## Signals

| Name                 | Type                             | Description                                                                                                                                                                                          |
| -------------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| spi_active           | reg                              |                                                                                                                                                                                                      |
| ctrl_cmd_wr_addr     | reg [CMD_MEM_ADDRESS_WIDTH-1:0]  |                                                                                                                                                                                                      |
| spi_cmd_rd_addr      | reg [CMD_MEM_ADDRESS_WIDTH-1:0]  |                                                                                                                                                                                                      |
| ctrl_sdo_wr_addr     | reg [SDO_MEM_ADDRESS_WIDTH-1:0]  |                                                                                                                                                                                                      |
| spi_sdo_rd_addr      | reg [SDO_MEM_ADDRESS_WIDTH-1:0]  |                                                                                                                                                                                                      |
| cmd_mem              | reg [15:0]                       |                                                                                                                                                                                                      |
| sdo_mem              | reg [(DATA_WIDTH-1):0]           |                                                                                                                                                                                                      |
| cmd_int_s            | wire [15:0]                      |                                                                                                                                                                                                      |
| spi_cmd_rd_addr_next | wire [CMD_MEM_ADDRESS_WIDTH-1:0] |                                                                                                                                                                                                      |
| spi_enable           | wire                             |                                                                                                                                                                                                      |
| ctrl_sync_id_init    | reg [ 7:0]                       | SYNC ID counter. The offload module increments the sync_id on each  * transaction. The initial value of the sync_id is the value of the last  * sync_id command loaded into the command buffer.  */  |
| ctrl_sync_id_load    | reg                              |                                                                                                                                                                                                      |
| spi_sync_id_counter  | reg [ 7:0]                       |                                                                                                                                                                                                      |
| spi_sync_id_init_s   | wire [ 7:0]                      |                                                                                                                                                                                                      |
| spi_sync_id_load_s   | wire                             |                                                                                                                                                                                                      |
| trigger_s            | wire                             |                                                                                                                                                                                                      |
## Processes
- unnamed: ( @(posedge ctrl_clk) )
- unnamed: ( @(posedge spi_clk) )
- unnamed: ( @(posedge spi_clk) )
- unnamed: ( @(posedge spi_clk) )
- unnamed: ( @(posedge spi_clk) )
- unnamed: ( @(posedge ctrl_clk) )
- unnamed: ( @(posedge ctrl_clk) )
- unnamed: ( @(posedge ctrl_clk) )
- unnamed: ( @(posedge ctrl_clk) )
## Instantiations

- i_sync_sync_id_load: sync_event
- i_sync_sync_id: sync_bits
- i_sync_trigger: sync_bits
