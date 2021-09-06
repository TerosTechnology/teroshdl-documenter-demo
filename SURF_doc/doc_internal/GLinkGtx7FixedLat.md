# Entity: GLinkGtx7FixedLat

- **File**: GLinkGtx7FixedLat.vhd
## Diagram

![Diagram](GLinkGtx7FixedLat.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: G-Link wrapper for GTX7 Fixed Latency transceiver
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

| Generic name          | Type       | Value                 | Description              |
| --------------------- | ---------- | --------------------- | ------------------------ |
| FLAGSEL_G             | boolean    | false                 | GLink Settings           |
| SYNTH_TX_G            | boolean    | true                  |                          |
| SYNTH_RX_G            | boolean    | true                  |                          |
| TPD_G                 | time       | 1 ns                  | Simulation Generics      |
| SIM_GTRESET_SPEEDUP_G | string     | "FALSE"               |                          |
| SIM_VERSION_G         | string     | "4.0"                 |                          |
| SIMULATION_G          | boolean    | false                 |                          |
| CPLL_REFCLK_SEL_G     | bit_vector | "001"                 | CPLL Settings            |
| CPLL_FBDIV_G          | integer    | 4                     |                          |
| CPLL_FBDIV_45_G       | integer    | 5                     |                          |
| CPLL_REFCLK_DIV_G     | integer    | 1                     |                          |
| RXOUT_DIV_G           | integer    | 2                     | MGT Settings             |
| TXOUT_DIV_G           | integer    | 2                     |                          |
| RX_CLK25_DIV_G        | integer    | 5                     |  Set by wizard           |
| TX_CLK25_DIV_G        | integer    | 5                     |  Set by wizard           |
| RX_OS_CFG_G           | bit_vector | "0000010000000"       |  Set by wizard           |
| RXCDR_CFG_G           | bit_vector | x"03000023ff40200020" |  Set by wizard           |
| RX_DFE_KL_CFG2_G      | bit_vector | x"3008E56A"           |  Set by wizard           |
| RX_CM_TRIM_G          | bit_vector | "010"                 |                          |
| RX_DFE_LPM_CFG_G      | bit_vector | x"0954"               |                          |
| RXDFELFOVRDEN_G       | sl         | '1'                   |                          |
| RXDFEXYDEN_G          | sl         | '1'                   |  This should always be 1 |
| TX_PLL_G              | string     | "QPLL"                | Configure PLL sources    |
| RX_PLL_G              | string     | "CPLL"                |                          |
## Ports

| Port name        | Direction | Type            | Description                             |
| ---------------- | --------- | --------------- | --------------------------------------- |
| gLinkTx          | in        | GLinkTxType     | G-Link TX Interface (gLinkTxClk Domain) |
| txReady          | out       | sl              |                                         |
| gLinkTxClk       | in        | sl              |                                         |
| gLinkTxClkEn     | in        | sl              |                                         |
| gLinkTxRst       | in        | sl              |                                         |
| gLinkRx          | out       | GLinkRxType     | G-Link TX Interface (gLinkClk Domain)   |
| rxReady          | out       | sl              |                                         |
| gLinkRxClk       | in        | sl              |                                         |
| gLinkRxClkEn     | in        | sl              |                                         |
| gLinkRxRst       | in        | sl              |                                         |
| gLinkTxRefClk    | in        | sl              |  G-Link TX clock reference              |
| stableClk        | in        | sl              |                                         |
| gtCPllRefClk     | in        | sl              |                                         |
| gtCPllLock       | out       | sl              |                                         |
| gtQPllRefClk     | in        | sl              |                                         |
| gtQPllClk        | in        | sl              |                                         |
| gtQPllLock       | in        | sl              |                                         |
| gtQPllRefClkLost | in        | sl              |                                         |
| gtQPllReset      | out       | sl              |                                         |
| lpmMode          | in        | sl              | Misc. MGT control                       |
| loopback         | in        | slv(2 downto 0) |                                         |
| txPowerDown      | in        | sl              |                                         |
| rxPowerDown      | in        | sl              |                                         |
| rxClkDebug       | out       | sl              |  debug only                             |
| gtTxP            | out       | sl              | MGT Serial IO                           |
| gtTxN            | out       | sl              |                                         |
| gtRxP            | in        | sl              |                                         |
| gtRxN            | in        | sl              |                                         |
## Signals

| Name                    | Type             | Description |
| ----------------------- | ---------------- | ----------- |
| txFifoValid             | sl               |             |
| 
      rxFifoValid      | sl               |             |
| 
      rxRecClk         | sl               |             |
| 
      rxClk            | sl               |             |
| 
      rxRst            | sl               |             |
| 
      txClk            | sl               |             |
| 
      txUserReset      | sl               |             |
| 
      rxUserReset      | sl               |             |
| 
      gtTxRstDone      | sl               |             |
| 
      gtRxRstDone      | sl               |             |
| 
      gtTxRst          | sl               |             |
| 
      gtRxRst          | sl               |             |
| 
      dataValid        | sl               |             |
| txFifoDout              | slv(19 downto 0) |             |
| 
      gtTxData         | slv(19 downto 0) |             |
| 
      gtRxData         | slv(19 downto 0) |             |
| 
      gtTxDataReversed | slv(19 downto 0) |             |
| 
      gtRxDataReversed | slv(19 downto 0) |             |
| rxFifoDout              | slv(23 downto 0) |             |
| gLinkTxSync             | GLinkTxType      |             |
| gLinkRxSync             | GLinkRxType      |             |
## Constants

| Name                  | Type             | Value                                                             | Description |
| --------------------- | ---------------- | ----------------------------------------------------------------- | ----------- |
| FIXED_ALIGN_COMMA_0_C | slv(19 downto 0) |  bitReverse((GLINK_VALID_IDLE_WORDS_C(0) & GLINK_CONTROL_WORD_C)) |  FF0        |
| FIXED_ALIGN_COMMA_1_C | slv(19 downto 0) |  bitReverse((GLINK_VALID_IDLE_WORDS_C(1) & GLINK_CONTROL_WORD_C)) |  FF1A       |
| FIXED_ALIGN_COMMA_2_C | slv(19 downto 0) |  bitReverse((GLINK_VALID_IDLE_WORDS_C(2) & GLINK_CONTROL_WORD_C)) |  FF1B       |
## Instantiations

- Gtx7Core_Inst: surf.GLinkGtx7Core
**Description**
 GTX 7 Core in Fixed Latency mode

