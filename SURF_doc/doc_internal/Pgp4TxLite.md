# Entity: Pgp4TxLite

- **File**: Pgp4TxLite.vhd
## Diagram

![Diagram](Pgp4TxLite.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : PGPv4: https://confluence.slac.stanford.edu/x/1dzgEQ
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Pgp4TxLite (no SOC/EOC support)
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

| Generic name   | Type                  | Value | Description |
| -------------- | --------------------- | ----- | ----------- |
| TPD_G          | time                  | 1 ns  |             |
| NUM_VC_G       | integer range 1 to 16 | 1     |             |
| SKIP_EN_G      | boolean               | false |             |
| FLOW_CTRL_EN_G | boolean               | false |             |
## Ports

| Port name      | Direction | Type                                      | Description                                       |
| -------------- | --------- | ----------------------------------------- | ------------------------------------------------- |
| pgpTxClk       | in        | sl                                        | Transmit interface                                |
| pgpTxRst       | in        | sl                                        |                                                   |
| pgpTxIn        | in        | Pgp4TxInType                              |                                                   |
| pgpTxOut       | out       | Pgp4TxOutType                             |                                                   |
| pgpTxActive    | in        | sl                                        |                                                   |
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

| Name               | Type                                    | Description        |
| ------------------ | --------------------------------------- | ------------------ |
| syncLocRxFifoCtrl  | AxiStreamCtrlArray(NUM_VC_G-1 downto 0) |                    |
| syncLocRxLinkReady | sl                                      |                    |
| syncRemRxFifoCtrl  | AxiStreamCtrlArray(NUM_VC_G-1 downto 0) |                    |
| syncRemRxLinkReady | sl                                      |                    |
| disableSel         | slv(NUM_VC_G-1 downto 0)                |  Pipeline signals  |
| rearbitrate        | sl                                      |                    |
| muxedTxMaster      | AxiStreamMasterType                     |                    |
| muxedTxSlave       | AxiStreamSlaveType                      |                    |
| phyTxActiveL       | sl                                      |                    |
| protTxValid        | sl                                      |                    |
| protTxReady        | sl                                      |                    |
| protTxStart        | sl                                      |                    |
| protTxData         | slv(63 downto 0)                        |                    |
| protTxHeader       | slv(1 downto 0)                         |                    |
## Processes
- DISABLE_SEL: ( pgpTxIn, syncRemRxFifoCtrl )
**Description**
----------------------------------------------------------------------  Use synchronized remote status to disable channels from mux selection  All flow control overridden by pgpTxIn 'disable' and 'flowCntlDis' ---------------------------------------------------------------------- 
## Instantiations

- U_Protocol: surf.Pgp4TxLiteProtocol
**Description**
--------------------------------------------------------------------------------------
 Feed packets into PGP TX Protocol engine
 Translates Packetizer2 frames, status, and opcodes into unscrambled 64b66b characters
--------------------------------------------------------------------------------------

- U_Scrambler_1: surf.Scrambler
**Description**
 [out]
 Scramble the data for 64b66b

