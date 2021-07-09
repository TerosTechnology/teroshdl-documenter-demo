# Entity: IpV4Engine

## Diagram

![Diagram](IpV4Engine.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: IPv4 Top-level Module for IPv4/ARP/ICMP
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name    | Type            | Value        | Description                                |
| --------------- | --------------- | ------------ | ------------------------------------------ |
| TPD_G           | time            | 1 ns         | Simulation parameter only                  |
| PROTOCOL_SIZE_G | positive        | 1            | Default to 1x protocol                     |
| PROTOCOL_G      | Slv8Array       | (0 => UDP_C) | Default to UDP protocol                    |
| CLIENT_SIZE_G   | positive        | 1            | Sets the number of attached client engines |
| CLK_FREQ_G      | real            | 156.25E+06   | In units of Hz                             |
| TTL_G           | slv(7 downto 0) | x"20"        |                                            |
| ICMP_G          | boolean         | true         |                                            |
| ARP_G           | boolean         | true         |                                            |
| VLAN_G          | boolean         | false        |                                            |
## Ports

| Port name         | Direction | Type                                             | Description                                         |
| ----------------- | --------- | ------------------------------------------------ | --------------------------------------------------- |
| localMac          | in        | slv(47 downto 0)                                 |  big-Endian configuration                           |
| localIp           | in        | slv(31 downto 0)                                 |  big-Endian configuration                           |
| obMacMaster       | in        | AxiStreamMasterType                              | Interface to Ethernet Media Access Controller (MAC) |
| obMacSlave        | out       | AxiStreamSlaveType                               |                                                     |
| ibMacMaster       | out       | AxiStreamMasterType                              |                                                     |
| ibMacSlave        | in        | AxiStreamSlaveType                               |                                                     |
| obProtocolMasters | in        | AxiStreamMasterArray(PROTOCOL_SIZE_G-1 downto 0) | Interface to Protocol Engine(s)                     |
| obProtocolSlaves  | out       | AxiStreamSlaveArray(PROTOCOL_SIZE_G-1 downto 0)  |                                                     |
| ibProtocolMasters | out       | AxiStreamMasterArray(PROTOCOL_SIZE_G-1 downto 0) |                                                     |
| ibProtocolSlaves  | in        | AxiStreamSlaveArray(PROTOCOL_SIZE_G-1 downto 0)  |                                                     |
| arpReqMasters     | in        | AxiStreamMasterArray(CLIENT_SIZE_G-1 downto 0)   | Request via IP address                              |
| arpReqSlaves      | out       | AxiStreamSlaveArray(CLIENT_SIZE_G-1 downto 0)    |                                                     |
| arpAckMasters     | out       | AxiStreamMasterArray(CLIENT_SIZE_G-1 downto 0)   | Respond with MAC address                            |
| arpAckSlaves      | in        | AxiStreamSlaveArray(CLIENT_SIZE_G-1 downto 0)    |                                                     |
| clk               | in        | sl                                               | Clock and Reset                                     |
| rst               | in        | sl                                               |                                                     |
## Signals

| Name            | Type                                           | Description |
| --------------- | ---------------------------------------------- | ----------- |
| ibArpMaster     | AxiStreamMasterType                            |             |
| ibArpSlave      | AxiStreamSlaveType                             |             |
| obArpMaster     | AxiStreamMasterType                            |             |
| obArpSlave      | AxiStreamSlaveType                             |             |
| ibIpv4Master    | AxiStreamMasterType                            |             |
| ibIpv4Slave     | AxiStreamSlaveType                             |             |
| obIpv4Master    | AxiStreamMasterType                            |             |
| obIpv4Slave     | AxiStreamSlaveType                             |             |
| localhostMaster | AxiStreamMasterType                            |             |
| localhostSlave  | AxiStreamSlaveType                             |             |
| ibMasters       | AxiStreamMasterArray(PROTOCOL_SIZE_G downto 0) |             |
| ibSlaves        | AxiStreamSlaveArray(PROTOCOL_SIZE_G downto 0)  |             |
| obMasters       | AxiStreamMasterArray(PROTOCOL_SIZE_G downto 0) |             |
| obSlaves        | AxiStreamSlaveArray(PROTOCOL_SIZE_G downto 0)  |             |
## Constants

| Name       | Type                                | Value                    | Description |
| ---------- | ----------------------------------- | ------------------------ | ----------- |
| PROTOCOL_C | Slv8Array(PROTOCOL_SIZE_G downto 0) |  GenIPv4List(PROTOCOL_G) |             |
## Functions
- GenIPv4List <font id="function_arguments">(foo : Slv8Array(PROTOCOL_SIZE_G-1 downto 0)) </font> <font id="function_return">return Slv8Array </font>
## Instantiations

- U_EthFrameDeMux: surf.IpV4EngineDeMux
- U_EthFrameMux: surf.AxiStreamMux
- U_IpV4EngineRx: surf.IpV4EngineRx
- U_IpV4EngineTx: surf.IpV4EngineTx
