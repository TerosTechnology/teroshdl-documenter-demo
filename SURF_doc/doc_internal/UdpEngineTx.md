# Entity: UdpEngineTx

- **File**: UdpEngineTx.vhd
## Diagram

![Diagram](UdpEngineTx.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: UDP TX Engine Module
 Note: UDP checksum checked in EthMac core
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

| Generic name   | Type          | Value       | Description                                                                           |
| -------------- | ------------- | ----------- | ------------------------------------------------------------------------------------- |
| TPD_G          | time          | 1 ns        | Simulation Generics                                                                   |
| SIZE_G         | positive      | 1           | UDP General Generic                                                                   |
| TX_FLOW_CTRL_G | boolean       | true        |  True: Blow off the UDP TX data if link down, False: Backpressure until TX link is up |
| PORT_G         | PositiveArray | (0 => 8192) |                                                                                       |
## Ports

| Port name    | Direction | Type                                    | Description                   |
| ------------ | --------- | --------------------------------------- | ----------------------------- |
| obUdpMaster  | out       | AxiStreamMasterType                     | Interface to IPV4 Engine      |
| obUdpSlave   | in        | AxiStreamSlaveType                      |                               |
| linkUp       | out       | slv(SIZE_G-1 downto 0)                  | Interface to User Application |
| localMac     | in        | slv(47 downto 0)                        |                               |
| localIp      | in        | slv(31 downto 0)                        |                               |
| remotePort   | in        | Slv16Array(SIZE_G-1 downto 0)           |                               |
| remoteIp     | in        | Slv32Array(SIZE_G-1 downto 0)           |                               |
| remoteMac    | in        | Slv48Array(SIZE_G-1 downto 0)           |                               |
| ibMasters    | in        | AxiStreamMasterArray(SIZE_G-1 downto 0) |                               |
| ibSlaves     | out       | AxiStreamSlaveArray(SIZE_G-1 downto 0)  |                               |
| obDhcpMaster | in        | AxiStreamMasterType                     | Interface to DHCP Engine      |
| obDhcpSlave  | out       | AxiStreamSlaveType                      |                               |
| clk          | in        | sl                                      | Clock and Reset               |
| rst          | in        | sl                                      |                               |
## Signals

| Name     | Type                | Description |
| -------- | ------------------- | ----------- |
| r        | RegType             |             |
| rin      | RegType             |             |
| txMaster | AxiStreamMasterType |             |
| txSlave  | AxiStreamSlaveType  |             |
## Constants

| Name       | Type                          | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ---------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| PORT_C     | Slv16Array(SIZE_G-1 downto 0) |  EthPortArrayBigEndian(PORT_G,<br><span style="padding-left:20px"> SIZE_G)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |             |
| REG_INIT_C | RegType                       |  (       linkUp      => (others => '0'),<br><span style="padding-left:20px">       tKeep       => (others => '0'),<br><span style="padding-left:20px">       tData       => (others => '0'),<br><span style="padding-left:20px">       tLast       => '0',<br><span style="padding-left:20px">       eofe        => '0',<br><span style="padding-left:20px">       chPntr      => 0,<br><span style="padding-left:20px">       index       => 0,<br><span style="padding-left:20px">       obDhcpSlave => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       ibSlaves    => (others => AXI_STREAM_SLAVE_INIT_C),<br><span style="padding-left:20px">       txMaster    => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       state       => IDLE_S) |             |
## Types

| Name      | Type                                                                                                                                                                                                                                               | Description |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> DHCP_HDR_S,<br><span style="padding-left:20px"> HDR_S,<br><span style="padding-left:20px"> DHCP_BUFFER_S,<br><span style="padding-left:20px"> BUFFER_S,<br><span style="padding-left:20px"> LAST_S)  |             |
| RegType   |                                                                                                                                                                                                                                                    |             |
## Processes
- comb: ( ibMasters, localIp, localMac, obDhcpMaster, r, remoteIp,
                   remoteMac, remotePort, rst, txSlave )
- seq: ( clk )
## Instantiations

- U_TxPipeline: surf.AxiStreamPipeline
