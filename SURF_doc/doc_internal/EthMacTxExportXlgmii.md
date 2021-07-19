# Entity: EthMacTxExportXlgmii

- **File**: EthMacTxExportXlgmii.vhd
## Diagram

![Diagram](EthMacTxExportXlgmii.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: 40GbE Export MAC core with XLGMII interface
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name      | Direction | Type                | Description          |
| -------------- | --------- | ------------------- | -------------------- |
| ethClk         | in        | sl                  | Clock and Reset      |
| ethRst         | in        | sl                  |                      |
| macObMaster    | in        | AxiStreamMasterType | AXIS Interface       |
| macObSlave     | out       | AxiStreamSlaveType  |                      |
| phyTxd         | out       | slv(127 downto 0)   | XLGMII PHY Interface |
| phyTxc         | out       | slv(15 downto 0)    |                      |
| phyReady       | in        | sl                  |                      |
| txCountEn      | out       | sl                  | Errors               |
| txUnderRun     | out       | sl                  |                      |
| txLinkNotReady | out       | sl                  |                      |
