# Entity: GLinkEncoder

- **File**: GLinkEncoder.vhd
## Diagram

![Diagram](GLinkEncoder.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Encodes 16 bit data raw words into 20 bit GLink words.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type    | Value | Description                                         |
| -------------- | ------- | ----- | --------------------------------------------------- |
| TPD_G          | time    | 1 ns  |                                                     |
| RST_ASYNC_G    | boolean | false |                                                     |
| RST_POLARITY_G | sl      | '1'   | '1' for active HIGH reset, '0' for active LOW reset |
| FLAGSEL_G      | boolean | false |                                                     |
## Ports

| Port name   | Direction | Type             | Description |
| ----------- | --------- | ---------------- | ----------- |
| en          | in        | sl               |             |
| clk         | in        | sl               |             |
| rst         | in        | sl               |             |
| gLinkTx     | in        | GLinkTxType      |             |
| encodedData | out       | slv(19 downto 0) |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                              | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| REG_INIT_C | RegType |  (       '0',<br><span style="padding-left:20px">       (GLINK_IDLE_WORD_FF0_C & GLINK_CONTROL_WORD_C),<br><span style="padding-left:20px">       (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Functions
- disparity <font id="function_arguments">(vec : slv(19 downto 0)) </font> <font id="function_return">return signed </font>
## Processes
- comb: ( gLinkTx, r, rst )
- seq: ( clk, rst )
