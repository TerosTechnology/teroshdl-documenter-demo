# Entity: RawEthFramerRx

- **File**: RawEthFramerRx.vhd
## Diagram

![Diagram](RawEthFramerRx.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Raw L2 Ethernet Framer's RX Engine
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

| Generic name | Type             | Value   | Description |
| ------------ | ---------------- | ------- | ----------- |
| TPD_G        | time             | 1 ns    |             |
| ETH_TYPE_G   | slv(15 downto 0) | x"0010" |             |
## Ports

| Port name   | Direction | Type                | Description                                         |
| ----------- | --------- | ------------------- | --------------------------------------------------- |
| localMac    | in        | slv(47 downto 0)    |   big-Endian configuration                          |
| remoteMac   | in        | slv(47 downto 0)    |   big-Endian configuration                          |
| tDest       | out       | slv(7 downto 0)     |                                                     |
| req         | out       | sl                  |                                                     |
| ack         | in        | sl                  |                                                     |
| obMacMaster | in        | AxiStreamMasterType | Interface to Ethernet Media Access Controller (MAC) |
| obMacSlave  | out       | AxiStreamSlaveType  |                                                     |
| ibAppMaster | out       | AxiStreamMasterType | Interface to Application engine(s)                  |
| ibAppSlave  | in        | AxiStreamSlaveType  |                                                     |
| clk         | in        | sl                  | Clock and Reset                                     |
| rst         | in        | sl                  |                                                     |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type             | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ---------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| BC_MAC_C   | slv(47 downto 0) |  x"FFFFFFFFFFFF"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |             |
| REG_INIT_C | RegType          |  (       bcf         => '0',<br><span style="padding-left:20px">       req         => '0',<br><span style="padding-left:20px">       dstMac      => (others => '0'),<br><span style="padding-left:20px">       srcMac      => (others => '0'),<br><span style="padding-left:20px">       minByteCnt  => 0,<br><span style="padding-left:20px">       sof         => '1',<br><span style="padding-left:20px">       eof         => '0',<br><span style="padding-left:20px">       eofe        => '0',<br><span style="padding-left:20px">       obMacSlave  => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       ibAppMaster => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       state       => IDLE_S) |             |
## Types

| Name      | Type                                                                                                                                           | Description |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> HDR_S,<br><span style="padding-left:20px"> TDEST_S,<br><span style="padding-left:20px"> MOVE_S)  |             |
| RegType   |                                                                                                                                                |             |
## Processes
- comb: ( ack, ibAppSlave, localMac, obMacMaster, r, remoteMac, rst )
- seq: ( clk )
