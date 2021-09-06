# Entity: AxiXcf128Core

- **File**: AxiXcf128Core.vhd
## Diagram

![Diagram](AxiXcf128Core.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: AXI-Lite interface to XCF128 FLASH IC
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
## Generics

| Generic name   | Type | Value    | Description |
| -------------- | ---- | -------- | ----------- |
| TPD_G          | time | 1 ns     |             |
| AXI_CLK_FREQ_G | real | 200.0E+6 |             |
## Ports

| Port name      | Direction | Type                   | Description                 |
| -------------- | --------- | ---------------------- | --------------------------- |
| xcfInOut       | inout     | AxiXcf128InOutType     | XCF128 Ports                |
| xcfOut         | out       | AxiXcf128OutType       |                             |
| axiReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Register Interface |
| axiReadSlave   | out       | AxiLiteReadSlaveType   |                             |
| axiWriteMaster | in        | AxiLiteWriteMasterType |                             |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType  |                             |
| axiClk         | in        | sl                     | Clocks and Resets           |
| axiRst         | in        | sl                     |                             |
## Signals

| Name   | Type                | Description |
| ------ | ------------------- | ----------- |
| status | AxiXcf128StatusType |             |
| config | AxiXcf128ConfigType |             |
## Instantiations

- AxiXcf128Reg_Inst: surf.AxiXcf128Reg
