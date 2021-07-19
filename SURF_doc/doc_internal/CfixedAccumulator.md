# Entity: CfixedAccumulator

- **File**: CfixedAccumulator.vhd
## Diagram

![Diagram](CfixedAccumulator.svg "Diagram")
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
| din       | in        | cfixed                         |             |
| validOut  | out       | sl                             | outputs     |
| userOut   | out       | slv(USER_WIDTH_G - 1 downto 0) |             |
| dout      | out       | cfixed                         |             |
## Instantiations

- U_REAL_ACCUM: surf.SfixedAccumulator
- U_IMAG_ACCUM: surf.Accumulator
