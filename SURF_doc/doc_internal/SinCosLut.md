# Entity: SinCosLut

- **File**: SinCosLut.vhd
## Diagram

![Diagram](SinCosLut.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: SinCosLut, stores 1/4 cos in PHASE_WIDTH_G - 2 bits LUT
             dout.re <= cos
             dout.im <= sin
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type    | Value             | Description |
| ------------- | ------- | ----------------- | ----------- |
| TPD_G         | time    | 1 ns              |             |
| XIL_DEVICE_G  | string  | "ULTRASCALE_PLUS" |             |
| FULL_RANGE_G  | boolean | true              |             |
| MEMORY_TYPE_G | string  | "block"           |             |
| REG_IN_G      | boolean | true              |             |
| USER_WIDTH_G  | integer | 0                 |             |
| PHASE_WIDTH_G | integer | 12                |             |
## Ports

| Port name | Direction | Type                                 | Description |
| --------- | --------- | ------------------------------------ | ----------- |
| clk       | in        | sl                                   |             |
| rst       | in        | sl                                   |             |
| validIn   | in        | sl                                   |             |
| userIn    | in        | slv(USER_WIDTH_G - 1 downto 0)       |             |
| phaseIn   | in        | unsigned(PHASE_WIDTH_G - 1 downto 0) |             |
| validOut  | out       | sl                                   |             |
| userOut   | out       | slv(USER_WIDTH_G - 1 downto 0)       |             |
| sinCosOut | out       | cfixed                               |             |
## Signals

| Name           | Type                       | Description |
| -------------- | -------------------------- | ----------- |
| r              | RegType                    |             |
| rin            | RegType                    |             |
| quarterWaveLut | QuarterWaveLutType         |             |
| slvDelayIn     | slv(USER_WIDTH_G downto 0) |             |
| slvDelayOut    | slv(USER_WIDTH_G downto 0) |             |
## Constants

| Name                 | Type                      | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                              |
| -------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| TOT_LATENCY_C        | integer                   |  4 + ite(REG_IN_G,<br><span style="padding-left:20px"> 1,<br><span style="padding-left:20px"> 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                          |
| INT_PHASE_WIDTH_C    | integer                   |  PHASE_WIDTH_G - 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Only store 1/4 of a sine wave internally |
| QUARTER_DEPTH_C      | integer                   |  2**INT_PHASE_WIDTH_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                          |
| INT_OVERFLOW_STYLE_C | fixed_overflow_style_type |  fixed_wrap                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                          |
| INT_ROUNDING_STYLE_C | fixed_round_style_type    |  fixed_truncate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                          |
| REG_INIT_C           | RegType                   |  (       rst          => (others => '0'),<br><span style="padding-left:20px">       phaseMsb     => (others => '0'),<br><span style="padding-left:20px">       phaseMsbR    => (others => '0'),<br><span style="padding-left:20px">       phaseMsbRR   => (others => '0'),<br><span style="padding-left:20px">       phaseMsbRRR  => (others => '0'),<br><span style="padding-left:20px">       phaseLsb     => (others => '0'),<br><span style="padding-left:20px">       sinAddr      => (others => '0'),<br><span style="padding-left:20px">       cosAddr      => (others => '0'),<br><span style="padding-left:20px">       lutSin       => (others => '0'),<br><span style="padding-left:20px">       lutCos       => (others => '0'),<br><span style="padding-left:20px">       lutSinDoReg  => (others => '0'),<br><span style="padding-left:20px">       lutCosDoReg  => (others => '0'),<br><span style="padding-left:20px">       sinCosOut    => (others => (others => '0'))) |                                          |
## Types

| Name               | Type | Description |
| ------------------ | ---- | ----------- |
| QuarterWaveLutType |      |             |
| RegType            |      |             |
## Functions
- initQuarterWaveLut <font id="function_arguments">(QUARTER_DEPTH : integer;<br><span style="padding-left:20px"> STYP : sfixed) </font> <font id="function_return">return QuarterWaveLutType </font>
## Processes
- comb: ( phaseIn, rst, r )
- seq: ( clk )
## Instantiations

- U_MATCH_CMULT_DELAY: surf.SlvFixedDelay
