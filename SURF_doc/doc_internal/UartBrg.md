# Entity: UartBrg

## Diagram

![Diagram](UartBrg.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: UART Baud Rate Generator
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type    | Value   | Description        |
| ------------ | ------- | ------- | ------------------ |
| CLK_FREQ_G   | real    | 125.0E6 | Default 125 MHz    |
| BAUD_RATE_G  | integer | 115200  | Default 115.2 kbps |
| MULTIPLIER_G | integer | 16      |                    |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| clk       | in        | sl   |             |
| rst       | in        | sl   |             |
| baudClkEn | out       | sl   |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | Regtype |             |
## Constants

| Name       | Type    | Value                                                                                | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------ | ----------- |
| CLK_DIV_C  | integer |  integer(CLK_FREQ_G / real(BAUD_RATE_G * MULTIPLIER_G)) - 1                          |             |
| REG_INIT_C | RegType |  (       count     => 0,<br><span style="padding-left:20px">       baudClkEn => '0') |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( r, rst )
- seq: ( clk )
