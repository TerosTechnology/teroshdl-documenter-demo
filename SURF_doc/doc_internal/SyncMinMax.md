# Entity: SyncMinMax

## Diagram

![Diagram](SyncMinMax.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: General Purpose Max/Min monitor and synchronizer
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| TPD_G        | time     | 1 ns  |             |
| COMMON_CLK_G | boolean  | false |             |
| WIDTH_G      | positive | 16    |             |
## Ports

| Port name | Direction | Type                    | Description                    |
| --------- | --------- | ----------------------- | ------------------------------ |
| rstStat   | in        | sl                      | ASYNC statistics reset         |
| wrClk     | in        | sl                      | Write Interface (wrClk domain) |
| wrRst     | in        | sl                      |                                |
| wrEn      | in        | sl                      |                                |
| dataIn    | in        | slv(WIDTH_G-1 downto 0) |                                |
| rdClk     | in        | sl                      | Read Interface (rdClk domain)  |
| rdEn      | in        | sl                      |                                |
| updated   | out       | sl                      |                                |
| dataOut   | out       | slv(WIDTH_G-1 downto 0) |                                |
| dataMin   | out       | slv(WIDTH_G-1 downto 0) |                                |
| dataMax   | out       | slv(WIDTH_G-1 downto 0) |                                |
## Signals

| Name            | Type                    | Description |
| --------------- | ----------------------- | ----------- |
| r               | RegType                 |             |
| rin             | RegType                 |             |
| resetStat       | sl                      |             |
| ls              | sl                      |             |
| gt              | sl                      |             |
| valid           | sl                      |             |
| data            | slv(WIDTH_G-1 downto 0) |             |
| dataMinFeadback | slv(WIDTH_G-1 downto 0) |             |
| dataMaxFeadback | slv(WIDTH_G-1 downto 0) |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                          | Description |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       reset   => '1',<br><span style="padding-left:20px">       armed   => '0',<br><span style="padding-left:20px">       update  => '0',<br><span style="padding-left:20px">       dataIn  => (others => '0'),<br><span style="padding-left:20px">       dataMin => (others => '0'),<br><span style="padding-left:20px">       dataMax => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- unnamed: ( data, gt, ls, r, resetStat, valid, wrRst )
**Description**
 Using gtEq because better performance than gt in the DspComparator.vhd, and gtEq give the same result as gt with respect to this module's implementation

- unnamed: ( wrClk )
## Instantiations

- U_rstStat: surf.SynchronizerOneShot
- U_LessThan: surf.DspComparator
- U_GreaterThan: surf.DspComparator
**Description**
 (a <  b)

- U_dataOut: surf.SynchronizerFifo
- U_dataMin: surf.SynchronizerFifo
- U_dataMax: surf.SynchronizerFifo
