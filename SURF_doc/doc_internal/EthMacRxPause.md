# Entity: EthMacRxPause

## Diagram

![Diagram](EthMacRxPause.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
Generic pause frame receiver for Ethernet MACs. Pause frames are dropped
from the incoming data stream.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type                  | Value         | Description |
| ------------ | --------------------- | ------------- | ----------- |
| TPD_G        | time                  | 1 ns          |             |
| PAUSE_EN_G   | boolean               | true          |             |
| VLAN_EN_G    | boolean               | false         |             |
| VLAN_SIZE_G  | positive range 1 to 8 | 1             |             |
| VLAN_VID_G   | Slv12Array            | (0 => x"001") |             |
## Ports

| Port name    | Direction | Type                                         | Description            |
| ------------ | --------- | -------------------------------------------- | ---------------------- |
| ethClk       | in        | sl                                           | Clock and Reset        |
| ethRst       | in        | sl                                           |                        |
| sAxisMaster  | in        | AxiStreamMasterType                          | Incoming data from MAC |
| mAxisMaster  | out       | AxiStreamMasterType                          | Outgoing data          |
| mAxisMasters | out       | AxiStreamMasterArray(VLAN_SIZE_G-1 downto 0) |                        |
| rxPauseReq   | out       | sl                                           | Pause Values           |
| rxPauseValue | out       | slv(15 downto 0)                             |                        |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       idx          => 0,<br><span style="padding-left:20px">       pauseEn      => '0',<br><span style="padding-left:20px">       pauseValue   => (others => '0'),<br><span style="padding-left:20px">       mAxisMaster  => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       mAxisMasters => (others => AXI_STREAM_MASTER_INIT_C),<br><span style="padding-left:20px">       state        => IDLE_S) |             |
## Types

| Name      | Type                                                                                                                                                                                        | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> PAUSE_S,<br><span style="padding-left:20px"> DUMP_S,<br><span style="padding-left:20px"> PASS_S,<br><span style="padding-left:20px"> VLAN_S)  |             |
| RegType   |                                                                                                                                                                                             |             |
