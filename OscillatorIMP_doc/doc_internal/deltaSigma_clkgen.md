# Entity: deltaSigma_clkgen

- **File**: deltaSigma_clkgen.vhd
## Diagram

![Diagram](deltaSigma_clkgen.svg "Diagram")
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
## Ports

| Port name      | Direction | Type                   | Description      |
| -------------- | --------- | ---------------------- | ---------------- |
| clk            | in        | std_logic              |  System clock    |
| resetn         | in        | std_logic              |  System reset    |
| enable         | in        | Boolean                |  Enable clockgen |
| tick           | in        | std_logic              |                  |
| bclk_div_rate  | in        | natural range 0 to 255 |                  |
| lrclk_div_rate | in        | natural range 0 to 255 |                  |
| bclk           | out       | std_logic              |  Bit Clock       |
| frame_sync     | out       | std_logic              |                  |
## Signals

| Name        | Type                   | Description |
| ----------- | ---------------------- | ----------- |
| reset_int   | Boolean                |             |
| bclk_count  | natural range 0 to 255 |             |
| lrclk_count | natural range 0 to 255 |             |
| bclk_int    | std_logic              |             |
| lrclk_int   | std_logic              |             |
| lrclk_tick  | Boolean                |             |
## Processes
- bclk_gen: ( clk )
</br>**Description**
---------------------------------------------------------------------------------  Serial clock generation BCLK_O --------------------------------------------------------------------------------- 
- lrclk_gen: ( clk )
</br>**Description**
---------------------------------------------------------------------------------  Frame clock generator LRCLK_O --------------------------------------------------------------------------------- 
