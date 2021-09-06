# Entity: EthMacRxImportXlgmii

- **File**: EthMacRxImportXlgmii.vhd
## Diagram

![Diagram](EthMacRxImportXlgmii.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: 40GbE Import MAC core with XLGMII interface
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name   | Direction | Type                | Description              |
| ----------- | --------- | ------------------- | ------------------------ |
| ethClk      | in        | sl                  | Clock and Reset          |
| ethRst      | in        | sl                  |                          |
| macIbMaster | out       | AxiStreamMasterType | AXIS Interface           |
| phyRxd      | in        | slv(127 downto 0)   | XLGMII PHY Interface     |
| phyRxc      | in        | slv(15 downto 0)    |                          |
| phyReady    | in        | sl                  | Configuration and status |
| rxCountEn   | out       | sl                  |                          |
| rxCrcError  | out       | sl                  |                          |
