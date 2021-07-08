# Entity: AxiToAxiLite

## Diagram

![Diagram](AxiToAxiLite.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI4-to-AXI-Lite bridge
Note: This module only supports 32-bit aligned addresses and 32-bit transactions.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name    | Type    | Value | Description |
| --------------- | ------- | ----- | ----------- |
| TPD_G           | time    | 1 ns  |             |
| EN_SLAVE_RESP_G | boolean | true  |             |
## Ports

| Port name       | Direction | Type                   | Description    |
| --------------- | --------- | ---------------------- | -------------- |
| axiClk          | in        | sl                     | Clocks & Reset |
| axiClkRst       | in        | sl                     |                |
| axiReadMaster   | in        | AxiReadMasterType      | AXI Slave      |
| axiReadSlave    | out       | AxiReadSlaveType       |                |
| axiWriteMaster  | in        | AxiWriteMasterType     |                |
| axiWriteSlave   | out       | AxiWriteSlaveType      |                |
| axilReadMaster  | out       | AxiLiteReadMasterType  | AXI Lite       |
| axilReadSlave   | in        | AxiLiteReadSlaveType   |                |
| axilWriteMaster | out       | AxiLiteWriteMasterType |                |
| axilWriteSlave  | in        | AxiLiteWriteSlaveType  |                |
## Processes
- unnamed: ( axiWriteMaster )
**Description**
Collapse Axi wdata onto 32-bit AxiLite wdata
  Assumes only active 32 bits are asserted,
    otherwise could use wstrb to pick correct 32 bits

- unnamed: ( axilReadSlave )
- unnamed: ( axiClk )
**Description**
ID Tracking

