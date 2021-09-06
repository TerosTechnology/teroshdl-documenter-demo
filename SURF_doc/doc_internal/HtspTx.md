# Entity: HtspTx

- **File**: HtspTx.vhd
## Diagram

![Diagram](HtspTx.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : HTSP: https://confluence.slac.stanford.edu/x/pQmODw
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: HTSP Ethernet Transmitter
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

| Generic name       | Type                   | Value | Description |
| ------------------ | ---------------------- | ----- | ----------- |
| TPD_G              | time                   | 1 ns  |             |
| NUM_VC_G           | positive range 1 to 16 | 1     |             |
| MAX_PAYLOAD_SIZE_G | positive               | 8192  |             |
## Ports

| Port name      | Direction | Type                                      | Description                        |
| -------------- | --------- | ----------------------------------------- | ---------------------------------- |
| remoteMac      | in        | slv(47 downto 0)                          | Ethernet Configuration             |
| localMac       | in        | slv(47 downto 0)                          |                                    |
| broadcastMac   | in        | slv(47 downto 0)                          |                                    |
| etherType      | in        | slv(15 downto 0)                          |                                    |
| htspClk        | in        | sl                                        | User interface                     |
| htspRst        | in        | sl                                        |                                    |
| htspTxIn       | in        | HtspTxInType                              |                                    |
| htspTxOut      | out       | HtspTxOutType                             |                                    |
| htspTxMasters  | in        | AxiStreamMasterArray(NUM_VC_G-1 downto 0) |                                    |
| htspTxSlaves   | out       | AxiStreamSlaveArray(NUM_VC_G-1 downto 0)  |                                    |
| locRxFifoCtrl  | in        | AxiStreamCtrlArray(NUM_VC_G-1 downto 0)   | Status of receive and remote FIFOs |
| locRxLinkReady | in        | sl                                        |                                    |
| remRxFifoCtrl  | in        | AxiStreamCtrlArray(NUM_VC_G-1 downto 0)   |                                    |
| remRxLinkReady | in        | sl                                        |                                    |
| phyTxRdy       | in        | sl                                        | PHY interface                      |
| phyTxMaster    | out       | AxiStreamMasterType                       |                                    |
| phyTxSlave     | in        | AxiStreamSlaveType                        |                                    |
## Signals

| Name         | Type                                      | Description |
| ------------ | ----------------------------------------- | ----------- |
| r            | RegType                                   |             |
| rin          | RegType                                   |             |
| ibTxMasters  | AxiStreamMasterArray(NUM_VC_G-1 downto 0) |             |
| ibTxSlaves   | AxiStreamSlaveArray(NUM_VC_G-1 downto 0)  |             |
| htspTxMaster | AxiStreamMasterType                       |             |
| htspTxSlave  | AxiStreamSlaveType                        |             |
| txSlave      | AxiStreamSlaveType                        |             |
## Constants

| Name       | Type     | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description             |
| ---------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| MAX_SIZE_C | positive |  (MAX_PAYLOAD_SIZE_G/64)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |  units of 512-bit words |
| REG_INIT_C | RegType  |  (       disableSel   => (others => '0'),<br><span style="padding-left:20px">       sof          => (others => '1'),<br><span style="padding-left:20px">       eof          => '0',<br><span style="padding-left:20px">       eofe         => '0',<br><span style="padding-left:20px">       lastKeep     => (others => '1'),<br><span style="padding-left:20px">       wrdCnt       => 0,<br><span style="padding-left:20px">       tid          => (others => '0'),<br><span style="padding-left:20px">       nullCnt      => (others => '0'),<br><span style="padding-left:20px">       nullInterval => (others => '0'),<br><span style="padding-left:20px">       pause        => (others => '0'),<br><span style="padding-left:20px">       lastPausSent => (others => '0'),<br><span style="padding-left:20px">       tDest        => (others => '0'),<br><span style="padding-left:20px">       htspTxOut    => HTSP_TX_OUT_INIT_C,<br><span style="padding-left:20px">       htspTxSlave  => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       txMaster     => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       state        => IDLE_S) |                         |
## Types

| Name      | Type                                                                                                                                               | Description |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> HDR_S,<br><span style="padding-left:20px"> PAYLOAD_S,<br><span style="padding-left:20px"> FOOTER_S)  |             |
| RegType   |                                                                                                                                                    |             |
## Processes
- comb: ( broadcastMac, etherType, htspRst, htspTxIn, htspTxMaster,
                   locRxFifoCtrl, locRxLinkReady, localMac, phyTxRdy, r,
                   remRxFifoCtrl, remRxLinkReady, remoteMac, txSlave )
- seq: ( htspClk )
## Instantiations

- U_Mux: surf.AxiStreamMux
</br>**Description**
----------------------------------------------------
 Multiplex the incoming TX streams with interleaving
----------------------------------------------------

- U_Pipeline: surf.AxiStreamPipeline
