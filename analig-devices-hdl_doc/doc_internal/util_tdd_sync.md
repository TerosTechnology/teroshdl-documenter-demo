# Entity: util_tdd_sync

- **File**: util_tdd_sync.v
## Diagram

![Diagram](util_tdd_sync.svg "Diagram")
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
 Simple pulse generator for TDD control
 The module has two modes. In function of the state of sync_mode,
 the syncronization signal (sync_out) can get its value from an external
 source or from its internal generator.
 
## Generics

| Generic name    | Type | Value     | Description |
| --------------- | ---- | --------- | ----------- |
| TDD_SYNC_PERIOD |      | 100000000 |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| clk       | input     |      |             |
| rstn      | input     |      |             |
| sync_mode | input     |      |             |
| sync_in   | input     |      |             |
| sync_out  | output    |      |             |
## Signals

| Name          | Type | Description |
| ------------- | ---- | ----------- |
| sync_mode_d1  | reg  |             |
| sync_mode_d2  | reg  |             |
| sync_internal | wire |             |
| sync_external | wire |             |
## Processes
- unnamed: ( @(posedge clk) )
**Description**
synchronization logic

- unnamed: ( @(posedge clk) )
## Instantiations

- i_tdd_sync: util_pulse_gen
**Description**
pulse generator

