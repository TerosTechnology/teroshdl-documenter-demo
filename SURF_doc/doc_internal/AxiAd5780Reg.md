# Entity: AxiAd5780Reg

- **File**: AxiAd5780Reg.vhd
## Diagram

![Diagram](AxiAd5780Reg.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: AXI-Lite interface to AD5780 DAC IC
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

| Generic name       | Type                  | Value    | Description  |
| ------------------ | --------------------- | -------- | ------------ |
| TPD_G              | time                  | 1 ns     |              |
| STATUS_CNT_WIDTH_G | natural range 1 to 32 | 32       |              |
| AXI_CLK_FREQ_G     | real                  | 200.0E+6 |  units of Hz |
| SPI_CLK_FREQ_G     | real                  | 25.0E+6  |              |
## Ports

| Port name      | Direction | Type                   | Description                 |
| -------------- | --------- | ---------------------- | --------------------------- |
| axiReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Register Interface |
| axiReadSlave   | out       | AxiLiteReadSlaveType   |                             |
| axiWriteMaster | in        | AxiLiteWriteMasterType |                             |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType  |                             |
| status         | in        | AxiAd5780StatusType    | Register Inputs/Outputs     |
| config         | out       | AxiAd5780ConfigType    |                             |
| axiClk         | in        | sl                     | Global Signals              |
| axiRst         | in        | sl                     |                             |
| dacRst         | out       | sl                     |                             |
## Signals

| Name           | Type                               | Description |
| -------------- | ---------------------------------- | ----------- |
| r              | RegType                            |             |
| rin            | RegType                            |             |
| regIn          | AxiAd5780StatusType                |             |
| regOut         | AxiAd5780ConfigType                |             |
| dacRefreshRate | slv(STATUS_CNT_WIDTH_G-1 downto 0) |             |
## Constants

| Name                   | Type             | Value                                                                                                                                                                                                                          | Description |
| ---------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| DOUBLE_SCK_FREQ_C      | real             |  SPI_CLK_FREQ_G * 2.0E+0                                                                                                                                                                                                       |             |
| HALF_SCK_PERIOD_C      | natural          |  (getTimeRatio(AXI_CLK_FREQ_G,<br><span style="padding-left:20px"> DOUBLE_SCK_FREQ_C))-1                                                                                                                                       |             |
| HALF_SCK_PERIOD_INIT_C | slv(31 downto 0) |  toSlv(HALF_SCK_PERIOD_C,<br><span style="padding-left:20px"> 32)                                                                                                                                                              |             |
| REG_INIT_C             | RegType          |  (       '1',<br><span style="padding-left:20px">       AXI_AD5780_CONFIG_INIT_C,<br><span style="padding-left:20px">       AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       AXI_LITE_WRITE_SLAVE_INIT_C) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( axiReadMaster, axiRst, axiWriteMaster, dacRefreshRate, r, regIn )
- seq: ( axiClk )
## Instantiations

- SyncTrigRate_Inst: surf.SyncTrigRate
