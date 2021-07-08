# Entity: RogueTcpMemoryWrap

## Diagram

![Diagram](RogueTcpMemoryWrap.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Rogue Stream Module Wrapper
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type                        | Value | Description |
| ------------ | --------------------------- | ----- | ----------- |
| TPD_G        | time                        | 1 ns  |             |
| PORT_NUM_G   | natural range 1024 to 49151 | 9000  |             |
## Ports

| Port name       | Direction | Type                   | Description |
| --------------- | --------- | ---------------------- | ----------- |
| axilClk         | in        | sl                     |             |
| axilRst         | in        | sl                     |             |
| axilReadMaster  | out       | AxiLiteReadMasterType  |             |
| axilReadSlave   | in        | AxiLiteReadSlaveType   |             |
| axilWriteMaster | out       | AxiLiteWriteMasterType |             |
| axilWriteSlave  | in        | AxiLiteWriteSlaveType  |             |
## Instantiations

- U_RogueTcpMemory: surf.RogueTcpMemory
