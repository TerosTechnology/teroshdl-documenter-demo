# Entity: SfixedAccumulator

- **File**: SfixedAccumulator.vhd
## Diagram

![Diagram](SfixedAccumulator.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: sfixed accumultaor, supports interleaved channels
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

| Name         | Type                        | Description                                       |
| ------------ | --------------------------- | ------------------------------------------------- |
| r            | RegType                     |                                                   |
| rin          | RegType                     |                                                   |
| sumDly       | sfixed(dout'range)          |                                                   |
| userDelayIn  | slv(userIn'length downto 0) | add 1 bit so we can delay valid and user together |
| userDelayOut | slv(userIn'length downto 0) |                                                   |
## Constants

| Name                 | Type                      | Value                                                                                                                                                                                                                                      | Description |
| -------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| TOT_LATENCY_C        | integer                   |  1 + ite(REG_IN_G,<br><span style="padding-left:20px"> 1,<br><span style="padding-left:20px"> 0) + ite(REG_OUT_G,<br><span style="padding-left:20px"> 1,<br><span style="padding-left:20px"> 0)                                            |             |
| INT_OVERFLOW_STYLE_C | fixed_overflow_style_type |  fixed_wrap                                                                                                                                                                                                                                |             |
| INT_ROUNDING_STYLE_C | fixed_round_style_type    |  fixed_truncate                                                                                                                                                                                                                            |             |
| REG_INIT_C           | RegType                   |  (       rst     => '0',<br><span style="padding-left:20px">       dinR    => (others => '0'),<br><span style="padding-left:20px">       doutR   => (others => '0'),<br><span style="padding-left:20px">       sum     => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( din, sumDly, rst, r )
- seq: ( clk )
## Instantiations

- U_USER_DELAY: surf.SlvFixedDelay
