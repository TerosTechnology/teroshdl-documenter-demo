# Entity: Pgp3RxProtocol

- **File**: Pgp3RxProtocol.vhd
## Diagram

![Diagram](Pgp3RxProtocol.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : PGPv3: https://confluence.slac.stanford.edu/x/OndODQ
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: PGPv3 Receive Protocol
 Takes pre-packetized AxiStream frames and creates a PGPv3 66/64 protocol
 stream (pre-scrambler). Inserts IDLE and SKP codes as needed. Inserts
 user K codes on request.
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

| Generic name | Type                  | Value | Description |
| ------------ | --------------------- | ----- | ----------- |
| TPD_G        | time                  | 1 ns  |             |
| NUM_VC_G     | integer range 1 to 16 | 4     |             |
## Ports

| Port name      | Direction | Type                                    | Description                           |
| -------------- | --------- | --------------------------------------- | ------------------------------------- |
| pgpRxClk       | in        | sl                                      | User Transmit interface               |
| pgpRxRst       | in        | sl                                      |                                       |
| pgpRxIn        | in        | Pgp3RxInType                            |                                       |
| pgpRxOut       | out       | Pgp3RxOutType                           |                                       |
| pgpRxMaster    | out       | AxiStreamMasterType                     |                                       |
| pgpRxSlave     | in        | AxiStreamSlaveType                      |                                       |
| remRxFifoCtrl  | out       | AxiStreamCtrlArray(NUM_VC_G-1 downto 0) | Status of local receive fifos         |
| remRxLinkReady | out       | sl                                      |                                       |
| locRxLinkReady | out       | sl                                      |                                       |
| phyRxActive    | in        | sl                                      | Received data from descramber/CC FIFO |
| protRxValid    | in        | sl                                      |                                       |
| protRxPhyInit  | out       | sl                                      |                                       |
| protRxData     | in        | slv(63 downto 0)                        |                                       |
| protRxHeader   | in        | slv(1 downto 0)                         |                                       |
## Signals

| Name                | Type    | Description |
| ------------------- | ------- | ----------- |
| r                   | RegType |             |
| rin                 | RegType |             |
| phyRxActiveSyncFall | sl      |             |
| phyRxActiveSync     | sl      |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       notValidCnt    => (others => '0'),<br><span style="padding-left:20px">       count          => (others => '0'),<br><span style="padding-left:20px">       pgpRxMaster    => axiStreamMasterInit(PGP3_AXIS_CONFIG_C),<br><span style="padding-left:20px">       pgpRxOut       => PGP3_RX_OUT_INIT_C,<br><span style="padding-left:20px">       protRxPhyInit  => '1',<br><span style="padding-left:20px">       remRxFifoCtrl  => (others => AXI_STREAM_CTRL_INIT_C),<br><span style="padding-left:20px">  -- init paused       remRxLinkReady => '0',<br><span style="padding-left:20px">       locRxLinkReady => '0',<br><span style="padding-left:20px">       version        => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( pgpRxIn, pgpRxRst, phyRxActiveSync, phyRxActiveSyncFall, protRxData,
                   protRxHeader, protRxValid, r )
**Description**
 [out] 
- seq: ( pgpRxClk )
## Instantiations

- U_SynchronizerEdge_1: surf.SynchronizerEdge
