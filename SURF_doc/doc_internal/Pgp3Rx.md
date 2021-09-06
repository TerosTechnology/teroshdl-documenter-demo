# Entity: Pgp3Rx

- **File**: Pgp3Rx.vhd
## Diagram

![Diagram](Pgp3Rx.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : PGPv3: https://confluence.slac.stanford.edu/x/OndODQ
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: PGPv3 Receive Block
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

| Generic name      | Type                  | Value | Description |
| ----------------- | --------------------- | ----- | ----------- |
| TPD_G             | time                  | 1 ns  |             |
| NUM_VC_G          | integer range 1 to 16 | 4     |             |
| ALIGN_SLIP_WAIT_G | integer               | 32    |             |
## Ports

| Port name      | Direction | Type                                      | Description                   |
| -------------- | --------- | ----------------------------------------- | ----------------------------- |
| pgpRxClk       | in        | sl                                        | User Transmit interface       |
| pgpRxRst       | in        | sl                                        |                               |
| pgpRxIn        | in        | Pgp3RxInType                              |                               |
| pgpRxOut       | out       | Pgp3RxOutType                             |                               |
| pgpRxMasters   | out       | AxiStreamMasterArray(NUM_VC_G-1 downto 0) |                               |
| pgpRxCtrl      | in        | AxiStreamCtrlArray(NUM_VC_G-1 downto 0)   |  Unused                       |
| remRxFifoCtrl  | out       | AxiStreamCtrlArray(NUM_VC_G-1 downto 0)   | Status of local receive fifos |
| remRxLinkReady | out       | sl                                        |                               |
| locRxLinkReady | out       | sl                                        |                               |
| phyRxClk       | in        | sl                                        | Phy interface                 |
| phyRxRst       | in        | sl                                        |                               |
| phyRxInit      | out       | sl                                        |                               |
| phyRxActive    | in        | sl                                        |                               |
| phyRxValid     | in        | sl                                        |                               |
| phyRxHeader    | in        | slv(1 downto 0)                           |                               |
| phyRxData      | in        | slv(63 downto 0)                          |                               |
| phyRxStartSeq  | in        | sl                                        |                               |
| phyRxSlip      | out       | sl                                        |                               |
## Signals

| Name                   | Type                                    | Description |
| ---------------------- | --------------------------------------- | ----------- |
| gearboxAligned         | sl                                      |             |
| unscramblerValid       | sl                                      |             |
| unscrambledValid       | sl                                      |             |
| unscrambledData        | slv(63 downto 0)                        |             |
| unscrambledHeader      | slv(1 downto 0)                         |             |
| remLinkData            | slv(55 downto 0)                        |             |
| ebValid                | sl                                      |             |
| ebData                 | slv(63 downto 0)                        |             |
| ebHeader               | slv(1 downto 0)                         |             |
| ebOverflow             | sl                                      |             |
| ebStatus               | slv(8 downto 0)                         |             |
| phyRxInitInt           | sl                                      |             |
| pgpRawRxMaster         | AxiStreamMasterType                     |             |
| pgpRawRxSlave          | AxiStreamSlaveType                      |             |
| depacketizedAxisMaster | AxiStreamMasterType                     |             |
| depacketizedAxisSlave  | AxiStreamSlaveType                      |             |
| pgpRxOutProtocol       | Pgp3RxOutType                           |             |
| depacketizerDebug      | Packetizer2DebugType                    |             |
| locRxLinkReadyInt      | sl                                      |             |
| remRxLinkReadyInt      | sl                                      |             |
| remRxFifoCtrlInt       | AxiStreamCtrlArray(NUM_VC_G-1 downto 0) |             |
## Constants

| Name             | Type         | Value                                                   | Description |
| ---------------- | ------------ | ------------------------------------------------------- | ----------- |
| SCRAMBLER_TAPS_C | IntegerArray |  (0 => 39,<br><span style="padding-left:20px"> 1 => 58) |             |
## Instantiations

- U_Pgp3RxGearboxAligner_1: surf.Pgp3RxGearboxAligner
</br>**Description**
 Gearbox aligner

- U_Scrambler_1: surf.Scrambler
- U_Pgp3RxEb_1: surf.Pgp3RxEb
</br>**Description**
 [out]
 Elastic Buffer

- U_Pgp3RxProtocol_1: surf.Pgp3RxProtocol
</br>**Description**
 [out]
 Main RX protocol logic

- U_AxiStreamDepacketizer2_1: surf.AxiStreamDepacketizer2
</br>**Description**
 [in]
 Depacketize the RX data frames

- U_AxiStreamDeMux_1: surf.AxiStreamDeMux
</br>**Description**
 [in]
 Demultiplex the depacketized streams

