# Entity: JesdSysrefMon

## Diagram

![Diagram](JesdSysrefMon.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Monitors the time between sysref rising edge detections
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name       | Direction | Type             | Description                            |
| --------------- | --------- | ---------------- | -------------------------------------- |
| devClk          | in        | sl               | SYSREF Edge detection (devClk domain)  |
| sysrefEdgeDet_i | in        | sl               |                                        |
| axilClk         | in        | sl               | Max/Min measurements  (axilClk domain) |
| statClr         | in        | sl               |                                        |
| sysRefPeriodmin | out       | slv(15 downto 0) |                                        |
| sysRefPeriodmax | out       | slv(15 downto 0) |                                        |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
| clr  | sl      |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                               | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       armed           => "00",<br><span style="padding-left:20px">       cnt             => x"0000",<br><span style="padding-left:20px">       sysRefPeriodmin => x"0000",<br><span style="padding-left:20px">       sysRefPeriodmax => x"0000") |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( clr, r, sysrefEdgeDet_i )
- seq: ( devClk )
## Instantiations

- U_RstOneShot: surf.SynchronizerOneShot
- U_sync: surf.SynchronizerFifo
