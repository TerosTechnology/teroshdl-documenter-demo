# Entity: avl_adxcfg

- **File**: avl_adxcfg.v
## Diagram

![Diagram](avl_adxcfg.svg "Diagram")
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
| ADDRESS_WIDTH |      | 10    |             |
## Ports

| Port name              | Direction | Type                | Description      |
| ---------------------- | --------- | ------------------- | ---------------- |
| rcfg_clk               | input     |                     | reconfig sharing |
| rcfg_reset_n           | input     |                     |                  |
| rcfg_in_read_0         | input     |                     |                  |
| rcfg_in_write_0        | input     |                     |                  |
| rcfg_in_address_0      | input     | [ADDRESS_WIDTH-1:0] |                  |
| rcfg_in_writedata_0    | input     | [31:0]              |                  |
| rcfg_in_readdata_0     | output    | [31:0]              |                  |
| rcfg_in_waitrequest_0  | output    |                     |                  |
| rcfg_in_read_1         | input     |                     |                  |
| rcfg_in_write_1        | input     |                     |                  |
| rcfg_in_address_1      | input     | [ADDRESS_WIDTH-1:0] |                  |
| rcfg_in_writedata_1    | input     | [31:0]              |                  |
| rcfg_in_readdata_1     | output    | [31:0]              |                  |
| rcfg_in_waitrequest_1  | output    |                     |                  |
| rcfg_out_read_0        | output    |                     |                  |
| rcfg_out_write_0       | output    |                     |                  |
| rcfg_out_address_0     | output    | [ADDRESS_WIDTH-1:0] |                  |
| rcfg_out_writedata_0   | output    | [31:0]              |                  |
| rcfg_out_readdata_0    | input     | [31:0]              |                  |
| rcfg_out_waitrequest_0 | input     |                     |                  |
| rcfg_out_read_1        | output    |                     |                  |
| rcfg_out_write_1       | output    |                     |                  |
| rcfg_out_address_1     | output    | [ADDRESS_WIDTH-1:0] |                  |
| rcfg_out_writedata_1   | output    | [31:0]              |                  |
| rcfg_out_readdata_1    | input     | [31:0]              |                  |
| rcfg_out_waitrequest_1 | input     |                     |                  |
## Signals

| Name                   | Type                        | Description         |
| ---------------------- | --------------------------- | ------------------- |
| rcfg_select            | reg     [ 1:0]              | internal registers  |
| rcfg_read_int          | reg                         |                     |
| rcfg_write_int         | reg                         |                     |
| rcfg_address_int       | reg     [ADDRESS_WIDTH-1:0] |                     |
| rcfg_writedata_int     | reg     [31:0]              |                     |
| rcfg_readdata_int      | reg     [31:0]              |                     |
| rcfg_waitrequest_int_0 | reg                         |                     |
| rcfg_waitrequest_int_1 | reg                         |                     |
| rcfg_readdata_s        | wire [31:0]                 | internal signals    |
| rcfg_waitrequest_s     | wire                        |                     |
## Processes
- unnamed: ( @(negedge rcfg_reset_n or posedge rcfg_clk) )
