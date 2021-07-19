# Entity: Pgp4Tx

- **File**: Pgp4Tx.vhd
## Diagram

![Diagram](Pgp4Tx.svg "Diagram")
## Description

Title      : PGPv4: https://confluence.slac.stanford.edu/x/1dzgEQ
Company    : SLAC National Accelerator Laboratory
Description: Pgpv4 Transmit
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name             | Type                  | Value             | Description                     |
| ------------------------ | --------------------- | ----------------- | ------------------------------- |
| TPD_G                    | time                  | 1 ns              |                                 |
| NUM_VC_G                 | integer range 1 to 16 | 1                 | PGP configuration               |
| CELL_WORDS_MAX_G         | integer               | 256               | Number of 64-bit words per cell |
| MUX_MODE_G               | string                | "INDEXED"         | Or "ROUTED"                     |
| MUX_TDEST_ROUTES_G       | Slv8Array             | (0 => "--------") | Only used in ROUTED mode        |
| MUX_TDEST_LOW_G          | integer range 0 to 7  | 0                 |                                 |
| MUX_ILEAVE_EN_G          | boolean               | true              |                                 |
| MUX_ILEAVE_ON_NOTVALID_G | boolean               | true              |                                 |
## Ports

| Port name      | Direction | Type                                      | Description                                       |
| -------------- | --------- | ----------------------------------------- | ------------------------------------------------- |
| pgpTxClk       | in        | sl                                        | Transmit interface                                |
| pgpTxRst       | in        | sl                                        |                                                   |
| pgpTxIn        | in        | Pgp4TxInType                              |                                                   |
| pgpTxOut       | out       | Pgp4TxOutType                             |                                                   |
| pgpTxMasters   | in        | AxiStreamMasterArray(NUM_VC_G-1 downto 0) |                                                   |
| pgpTxSlaves    | out       | AxiStreamSlaveArray(NUM_VC_G-1 downto 0)  |                                                   |
| locRxFifoCtrl  | in        | AxiStreamCtrlArray(NUM_VC_G-1 downto 0)   | Status of receive and remote FIFOs (Asynchronous) |
| locRxLinkReady | in        | sl                                        |                                                   |
| remRxFifoCtrl  | in        | AxiStreamCtrlArray(NUM_VC_G-1 downto 0)   |                                                   |
| remRxLinkReady | in        | sl                                        |                                                   |
| phyTxActive    | in        | sl                                        | PHY interface                                     |
| phyTxReady     | in        | sl                                        |                                                   |
| phyTxValid     | out       | sl                                        |                                                   |
| phyTxStart     | out       | sl                                        |                                                   |
| phyTxData      | out       | slv(63 downto 0)                          |                                                   |
| phyTxHeader    | out       | slv(1 downto 0)                           |                                                   |
## Signals

| Name               | Type                                    | Description      |
| ------------------ | --------------------------------------- | ---------------- |
| syncLocRxFifoCtrl  | AxiStreamCtrlArray(NUM_VC_G-1 downto 0) |                  |
| syncLocRxLinkReady | sl                                      |                  |
| syncRemRxFifoCtrl  | AxiStreamCtrlArray(NUM_VC_G-1 downto 0) |                  |
| syncRemRxLinkReady | sl                                      |                  |
| disableSel         | slv(NUM_VC_G-1 downto 0)                | Pipeline signals |
| rearbitrate        | sl                                      |                  |
| muxedTxMaster      | AxiStreamMasterType                     |                  |
| muxedTxSlave       | AxiStreamSlaveType                      |                  |
| packetizedTxMaster | AxiStreamMasterType                     |                  |
| packetizedTxSlave  | AxiStreamSlaveType                      |                  |
| phyTxActiveL       | sl                                      |                  |
| protTxValid        | sl                                      |                  |
| protTxReady        | sl                                      |                  |
| protTxStart        | sl                                      |                  |
| protTxData         | slv(63 downto 0)                        |                  |
| protTxHeader       | slv(1 downto 0)                         |                  |
## Processes
- DISABLE_SEL: ( pgpTxIn, syncRemRxFifoCtrl )
**Description**
Use synchronized remote status to disable channels from mux selection
All flow control overriden by pgpTxIn 'disable' and 'flowCntlDis'

## Instantiations

- U_Synchronizer_REM: surf.Synchronizer
- U_Synchronizer_LOC: surf.Synchronizer
**Description**
Synchronize local rx status

- U_AxiStreamMux_1: surf.AxiStreamMux
**Description**
Multiplex the incomming tx streams with interleaving

- U_AxiStreamPacketizer2_1: surf.AxiStreamPacketizer2
**Description**
[in]
Feed muxed stream to packetizer
Note that the mux is doing the work of chunking
Packetizer applies packet formatting and CRC
rearbitrate signal doesn't really do anything (yet)

- U_Pgp4TxProtocol_1: surf.Pgp4TxProtocol
**Description**
[in]
Feed packets into PGP TX Protocol engine
Translates Packetizer2 frames, status, and opcodes into unscrambled 64b66b charachters

- U_Scrambler_1: surf.Scrambler
**Description**
[out]
Scramble the data for 64b66b

