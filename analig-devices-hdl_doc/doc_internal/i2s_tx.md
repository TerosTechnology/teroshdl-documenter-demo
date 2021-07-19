# Entity: i2s_tx

- **File**: i2s_tx.vhd
## Diagram

![Diagram](i2s_tx.svg "Diagram")
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

| Generic name | Type    | Value | Description       |
| ------------ | ------- | ----- | ----------------- |
| C_SLOT_WIDTH | integer | 24    | Width of one Slot |
| C_NUM        | integer | 1     |                   |
## Ports

| Port name    | Direction | Type                                      | Description           |
| ------------ | --------- | ----------------------------------------- | --------------------- |
| clk          | in        | std_logic                                 | System clock          |
| resetn       | in        | std_logic                                 | System reset          |
| enable       | in        | Boolean                                   | Enable TX             |
| bclk         | in        | std_logic                                 | Bit Clock             |
| channel_sync | in        | std_logic                                 | Channel Sync          |
| frame_sync   | in        | std_logic                                 | Frame Sync            |
| sdata        | out       | std_logic_vector(C_NUM - 1 downto 0)      | Serial Data Output    |
| ack          | out       | std_logic                                 | Request new Slot Data |
| stb          | in        | std_logic                                 | Request new Slot Data |
| data         | in        | std_logic_vector(C_SLOT_WIDTH-1 downto 0) | Slot Data in          |
## Signals

| Name                | Type      | Description |
| ------------------- | --------- | ----------- |
| data_int            | mem       |             |
| reset_int           | Boolean   |             |
| enable_int          | Boolean   |             |
| bit_sync            | std_logic |             |
| channel_sync_int    | std_logic |             |
| frame_sync_int      | std_logic |             |
| channel_sync_int_d1 | std_logic |             |
| bclk_d1             | std_logic |             |
## Types

| Name | Type | Description |
| ---- | ---- | ----------- |
| mem  |      |             |
## Processes
- unnamed: ( clk )
- enable_sync: ( clk )
