# Entity: AxisJtagDebugBridge

## Diagram

![Diagram](AxisJtagDebugBridge.svg "Diagram")
## Description

Title      : JTAG Support
Company    : SLAC National Accelerator Laboratory
Description: AXI Stream Debug Bridge
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
Axi Stream to JTAG Protocol
Connect AxisToJtag to a debug bridge IP (convenience wrapper)
## Generics

| Generic name | Type                      | Value  | Description                          |
| ------------ | ------------------------- | ------ | ------------------------------------ |
| TPD_G        | time                      | 1 ns   |                                      |
| AXIS_FREQ_G  | real                      | 0.0    | Hz (for computing TCK period)        |
| AXIS_WIDTH_G | positive range 4 to 16    | 4      | bytes                                |
| CLK_DIV2_G   | positive                  | 4      | half-period of TCK in axisClk cycles |
| MEM_DEPTH_G  | natural  range 0 to 65535 | 4      | size of buffer memory (0 for none)   |
| MEM_STYLE_G  | string                    | "auto" | 'auto', 'block' or 'distributed'     |
## Ports

| Port name | Direction | Type                | Description |
| --------- | --------- | ------------------- | ----------- |
| axisClk   | in        | sl                  |             |
| axisRst   | in        | sl                  |             |
| mAxisReq  | in        | AxiStreamMasterType |             |
| sAxisReq  | out       | AxiStreamSlaveType  |             |
| mAxisTdo  | out       | AxiStreamMasterType |             |
| sAxisTdo  | in        | AxiStreamSlaveType  |             |
## Signals

| Name | Type | Description |
| ---- | ---- | ----------- |
| tck  | sl   |             |
|  tdi | sl   |             |
|  tms | sl   |             |
|  tdo | sl   |             |
## Instantiations

- U_AXIS_JTAG: surf.AxisToJtag
- U_JTAG_BSCAN: component DebugBridgeJtag
