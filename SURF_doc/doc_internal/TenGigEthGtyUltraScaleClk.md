# Entity: TenGigEthGtyUltraScaleClk

## Diagram

![Diagram](TenGigEthGtyUltraScaleClk.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: 10GBASE-R Ethernet's Clock Module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name      | Type            | Value     | Description                   |
| ----------------- | --------------- | --------- | ----------------------------- |
| TPD_G             | time            | 1 ns      |                               |
| REF_CLK_FREQ_G    | real            | 156.25E+6 | Support 156.25MHz or 312.5MHz |
| QPLL_REFCLK_SEL_G | slv(2 downto 0) | "001"     |                               |
## Ports

| Port name     | Direction | Type            | Description                 |
| ------------- | --------- | --------------- | --------------------------- |
| gtRefClk      | in        | sl              | MGT Clock Port (156.25 MHz) |
| gtClkP        | in        | sl              |                             |
| gtClkN        | in        | sl              |                             |
| coreClk       | out       | sl              |                             |
| coreRst       | in        | sl              |                             |
| gtClk         | out       | sl              |                             |
| qplllock      | out       | slv(1 downto 0) | Quad PLL Ports              |
| qplloutclk    | out       | slv(1 downto 0) |                             |
| qplloutrefclk | out       | slv(1 downto 0) |                             |
| qpllRst       | in        | slv(1 downto 0) |                             |
## Signals

| Name       | Type            | Description |
| ---------- | --------------- | ----------- |
| refClk     | sl              |             |
| refClkCopy | sl              |             |
| refClock   | sl              |             |
| coreClock  | sl              |             |
| qpllReset  | slv(1 downto 0) |             |
## Instantiations

- IBUFDS_GTE3_Inst: IBUFDS_GTE4
- BUFG_GT_Inst: BUFG_GT
- GtyUltraScaleQuadPll_Inst: surf.GtyUltraScaleQuadPll
