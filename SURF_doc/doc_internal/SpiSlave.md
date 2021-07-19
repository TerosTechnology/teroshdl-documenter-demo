# Entity: SpiSlave

- **File**: SpiSlave.vhd
## Diagram

![Diagram](SpiSlave.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Generic SPI Slave Module
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
| CPOL_G       | sl       | '0'   |             |
| CPHA_G       | sl       | '1'   |             |
| WORD_SIZE_G  | positive | 16    |             |
## Ports

| Port name | Direction | Type                        | Description |
| --------- | --------- | --------------------------- | ----------- |
| clk       | in        | sl                          |             |
| rst       | in        | sl                          |             |
| sclk      | in        | sl                          |             |
| mosi      | in        | sl                          |             |
| miso      | out       | sl                          |             |
| selL      | in        | sl                          |             |
| rdData    | in        | slv(WORD_SIZE_G-1 downto 0) |             |
| rdStb     | in        | sl                          |             |
| wrData    | out       | slv(WORD_SIZE_G-1 downto 0) |             |
| wrStb     | out       | sl                          |             |
## Signals

| Name     | Type    | Description |
| -------- | ------- | ----------- |
| r        | RegType |             |
| rin      | RegType |             |
| mosiSync | sl      |             |
| sclkSync | sl      |             |
| selLSync | sl      |             |
## Constants

| Name        | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| ----------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| MAX_COUNT_C | integer |  WORD_SIZE_G-1                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| REG_INIT_C  | RegType |  (       mosiLast => '0',<br><span style="padding-left:20px">       sclkLast => '0',<br><span style="padding-left:20px">       selLLast => '1',<br><span style="padding-left:20px">       shiftReg => (others => '0'),<br><span style="padding-left:20px">       shiftCnt => toSlv(MAX_COUNT_C,<br><span style="padding-left:20px"> log2(WORD_SIZE_G)),<br><span style="padding-left:20px">       gotSclk  => '0',<br><span style="padding-left:20px">       wrStb    => '0') |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- seq: ( clk )
- comb: ( mosiSync, r, rdData, rdStb, rst, sclkSync, selLSync )
## Instantiations

- SEL_SYNCHRONIZER: surf.Synchronizer
- SCLK_SYNCHRONIZER: surf.Synchronizer
- MOSI_SYNCHRONIZER: surf.Synchronizer
