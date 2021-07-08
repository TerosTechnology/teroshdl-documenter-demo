# Entity: Scrambler

## Diagram

![Diagram](Scrambler.svg "Diagram")
## Description

Title      : Source Synchronous Scrambler
Company    : SLAC National Accelerator Laboratory
Description:
A source synchronous (multiplicative) scrambler with paramatized data width
and scrambling polynomial.
This file is part of SURF. It is subject to
the license terms in the LICENSE.txt file found in the top-level directory
of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of SURF, including this file, may be
copied, modified, propagated, or distributed except according to the terms
contained in the LICENSE.txt file.
## Generics

| Generic name      | Type         | Value              | Description    |
| ----------------- | ------------ | ------------------ | -------------- |
| TPD_G             | time         | 1 ns               |                |
| DIRECTION_G       | string       | "SCRAMBLER"        | or DESCRAMBLER |
| DATA_WIDTH_G      | integer      | 64                 |                |
| SIDEBAND_WIDTH_G  | integer      | 2                  |                |
| BIT_REVERSE_IN_G  | boolean      | false              |                |
| BIT_REVERSE_OUT_G | boolean      | false              |                |
| TAPS_G            | IntegerArray | (0 => 39, 1 => 58) |                |
## Ports

| Port name      | Direction | Type                             | Description |
| -------------- | --------- | -------------------------------- | ----------- |
| clk            | in        | sl                               |             |
| rst            | in        | sl                               |             |
| inputValid     | in        | sl                               |             |
| inputReady     | out       | sl                               |             |
| inputData      | in        | slv(DATA_WIDTH_G-1 downto 0)     |             |
| inputSideband  | in        | slv(SIDEBAND_WIDTH_G-1 downto 0) |             |
| outputValid    | out       | sl                               |             |
| outputReady    | in        | sl                               |             |
| outputData     | out       | slv(DATA_WIDTH_G-1 downto 0)     |             |
| outputSideband | out       | slv(SIDEBAND_WIDTH_G-1 downto 0) |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name              | Type    | Value                                                                                                                                                                                                                                                                                                                                   | Description |
| ----------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SCRAMBLER_WIDTH_C | integer |  maximum(TAPS_G)                                                                                                                                                                                                                                                                                                                        |             |
| REG_INIT_C        | RegType |  (       inputReady     => '0',<br><span style="padding-left:20px">       outputValid    => '0',<br><span style="padding-left:20px">       scrambler      => (others => '0'),<br><span style="padding-left:20px">       outputData     => (others => '0'),<br><span style="padding-left:20px">       outputSideband => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( inputData, inputSideband, inputValid, outputReady, r, rst )
- seq: ( clk )
