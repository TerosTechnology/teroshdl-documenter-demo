# Entity: IirSimple

- **File**: IirSimple.vhd
## Diagram

![Diagram](IirSimple.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Simple IIR filter using bitshifts
             y(n) = alpha*x(n) + (1 - alpha)*y(n-1)
                where alpha = 2**(-IIR_SHIFT_G)
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

| Generic name  | Type    | Value             | Description                    |
| ------------- | ------- | ----------------- | ------------------------------ |
| TPD_G         | time    | 1 ns              |                                |
| XIL_DEVICE_G  | string  | "ULTRASCALE_PLUS" |                                |
| USE_CSA3_G    | boolean | false             |                                |
| BRAM_THRESH_G | integer | 256               |                                |
| IIR_SHIFT_G   | integer | 4                 | alpha = 2**(-IIR_SHIFT_G)      |
| ILEAVE_CHAN_G | integer | 1                 | Number of interleaved channels |
| USER_WIDTH_G  | integer | 0                 |                                |
| REG_IN_G      | boolean | true              |                                |
| REG_OUT_G     | boolean | true              |                                |
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

| Name         | Type                                                                | Description                                       |
| ------------ | ------------------------------------------------------------------- | ------------------------------------------------- |
| r            | RegType                                                             |                                                   |
| rin          | RegType                                                             |                                                   |
| dinInt       | sfixed(din'range)                                                   |                                                   |
| doutInt      | sfixed(dout'range)                                                  |                                                   |
| filtOut      | sfixed(dout'high downto dout'low - IIR_SHIFT_G)                     |                                                   |
| filtDly      | sfixed(dout'high downto dout'low - IIR_SHIFT_G)                     |                                                   |
| userDelayIn  | slv(userIn'length downto 0)                                         | add 1 bit so we can delay valid and user together |
| userDelayOut | slv(userIn'length downto 0)                                         |                                                   |
| shiftInA     | sfixed(din'high - IIR_SHIFT_G downto din'low - IIR_SHIFT_G)         |                                                   |
| shiftInB     | sfixed(filtOut'high - IIR_SHIFT_G downto filtOut'low - IIR_SHIFT_G) |                                                   |
## Constants

| Name                 | Type                      | Value                                                                                                                                                                                           | Description            |
| -------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| IIR_DELAY_C          | integer                   |  ILEAVE_CHAN_G - 1                                                                                                                                                                              |                        |
| IIR_DELAY_STYLE_C    | string                    |  ite(IIR_DELAY_C > BRAM_THRESH_G,<br><span style="padding-left:20px"> "block",<br><span style="padding-left:20px"> "srl_reg")                                                                   |                        |
| TOT_LATENCY_C        | integer                   |  1 + ite(REG_IN_G,<br><span style="padding-left:20px"> 1,<br><span style="padding-left:20px"> 0) + ite(REG_OUT_G,<br><span style="padding-left:20px"> 1,<br><span style="padding-left:20px"> 0) | Latency for user/valid |
| INT_OVERFLOW_STYLE_C | fixed_overflow_style_type |  fixed_wrap                                                                                                                                                                                     |                        |
| INT_ROUNDING_STYLE_C | fixed_round_style_type    |  fixed_truncate                                                                                                                                                                                 |                        |
| REG_INIT_C           | RegType                   |  (       din     => (others => '0'),<br><span style="padding-left:20px">       dout    => (others => '0'))                                                                                      |                        |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( din, filtOut, r )
- seq: ( clk )
## Instantiations

- U_USER_DELAY: surf.SlvFixedDelay
- U_ACCUM_DELAY: surf.sfixedDelay
- U_ADD_SUB: surf.add3
