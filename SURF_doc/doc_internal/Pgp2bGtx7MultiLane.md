# Entity: Pgp2bGtx7MultiLane

- **File**: Pgp2bGtx7MultiLane.vhd
## Diagram

![Diagram](Pgp2bGtx7MultiLane.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : PGPv2b: https://confluence.slac.stanford.edu/x/q86fD
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Gtx7 Variable Latency, multi-lane Module
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

| Generic name          | Type                 | Value                 | Description                                                                                                                                                                                                       |
| --------------------- | -------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TPD_G                 | time                 | 1 ns                  |                                                                                                                                                                                                                   |
| SIM_GTRESET_SPEEDUP_G | string               | "FALSE"               | ------------------------------------------------------------------------------------------- GT Settings ------------------------------------------------------------------------------------------- Sim Generics  |
| SIM_VERSION_G         | string               | "4.0"                 |                                                                                                                                                                                                                   |
| STABLE_CLOCK_PERIOD_G | real                 | 6.4E-9                | units of seconds                                                                                                                                                                                                  |
| CPLL_REFCLK_SEL_G     | bit_vector           | "001"                 | CPLL Settings                                                                                                                                                                                                     |
| CPLL_FBDIV_G          | integer              | 4                     |                                                                                                                                                                                                                   |
| CPLL_FBDIV_45_G       | integer              | 5                     |                                                                                                                                                                                                                   |
| CPLL_REFCLK_DIV_G     | integer              | 1                     |                                                                                                                                                                                                                   |
| RXOUT_DIV_G           | integer              | 2                     |                                                                                                                                                                                                                   |
| TXOUT_DIV_G           | integer              | 2                     |                                                                                                                                                                                                                   |
| RX_CLK25_DIV_G        | integer              | 7                     |                                                                                                                                                                                                                   |
| TX_CLK25_DIV_G        | integer              | 7                     |                                                                                                                                                                                                                   |
| PMA_RSV_G             | bit_vector           | x"00018480"           |                                                                                                                                                                                                                   |
| RX_OS_CFG_G           | bit_vector           | "0000010000000"       |  Set by wizard                                                                                                                                                                                                    |
| RXCDR_CFG_G           | bit_vector           | x"03000023ff40200020" |  Set by wizard                                                                                                                                                                                                    |
| RXDFEXYDEN_G          | sl                   | '0'                   |  Set by wizard                                                                                                                                                                                                    |
| RX_EQUALIZER_G        | string               | "DFE"                 |  Or "LPM"                                                                                                                                                                                                         |
| RX_DFE_KL_CFG2_G      | bit_vector           | x"3010D90C"           |  Set by wizard                                                                                                                                                                                                    |
| TX_PLL_G              | string               | "QPLL"                | Configure PLL sources                                                                                                                                                                                             |
| RX_PLL_G              | string               | "CPLL"                |                                                                                                                                                                                                                   |
| TX_BUF_EN_G           | boolean              | true                  | Configure Buffer usage                                                                                                                                                                                            |
| TX_OUTCLK_SRC_G       | string               | "OUTCLKPMA"           |                                                                                                                                                                                                                   |
| TX_DLY_BYPASS_G       | sl                   | '1'                   |                                                                                                                                                                                                                   |
| TX_PHASE_ALIGN_G      | string               | "NONE"                |                                                                                                                                                                                                                   |
| TX_BUF_ADDR_MODE_G    | string               | "FULL"                |                                                                                                                                                                                                                   |
| LANE_CNT_G            | integer range 1 to 2 | 2                     | Configure Number of Lanes                                                                                                                                                                                         |
| VC_INTERLEAVE_G       | integer              | 0                     |  No interleave Frames                                                                                                                                                                                             |
| PAYLOAD_CNT_TOP_G     | integer              | 7                     |  Top bit for payload counter                                                                                                                                                                                      |
| NUM_VC_EN_G           | integer range 1 to 4 | 4                     |                                                                                                                                                                                                                   |
| TX_POLARITY_G         | sl                   | '0'                   |                                                                                                                                                                                                                   |
| RX_POLARITY_G         | sl                   | '0'                   |                                                                                                                                                                                                                   |
| TX_ENABLE_G           | boolean              | true                  |  Enable TX direction                                                                                                                                                                                              |
| RX_ENABLE_G           | boolean              | true                  |                                                                                                                                                                                                                   |
## Ports

| Port name        | Direction | Type                                             | Description                                       |
| ---------------- | --------- | ------------------------------------------------ | ------------------------------------------------- |
| stableClk        | in        | sl                                               |  GT needs a stable clock to "boot up"             |
| gtCPllRefClk     | in        | sl                                               |  Drives CPLL if used                              |
| gtCPllLock       | out       | sl                                               |                                                   |
| gtQPllRefClk     | in        | sl                                               |  Signals from QPLL if used                        |
| gtQPllClk        | in        | sl                                               |                                                   |
| gtQPllLock       | in        | sl                                               |                                                   |
| gtQPllRefClkLost | in        | sl                                               |                                                   |
| gtQPllReset      | out       | sl                                               |                                                   |
| gtTxP            | out       | slv((LANE_CNT_G-1) downto 0)                     |  GT Serial Transmit Positive                      |
| gtTxN            | out       | slv((LANE_CNT_G-1) downto 0)                     |  GT Serial Transmit Negative                      |
| gtRxP            | in        | slv((LANE_CNT_G-1) downto 0)                     |  GT Serial Receive Positive                       |
| gtRxN            | in        | slv((LANE_CNT_G-1) downto 0)                     |  GT Serial Receive Negative                       |
| pgpTxReset       | in        | sl                                               | Tx Clocking                                       |
| pgpTxRecClk      | out       | sl                                               |  recovered clock                                  |
| pgpTxClk         | in        | sl                                               |                                                   |
| pgpTxMmcmReset   | out       | sl                                               |                                                   |
| pgpTxMmcmLocked  | in        | sl                                               |                                                   |
| pgpRxReset       | in        | sl                                               | Rx clocking                                       |
| pgpRxRecClk      | out       | sl                                               |  recovered clock                                  |
| pgpRxClk         | in        | sl                                               |                                                   |
| pgpRxMmcmReset   | out       | sl                                               |                                                   |
| pgpRxMmcmLocked  | in        | sl                                               |                                                   |
| pgpRxIn          | in        | Pgp2bRxInType                                    | Non VC Rx Signals                                 |
| pgpRxOut         | out       | Pgp2bRxOutType                                   |                                                   |
| pgpTxIn          | in        | Pgp2bTxInType                                    | Non VC Tx Signals                                 |
| pgpTxOut         | out       | Pgp2bTxOutType                                   |                                                   |
| pgpTxMasters     | in        | AxiStreamMasterArray(3 downto 0)                 | Frame Transmit Interface - 1 Lane, Array of 4 VCs |
| pgpTxSlaves      | out       | AxiStreamSlaveArray(3 downto 0)                  |                                                   |
| pgpRxMasters     | out       | AxiStreamMasterArray(3 downto 0)                 | Frame Receive Interface - 1 Lane, Array of 4 VCs  |
| pgpRxMasterMuxed | out       | AxiStreamMasterType                              |                                                   |
| pgpRxCtrl        | in        | AxiStreamCtrlArray(3 downto 0)                   |                                                   |
| txPreCursor      | in        | slv(4 downto 0)                                  | Debug Interface                                   |
| txPostCursor     | in        | slv(4 downto 0)                                  |                                                   |
| txDiffCtrl       | in        | slv(3 downto 0)                                  |                                                   |
| axilClk          | in        | sl                                               | AXI-Lite Interface                                |
| axilRst          | in        | sl                                               |                                                   |
| axilReadMasters  | in        | AxiLiteReadMasterArray((LANE_CNT_G-1) downto 0)  |                                                   |
| axilReadSlaves   | out       | AxiLiteReadSlaveArray((LANE_CNT_G-1) downto 0)   |                                                   |
| axilWriteMasters | in        | AxiLiteWriteMasterArray((LANE_CNT_G-1) downto 0) |                                                   |
| axilWriteSlaves  | out       | AxiLiteWriteSlaveArray((LANE_CNT_G-1) downto 0)  |                                                   |
## Signals

| Name            | Type                                            | Description          |
| --------------- | ----------------------------------------------- | -------------------- |
| gtQPllResets    | slv((LANE_CNT_G-1) downto 0)                    |                      |
| cPllLock        | slv((LANE_CNT_G-1) downto 0)                    |                      |
| pgpRxMmcmResets | slv((LANE_CNT_G-1) downto 0)                    |  PgpRx Signals       |
| pgpRxRecClock   | slv((LANE_CNT_G-1) downto 0)                    |                      |
| gtRxResetDone   | slv((LANE_CNT_G-1) downto 0)                    |                      |
| gtRxUserReset   | sl                                              |                      |
| gtRxUserResetIn | sl                                              |                      |
| phyRxLanesIn    | Pgp2bRxPhyLaneInArray((LANE_CNT_G-1) downto 0)  |                      |
| phyRxLanesOut   | Pgp2bRxPhyLaneOutArray((LANE_CNT_G-1) downto 0) |                      |
| phyRxReady      | sl                                              |                      |
| phyRxInit       | sl                                              |                      |
| rxChBondLevel   | slv(2 downto 0)                                 |  Rx Channel Bonding  |
| rxChBondIn      | Slv5Array(LANE_CNT_G-1 downto 0)                |                      |
| rxChBondOut     | Slv5Array(LANE_CNT_G-1 downto 0)                |                      |
| pgpTxMmcmResets | slv((LANE_CNT_G-1) downto 0)                    |  PgpTx Signals       |
| pgpTxRecClock   | slv((LANE_CNT_G-1) downto 0)                    |                      |
| gtTxResetDone   | slv((LANE_CNT_G-1) downto 0)                    |                      |
| gtTxUserResetIn | sl                                              |                      |
| phyTxLanesOut   | Pgp2bTxPhyLaneOutArray((LANE_CNT_G-1) downto 0) |                      |
| phyTxReady      | sl                                              |                      |
| drpRdy          | slv(LANE_CNT_G-1 downto 0)                      |                      |
| drpEn           | slv(LANE_CNT_G-1 downto 0)                      |                      |
| drpWe           | slv(LANE_CNT_G-1 downto 0)                      |                      |
| drpAddr         | Slv9Array(LANE_CNT_G-1 downto 0)                |                      |
| drpDi           | Slv16Array(LANE_CNT_G-1 downto 0)               |                      |
| drpDo           | Slv16Array(LANE_CNT_G-1 downto 0)               |                      |
## Instantiations

- U_Pgp2bLane: surf.Pgp2bLane
