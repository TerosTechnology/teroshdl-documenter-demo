# Entity: SinCosTaylor

- **File**: SinCosTaylor.vhd
## Diagram

![Diagram](SinCosTaylor.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Taylor series corrected SinCosLut, stores 1/4 cos in
              INT_PHASE_WIDTH_G - 2 bits LUT and does 1st order taylor series
              correction on ouput (3 real multipliers)
              dout.re <= cos
              dout.im <= sin

              9  cycle latency REG_IN_G = false
              10 cycle latency REG_IN_G = true
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
## Generics

| Generic name      | Type    | Value             | Description |
| ----------------- | ------- | ----------------- | ----------- |
| TPD_G             | time    | 1 ns              |             |
| XIL_DEVICE_G      | string  | "ULTRASCALE_PLUS" |             |
| FULL_RANGE_G      | boolean | true              |             |
| MEMORY_TYPE_G     | string  | "block"           |             |
| REG_IN_G          | boolean | true              |             |
| USER_WIDTH_G      | integer | 0                 |             |
| PHASE_WIDTH_G     | integer | 24                |             |
| INT_PHASE_WIDTH_G | integer | 12                |             |
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

| Name            | Type                                                                                       | Description                                       |
| --------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| phaseTrun       | unsigned(phaseIn'high downto phaseIn'high - INT_PHASE_WIDTH_G + 1)                         |  Truncate upper bits of phaseIn for LUT           |
| phaseRemainder  | sfixed(1 - INT_PHASE_WIDTH_G downto 1 - phaseIn'length)                                    |  Lower bits, zero pad (error is always positive)  |
| phaseRad        | sfixed(phaseRemainder'high + 2 downto phaseRemainder'high + 2 - 17)                        |  18 bit phaseRad, MATH_PI gain                    |
| sinCosTrun      | cfixed(re(sinCosOut.re'range),<br><span style="padding-left:20px"> im(sinCosOut.im'range)) |  phase truncated sinCos from LUT                  |
| sinCosTrunDelay | cfixed(re(sinCosOut.re'range),<br><span style="padding-left:20px"> im(sinCosOut.im'range)) |                                                   |
| sinPiInt        | sfixed(sinCosOut.re'range)                                                                 |                                                   |
| cosPiInt        | sfixed(sinCosOut.re'range)                                                                 |                                                   |
| sinCosCorr      | cfixed(re(sinCosOut.re'range),<br><span style="padding-left:20px"> im(sinCosOut.im'range)) |                                                   |
| slvDelayIn      | slv(USER_WIDTH_G downto 0)                                                                 |                                                   |
| slvDelayOut     | slv(USER_WIDTH_G downto 0)                                                                 |                                                   |
## Constants

| Name           | Type                 | Value                                                                                               | Description |
| -------------- | -------------------- | --------------------------------------------------------------------------------------------------- | ----------- |
| LUT_LATENCY_C  | integer              |  4 + ite(REG_IN_G,<br><span style="padding-left:20px"> 1,<br><span style="padding-left:20px"> 0)    |             |
| MULT_LATENCY_C | integer              |  4                                                                                                  |             |
| ADD_LATENCY_C  | integer              |  1                                                                                                  |             |
| TOT_LATENCY_C  | integer              |  LUT_LATENCY_C + MULT_LATENCY_C + ADD_LATENCY_C                                                     |             |
| TRUN_BITS_C    | integer              |  PHASE_WIDTH_G - INT_PHASE_WIDTH_G                                                                  |             |
| M_PI_C         | sfixed(2 downto -15) |  to_sfixed(MATH_PI,<br><span style="padding-left:20px"> 2,<br><span style="padding-left:20px"> -15) |             |
## Processes
- seq: ( clk )
</br>**Description**
 reset handled by DOREG reset in SinCosLut module 
## Instantiations

- U_MATCH_TOT_DELAY: surf.SlvFixedDelay
- U_SIN_COS_LUT: surf.SinCosLut
- U_MATCH_DELAY: surf.cfixedDelay
- U_MULT_PI: surf.sfixedMult
- U_MULT_COS: surf.sfixedMult
- U_MULT_SIN: surf.sfixedMult
