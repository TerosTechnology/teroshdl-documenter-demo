# Entity: AxiDac7654Core

- **File**: AxiDac7654Core.vhd
## Diagram

![Diagram](AxiDac7654Core.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI-Lite interface to DAC7654 DAC IC
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name       | Type                  | Value    | Description |
| ------------------ | --------------------- | -------- | ----------- |
| TPD_G              | time                  | 1 ns     |             |
| AXI_CLK_FREQ_G     | real                  | 125.0E+6 | units of Hz |
| STATUS_CNT_WIDTH_G | natural range 1 to 32 | 32       |             |
## Ports

| Port name      | Direction | Type                   | Description                                 |
| -------------- | --------- | ---------------------- | ------------------------------------------- |
| dacIn          | in        | AxiDac7654InType       | DAC Ports                                   |
| dacOut         | out       | AxiDac7654OutType      |                                             |
| axiClk         | in        | sl                     | AXI-Lite Register Interface (axiClk domain) |
| axiRst         | in        | sl                     |                                             |
| axiReadMaster  | in        | AxiLiteReadMasterType  |                                             |
| axiReadSlave   | out       | AxiLiteReadSlaveType   |                                             |
| axiWriteMaster | in        | AxiLiteWriteMasterType |                                             |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType  |                                             |
## Signals

| Name   | Type                 | Description |
| ------ | -------------------- | ----------- |
| status | AxiDac7654StatusType |             |
| config | AxiDac7654ConfigType |             |
## Instantiations

- AxiDac7654Reg_Inst: surf.AxiDac7654Reg
- AxiDac7654Spi_Inst: surf.AxiDac7654Spi
