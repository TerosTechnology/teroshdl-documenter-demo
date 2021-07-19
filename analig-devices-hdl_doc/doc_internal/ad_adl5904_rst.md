# Entity: ad_adl5904_rst

- **File**: ad_adl5904_rst.v
## Diagram

![Diagram](ad_adl5904_rst.svg "Diagram")
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
 
## Ports

| Port name     | Direction | Type | Description |
| ------------- | --------- | ---- | ----------- |
| sys_cpu_clk   | input     |      |             |
| rf_peak_det_n | input     |      |             |
| rf_peak_rst   | output    |      |             |
## Signals

| Name              | Type | Description         |
| ----------------- | ---- | ------------------- |
| rf_peak_det_n_d   | reg  | internal registers  |
| rf_peak_det_enb_d | reg  |                     |
| rf_peak_rst_enb   | reg  |                     |
| rf_peak_rst_int   | reg  |                     |
| rf_peak_det_enb_s | wire | internal signals    |
| rf_peak_rst_1_s   | wire |                     |
| rf_peak_rst_0_s   | wire |                     |
## Processes
- unnamed: ( @(posedge sys_cpu_clk) )
