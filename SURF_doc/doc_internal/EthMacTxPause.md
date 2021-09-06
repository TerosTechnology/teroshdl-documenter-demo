# Entity: EthMacTxPause

- **File**: EthMacTxPause.vhd
## Diagram

![Diagram](EthMacTxPause.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:
 Generic pause frame generator for Ethernet MACs.  This module as acts as
 a gate keeper when the peer has requested a pause period.
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

| Generic name    | Type                    | Value | Description |
| --------------- | ----------------------- | ----- | ----------- |
| TPD_G           | time                    | 1 ns  |             |
| PAUSE_EN_G      | boolean                 | true  |             |
| PAUSE_512BITS_G | natural range 1 to 1024 | 8     |             |
| VLAN_EN_G       | boolean                 | false |             |
| VLAN_SIZE_G     | positive range 1 to 8   | 1     |             |
## Ports

| Port name    | Direction | Type                                         | Description                |
| ------------ | --------- | -------------------------------------------- | -------------------------- |
| ethClk       | in        | sl                                           | Clock and Reset            |
| ethRst       | in        | sl                                           |                            |
| sAxisMaster  | in        | AxiStreamMasterType                          | Incoming data from client  |
| sAxisSlave   | out       | AxiStreamSlaveType                           |                            |
| sAxisMasters | in        | AxiStreamMasterArray(VLAN_SIZE_G-1 downto 0) |                            |
| sAxisSlaves  | out       | AxiStreamSlaveArray(VLAN_SIZE_G-1 downto 0)  |                            |
| mAxisMaster  | out       | AxiStreamMasterType                          | Outgoing data to MAC       |
| mAxisSlave   | in        | AxiStreamSlaveType                           |                            |
| clientPause  | in        | sl                                           | Flow control input         |
| rxPauseReq   | in        | sl                                           | Inputs from pause frame RX |
| rxPauseValue | in        | slv(15 downto 0)                             |                            |
| phyReady     | in        | sl                                           | Configuration and status   |
| pauseEnable  | in        | sl                                           |                            |
| pauseTime    | in        | slv(15 downto 0)                             |                            |
| macAddress   | in        | slv(47 downto 0)                             |                            |
| pauseTx      | out       | sl                                           |                            |
## Signals

| Name      | Type                                    | Description |
| --------- | --------------------------------------- | ----------- |
| r         | RegType                                 |             |
| rin       | RegType                                 |             |
| rxMasters | AxiStreamMasterArray(SIZE_C-1 downto 0) |             |
| rxSlaves  | AxiStreamSlaveArray(SIZE_C-1 downto 0)  |             |
| rxMaster  | AxiStreamMasterType                     |             |
| rxSlave   | AxiStreamSlaveType                      |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| CNT_BITS_C | integer |  bitSize(PAUSE_512BITS_G-1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |             |
| SIZE_C     | natural |  ite(VLAN_EN_G,<br><span style="padding-left:20px"> (VLAN_SIZE_G+1),<br><span style="padding-left:20px"> 1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |             |
| REG_INIT_C | RegType |  (       locPauseCnt => (others => '0'),<br><span style="padding-left:20px">       remPauseCnt => (others => '0'),<br><span style="padding-left:20px">       txCount     => (others => '0'),<br><span style="padding-left:20px">       locPreCnt   => (others => '0'),<br><span style="padding-left:20px">       remPreCnt   => (others => '0'),<br><span style="padding-left:20px">       pauseTx     => '0',<br><span style="padding-left:20px">       mAxisMaster => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       rxSlave     => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       state       => IDLE_S) |             |
## Types

| Name      | Type                                                                                                | Description |
| --------- | --------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> PAUSE_S,<br><span style="padding-left:20px"> PASS_S)  |             |
| RegType   |                                                                                                     |             |
