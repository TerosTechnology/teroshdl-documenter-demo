# Entity: IpV4EngineTx

## Diagram

![Diagram](IpV4EngineTx.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: IPv4 TX Engine Module
Note: IPv4 checksum checked in EthMac core
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name    | Type            | Value        | Description |
| --------------- | --------------- | ------------ | ----------- |
| TPD_G           | time            | 1 ns         |             |
| PROTOCOL_SIZE_G | positive        | 1            |             |
| PROTOCOL_G      | Slv8Array       | (0 => UDP_C) |             |
| TTL_G           | slv(7 downto 0) | x"20"        |             |
| VLAN_G          | boolean         | false        |             |
## Ports

| Port name         | Direction | Type                                             | Description                           |
| ----------------- | --------- | ------------------------------------------------ | ------------------------------------- |
| localMac          | in        | slv(47 downto 0)                                 |  big-Endian configuration             |
| obIpv4Master      | out       | AxiStreamMasterType                              | Interface to Ethernet Frame MUX/DEMUX |
| obIpv4Slave       | in        | AxiStreamSlaveType                               |                                       |
| localhostMaster   | out       | AxiStreamMasterType                              |                                       |
| localhostSlave    | in        | AxiStreamSlaveType                               |                                       |
| obProtocolMasters | in        | AxiStreamMasterArray(PROTOCOL_SIZE_G-1 downto 0) | Interface to Protocol Engine          |
| obProtocolSlaves  | out       | AxiStreamSlaveArray(PROTOCOL_SIZE_G-1 downto 0)  |                                       |
| clk               | in        | sl                                               | Clock and Reset                       |
| rst               | in        | sl                                               |                                       |
## Signals

| Name        | Type                | Description |
| ----------- | ------------------- | ----------- |
| r           | RegType             |             |
| rin         | RegType             |             |
| rxMaster    | AxiStreamMasterType |             |
| rxSlave     | AxiStreamSlaveType  |             |
| txMaster    | AxiStreamMasterType |             |
| txSlave     | AxiStreamSlaveType  |             |
| mAxisMaster | AxiStreamMasterType |             |
| mAxisSlave  | AxiStreamSlaveType  |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       eofe     => '0',<br><span style="padding-left:20px">       tKeep    => (others => '0'),<br><span style="padding-left:20px">       tData    => (others => '0'),<br><span style="padding-left:20px">       tDest    => (others => '0'),<br><span style="padding-left:20px">       id       => (others => '0'),<br><span style="padding-left:20px">       rxSlave  => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       txMaster => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       state    => IDLE_S) |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                  | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> IPV4_HDR0_S,<br><span style="padding-left:20px"> IPV4_HDR1_S,<br><span style="padding-left:20px"> IPV4_HDR2_S,<br><span style="padding-left:20px"> MOVE_S,<br><span style="padding-left:20px"> LAST_S)  |             |
| RegType   |                                                                                                                                                                                                                                                       |             |
## Processes
- comb: ( localMac, r, rst, rxMaster, txSlave )
- seq: ( clk )
## Instantiations

- AxiStreamMux_Inst: surf.AxiStreamMux
- U_TxPipeline: surf.AxiStreamPipeline
- U_DeMux: surf.AxiStreamDeMux
