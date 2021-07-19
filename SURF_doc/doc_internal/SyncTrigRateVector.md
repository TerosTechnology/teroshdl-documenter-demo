# Entity: SyncTrigRateVector

- **File**: SyncTrigRateVector.vhd
## Diagram

![Diagram](SyncTrigRateVector.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Wrapper for multiple SyncTrigRate modules
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type     | Value    | Description                                |
| -------------- | -------- | -------- | ------------------------------------------ |
| TPD_G          | time     | 1 ns     | Simulation FF output delay                 |
| COMMON_CLK_G   | boolean  | false    | true if locClk & refClk are the same clock |
| ONE_SHOT_G     | boolean  | false    |                                            |
| IN_POLARITY_G  | slv      | "1"      | 0 for active LOW, 1 for active HIGH        |
| REF_CLK_FREQ_G | real     | 200.0E+6 | units of Hz                                |
| REFRESH_RATE_G | real     | 1.0E+0   | units of Hz                                |
| CNT_WIDTH_G    | positive | 32       | Counters' width                            |
| WIDTH_G        | positive | 16       |                                            |
## Ports

| Port name       | Direction | Type                                                      | Description                         |
| --------------- | --------- | --------------------------------------------------------- | ----------------------------------- |
| trigIn          | in        | slv(WIDTH_G-1 downto 0)                                   | Trigger Input (locClk domain)       |
| trigRateUpdated | out       | sl                                                        | Trigger Rate Output (locClk domain) |
| trigRateOut     | out       | SlVectorArray(WIDTH_G-1 downto 0, CNT_WIDTH_G-1 downto 0) | units of REFRESH_RATE_G             |
| locClkEn        | in        | sl                                                        | Clocks                              |
| locClk          | in        | sl                                                        |                                     |
| refClk          | in        | sl                                                        |                                     |
## Signals

| Name           | Type                    | Description |
| -------------- | ----------------------- | ----------- |
| trigRate       | MySlvArray              |             |
| trigRateUpdate | slv(WIDTH_G-1 downto 0) |             |
## Constants

| Name          | Type          | Value                           | Description |
| ------------- | ------------- | ------------------------------- | ----------- |
| IN_POLARITY_C | MyVectorArray |  FillVectorArray(IN_POLARITY_G) |             |
## Types

| Name          | Type | Description |
| ------------- | ---- | ----------- |
| MyVectorArray |      |             |
| MySlvArray    |      |             |
## Functions
- FillVectorArray <font id="function_arguments">(INPUT : slv) </font> <font id="function_return">return MyVectorArray </font>
