# Entity: IpV4EngineLoopback

- **File**: IpV4EngineLoopback.vhd
## Diagram

![Diagram](IpV4EngineLoopback.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Simulation Testbed for testing the IpV4Engine in Loopback
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type            | Value | Description |
| ------------ | --------------- | ----- | ----------- |
| TPD_G        | time            | 1 ns  |             |
| PROTOCOL_G   | slv(7 downto 0) | UDP_C |             |
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
| start            | in        | sl                  |                          |
| remoteIp         | in        | slv(31 downto 0)    |                          |
| done             | out       | sl                  |                          |
| remoteMac        | out       | slv(47 downto 0)    |                          |
| clk              | in        | sl                  | Clock and Reset          |
| rst              | in        | sl                  |                          |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description |
| ---------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       ibProtocolSlave  => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       obProtocolMaster => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       arpReqMaster     => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       arpAckSlave      => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       done             => '0',<br><span style="padding-left:20px">       remoteMac        => (others => '0'),<br><span style="padding-left:20px">       cnt              => (others => '0'),<br><span style="padding-left:20px">       state            => IDLE_S) |             |
## Types

| Name      | Type                                                                                              | Description |
| --------- | ------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> ARP_S,<br><span style="padding-left:20px"> DONE_S)  |             |
| RegType   |                                                                                                   |             |
## Processes
- comb: ( arpAckMaster, arpReqSlave, ibProtocolMaster, obProtocolSlave, r, remoteIp, rst,
                   start )
- seq: ( clk )
