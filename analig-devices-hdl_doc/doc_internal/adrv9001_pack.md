# Entity: adrv9001_pack

- **File**: adrv9001_pack.v
## Diagram

![Diagram](adrv9001_pack.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2020 (c) Analog Devices, Inc. All rights reserved.
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
 Pack two input beats into one and align it based on start of frame
 Frame size 2 beats:
 Temporal ordering of input:
   idata : MS Beat, LS Beat, MS Beat, LS Beat, ...
   sof   :       1,       0,       1,       0, ...
 Format of output beats:  {MS Beat, LS Beat}
 Frame size 4 beats:
 Temporal ordering of input:
   idata : MS Beat, LS Beat, MS Beat, LS Beat, MS Beat, LS Beat, ...
   sof   :       1,       0,       0,       0,       1,       0, ...
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| WIDTH        |      | 8     |             |
## Ports

| Port name | Direction | Type          | Description                                  |
| --------- | --------- | ------------- | -------------------------------------------- |
| clk       | input     |               | Input clock                                  |
| rst       | input     |               |                                              |
| sof       | input     |               | Start of frame indicator marking the MS Beat |
| idata     | input     | [WIDTH-1:0]   | Input data beat                              |
| ivalid    | input     |               | Input data qualifier                         |
| odata     | output    | [WIDTH*2-1:0] | Output data beat                             |
| ovalid    | output    |               | Output data qualifier                        |
| osof      | output    |               | Output Start of frame indicator              |
## Signals

| Name    | Type             | Description         |
| ------- | ---------------- | ------------------- |
| idata_d | reg  [WIDTH-1:0] |                     |
| sof_d   | reg [6:0]        | Single clock mode:  |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
Use sof_d[2] for frame size of 4 beats
Use sof_d[4,6] for frame size of 8 beats

