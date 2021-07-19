# Entity: IcmpEngine

- **File**: IcmpEngine.vhd
## Diagram

![Diagram](IcmpEngine.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: ICMP Engine (A.K.A. "ping" protocol)
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name    | Direction | Type                | Description               |
| ------------ | --------- | ------------------- | ------------------------- |
| localIp      | in        | slv(31 downto 0)    |  big-Endian configuration |
| ibIcmpMaster | in        | AxiStreamMasterType | Interface to ICMP Engine  |
| ibIcmpSlave  | out       | AxiStreamSlaveType  |                           |
| obIcmpMaster | out       | AxiStreamMasterType |                           |
| obIcmpSlave  | in        | AxiStreamSlaveType  |                           |
| clk          | in        | sl                  | Clock and Reset           |
| rst          | in        | sl                  |                           |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                         | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       tData        => (others => '0'),<br><span style="padding-left:20px">       checksum     => (others => '0'),<br><span style="padding-left:20px">       ibIcmpSlave  => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       obIcmpMaster => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       state        => IDLE_S) |             |
## Types

| Name      | Type                                                                                                                                               | Description |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> RX_HDR_S,<br><span style="padding-left:20px"> TX_HDR_S,<br><span style="padding-left:20px"> MOVE_S)  |             |
| RegType   |                                                                                                                                                    |             |
## Processes
- comb: ( ibIcmpMaster, localIp, obIcmpSlave, r, rst )
- seq: ( clk )
