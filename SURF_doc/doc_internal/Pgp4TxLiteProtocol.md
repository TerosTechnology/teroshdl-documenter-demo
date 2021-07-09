# Entity: Pgp4TxLiteProtocol

## Diagram

![Diagram](Pgp4TxLiteProtocol.svg "Diagram")
## Description

Title      : PGPv4: https://confluence.slac.stanford.edu/x/1dzgEQ
Company    : SLAC National Accelerator Laboratory
Description: PGPv4Lite Transmit Protocol
Takes pre-packetized AxiStream frames and creates a PGPv4 66/64 protocol
stream (pre-scrambler). Inserts IDLE and SKP codes as needed. Inserts
user K codes on request.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type                  | Value | Description |
| -------------- | --------------------- | ----- | ----------- |
| TPD_G          | time                  | 1 ns  |             |
| NUM_VC_G       | integer range 1 to 16 | 1     |             |
| SKIP_EN_G      | boolean               | false |             |
| FLOW_CTRL_EN_G | boolean               | false |             |
| STARTUP_HOLD_G | integer               | 0     |             |
## Ports

| Port name      | Direction | Type                                    | Description                                                               |
| -------------- | --------- | --------------------------------------- | ------------------------------------------------------------------------- |
| pgpTxClk       | in        | sl                                      | User Transmit interface                                                   |
| pgpTxRst       | in        | sl                                      |                                                                           |
| pgpTxIn        | in        | Pgp4TxInType                            |                                                                           |
| pgpTxOut       | out       | Pgp4TxOutType                           |                                                                           |
| pgpTxActive    | in        | sl                                      |                                                                           |
| pgpTxMaster    | in        | AxiStreamMasterType                     |                                                                           |
| pgpTxSlave     | out       | AxiStreamSlaveType                      |                                                                           |
| locRxFifoCtrl  | in        | AxiStreamCtrlArray(NUM_VC_G-1 downto 0) | Status of local receive fifosThese get synchronized by the Pgp4Tx parent  |
| locRxLinkReady | in        | sl                                      |                                                                           |
| remRxLinkReady | in        | sl                                      |                                                                           |
| phyTxActive    | in        | sl                                      | Output Interface                                                          |
| protTxReady    | in        | sl                                      |                                                                           |
| protTxValid    | out       | sl                                      |                                                                           |
| protTxStart    | out       | sl                                      |                                                                           |
| protTxData     | out       | slv(63 downto 0)                        |                                                                           |
| protTxHeader   | out       | slv(1 downto 0)                         |                                                                           |
## Signals

| Name         | Type             | Description |
| ------------ | ---------------- | ----------- |
| crcIn        | slv(63 downto 0) |             |
| crcOut       | slv(31 downto 0) |             |
| r            | RegType          |             |
| rin          | RegType          |             |
| crcReset     | sl               |             |
| crcDataValid | sl               |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       crcReset          => '0',<br><span style="padding-left:20px">       crcDataValid      => '0',<br><span style="padding-left:20px">       waitSof           => '1',<br><span style="padding-left:20px">       doEof             => '0',<br><span style="padding-left:20px">       tUserLast         => (others => '0'),<br><span style="padding-left:20px">       pauseDly          => (others => '0'),<br><span style="padding-left:20px">       pauseEvent        => (others => '0'),<br><span style="padding-left:20px">       pauseEventSent    => (others => '0'),<br><span style="padding-left:20px">       overflowDly       => (others => '0'),<br><span style="padding-left:20px">       overflowEvent     => (others => '0'),<br><span style="padding-left:20px">       overflowEventSent => (others => '0'),<br><span style="padding-left:20px">       skpInterval       => PGP4_TX_IN_INIT_C.skpInterval,<br><span style="padding-left:20px">       skpCount          => (others => '0'),<br><span style="padding-left:20px">       startupCount      => 0,<br><span style="padding-left:20px">       pgpTxSlave        => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       opCodeReady       => '0',<br><span style="padding-left:20px">       linkReady         => '0',<br><span style="padding-left:20px">       frameTx           => '0',<br><span style="padding-left:20px">       frameTxErr        => '0',<br><span style="padding-left:20px">       protTxValid       => '0',<br><span style="padding-left:20px">       protTxStart       => '0',<br><span style="padding-left:20px">       protTxData        => (others => '0'),<br><span style="padding-left:20px">       protTxHeader      => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( crcOut, locRxFifoCtrl, locRxLinkReady, pgpTxIn, pgpTxMaster,
                   pgpTxRst, phyTxActive, protTxReady, r, remRxLinkReady )
- seq: ( pgpTxClk )
## Instantiations

- U_Crc32: surf.Crc32Parallel
