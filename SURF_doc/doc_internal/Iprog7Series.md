# Entity: Iprog7Series

- **File**: Iprog7Series.vhd
## Diagram

![Diagram](Iprog7Series.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:   Uses the ICAP primitive to internally
               toggle the PROG_B via IPROG command
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type    | Value | Description |
| -------------- | ------- | ----- | ----------- |
| TPD_G          | time    | 1 ns  |             |
| USE_SLOWCLK_G  | boolean | false |             |
| BUFR_CLK_DIV_G | string  | "8"   |             |
## Ports

| Port name   | Direction | Type             | Description                              |
| ----------- | --------- | ---------------- | ---------------------------------------- |
| clk         | in        | sl               |                                          |
| rst         | in        | sl               |                                          |
| slowClk     | in        | sl               |                                          |
| start       | in        | sl               | Should be asserted and held until reboot |
| bootAddress | in        | slv(31 downto 0) |                                          |
## Signals

| Name       | Type             | Description |
| ---------- | ---------------- | ----------- |
| icapClk    | sl               |             |
| icapClkRst | sl               |             |
| icapCsl    | sl               |             |
| icapRnw    | sl               |             |
| icapI      | slv(31 downto 0) |             |
## Instantiations

- RstSync_Inst: surf.RstSync
**Description**
Synchronize reset to icapClk

- Iprog7SeriesCore_1: surf.Iprog7SeriesCore
**Description**
IPROG logic

- ICAPE2_Inst: ICAPE2
**Description**
ICAP Primative

