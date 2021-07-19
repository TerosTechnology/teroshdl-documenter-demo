# Entity: EthMacRxCsum

- **File**: EthMacRxCsum.vhd
## Diagram

![Diagram](EthMacRxCsum.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: RX Checksum Hardware Offloading Engine
https://docs.google.com/spreadsheets/d/1_1M1keasfq8RLmRYHkO0IlRhMq5YZTgJ7OGrWvkib8I/edit?usp=sharing
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
| JUMBO_G      | boolean | true  |             |
| VLAN_G       | boolean | false |             |
## Ports

| Port name   | Direction | Type                | Description           |
| ----------- | --------- | ------------------- | --------------------- |
| ethClk      | in        | sl                  | Clock and Reset       |
| ethRst      | in        | sl                  |                       |
| ipCsumEn    | in        | sl                  | Configurations        |
| tcpCsumEn   | in        | sl                  |                       |
| udpCsumEn   | in        | sl                  |                       |
| sAxisMaster | in        | AxiStreamMasterType | Inbound data from MAC |
| mAxisMaster | out       | AxiStreamMasterType |                       |
## Signals

| Name | Type                   | Description |
| ---- | ---------------------- | ----------- |
| r    | RegType                |             |
| rin  | RegType                |             |
| dbg  | Slv16Array(1 downto 0) |             |
## Constants

| Name             | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ---------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| MAX_FRAME_SIZE_C | natural |  ite(JUMBO_G,<br><span style="padding-left:20px"> 9000,<br><span style="padding-left:20px"> 1500)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |             |
| REG_INIT_C       | RegType |  (       valid        => (others => '0'),<br><span style="padding-left:20px">       fragDet      => (others => '0'),<br><span style="padding-left:20px">       eofeDet      => (others => '0'),<br><span style="padding-left:20px">       ipv4Det      => (others => '0'),<br><span style="padding-left:20px">       udpDet       => (others => '0'),<br><span style="padding-left:20px">       tcpDet       => (others => '0'),<br><span style="padding-left:20px">       tcpFlag      => '0',<br><span style="padding-left:20px">       pipeFlush    => '0',<br><span style="padding-left:20px">       byteCnt      => 0,<br><span style="padding-left:20px">       ipv4Hdr      => (others => (others => '0')),<br><span style="padding-left:20px">       ipv4Len      => (others => (others => '0')),<br><span style="padding-left:20px">       protLen      => (others => (others => '0')),<br><span style="padding-left:20px">       protCsum     => (others => (others => '0')),<br><span style="padding-left:20px">       calc         => (others => ETH_MAC_CSUM_ACCUM_INIT_C),<br><span style="padding-left:20px">       tKeep        => (others => '0'),<br><span style="padding-left:20px">       tData        => (others => '0'),<br><span style="padding-left:20px">       mAxisMaster  => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       mAxisMasters => (others => AXI_STREAM_MASTER_INIT_C),<br><span style="padding-left:20px">       state        => IDLE_S) |             |
## Types

| Name      | Type                                                                                                                                                                                                    | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> IPV4_HDR0_S,<br><span style="padding-left:20px"> IPV4_HDR1_S,<br><span style="padding-left:20px"> MOVE_S,<br><span style="padding-left:20px"> BLOWOFF_S)  |             |
| RegType   |                                                                                                                                                                                                         |             |
## Processes
- comb: ( ethRst, ipCsumEn, r, sAxisMaster, tcpCsumEn, udpCsumEn )
- seq: ( ethClk )
