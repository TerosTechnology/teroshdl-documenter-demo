# Entity: EthMacRxFilter

- **File**: EthMacRxFilter.vhd
## Diagram

![Diagram](EthMacRxFilter.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Ethernet MAC's RX frame filter
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
| FILT_EN_G    | boolean | false |             |
## Ports

| Port name   | Direction | Type                | Description            |
| ----------- | --------- | ------------------- | ---------------------- |
| ethClk      | in        | sl                  | Clock and Reset        |
| ethRst      | in        | sl                  |                        |
| sAxisMaster | in        | AxiStreamMasterType | Incoming data from MAC |
| mAxisMaster | out       | AxiStreamMasterType | Outgoing data          |
| mAxisCtrl   | in        | AxiStreamCtrlType   |                        |
| dropOnPause | in        | sl                  | Configuration          |
| macAddress  | in        | slv(47 downto 0)    |                        |
| filtEnable  | in        | sl                  |                        |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                              | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| REG_INIT_C | RegType |  (       state       => IDLE_S,<br><span style="padding-left:20px">       mAxisMaster => AXI_STREAM_MASTER_INIT_C) |             |
## Types

| Name      | Type                                                                                               | Description |
| --------- | -------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> DROP_S,<br><span style="padding-left:20px"> PASS_S)  |             |
| RegType   |                                                                                                    |             |
