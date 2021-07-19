# Entity: IpV4EngineDeMux

- **File**: IpV4EngineDeMux.vhd
## Diagram

![Diagram](IpV4EngineDeMux.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: IPv4 AXIS DEMUX module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| TPD_G        | time    | 1 ns  |             |
| VLAN_G       | boolean | false |             |
## Ports

| Port name    | Direction | Type                | Description               |
| ------------ | --------- | ------------------- | ------------------------- |
| localMac     | in        | slv(47 downto 0)    |  big-Endian configuration |
| obMacMaster  | in        | AxiStreamMasterType | Slave                     |
| obMacSlave   | out       | AxiStreamSlaveType  |                           |
| ibArpMaster  | out       | AxiStreamMasterType | Masters                   |
| ibArpSlave   | in        | AxiStreamSlaveType  |                           |
| ibIpv4Master | out       | AxiStreamMasterType |                           |
| ibIpv4Slave  | in        | AxiStreamSlaveType  |                           |
| clk          | in        | sl                  | Clock and Reset           |
| rst          | in        | sl                  |                           |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name            | Type             | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| --------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| BROADCAST_MAC_C | slv(47 downto 0) |  (others => '1')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |             |
| REG_INIT_C      | RegType          |  (       arpSel       => '0',<br><span style="padding-left:20px">       ipv4Sel      => '0',<br><span style="padding-left:20px">       dly          => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       ibArpMaster  => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       ibIpv4Master => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       obMacSlave   => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       state        => IDLE_S) |             |
## Types

| Name      | Type                                                                                                | Description |
| --------- | --------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> CHECK_S,<br><span style="padding-left:20px"> MOVE_S)  |             |
| RegType   |                                                                                                     |             |
## Processes
- comb: ( ibArpSlave, ibIpv4Slave, localMac, obMacMaster, r, rst )
- seq: ( clk )
