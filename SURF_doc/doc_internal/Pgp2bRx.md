# Entity: Pgp2bRx

- **File**: Pgp2bRx.vhd
## Diagram

![Diagram](Pgp2bRx.svg "Diagram")
## Description

Title      : PGPv2b: https://confluence.slac.stanford.edu/x/q86fD
Company    : SLAC National Accelerator Laboratory
Description:
Cell Receive interface module for the Pretty Good Protocol core.
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
| RX_LANE_CNT_G     | integer range 1 to 2 | 1     | Number of receive lanes, 1-2 |
| PAYLOAD_CNT_TOP_G | integer              | 7     | Top bit for payload counter  |
## Ports

| Port name     | Direction | Type                                         | Description             |
| ------------- | --------- | -------------------------------------------- | ----------------------- |
| pgpRxClkEn    | in        | sl                                           | Master clock enable     |
| pgpRxClk      | in        | sl                                           | Master clock            |
| pgpRxClkRst   | in        | sl                                           | Synchronous reset input |
| pgpRxIn       | in        | Pgp2bRxInType                                | Non-VC related IO       |
| pgpRxOut      | out       | Pgp2bRxOutType                               |                         |
| pgpRxMaster   | out       | AxiStreamMasterType                          | VC Output               |
| remFifoStatus | out       | AxiStreamCtrlArray(3 downto 0)               |                         |
| phyRxLanesOut | out       | Pgp2bRxPhyLaneOutArray(0 to RX_LANE_CNT_G-1) | PHY interface           |
| phyRxLanesIn  | in        | Pgp2bRxPhyLaneInArray(0 to RX_LANE_CNT_G-1)  |                         |
| phyRxReady    | in        | sl                                           |                         |
| phyRxInit     | out       | sl                                           |                         |
## Signals

| Name             | Type                               | Description                          |
| ---------------- | ---------------------------------- | ------------------------------------ |
| cellRxPause      | sl                                 |                                      |
| cellRxSOC        | sl                                 |                                      |
| cellRxSOF        | sl                                 |                                      |
| cellRxEOC        | sl                                 |                                      |
| cellRxEOF        | sl                                 |                                      |
| cellRxEOFE       | sl                                 |                                      |
| cellRxData       | slv(RX_LANE_CNT_G*16-1 downto 0)   |                                      |
| intRxLinkReady   | sl                                 |                                      |
| crcRxIn          | slv(RX_LANE_CNT_G*16-1 downto 0)   | Receive data for CRC                 |
| crcRxInit        | sl                                 | Receive CRC value init               |
| crcRxValid       | sl                                 | Receive data for CRC is valid        |
| crcRxOut         | slv(31 downto 0)                   |                                      |
| crcRxOutAdjust   | slv(31 downto 0)                   |                                      |
| crcRxRst         | sl                                 |                                      |
| crcRxInAdjust    | slv(31 downto 0)                   |                                      |
| crcRxWidthAdjust | slv(2 downto 0)                    |                                      |
| intPhyRxPolarity | slv(1 downto 0)                    | PHY receive signal polarity          |
| intPhyRxData     | slv(RX_LANE_CNT_G*16-1 downto 0)   | PHY receive data                     |
| intPhyRxDataK    | slv(RX_LANE_CNT_G*2-1 downto 0)    | PHY receive data is K character      |
| intPhyRxDispErr  | slv(RX_LANE_CNT_G*2-1 downto 0)    | PHY receive data has disparity error |
| intPhyRxDecErr   | slv(RX_LANE_CNT_G*2-1 downto 0)    | PHY receive data not in table        |
| intRxVcValid     | slv(3 downto 0)                    |                                      |
| intRxSof         | sl                                 |                                      |
| intRxEof         | sl                                 |                                      |
| intRxEofe        | sl                                 |                                      |
| intRxData        | slv((RX_LANE_CNT_G*16)-1 downto 0) |                                      |
| pause            | slv(3 downto 0)                    |                                      |
| overflow         | slv(3 downto 0)                    |                                      |
## Processes
- wrap: ( intPhyRxPolarity, phyRxLanesIn )
**Description**
Interface connection

- unnamed: ( overflow, pause )
**Description**
Pass FIFO status

- unnamed: ( pgpRxClk )
**Description**
Generate valid/vc

## Instantiations

- U_Pgp2bRxPhy: surf.Pgp2bRxPhy
**Description**
PHY Logic

- U_Pgp2bRxCell: surf.Pgp2bRxCell
**Description**
Cell Receiver

- Rx_CRC: surf.CRC32Rtl
