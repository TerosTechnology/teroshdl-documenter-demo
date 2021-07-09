# Entity: XauiReg

## Diagram

![Diagram](XauiReg.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI-Lite XAUI Register Interface
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
| EN_AXI_REG_G | boolean | false |             |
## Ports

| Port name      | Direction | Type                   | Description                        |
| -------------- | --------- | ---------------------- | ---------------------------------- |
| localMac       | in        | slv(47 downto 0)       | Local Configurations               |
| axiClk         | in        | sl                     | AXI-Lite Register Interface        |
| axiRst         | in        | sl                     |                                    |
| axiReadMaster  | in        | AxiLiteReadMasterType  |                                    |
| axiReadSlave   | out       | AxiLiteReadSlaveType   |                                    |
| axiWriteMaster | in        | AxiLiteWriteMasterType |                                    |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType  |                                    |
| phyClk         | in        | sl                     | Configuration and Status Interface |
| phyRst         | in        | sl                     |                                    |
| config         | out       | XauiConfig             |                                    |
| status         | in        | XauiStatus             |                                    |
## Signals

| Name         | Type                                                                                     | Description |
| ------------ | ---------------------------------------------------------------------------------------- | ----------- |
| r            | RegType                                                                                  |             |
| rin          | RegType                                                                                  |             |
| statusOut    | slv(STATUS_SIZE_C-1 downto 0)                                                            |             |
| cntOut       | SlVectorArray(STATUS_SIZE_C-1 downto 0,<br><span style="padding-left:20px"> 31 downto 0) |             |
| localMacSync | slv(47 downto 0)                                                                         |             |
## Constants

| Name          | Type     | Value                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| ------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| STATUS_SIZE_C | positive |  32                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
| REG_INIT_C    | RegType  |  (       hardRst       => '0',<br><span style="padding-left:20px">       cntRst        => '1',<br><span style="padding-left:20px">       rollOverEn    => (others => '0'),<br><span style="padding-left:20px">       config        => XAUI_CONFIG_INIT_C,<br><span style="padding-left:20px">       axiReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axiWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
