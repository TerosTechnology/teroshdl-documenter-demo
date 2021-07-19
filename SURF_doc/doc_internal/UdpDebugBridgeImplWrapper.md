# Entity: UdpDebugBridge

- **File**: UdpDebugBridgeImplWrapper.vhd
## Diagram

![Diagram](UdpDebugBridgeImplWrapper.svg "Diagram")
## Description

Title      : XVC Debug Bridge Support
Company    : SLAC National Accelerator Laboratory
Description: UDP Debug Bridge
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Ports

| Port name | Direction | Type                | Description |
| --------- | --------- | ------------------- | ----------- |
| axisClk   | in        | sl                  |             |
| axisRst   | in        | sl                  |             |
| mAxisReq  | in        | AxiStreamMasterType |             |
| sAxisReq  | out       | AxiStreamSlaveType  |             |
| mAxisTdo  | out       | AxiStreamMasterType |             |
| sAxisTdo  | in        | AxiStreamSlaveType  |             |
## Instantiations

- U_AxisJtagDebugBridge: surf.AxisJtagDebugBridge(AxisJtagDebugBridgeImpl)
