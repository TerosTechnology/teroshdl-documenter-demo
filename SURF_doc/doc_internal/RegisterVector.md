# Entity: RegisterVector

- **File**: RegisterVector.vhd
## Diagram

![Diagram](RegisterVector.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: 1 c-c register delay
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type     | Value | Description                                         |
| -------------- | -------- | ----- | --------------------------------------------------- |
| TPD_G          | time     | 1 ns  |                                                     |
| RST_POLARITY_G | sl       | '1'   | '1' for active HIGH reset, '0' for active LOW reset |
| WIDTH_G        | positive | 1     |                                                     |
| INIT_G         | slv      | "0"   |                                                     |
## Ports

| Port name | Direction | Type                    | Description           |
| --------- | --------- | ----------------------- | --------------------- |
| clk       | in        | sl                      |                       |
| rst       | in        | sl                      | Optional reset        |
| en        | in        | sl                      | Optional clock enable |
| sig_i     | in        | slv(WIDTH_G-1 downto 0) |                       |
| reg_o     | out       | slv(WIDTH_G-1 downto 0) |                       |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type                    | Value                                                                                                                | Description |
| ---------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| INIT_C     | slv(WIDTH_G-1 downto 0) |  ite(INIT_G = "0",<br><span style="padding-left:20px"> slvZero(WIDTH_G),<br><span style="padding-left:20px"> INIT_G) |             |
| REG_INIT_C | RegType                 |  (       reg => INIT_C)                                                                                              |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( en, r, rst, sig_i )
- seq: ( clk )
