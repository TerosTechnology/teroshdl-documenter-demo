# Entity: Jesd32bTo16b

## Diagram

![Diagram](Jesd32bTo16b.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Converts the 32-bit JESD interface to 16-bit interface
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type                 | Value      | Description |
| ------------- | -------------------- | ---------- | ----------- |
| TPD_G         | time                 | 1 ns       |             |
| SYNTH_MODE_G  | string               | "inferred" |             |
| SYNC_STAGES_G | natural range 2 to 8 | 3          |             |
## Ports

| Port name | Direction | Type             | Description            |
| --------- | --------- | ---------------- | ---------------------- |
| wrClk     | in        | sl               | 32-bit Write Interface |
| wrRst     | in        | sl               |                        |
| validIn   | in        | sl               |                        |
| trigIn    | in        | slv(1 downto 0)  |                        |
| overflow  | out       | sl               |                        |
| dataIn    | in        | slv(31 downto 0) |                        |
| rdClk     | in        | sl               | 16-bit Read Interface  |
| rdRst     | in        | sl               |                        |
| validOut  | out       | sl               |                        |
| trigOut   | out       | sl               |                        |
| underflow | out       | sl               |                        |
| dataOut   | out       | slv(15 downto 0) |                        |
## Signals

| Name  | Type             | Description |
| ----- | ---------------- | ----------- |
| r     | RegType          |             |
| rin   | RegType          |             |
| rdEn  | sl               |             |
| valid | sl               |             |
| trig  | slv(1 downto 0)  |             |
| data  | slv(31 downto 0) |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                        | Description |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       rdEn    => '0',<br><span style="padding-left:20px">       wordSel => '0',<br><span style="padding-left:20px">       valid   => '0',<br><span style="padding-left:20px">       trig    => '0',<br><span style="padding-left:20px">       data    => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( data, r, rdRst, trig, valid )
- seq: ( rdClk )
## Instantiations

- U_FIFO: surf.Fifo
