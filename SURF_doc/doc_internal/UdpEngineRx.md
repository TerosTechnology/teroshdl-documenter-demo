# Entity: UdpEngineRx

## Diagram

![Diagram](UdpEngineRx.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: UDP RX Engine Module
Note: UDP checksum checked in EthMac core
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type          | Value       | Description          |
| -------------- | ------------- | ----------- | -------------------- |
| TPD_G          | time          | 1 ns        | Simulation Generics  |
| DHCP_G         | boolean       | false       | UDP General Generic  |
| SERVER_EN_G    | boolean       | true        | UDP Server Generics  |
| SERVER_SIZE_G  | positive      | 1           |                      |
| SERVER_PORTS_G | PositiveArray | (0 => 8192) |                      |
| CLIENT_EN_G    | boolean       | true        | UDP Client Generics  |
| CLIENT_SIZE_G  | positive      | 1           |                      |
| CLIENT_PORTS_G | PositiveArray | (0 => 8193) |                      |
## Ports

| Port name        | Direction | Type                                           | Description                       |
| ---------------- | --------- | ---------------------------------------------- | --------------------------------- |
| localIp          | in        | slv(31 downto 0)                               |  big-Endian configuration         |
| broadcastIp      | in        | slv(31 downto 0)                               |  big-Endian configuration         |
| ibUdpMaster      | in        | AxiStreamMasterType                            | Interface to IPV4 Engine          |
| ibUdpSlave       | out       | AxiStreamSlaveType                             |                                   |
| serverRemotePort | out       | Slv16Array(SERVER_SIZE_G-1 downto 0)           | Interface to UDP Server engine(s) |
| serverRemoteIp   | out       | Slv32Array(SERVER_SIZE_G-1 downto 0)           |                                   |
| serverRemoteMac  | out       | Slv48Array(SERVER_SIZE_G-1 downto 0)           |                                   |
| obServerMasters  | out       | AxiStreamMasterArray(SERVER_SIZE_G-1 downto 0) |                                   |
| obServerSlaves   | in        | AxiStreamSlaveArray(SERVER_SIZE_G-1 downto 0)  |                                   |
| clientRemoteDet  | out       | slv(CLIENT_SIZE_G-1 downto 0)                  | Interface to UDP Client engine(s) |
| obClientMasters  | out       | AxiStreamMasterArray(CLIENT_SIZE_G-1 downto 0) |                                   |
| obClientSlaves   | in        | AxiStreamSlaveArray(CLIENT_SIZE_G-1 downto 0)  |                                   |
| ibDhcpMaster     | out       | AxiStreamMasterType                            | Interface to DHCP Engine          |
| ibDhcpSlave      | in        | AxiStreamSlaveType                             |                                   |
| clk              | in        | sl                                             | Clock and Reset                   |
| rst              | in        | sl                                             |                                   |
## Signals

| Name        | Type                | Description |
| ----------- | ------------------- | ----------- |
| r           | RegType             |             |
| rin         | RegType             |             |
| rxMaster    | AxiStreamMasterType |             |
| rxSlave     | AxiStreamSlaveType  |             |
| serverSlave | AxiStreamSlaveType  |             |
| clientSlave | AxiStreamSlaveType  |             |
| dhcpSlave   | AxiStreamSlaveType  |             |
## Constants

| Name           | Type                                 | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| -------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SERVER_PORTS_C | Slv16Array(SERVER_SIZE_G-1 downto 0) |  EthPortArrayBigEndian(SERVER_PORTS_G,<br><span style="padding-left:20px"> SERVER_SIZE_G)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| CLIENT_PORTS_C | Slv16Array(CLIENT_SIZE_G-1 downto 0) |  EthPortArrayBigEndian(CLIENT_PORTS_G,<br><span style="padding-left:20px"> CLIENT_SIZE_G)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| REG_INIT_C     | RegType                              |  (       tDestServer      => (others => '0'),<br><span style="padding-left:20px">       tDestClient      => (others => '0'),<br><span style="padding-left:20px">       serverRemotePort => (others => (others => '0')),<br><span style="padding-left:20px">       serverRemoteIp   => (others => (others => '0')),<br><span style="padding-left:20px">       serverRemoteMac  => (others => (others => '0')),<br><span style="padding-left:20px">       clientRemoteDet  => (others => '0'),<br><span style="padding-left:20px">       byteCnt          => (others => '0'),<br><span style="padding-left:20px">       tData            => (others => '0'),<br><span style="padding-left:20px">       sof              => '1',<br><span style="padding-left:20px">       localHost        => '0',<br><span style="padding-left:20px">       route            => NULL_S,<br><span style="padding-left:20px">       rxSlave          => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       dhcpMaster       => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       serverMaster     => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       clientMaster     => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       state            => IDLE_S) |             |
## Types

| Name      | Type                                                                                                                                                 | Description |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| RouteType | ( NULL_S,<br><span style="padding-left:20px"> SERVER_S,<br><span style="padding-left:20px"> CLIENT_S,<br><span style="padding-left:20px"> DHCP_S)    |             |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> CHECK_PORT_S,<br><span style="padding-left:20px"> MOVE_S,<br><span style="padding-left:20px"> LAST_S)  |             |
| RegType   |                                                                                                                                                      |             |
## Processes
- comb: ( broadcastIp, clientSlave, dhcpSlave, localIp, r, rst,
                   rxMaster, serverSlave )
- seq: ( clk )
## Instantiations

- U_RxPipeline: surf.AxiStreamPipeline
- U_Servers: surf.AxiStreamDeMux
- U_Clients: surf.AxiStreamDeMux
- U_Dhcp: surf.AxiStreamPipeline
