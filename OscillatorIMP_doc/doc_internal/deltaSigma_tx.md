# Entity: deltaSigma_tx

## Diagram

![Diagram](deltaSigma_tx.svg "Diagram")
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

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| C_SLOT_WIDTH | integer | 32    |             |
## Ports

| Port name   | Direction | Type                                      | Description           |
| ----------- | --------- | ----------------------------------------- | --------------------- |
| clk         | in        | std_logic                                 | System clock          |
| resetn      | in        | std_logic                                 | System reset          |
| enable      | in        | Boolean                                   | Enable TX             |
| bit_left_o  | out       | std_logic                                 |                       |
| bit_right_o | out       | std_logic                                 |                       |
| bclk        | in        | std_logic                                 | Bit Clock             |
| frame_sync  | in        | std_logic                                 | Frame Sync            |
| ack         | out       | std_logic                                 | Request new Slot Data |
| stb         | in        | std_logic                                 | Request new Slot Data |
| data_left   | in        | std_logic_vector(C_SLOT_WIDTH-1 downto 0) | Slot Data in          |
| data_right  | in        | std_logic_vector(C_SLOT_WIDTH-1 downto 0) | Slot Data in          |
## Signals

| Name               | Type                                      | Description |
| ------------------ | ----------------------------------------- | ----------- |
| left_data_int      | std_logic_vector(C_SLOT_WIDTH-1 downto 0) |             |
|  right_data_int    | std_logic_vector(C_SLOT_WIDTH-1 downto 0) |             |
| reset_int          | Boolean                                   |             |
| rst_s              | std_logic                                 |             |
| enable_int         | Boolean                                   |             |
| bit_sync           | std_logic                                 |             |
| frame_sync_int     | std_logic                                 |             |
| frame_sync_int_d1  | std_logic                                 |             |
| bclk_d1            | std_logic                                 |             |
| left_dac_s         | std_logic                                 |             |
|  right_dac_s       | std_logic                                 |             |
| data_left_shift_s  | std_logic_vector(C_SLOT_WIDTH-1 downto 0) |             |
| data_right_shift_s | std_logic_vector(C_SLOT_WIDTH-1 downto 0) |             |
## Processes
- unnamed: ( clk )
- serialize_data: ( clk )
- enable_sync: ( clk )
## Instantiations

- left_deltaSigma_inst: deltaSigma
- right_deltaSigma_inst: deltaSigma
