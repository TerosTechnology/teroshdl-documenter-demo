# Entity: FirAverage

- **File**: FirAverage.vhd
## Diagram

![Diagram](FirAverage.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Simple FIR  averaging filter using 3 input add/sub module
             y(n) = x(n) - x(n - FIR_LEN_G) + y(n)
             Adds log2(FIR_LEN_G) bits to the internal calculation to
                avoid overflow and shifts by log2(FIR_LEN_G) (non pow2
                FILT_LEN_G will have some < 1 filter gain)
             optionally supports time multiplexed channels with the
                ILEAVE_CHAN_G generic
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
| USE_CSA3_G    | boolean | false             |             |
| BRAM_THRESH_G | integer | 256               |             |
| FIR_LEN_G     | integer | 16                |             |
| ILEAVE_CHAN_G | integer | 1                 |             |
| USER_WIDTH_G  | integer | 0                 |             |
| REG_IN_G      | boolean | true              |             |
| REG_OUT_G     | boolean | true              |             |
## Ports

| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| clk       | in        | sl                             |             |
| rst       | in        | sl                             |             |
| validIn   | in        | sl                             | inputs      |
| userIn    | in        | slv(USER_WIDTH_G - 1 downto 0) |             |
| din       | in        | sfixed                         |             |
| validOut  | out       | sl                             | outputs     |
| userOut   | out       | slv(USER_WIDTH_G - 1 downto 0) |             |
| dout      | out       | sfixed                         |             |
## Signals

| Name         | Type                                           | Description                                       |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| r            | RegType                                        |                                                   |
| rin          | RegType                                        |                                                   |
| dinInt       | sfixed(din'range)                              |                                                   |
| dinIntDelay  | sfixed(din'range)                              |                                                   |
| doutInt      | sfixed(dout'range)                             |                                                   |
| filtOut      | sfixed(din'high + BIT_GROWTH_C downto din'low) |                                                   |
| filtDly      | sfixed(din'high + BIT_GROWTH_C downto din'low) |                                                   |
| filtOutShift | sfixed(din'high downto din'low - BIT_GROWTH_C) |                                                   |
| userDelayIn  | slv(userIn'length downto 0)                    | add 1 bit so we can delay valid and user together |
| userDelayOut | slv(userIn'length downto 0)                    |                                                   |
## Constants

| Name                 | Type                      | Value                                                                                                                                                                                           | Description            |
| -------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| BIT_GROWTH_C         | integer                   |  log2(FIR_LEN_G)                                                                                                                                                                                |                        |
| DIN_DELAY_C          | integer                   |  FIR_LEN_G * ILEAVE_CHAN_G                                                                                                                                                                      |                        |
| DIN_DELAY_STYLE_C    | string                    |  ite(DIN_DELAY_C > BRAM_THRESH_G,<br><span style="padding-left:20px"> "block",<br><span style="padding-left:20px"> "srl_reg")                                                                   |                        |
| ACCUM_DELAY_C        | integer                   |  ILEAVE_CHAN_G - 1                                                                                                                                                                              |                        |
| ACCUM_DELAY_STYLE_C  | string                    |  ite(ACCUM_DELAY_C > BRAM_THRESH_G,<br><span style="padding-left:20px"> "block",<br><span style="padding-left:20px"> "srl_reg")                                                                 |                        |
| TOT_LATENCY_C        | integer                   |  1 + ite(REG_IN_G,<br><span style="padding-left:20px"> 1,<br><span style="padding-left:20px"> 0) + ite(REG_OUT_G,<br><span style="padding-left:20px"> 1,<br><span style="padding-left:20px"> 0) | Latency for user/valid |
| INT_OVERFLOW_STYLE_C | fixed_overflow_style_type |  fixed_wrap                                                                                                                                                                                     |                        |
| INT_ROUNDING_STYLE_C | fixed_round_style_type    |  fixed_truncate                                                                                                                                                                                 |                        |
| REG_INIT_C           | RegType                   |  (       din     => (others => '0'),<br><span style="padding-left:20px">       dout    => (others => '0'))                                                                                      |                        |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( din, filtOutShift, r )
- seq: ( clk )
## Instantiations

- U_USER_DELAY: surf.SlvFixedDelay
- U_DIN_DELAY: surf.sfixedDelay
- U_ACCUM_DELAY: surf.sfixedDelay
- U_ADD_SUB: surf.add3
