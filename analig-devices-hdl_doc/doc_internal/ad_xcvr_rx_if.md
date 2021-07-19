# Entity: ad_xcvr_rx_if

- **File**: ad_xcvr_rx_if.v
## Diagram

![Diagram](ad_xcvr_rx_if.svg "Diagram")
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

| Generic name    | Type | Value               | Description |
| --------------- | ---- | ------------------- | ----------- |
| OCTETS_PER_BEAT |      | 4                   |             |
| DW              |      | OCTETS_PER_BEAT * 8 |             |
## Ports

| Port name  | Direction | Type                  | Description    |
| ---------- | --------- | --------------------- | -------------- |
| rx_clk     | input     |                       | jesd interface |
| rx_ip_sof  | input     | [OCTETS_PER_BEAT-1:0] |                |
| rx_ip_data | input     | [DW-1:0]              |                |
| rx_sof     | output    |                       |                |
| rx_data    | output    | [DW-1:0]              |                |
## Signals

| Name           | Type                          | Description                                                                                                                                                                                                            |
| -------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rx_ip_data_d   | reg     [DW-1:0]              | rx_ip_data: The temporal ordering of the octets is from LSB to MSB, this means the octet placed in the lowest 8 bits was received first, the octet placed in the highest 8 bits was received last. internal registers  |
| rx_ip_sof_hold | reg     [OCTETS_PER_BEAT-1:0] |                                                                                                                                                                                                                        |
| rx_ip_sof_d    | reg     [OCTETS_PER_BEAT-1:0] |                                                                                                                                                                                                                        |
| rx_data_s      | wire [OCTETS_PER_BEAT*DW-1:0] |                                                                                                                                                                                                                        |
| j              | integer                       |                                                                                                                                                                                                                        |
## Processes
- unnamed: ( @(posedge rx_clk) )
- unnamed: ( @(posedge rx_clk) )
