# Entity: Encoder8b10b

- **File**: Encoder8b10b.vhd
## Diagram

![Diagram](Encoder8b10b.svg "Diagram")
## Description

Title      : Line Code 8B10B: https://en.wikipedia.org/wiki/8b/10b_encoding
Company    : SLAC National Accelerator Laboratory
Description: 8B10B Encoder Module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type     | Value | Description |
| -------------- | -------- | ----- | ----------- |
| TPD_G          | time     | 1 ns  |             |
| NUM_BYTES_G    | positive | 2     |             |
| RST_POLARITY_G | sl       | '0'   |             |
| RST_ASYNC_G    | boolean  | true  |             |
| FLOW_CTRL_EN_G | boolean  | false |             |
## Ports

| Port name | Direction | Type                           | Description           |
| --------- | --------- | ------------------------------ | --------------------- |
| clk       | in        | sl                             |                       |
| clkEn     | in        | sl                             | Optional Clock Enable |
| rst       | in        | sl                             | Optional Reset        |
| validIn   | in        | sl                             |                       |
| readyIn   | out       | sl                             |                       |
| dataIn    | in        | slv(NUM_BYTES_G*8-1 downto 0)  |                       |
| dataKIn   | in        | slv(NUM_BYTES_G-1 downto 0)    |                       |
| validOut  | out       | sl                             |                       |
| readyOut  | in        | sl                             |                       |
| dataOut   | out       | slv(NUM_BYTES_G*10-1 downto 0) |                       |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                       | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       validOut => toSl(not FLOW_CTRL_EN_G),<br><span style="padding-left:20px">       readyIn  => '0',<br><span style="padding-left:20px">       runDisp  => '0',<br><span style="padding-left:20px">       dataOut  => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( dataIn, dataKIn, r, readyOut, rst )
- seq: ( clk, rst )
