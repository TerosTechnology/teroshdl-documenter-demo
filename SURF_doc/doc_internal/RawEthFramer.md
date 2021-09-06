# Entity: RawEthFramer

- **File**: RawEthFramer.vhd
## Diagram

![Diagram](RawEthFramer.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Top-level Raw L2 Ethernet Framer
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
| obMacMaster | in        | AxiStreamMasterType | Interface to Ethernet Media Access Controller (MAC) |
| obMacSlave  | out       | AxiStreamSlaveType  |                                                     |
| ibMacMaster | out       | AxiStreamMasterType |                                                     |
| ibMacSlave  | in        | AxiStreamSlaveType  |                                                     |
| ibAppMaster | out       | AxiStreamMasterType | Interface to Application engine(s)                  |
| ibAppSlave  | in        | AxiStreamSlaveType  |                                                     |
| obAppMaster | in        | AxiStreamMasterType |                                                     |
| obAppSlave  | out       | AxiStreamSlaveType  |                                                     |
| clk         | in        | sl                  | Clock and Reset                                     |
| rst         | in        | sl                  |                                                     |
## Signals

| Name   | Type             | Description |
| ------ | ---------------- | ----------- |
| r      | RegType          |             |
| rin    | RegType          |             |
| rxReq  | sl               |             |
| txReq  | sl               |             |
| rxDest | slv(7 downto 0)  |             |
| txDest | slv(7 downto 0)  |             |
| rxAck  | sl               |             |
| txAck  | sl               |             |
| rxMac  | slv(47 downto 0) |             |
| txMac  | slv(47 downto 0) |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       rxAck => '0',<br><span style="padding-left:20px">       txAck => '0',<br><span style="padding-left:20px">       rxMac => (others => '0'),<br><span style="padding-left:20px">       txMac => (others => '0'),<br><span style="padding-left:20px">       rdEn  => '0',<br><span style="padding-left:20px">       tDest => (others => '0'),<br><span style="padding-left:20px">       state => IDLE_S) |             |
## Types

| Name      | Type                                                                                           | Description |
| --------- | ---------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> RX_S,<br><span style="padding-left:20px"> TX_S)  |             |
| RegType   |                                                                                                |             |
## Processes
- comb: ( r, remoteMac, rst, rxDest, rxReq, txDest, txReq )
- seq: ( clk )
## Instantiations

- U_Tx: surf.RawEthFramerTx
- U_Rx: surf.RawEthFramerRx
