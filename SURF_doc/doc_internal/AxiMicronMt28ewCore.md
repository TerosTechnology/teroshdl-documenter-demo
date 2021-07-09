# Entity: AxiMicronMt28ewCore

## Diagram

![Diagram](AxiMicronMt28ewCore.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI-Lite interface to Micron MT28EW FLASH IC
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name       | Type             | Value       | Description |
| ------------------ | ---------------- | ----------- | ----------- |
| TPD_G              | time             | 1 ns        |             |
| EN_PASSWORD_LOCK_G | boolean          | false       |             |
| PASSWORD_LOCK_G    | slv(31 downto 0) | x"DEADBEEF" |             |
| MEM_ADDR_MASK_G    | slv(31 downto 0) | x"00000000" |             |
| AXI_CLK_FREQ_G     | real             | 200.0E+6    |             |
## Ports

| Port name      | Direction | Type                     | Description                 |
| -------------- | --------- | ------------------------ | --------------------------- |
| flashInOut     | inout     | AxiMicronMt28ewInOutType | FLASH Interface             |
| flashOut       | out       | AxiMicronMt28ewOutType   |                             |
| axiReadMaster  | in        | AxiLiteReadMasterType    | AXI-Lite Register Interface |
| axiReadSlave   | out       | AxiLiteReadSlaveType     |                             |
| axiWriteMaster | in        | AxiLiteWriteMasterType   |                             |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType    |                             |
| axiClk         | in        | sl                       | Clocks and Resets           |
| axiRst         | in        | sl                       |                             |
## Signals

| Name      | Type             | Description |
| --------- | ---------------- | ----------- |
| flashDin  | slv(15 downto 0) |             |
| flashDout | slv(15 downto 0) |             |
| flashTri  | sl               |             |
## Instantiations

- U_CTRL: surf.AxiMicronMt28ewReg
