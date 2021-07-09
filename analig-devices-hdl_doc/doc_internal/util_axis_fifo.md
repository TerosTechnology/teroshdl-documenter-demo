# Entity: util_axis_fifo

## Diagram

![Diagram](util_axis_fifo.svg "Diagram")
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

| Generic name        | Type                | Value | Description |
| ------------------- | ------------------- | ----- | ----------- |
| DATA_WIDTH          |                     | 64    |             |
| ADDRESS_WIDTH       |                     | 5     |             |
| ASYNC_CLK           |                     | 1     |             |
| M_AXIS_REGISTERED   |                     | 1     |             |
| ADDRESS_WIDTH       | [ADDRESS_WIDTH-1:0] | 16    |             |
| ADDRESS_WIDTH       | [ADDRESS_WIDTH-1:0] | 16    |             |
| TLAST_EN            |                     | 0     |             |
| TKEEP_EN            |                     | 0     |             |
| REMOVE_NULL_BEAT_EN |                     | 0     |             |
## Ports

| Port name           | Direction | Type                | Description |
| ------------------- | --------- | ------------------- | ----------- |
| m_axis_aclk         | input     |                     |             |
| m_axis_aresetn      | input     |                     |             |
| m_axis_ready        | input     |                     |             |
| m_axis_valid        | output    |                     |             |
| m_axis_data         | output    | [DATA_WIDTH-1:0]    |             |
| m_axis_tkeep        | output    | [DATA_WIDTH/8-1:0]  |             |
| m_axis_tlast        | output    |                     |             |
| m_axis_level        | output    | [ADDRESS_WIDTH-1:0] |             |
| m_axis_empty        | output    |                     |             |
| m_axis_almost_empty | output    |                     |             |
| s_axis_aclk         | input     |                     |             |
| s_axis_aresetn      | input     |                     |             |
| s_axis_ready        | output    |                     |             |
| s_axis_valid        | input     |                     |             |
| s_axis_data         | input     | [DATA_WIDTH-1:0]    |             |
| s_axis_tkeep        | input     | [DATA_WIDTH/8-1:0]  |             |
| s_axis_tlast        | input     |                     |             |
| s_axis_room         | output    | [ADDRESS_WIDTH-1:0] |             |
| s_axis_full         | output    |                     |             |
| s_axis_almost_full  | output    |                     |             |
## Signals

| Name              | Type                | Description |
| ----------------- | ------------------- | ----------- |
| m_axis_data_int_s | wire [MEM_WORD-1:0] |             |
## Constants

| Name     | Type | Value      | Description |
| -------- | ---- | ---------- | ----------- |
| MEM_WORD |      | MEM_WORD-1 |             |
