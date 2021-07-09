# Entity: Pgp2bTx

## Diagram

![Diagram](Pgp2bTx.svg "Diagram")
## Description

Title      : PGPv2b: https://confluence.slac.stanford.edu/x/q86fD
Company    : SLAC National Accelerator Laboratory
Description:
Top Level Transmit interface module for the Pretty Good Protocol core.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name      | Type                 | Value | Description                  |
| ----------------- | -------------------- | ----- | ---------------------------- |
| TPD_G             | time                 | 1 ns  |                              |
| TX_LANE_CNT_G     | integer range 1 to 2 | 1     | Number of receive lanes, 1-2 |
| VC_INTERLEAVE_G   | integer              | 1     | Interleave Frames            |
| PAYLOAD_CNT_TOP_G | integer              | 7     | Top bit for payload counter  |
| NUM_VC_EN_G       | integer range 1 to 4 | 4     |                              |
## Ports

| Port name     | Direction | Type                                         | Description             |
| ------------- | --------- | -------------------------------------------- | ----------------------- |
| pgpTxClkEn    | in        | sl                                           | Master clock enable     |
| pgpTxClk      | in        | sl                                           | Master clock            |
| pgpTxClkRst   | in        | sl                                           | Synchronous reset input |
| pgpTxIn       | in        | Pgp2bTxInType                                | Non-VC related IO       |
| pgpTxOut      | out       | Pgp2bTxOutType                               |                         |
| locLinkReady  | in        | sl                                           |                         |
| pgpTxMasters  | in        | AxiStreamMasterArray(3 downto 0)             | VC Interface            |
| pgpTxSlaves   | out       | AxiStreamSlaveArray(3 downto 0)              |                         |
| locFifoStatus | in        | AxiStreamCtrlArray(3 downto 0)               |                         |
| remFifoStatus | in        | AxiStreamCtrlArray(3 downto 0)               |                         |
| phyTxLanesOut | out       | Pgp2bTxPhyLaneOutArray(0 to TX_LANE_CNT_G-1) | Phy interface           |
| phyTxReady    | in        | sl                                           |                         |
## Signals

| Name             | Type                             | Description                    |
| ---------------- | -------------------------------- | ------------------------------ |
| cellTxSOC        | sl                               |                                |
| cellTxSOF        | sl                               |                                |
| cellTxEOC        | sl                               |                                |
| cellTxEOF        | sl                               |                                |
| cellTxEOFE       | sl                               |                                |
| cellTxData       | slv(TX_LANE_CNT_G*16-1 downto 0) |                                |
| schTxSOF         | sl                               |                                |
| schTxEOF         | sl                               |                                |
| schTxIdle        | sl                               |                                |
| schTxReq         | sl                               |                                |
| schTxAck         | sl                               |                                |
| schTxDataVc      | slv(1 downto 0)                  |                                |
| intTxLinkReady   | sl                               |                                |
| schTxTimeout     | sl                               |                                |
| intPhyTxData     | slv(TX_LANE_CNT_G*16-1 downto 0) |                                |
| intPhyTxDataK    | slv(TX_LANE_CNT_G*2-1  downto 0) |                                |
| crcTxIn          | slv(TX_LANE_CNT_G*16-1 downto 0) | Transmit data for CRC          |
| crcTxInit        | sl                               | Transmit CRC value init        |
| crcTxValid       | sl                               | Transmit data for CRC is valid |
| crcTxOut         | slv(31 downto 0)                 | Transmit calculated CRC value  |
| crcTxOutAdjust   | slv(31 downto 0)                 | Transmit calculated CRC value  |
| crcTxRst         | sl                               |                                |
| crcTxInAdjust    | slv(31 downto 0)                 |                                |
| crcTxWidthAdjust | slv(2 downto 0)                  |                                |
| intTxSof         | slv(3 downto 0)                  |                                |
| intTxEofe        | slv(3 downto 0)                  |                                |
| intvalid         | slv(3 downto 0)                  |                                |
| rawReady         | slv(3 downto 0)                  |                                |
| syncLocPause     | slv(3 downto 0)                  |                                |
| syncLocOverFlow  | slv(3 downto 0)                  |                                |
| syncRemPause     | slv(3 downto 0)                  |                                |
| gateRemPause     | slv(3 downto 0)                  |                                |
| syncLocLinkReady | sl                               |                                |
| intTxMasters     | AxiStreamMasterArray(3 downto 0) |                                |
| intTxSlaves      | AxiStreamSlaveArray(3 downto 0)  |                                |
## Processes
- unnamed: ( pgpTxClk )
## Instantiations

- U_LinkReady: surf.Synchronizer
- U_Pgp2bTxPhy: surf.Pgp2bTxPhy
**Description**
Physical Interface

- U_Pgp2bTxSched: surf.Pgp2bTxSched
**Description**
Scheduler

- U_Pgp2bTxCell: surf.Pgp2bTxCell
**Description**
Cell Transmitter

- Tx_CRC: surf.CRC32Rtl
