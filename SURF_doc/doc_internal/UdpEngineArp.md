# Entity: UdpEngineArp

- **File**: UdpEngineArp.vhd
## Diagram

![Diagram](UdpEngineArp.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: UDP Client's ARP Messaging Module
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

| Generic name   | Type     | Value      | Description |
| -------------- | -------- | ---------- | ----------- |
| TPD_G          | time     | 1 ns       |             |
| CLIENT_SIZE_G  | positive | 1          |             |
| CLK_FREQ_G     | real     | 156.25E+06 |             |
| COMM_TIMEOUT_G | positive | 30         |             |
| RESP_TIMEOUT_G | positive | 5          |             |
## Ports

| Port name       | Direction | Type                                           | Description                       |
| --------------- | --------- | ---------------------------------------------- | --------------------------------- |
| localIp         | in        | slv(31 downto 0)                               |   big-Endian configuration        |
| arpReqMasters   | out       | AxiStreamMasterArray(CLIENT_SIZE_G-1 downto 0) |  Request via IP address           |
| arpReqSlaves    | in        | AxiStreamSlaveArray(CLIENT_SIZE_G-1 downto 0)  |                                   |
| arpAckMasters   | in        | AxiStreamMasterArray(CLIENT_SIZE_G-1 downto 0) |  Respond with MAC address         |
| arpAckSlaves    | out       | AxiStreamSlaveArray(CLIENT_SIZE_G-1 downto 0)  |                                   |
| clientRemoteDet | in        | slv(CLIENT_SIZE_G-1 downto 0)                  | Interface to UDP Client engine(s) |
| clientRemoteIp  | in        | Slv32Array(CLIENT_SIZE_G-1 downto 0)           |                                   |
| clientRemoteMac | out       | Slv48Array(CLIENT_SIZE_G-1 downto 0)           |                                   |
| clk             | in        | sl                                             | Clock and Reset                   |
| rst             | in        | sl                                             |                                   |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name          | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description |
| ------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| TIMER_1_SEC_C | natural |  getTimeRatio(CLK_FREQ_G,<br><span style="padding-left:20px"> 1.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
| REG_INIT_C    | RegType |  (       clientRemoteMac  => (others => (others => '0')),<br><span style="padding-left:20px">       arpAckSlaves     => (others => AXI_STREAM_SLAVE_INIT_C),<br><span style="padding-left:20px">       arpReqMasters    => (others => AXI_STREAM_MASTER_INIT_C),<br><span style="padding-left:20px">       timerEn          => '0',<br><span style="padding-left:20px">       timer            => 0,<br><span style="padding-left:20px">       arpTimers        => (others => 0),<br><span style="padding-left:20px">       respTimers       => (others => 0),<br><span style="padding-left:20px">       state            => (others => IDLE_S)) |             |
## Types

| Name       | Type                                                                                                       | Description |
| ---------- | ---------------------------------------------------------------------------------------------------------- | ----------- |
| TimerArray | array (natural range <>) of natural range 0 to COMM_TIMEOUT_G                                              |             |
| StateType  | ( IDLE_S,<br><span style="padding-left:20px"> WAIT_S,<br><span style="padding-left:20px"> COMM_MONITOR_S)  |             |
| StateArray | array (natural range <>) of StateType                                                                      |             |
| RegType    |                                                                                                            |             |
## Processes
- comb: ( arpAckMasters, arpReqSlaves, clientRemoteDet, clientRemoteIp, r, rst )
- seq: ( clk )
