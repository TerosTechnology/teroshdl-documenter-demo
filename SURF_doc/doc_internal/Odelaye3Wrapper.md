# Entity: Odelaye3Wrapper

## Diagram

![Diagram](Odelaye3Wrapper.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Wrapper on ODELAYE3 that patches the silicon's issue of increments > 8
https://forums.xilinx.com/t5/Versal-and-UltraScale/IDELAY-ODELAY-Usage/td-p/812362
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name     | Type    | Value        | Description                                                |
| ---------------- | ------- | ------------ | ---------------------------------------------------------- |
| TPD_G            | time    | 1 ns         |                                                            |
| CASCADE          | string  | "NONE"       | Cascade setting (MASTER, NONE, SLAVE_END, SLAVE_MIDDLE)    |
| DELAY_FORMAT     | string  | "TIME"       | (COUNT, TIME)                                              |
| DELAY_TYPE       | string  | "FIXED"      | Set the type of tap delay line (FIXED, VARIABLE, VAR_LOAD) |
| DELAY_VALUE      | integer | 0            | Output delay tap setting                                   |
| IS_CLK_INVERTED  | bit     | '0'          | Optional inversion for CLK                                 |
| IS_RST_INVERTED  | bit     | '0'          | Optional inversion for RST                                 |
| REFCLK_FREQUENCY | real    | 300.0        | IDELAYCTRL clock input frequency in MHz (200.0-2667.0).    |
| SIM_DEVICE       | string  | "ULTRASCALE" | Set the device version (ULTRASCALE, ULTRASCALE_PLUS)       |
| UPDATE_MODE      | string  | "ASYNC"      |                                                            |
## Ports

| Port name   | Direction | Type            | Description                                                    |
| ----------- | --------- | --------------- | -------------------------------------------------------------- |
| BUSY        | out       | sl              | 1-bit output: Patch module is busy                             |
| CASC_OUT    | out       | sl              | 1-bit output: Cascade delay output to IDELAY input cascade     |
| CNTVALUEOUT | out       | slv(8 downto 0) | 9-bit output: Counter value output                             |
| DATAOUT     | out       | sl              | 1-bit output: Delayed data from ODATAIN input port             |
| CASC_IN     | in        | sl              | 1-bit input: Cascade delay input from slave IDELAY CASCADE_OUT |
| CASC_RETURN | in        | sl              | 1-bit input: Cascade delay returning from slave IDELAY DATAOUT |
| CE          | in        | sl              | 1-bit input: Active high enable increment/decrement input      |
| CLK         | in        | sl              | 1-bit input: Clock input                                       |
| CNTVALUEIN  | in        | slv(8 downto 0) | 9-bit input: Counter value input                               |
| EN_VTC      | in        | sl              | 1-bit input: Keep delay constant over VT                       |
| INC         | in        | sl              | 1-bit input: Increment/Decrement tap delay input               |
| LOAD        | in        | sl              | 1-bit input: Load DELAY_VALUE input                            |
| ODATAIN     | in        | sl              | 1-bit input: Data input                                        |
| RST         | in        | sl              |                                                                |
## Signals

| Name            | Type            | Description |
| --------------- | --------------- | ----------- |
| currentCntValue | slv(8 downto 0) |             |
| patchCntValue   | slv(8 downto 0) |             |
| patchLoad       | sl              |             |
## Instantiations

- U_patch: surf.Delaye3PatchFsm
- U_ODELAYE3: ODELAYE3
