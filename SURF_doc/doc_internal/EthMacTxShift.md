# Entity: EthMacTxShift

## Diagram

![Diagram](EthMacTxShift.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Ethernet MAC's TX byte Shifting Module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| TPD_G        | time    | 1 ns  |             |
| SHIFT_EN_G   | boolean | false |             |
## Ports

| Port name   | Direction | Type                | Description     |
| ----------- | --------- | ------------------- | --------------- |
| ethClk      | in        | sl                  | Clock and Reset |
| ethRst      | in        | sl                  |                 |
| sAxisMaster | in        | AxiStreamMasterType | AXIS Interface  |
| sAxisSlave  | out       | AxiStreamSlaveType  |                 |
| mAxisMaster | out       | AxiStreamMasterType |                 |
| mAxisSlave  | in        | AxiStreamSlaveType  |                 |
| txShift     | in        | slv(3 downto 0)     | Configuration   |
