# Entity: AxiSy56040Core

- **File**: AxiSy56040Core.vhd
## Diagram

![Diagram](AxiSy56040Core.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI-Lite interface to Clock Crossbar
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type                  | Value                    | Description |
| -------------- | --------------------- | ------------------------ | ----------- |
| TPD_G          | time                  | 1 ns                     |             |
| AXI_CLK_FREQ_G | real                  | 200.0E+6                 | units of Hz |
| XBAR_DEFAULT_G | Slv2Array(3 downto 0) | ("11", "10", "01", "00") |             |
## Ports

| Port name      | Direction | Type                   | Description                 |
| -------------- | --------- | ---------------------- | --------------------------- |
| xBar           | out       | AxiSy56040OutType      | XBAR Ports                  |
| axiReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Register Interface |
| axiReadSlave   | out       | AxiLiteReadSlaveType   |                             |
| axiWriteMaster | in        | AxiLiteWriteMasterType |                             |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType  |                             |
| axiClk         | in        | sl                     | Clocks and Resets           |
| axiRst         | in        | sl                     |                             |
## Instantiations

- AxiSy56040Reg_Inst: surf.AxiSy56040Reg
