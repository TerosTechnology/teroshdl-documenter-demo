# Entity: Pgp2bLane

- **File**: Pgp2bLane.vhd
## Diagram

![Diagram](Pgp2bLane.svg "Diagram")
## Description

Title      : PGPv2b: https://confluence.slac.stanford.edu/x/q86fD
Company    : SLAC National Accelerator Laboratory
Description:
Top Level Transmit/Receive interface module for the Pretty Good Protocol core.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name      | Type                 | Value | Description                 |
| ----------------- | -------------------- | ----- | --------------------------- |
| TPD_G             | time                 | 1 ns  |                             |
| LANE_CNT_G        | integer range 1 to 2 | 1     | Number of lanes, 1-2        |
| VC_INTERLEAVE_G   | integer              | 1     | Interleave Frames           |
| PAYLOAD_CNT_TOP_G | integer              | 7     | Top bit for payload counter |
| NUM_VC_EN_G       | integer range 1 to 4 | 4     |                             |
| TX_ENABLE_G       | boolean              | true  | Enable TX direction         |
| RX_ENABLE_G       | boolean              | true  | Enable RX direction         |
## Ports

| Port name        | Direction | Type                                      | Description                                         |
| ---------------- | --------- | ----------------------------------------- | --------------------------------------------------- |
| pgpTxClkEn       | in        | sl                                        | Transmitter InterfaceSystem clock, reset & control  |
| pgpTxClk         | in        | sl                                        |                                                     |
| pgpTxClkRst      | in        | sl                                        |                                                     |
| pgpTxIn          | in        | Pgp2bTxInType                             | Non-VC related IO                                   |
| pgpTxOut         | out       | Pgp2bTxOutType                            |                                                     |
| pgpTxMasters     | in        | AxiStreamMasterArray(3 downto 0)          | VC Interface                                        |
| pgpTxSlaves      | out       | AxiStreamSlaveArray(3 downto 0)           |                                                     |
| phyTxLanesOut    | out       | Pgp2bTxPhyLaneOutArray(0 to LANE_CNT_G-1) | Phy interface                                       |
| phyTxReady       | in        | sl                                        |                                                     |
| pgpRxClkEn       | in        | sl                                        | Receiver InterfaceSystem clock, reset & control     |
| pgpRxClk         | in        | sl                                        |                                                     |
| pgpRxClkRst      | in        | sl                                        |                                                     |
| pgpRxIn          | in        | Pgp2bRxInType                             | Non-VC related IO                                   |
| pgpRxOut         | out       | Pgp2bRxOutType                            |                                                     |
| pgpRxMasters     | out       | AxiStreamMasterArray(3 downto 0)          | VC Outputs                                          |
| pgpRxMasterMuxed | out       | AxiStreamMasterType                       |                                                     |
| pgpRxCtrl        | in        | AxiStreamCtrlArray(3 downto 0)            | Receive flow control                                |
| phyRxLanesOut    | out       | Pgp2bRxPhyLaneOutArray(0 to LANE_CNT_G-1) | PHY interface                                       |
| phyRxLanesIn     | in        | Pgp2bRxPhyLaneInArray(0 to LANE_CNT_G-1)  |                                                     |
| phyRxReady       | in        | sl                                        |                                                     |
| phyRxInit        | out       | sl                                        |                                                     |
## Signals

| Name          | Type                           | Description |
| ------------- | ------------------------------ | ----------- |
| intRxMaster   | AxiStreamMasterType            |             |
| remFifoStatus | AxiStreamCtrlArray(3 downto 0) |             |
| intRxOut      | Pgp2bRxOutType                 |             |
