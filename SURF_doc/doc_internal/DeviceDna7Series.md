# Entity: DeviceDna7Series

- **File**: DeviceDna7Series.vhd
## Diagram

![Diagram](DeviceDna7Series.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Wrapper for the 7 Series DNA_PORT
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name    | Type       | Value              | Description |
| --------------- | ---------- | ------------------ | ----------- |
| TPD_G           | time       | 1 ns               |             |
| USE_SLOWCLK_G   | boolean    | false              |             |
| BUFR_CLK_DIV_G  | string     | "8"                |             |
| RST_POLARITY_G  | sl         | '1'                |             |
| SIM_DNA_VALUE_G | bit_vector | X"000000000000000" |             |
## Ports

| Port name | Direction | Type             | Description |
| --------- | --------- | ---------------- | ----------- |
| clk       | in        | sl               |             |
| rst       | in        | sl               |             |
| slowClk   | in        | sl               |             |
| dnaValue  | out       | slv(55 downto 0) |             |
| dnaValid  | out       | sl               |             |
## Signals

| Name       | Type    | Description |
| ---------- | ------- | ----------- |
| r          | RegType |             |
| rin        | RegType |             |
| dnaDout    | sl      |             |
| divClk     | sl      |             |
| locClk     | sl      |             |
| locRst     | sl      |             |
| locClkInv  | sl      |             |
| locClkInvR | sl      |             |
## Constants

| Name               | Type    | Value                                                                                                                                                                                                                                                                                                                                         | Description |
| ------------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| DNA_SHIFT_LENGTH_C | natural |  64                                                                                                                                                                                                                                                                                                                                           |             |
| REG_INIT_C         | RegType |  (       state    => READ_S,<br><span style="padding-left:20px">       bitCount => 0,<br><span style="padding-left:20px">       dnaValue => (others => '0'),<br><span style="padding-left:20px">       dnaValid => '0',<br><span style="padding-left:20px">       dnaRead  => '0',<br><span style="padding-left:20px">       dnaShift => '0') |             |
## Types

| Name      | Type                                                                                               | Description |
| --------- | -------------------------------------------------------------------------------------------------- | ----------- |
| StateType | (READ_S,<br><span style="padding-left:20px"> SHIFT_S,<br><span style="padding-left:20px"> DONE_S)  |             |
| RegType   |                                                                                                    |             |
## Processes
- comb: ( dnaDout, locRst, r )
- sync: ( locClkInvR )
## Instantiations

- BUFR_Inst: BUFR
- DNA_CLK_INV_BUFR: BUFR
- RstSync_Inst: surf.RstSync
- DNA_PORT_I: DNA_PORT
- SyncValid: surf.Synchronizer
- SyncData: surf.SynchronizerVector
