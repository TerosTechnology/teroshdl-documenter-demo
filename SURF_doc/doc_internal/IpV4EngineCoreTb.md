# Entity: IpV4EngineCoreTb

- **File**: IpV4EngineCoreTb.vhd
## Diagram

![Diagram](IpV4EngineCoreTb.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Simulation Testbed for testing the IpV4EngineCore
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

| Generic name | Type             | Value | Description |
| ------------ | ---------------- | ----- | ----------- |
| TPD_G        | time             | 1 ns  |             |
| LOCAL_MAC_G  | slv(47 downto 0) |       |             |
| LOCAL_IP_G   | slv(31 downto 0) |       |             |
| REMOTE_MAC_G | slv(47 downto 0) |       |             |
| REMOTE_IP_G  | slv(31 downto 0) |       |             |
| VLAN_G       | boolean          |       |             |
| VID_G        | slv(15 downto 0) |       |             |
| MAX_CNT_G    | natural          |       |             |
| UDP_LEN_G    | natural          |       |             |
## Ports

| Port name        | Direction | Type                | Description              |
| ---------------- | --------- | ------------------- | ------------------------ |
| obProtocolMaster | out       | AxiStreamMasterType | Interface to IPV4 Engine |
| obProtocolSlave  | in        | AxiStreamSlaveType  |                          |
| ibProtocolMaster | in        | AxiStreamMasterType |                          |
| ibProtocolSlave  | out       | AxiStreamSlaveType  |                          |
| arpReqMaster     | out       | AxiStreamMasterType | Interface to ARP Engine  |
| arpReqSlave      | in        | AxiStreamSlaveType  |                          |
| arpAckMaster     | in        | AxiStreamMasterType |                          |
| arpAckSlave      | out       | AxiStreamSlaveType  |                          |
| passed           | out       | sl                  | Simulation Result        |
| failed           | out       | sl                  |                          |
| clk              | in        | sl                  | Clock and Reset          |
| rst              | in        | sl                  |                          |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       passed           => '0',<br><span style="padding-left:20px">       failed           => (others => '0'),<br><span style="padding-left:20px">       passedDly        => '0',<br><span style="padding-left:20px">       failedDly        => '0',<br><span style="padding-left:20px">       txDone           => '0',<br><span style="padding-left:20px">       tKeep            => (others => '1'),<br><span style="padding-left:20px">       timer            => (others => '0'),<br><span style="padding-left:20px">       remoteMac        => (others => '0'),<br><span style="padding-left:20px">       len              => (others => '0'),<br><span style="padding-left:20px">       txCnt            => 0,<br><span style="padding-left:20px">       txWordCnt        => 0,<br><span style="padding-left:20px">       txWordSize       => 0,<br><span style="padding-left:20px">       txByteCnt        => 0,<br><span style="padding-left:20px">       rxCnt            => 0,<br><span style="padding-left:20px">       rxWordCnt        => 0,<br><span style="padding-left:20px">       rxWordSize       => 0,<br><span style="padding-left:20px">       rxByteCnt        => 0,<br><span style="padding-left:20px">       obProtocolMaster => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       ibProtocolSlave  => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       arpReqMaster     => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       arpAckSlave      => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       state            => IDLE_S) |             |
## Types

| Name      | Type                                                                                                                                         | Description |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> ARP_S,<br><span style="padding-left:20px"> UDP_S,<br><span style="padding-left:20px"> DONE_S)  |             |
| RegType   |                                                                                                                                              |             |
## Processes
- comb: ( arpAckMaster, arpReqSlave, ibProtocolMaster, obProtocolSlave, r, rst )
- seq: ( clk )
