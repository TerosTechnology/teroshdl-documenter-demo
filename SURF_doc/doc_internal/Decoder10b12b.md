# Entity: Decoder10b12b

## Diagram

![Diagram](Decoder10b12b.svg "Diagram")
## Description

Title      : Line Code 10B12B: https://confluence.slac.stanford.edu/x/QndODQ
Company    : SLAC National Accelerator Laboratory
Description: 10B12B Decoder Module
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
| RST_POLARITY_G | sl      | '0'   |             |
| RST_ASYNC_G    | boolean | true  |             |
| USE_CLK_EN_G   | boolean | false |             |
## Ports

| Port name | Direction | Type             | Description           |
| --------- | --------- | ---------------- | --------------------- |
| clk       | in        | sl               |                       |
| clkEn     | in        | sl               | Optional Clock Enable |
| rst       | in        | sl               | Optional Reset        |
| validIn   | in        | sl               |                       |
| dataIn    | in        | slv(11 downto 0) |                       |
| dataOut   | out       | slv(9 downto 0)  |                       |
| dataKOut  | out       | sl               |                       |
| validOut  | out       | sl               |                       |
| dispOut   | out       | sl               |                       |
| codeError | out       | sl               |                       |
| dispError | out       | sl               |                       |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                              | Description |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       dispOut   => '0',<br><span style="padding-left:20px">       dataOut   => (others => '0'),<br><span style="padding-left:20px">       dataKOut  => '0',<br><span style="padding-left:20px">       validOut  => '0',<br><span style="padding-left:20px">       codeError => '0',<br><span style="padding-left:20px">       dispError => '0') |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( dataIn, r, rst, validIn )
- seq: ( clk, rst )
