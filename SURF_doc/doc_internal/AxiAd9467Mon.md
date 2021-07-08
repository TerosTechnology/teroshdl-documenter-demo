# Entity: AxiAd9467Mon

## Diagram

![Diagram](AxiAd9467Mon.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AD9467 Monitor Module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type | Value    | Description |
| -------------- | ---- | -------- | ----------- |
| TPD_G          | time | 1 ns     |             |
| ADC_CLK_FREQ_G | real | 250.0E+6 |             |
## Ports

| Port name  | Direction | Type                | Description |
| ---------- | --------- | ------------------- | ----------- |
| adcClk     | in        | sl                  |             |
| adcRst     | in        | sl                  |             |
| adcData    | in        | slv(15 downto 0)    |             |
| adcDataMon | out       | Slv16Array(0 to 15) |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                     | Description           |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| MAX_CNT_C  | natural |  getTimeRatio(ADC_CLK_FREQ_G,<br><span style="padding-left:20px"> 1.0)                                                                                                    | 1 second refresh rate |
| REG_INIT_C | RegType |  (       0,<br><span style="padding-left:20px">       0,<br><span style="padding-left:20px">       (others => x"0000"),<br><span style="padding-left:20px">       IDLE_S) |                       |
## Types

| Name      | Type                                                   | Description |
| --------- | ------------------------------------------------------ | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> SMPL_S)  |             |
| RegType   |                                                        |             |
## Processes
- comb: ( adcData, adcRst, r )
- seq: ( adcClk )
