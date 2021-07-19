# Entity: AxiAd5780Core

- **File**: AxiAd5780Core.vhd
## Diagram

![Diagram](AxiAd5780Core.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI-Lite interface to AD5780 DAC IC
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
| STATUS_CNT_WIDTH_G | natural range 1 to 32 | 32       |             |
| AXI_CLK_FREQ_G     | real                  | 200.0E+6 | units of Hz |
| SPI_CLK_FREQ_G     | real                  | 25.0E+6  |             |
## Ports

| Port name      | Direction | Type                   | Description                                 |
| -------------- | --------- | ---------------------- | ------------------------------------------- |
| dacIn          | in        | AxiAd5780InType        | DAC Ports                                   |
| dacOut         | out       | AxiAd5780OutType       |                                             |
| dacData        | in        | slv(17 downto 0)       | 2's complement by default                   |
| axiReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Register Interface (axiClk domain) |
| axiReadSlave   | out       | AxiLiteReadSlaveType   |                                             |
| axiWriteMaster | in        | AxiLiteWriteMasterType |                                             |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType  |                                             |
| axiClk         | in        | sl                     | Clocks and Resets                           |
| axiRst         | in        | sl                     |                                             |
## Signals

| Name       | Type                | Description |
| ---------- | ------------------- | ----------- |
| status     | AxiAd5780StatusType |             |
| config     | AxiAd5780ConfigType |             |
| dacRst     | sl                  |             |
| dacDataMux | slv(17 downto 0)    |             |
## Processes
- unnamed: ( axiClk )
## Instantiations

- AxiAd5780Reg_Inst: surf.AxiAd5780Reg
- AxiAd5780Ser_Inst: surf.AxiAd5780Ser
