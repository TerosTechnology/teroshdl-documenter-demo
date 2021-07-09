# Entity: SpiMaster

## Diagram

![Diagram](SpiMaster.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Generic SPI Master Module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name      | Type                  | Value  | Description |
| ----------------- | --------------------- | ------ | ----------- |
| TPD_G             | time                  | 1 ns   |             |
| NUM_CHIPS_G       | positive range 1 to 8 | 4      |             |
| DATA_SIZE_G       | natural               | 16     |             |
| CPHA_G            | sl                    | '0'    |             |
| CPOL_G            | sl                    | '0'    |             |
| CLK_PERIOD_G      | real                  | 8.0E-9 |             |
| SPI_SCLK_PERIOD_G | real                  | 1.0E-6 |             |
## Ports

| Port name  | Direction | Type                                 | Description        |
| ---------- | --------- | ------------------------------------ | ------------------ |
| clk        | in        | sl                                   |                    |
| sRst       | in        | sl                                   |                    |
| freeRunClk | in        | sl                                   | Parallel interface |
| chipSel    | in        | slv(log2(NUM_CHIPS_G)-1 downto 0)    |                    |
| wrEn       | in        | sl                                   |                    |
| wrData     | in        | slv(DATA_SIZE_G-1 downto 0)          |                    |
| dataSize   | in        | slv(log2(DATA_SIZE_G)-1 downto 0)    |                    |
| rdEn       | out       | sl                                   |                    |
| rdData     | out       | slv(DATA_SIZE_G-1 downto 0)          |                    |
| shiftCount | out       | slv(bitSize(DATA_SIZE_G)-1 downto 0) |                    |
| spiCsL     | out       | slv(NUM_CHIPS_G-1 downto 0)          |                    |
| spiSclk    | out       | sl                                   |                    |
| spiSdi     | out       | sl                                   |                    |
| spiSdo     | in        | sl                                   |                    |
## Signals

| Name      | Type    | Description |
| --------- | ------- | ----------- |
| r         | RegType |             |
| rin       | RegType |             |
| spiSdoRes | sl      |             |
## Constants

| Name                         | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| ---------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SPI_CLK_PERIOD_DIV2_CYCLES_C | integer |  integer(SPI_SCLK_PERIOD_G / (2.0*CLK_PERIOD_G))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |             |
| SCLK_COUNTER_SIZE_C          | integer |  bitSize(SPI_CLK_PERIOD_DIV2_CYCLES_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
| REG_INIT_C                   | RegType |  (       state       => IDLE_S,<br><span style="padding-left:20px">       rdEn        => '0',<br><span style="padding-left:20px">       rdData      => (others => '0'),<br><span style="padding-left:20px">       wrData      => (others => '0'),<br><span style="padding-left:20px">       dataCounter => (others => '0'),<br><span style="padding-left:20px">       sclkCounter => (others => '0'),<br><span style="padding-left:20px">       spiCsL      => (others => '1'),<br><span style="padding-left:20px">       spiSclk     => '0',<br><span style="padding-left:20px">       spiSdi      => '0') |             |
## Types

| Name      | Type                                                                                                                                                                                                      | Description |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> FREE_RUNNING_CLK_S,<br><span style="padding-left:20px"> SHIFT_S,<br><span style="padding-left:20px"> SAMPLE_S,<br><span style="padding-left:20px"> DONE_S)  | Types       |
| RegType   |                                                                                                                                                                                                           |             |
## Processes
- comb: ( chipSel, dataSize, freeRunClk, r, sRst, spiSdoRes, wrData,
                   wrEn )
- seq: ( clk )
