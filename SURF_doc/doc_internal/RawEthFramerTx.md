# Entity: RawEthFramerTx

- **File**: RawEthFramerTx.vhd
## Diagram

![Diagram](RawEthFramerTx.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Raw L2 Ethernet Framer's TX Engine
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type             | Value   | Description |
| ------------ | ---------------- | ------- | ----------- |
| TPD_G        | time             | 1 ns    |             |
| ETH_TYPE_G   | slv(15 downto 0) | x"0010" |             |
## Ports

| Port name   | Direction | Type                | Description                                         |
| ----------- | --------- | ------------------- | --------------------------------------------------- |
| localMac    | in        | slv(47 downto 0)    |  big-Endian configuration                           |
| remoteMac   | in        | slv(47 downto 0)    |  big-Endian configuration                           |
| tDest       | out       | slv(7 downto 0)     |                                                     |
| req         | out       | sl                  |                                                     |
| ack         | in        | sl                  |                                                     |
| ibMacMaster | out       | AxiStreamMasterType | Interface to Ethernet Media Access Controller (MAC) |
| ibMacSlave  | in        | AxiStreamSlaveType  |                                                     |
| obAppMaster | in        | AxiStreamMasterType | Interface to Application engine(s)                  |
| obAppSlave  | out       | AxiStreamSlaveType  |                                                     |
| clk         | in        | sl                  | Clock and Reset                                     |
| rst         | in        | sl                  |                                                     |
## Signals

| Name   | Type             | Description |
| ------ | ---------------- | ----------- |
| r      | RegType          |             |
| rin    | RegType          |             |
| rdData | slv(63 downto 0) |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       bcf         => '0',<br><span style="padding-left:20px">       req         => '0',<br><span style="padding-left:20px">       tDest       => (others => '0'),<br><span style="padding-left:20px">       wen         => '0',<br><span style="padding-left:20px">       wrAddr      => (others => '0'),<br><span style="padding-left:20px">       wrData      => (others => '0'),<br><span style="padding-left:20px">       rdAddr      => (others => '0'),<br><span style="padding-left:20px">       minByteCnt  => 0,<br><span style="padding-left:20px">       eof         => '0',<br><span style="padding-left:20px">       eofe        => '0',<br><span style="padding-left:20px">       obAppSlave  => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       ibMacMaster => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       state       => IDLE_S) |             |
## Types

| Name      | Type                                                                                                                                             | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> TDEST_S,<br><span style="padding-left:20px"> CACHE_S,<br><span style="padding-left:20px"> MOVE_S)  |             |
| RegType   |                                                                                                                                                  |             |
## Processes
- comb: ( ack, ibMacSlave, localMac, obAppMaster, r, rdData, remoteMac, rst )
- seq: ( clk )
## Instantiations

- U_MinEthCache: surf.LutRam
