# Entity: dmac_address_generator

- **File**: address_generator.v
## Diagram

![Diagram](address_generator.svg "Diagram")
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

| Generic name          | Type | Value                    | Description |
| --------------------- | ---- | ------------------------ | ----------- |
| ID_WIDTH              |      | 3                        |             |
| DMA_DATA_WIDTH        |      | 64                       |             |
| DMA_ADDR_WIDTH        |      | 32                       |             |
| BEATS_PER_BURST_WIDTH |      | 4                        |             |
| BYTES_PER_BEAT_WIDTH  |      | $clog2(DMA_DATA_WIDTH/8) |             |
| LENGTH_WIDTH          |      | 8                        |             |
## Ports

| Port name                  | Direction | Type                                    | Description |
| -------------------------- | --------- | --------------------------------------- | ----------- |
| clk                        | input     |                                         |             |
| resetn                     | input     |                                         |             |
| req_valid                  | input     |                                         |             |
| req_ready                  | output    |                                         |             |
| req_address                | input     | [DMA_ADDR_WIDTH-1:BYTES_PER_BEAT_WIDTH] |             |
| id                         | output    | [ID_WIDTH-1:0]                          |             |
| request_id                 | input     | [ID_WIDTH-1:0]                          |             |
| bl_valid                   | input     |                                         |             |
| bl_ready                   | output    |                                         |             |
| measured_last_burst_length | input     | [BEATS_PER_BURST_WIDTH-1:0]             |             |
| eot                        | input     |                                         |             |
| enable                     | input     |                                         |             |
| enabled                    | output    |                                         |             |
| addr_ready                 | input     |                                         |             |
| addr_valid                 | output    |                                         |             |
| addr                       | output    | [DMA_ADDR_WIDTH-1:0]                    |             |
| len                        | output    | [LENGTH_WIDTH-1:0]                      |             |
| size                       | output    | [ 2:0]                                  |             |
| burst                      | output    | [ 1:0]                                  |             |
| prot                       | output    | [ 2:0]                                  |             |
| cache                      | output    | [ 3:0]                                  |             |
## Signals

| Name           | Type                                          | Description |
| -------------- | --------------------------------------------- | ----------- |
| length         | reg [LENGTH_WIDTH-1:0]                        |             |
| address        | reg [DMA_ADDR_WIDTH-BYTES_PER_BEAT_WIDTH-1:0] |             |
| last_burst_len | reg [BEATS_PER_BURST_WIDTH-1:0]               |             |
| addr_valid_d1  | reg                                           |             |
| last           | reg                                           |             |
## Constants

| Name                | Type | Value     | Description |
| ------------------- | ---- | --------- | ----------- |
| MAX_BEATS_PER_BURST |      | undefined |             |
| MAX_LENGTH          |      | undefined |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 If we already asserted addr_valid we have to wait until it is accepted before  we can disable the address generator. 
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
