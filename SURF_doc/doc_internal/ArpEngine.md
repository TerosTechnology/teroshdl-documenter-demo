# Entity: ArpEngine

## Diagram

![Diagram](ArpEngine.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: ARP Engine
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type     | Value      | Description    |
| ------------- | -------- | ---------- | -------------- |
| TPD_G         | time     | 1 ns       |                |
| CLIENT_SIZE_G | positive | 1          |                |
| CLK_FREQ_G    | real     | 156.25E+06 | In units of Hz |
| VLAN_G        | boolean  | false      |                |
## Ports

| Port name     | Direction | Type                                           | Description                           |
| ------------- | --------- | ---------------------------------------------- | ------------------------------------- |
| localMac      | in        | slv(47 downto 0)                               | Local Configuration                   |
| localIp       | in        | slv(31 downto 0)                               |                                       |
| arpReqMasters | in        | AxiStreamMasterArray(CLIENT_SIZE_G-1 downto 0) | Request via IP address                |
| arpReqSlaves  | out       | AxiStreamSlaveArray(CLIENT_SIZE_G-1 downto 0)  |                                       |
| arpAckMasters | out       | AxiStreamMasterArray(CLIENT_SIZE_G-1 downto 0) | Respond with MAC address              |
| arpAckSlaves  | in        | AxiStreamSlaveArray(CLIENT_SIZE_G-1 downto 0)  |                                       |
| ibArpMaster   | in        | AxiStreamMasterType                            | Interface to Ethernet Frame MUX/DEMUX |
| ibArpSlave    | out       | AxiStreamSlaveType                             |                                       |
| obArpMaster   | out       | AxiStreamMasterType                            |                                       |
| obArpSlave    | in        | AxiStreamSlaveType                             |                                       |
| clk           | in        | sl                                             | Clock and Reset                       |
| rst           | in        | sl                                             |                                       |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name             | Type             | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description                      |
| ---------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| BROADCAST_MAC_C  | slv(47 downto 0) |  (others => '1')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                  |
| HARDWWARE_TYPE_C | slv(15 downto 0) |  x"0100"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | HardwareType = ETH = 0x0001      |
| PROTOCOL_TYPE_C  | slv(15 downto 0) |  x"0008"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | ProtocolType = IP  = 0x0800      |
| HARDWWARE_LEN_C  | slv(7 downto 0)  |  x"06"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | HardwareLength = 6 (6 Bytes/MAC) |
| PROTOCOL_LEN_C   | slv(7 downto 0)  |  x"04"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | ProtocolLength = 4 (6 Bytes/IP)  |
| ARP_REQ_C        | slv(15 downto 0) |  x"0100"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | OpCode = ARP Request  = 0x0001   |
| ARP_REPLY_C      | slv(15 downto 0) |  x"0200"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | OpCode = ARP Reply    = 0x0002   |
| TIMER_1_SEC_C    | natural          |  getTimeRatio(CLK_FREQ_G,<br><span style="padding-left:20px"> 1.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                  |
| REG_INIT_C       | RegType          |  (       cnt           => 0,<br><span style="padding-left:20px">       tData         => (others => (others => '0')),<br><span style="padding-left:20px">       ibArpSlave    => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       txArpMaster   => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       arpReqSlaves  => (others => AXI_STREAM_SLAVE_INIT_C),<br><span style="padding-left:20px">       arpAckMasters => (others => AXI_STREAM_MASTER_INIT_C),<br><span style="padding-left:20px">       arpTimers     => (others => 0),<br><span style="padding-left:20px">       reqCnt        => 0,<br><span style="padding-left:20px">       ackCnt        => 0,<br><span style="padding-left:20px">       state         => IDLE_S) |                                  |
## Types

| Name      | Type                                                                                                                                                                                    | Description |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> RX_S,<br><span style="padding-left:20px"> CHECK_S,<br><span style="padding-left:20px"> SCAN_S,<br><span style="padding-left:20px"> TX_S)  |             |
| RegType   |                                                                                                                                                                                         |             |
## Processes
- comb: ( arpAckSlaves, arpReqMasters, ibArpMaster, localIp, localMac, obArpSlave, r, rst )
- seq: ( clk )
