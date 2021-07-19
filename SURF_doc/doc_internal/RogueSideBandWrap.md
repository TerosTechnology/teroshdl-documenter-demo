# Entity: RogueSideBandWrap

- **File**: RogueSideBandWrap.vhd
## Diagram

![Diagram](RogueSideBandWrap.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Wrapper for Rogue Sideband Simulation Module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type                        | Value | Description |
| ------------ | --------------------------- | ----- | ----------- |
| TPD_G        | time                        | 1 ns  |             |
| PORT_NUM_G   | natural range 1024 to 49151 | 9000  |             |
## Ports

| Port name  | Direction | Type            | Description |
| ---------- | --------- | --------------- | ----------- |
| sysClk     | in        | sl              |             |
| sysRst     | in        | sl              |             |
| txOpCode   | in        | slv(7 downto 0) |             |
| txOpCodeEn | in        | sl              |             |
| txRemData  | in        | slv(7 downto 0) |             |
| rxOpCode   | out       | slv(7 downto 0) |             |
| rxOpCodeEn | out       | sl              |             |
| rxRemData  | out       | slv(7 downto 0) |             |
## Instantiations

- U_RogueSideBand: surf.RogueSideBand
