# Entity: SaltTx

- **File**: SaltTx.vhd
## Diagram

![Diagram](SaltTx.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: SALT TX Engine Module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name       | Type                | Value | Description                                        |
| ------------------ | ------------------- | ----- | -------------------------------------------------- |
| TPD_G              | time                | 1 ns  |                                                    |
| COMMON_TX_CLK_G    | boolean             | false | Set to true if sAxisClk and clk are the same clock |
| SLAVE_AXI_CONFIG_G | AxiStreamConfigType |       |                                                    |
## Ports

| Port name   | Direction | Type                | Description    |
| ----------- | --------- | ------------------- | -------------- |
| sAxisClk    | in        | sl                  | Slave Port     |
| sAxisRst    | in        | sl                  |                |
| sAxisMaster | in        | AxiStreamMasterType |                |
| sAxisSlave  | out       | AxiStreamSlaveType  |                |
| clk         | in        | sl                  | GMII Interface |
| rst         | in        | sl                  |                |
| txPktSent   | out       | sl                  |                |
| txEofeSent  | out       | sl                  |                |
| txEn        | out       | sl                  |                |
| txData      | out       | slv(7 downto 0)     |                |
## Signals

| Name     | Type                | Description |
| -------- | ------------------- | ----------- |
| r        | RegType             |             |
| rin      | RegType             |             |
| rxMaster | AxiStreamMasterType |             |
| rxSlave  | AxiStreamSlaveType  |             |
| sMaster  | AxiStreamMasterType |             |
| sSlave   | AxiStreamSlaveType  |             |
| mMaster  | AxiStreamMasterType |             |
| mSlave   | AxiStreamSlaveType  |             |
| txMaster | AxiStreamMasterType |             |
| txSlave  | AxiStreamSlaveType  |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       flushBuffer => '1',<br><span style="padding-left:20px">       sof         => '0',<br><span style="padding-left:20px">       eof         => '0',<br><span style="padding-left:20px">       eofe        => '0',<br><span style="padding-left:20px">       txPktSent   => '0',<br><span style="padding-left:20px">       txEofeSent  => '0',<br><span style="padding-left:20px">       seqCnt      => (others => '0'),<br><span style="padding-left:20px">       tDest       => (others => '0'),<br><span style="padding-left:20px">       cnt         => (others => '0'),<br><span style="padding-left:20px">       size        => (others => '0'),<br><span style="padding-left:20px">       length      => (others => '0'),<br><span style="padding-left:20px">       checksum    => (others => '0'),<br><span style="padding-left:20px">       txMaster    => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       rxSlave     => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       sMaster     => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       mSlave      => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       state       => IDLE_S) |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> BUFFER_S,<br><span style="padding-left:20px"> PREAMBLE_S,<br><span style="padding-left:20px"> SFD_S,<br><span style="padding-left:20px"> HEADER_S,<br><span style="padding-left:20px"> LENGTH_S,<br><span style="padding-left:20px"> MOVE_S,<br><span style="padding-left:20px"> CHECKSUM_S,<br><span style="padding-left:20px"> FOOTER_S)  |             |
| RegType   |                                                                                                                                                                                                                                                                                                                                                                                           |             |
## Processes
- comb: ( mMaster, r, rst, rxMaster, sSlave, txSlave )
- seq: ( clk )
## Instantiations

- FIFO_RX: surf.AxiStreamFifoV2
- DATAGRAM_BUFFER: surf.AxiStreamFifoV2
- U_TxResize: surf.SaltTxResize
