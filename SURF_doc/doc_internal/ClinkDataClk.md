# Entity: ClinkDataClk

- **File**: ClinkDataClk.vhd
## Diagram

![Diagram](ClinkDataClk.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: A wrapper over MMCM
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

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| TPD_G         | time    | 1 ns  |             |
| REG_BUFF_EN_G | boolean | false |             |
## Ports

| Port name       | Direction | Type                   | Description        |
| --------------- | --------- | ---------------------- | ------------------ |
| clkIn           | in        | sl                     |                    |
| rstIn           | in        | sl                     |                    |
| clinkClk7x      | out       | sl                     |                    |
| clinkClk        | out       | sl                     |                    |
| clinkRst        | out       | sl                     |                    |
| sysClk          | in        | sl                     | AXI-Lite Interface |
| sysRst          | in        | sl                     |                    |
| axilReadMaster  | in        | AxiLiteReadMasterType  |                    |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                    |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                    |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                    |
## Signals

| Name       | Type             | Description |
| ---------- | ---------------- | ----------- |
| clkInLoc   | sl               |             |
| clkOutMmcm | slv(1 downto 0)  |             |
| clkOutLoc  | slv(1 downto 0)  |             |
| clkFbOut   | sl               |             |
| clkFbIn    | sl               |             |
| lockedLoc  | sl               |             |
| genReset   | sl               |             |
| drpRdy     | sl               |             |
| drpEn      | sl               |             |
| drpWe      | sl               |             |
| drpAddr    | slv(6 downto 0)  |             |
| drpDi      | slv(15 downto 0) |             |
| drpDo      | slv(15 downto 0) |             |
## Instantiations

- U_AxiLiteToDrp: surf.AxiLiteToDrp
- U_Mmcm: MMCME3_ADV
- U_RstSync: surf.RstSync
