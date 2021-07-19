# Entity: Gtpe2ChannelDummy

- **File**: Gtpe2ChannelDummy.vhd
## Diagram

![Diagram](Gtpe2ChannelDummy.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
This file is part of 'SLAC MGT Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC MGT Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type                  | Value | Description |
| ------------ | --------------------- | ----- | ----------- |
| TPD_G        | time                  | 1 ns  |             |
| SIMULATION_G | boolean               | false |             |
| EXT_QPLL_G   | boolean               | false |             |
| WIDTH_G      | positive range 1 to 4 | 1     |             |
## Ports

| Port name        | Direction | Type                    | Description              |
| ---------------- | --------- | ----------------------- | ------------------------ |
| refClk           | in        | sl                      | Required by DRC REQP #48 |
| qPllOutClkExt    | in        | slv(1 downto 0)         |                          |
| qPllOutRefClkExt | in        | slv(1 downto 0)         |                          |
| gtRxP            | in        | slv(WIDTH_G-1 downto 0) |                          |
| gtRxN            | in        | slv(WIDTH_G-1 downto 0) |                          |
| gtTxP            | out       | slv(WIDTH_G-1 downto 0) |                          |
| gtTxN            | out       | slv(WIDTH_G-1 downto 0) |                          |
## Signals

| Name          | Type            | Description |
| ------------- | --------------- | ----------- |
| qPllOutClk    | slv(1 downto 0) |             |
| qPllOutRefClk | slv(1 downto 0) |             |
