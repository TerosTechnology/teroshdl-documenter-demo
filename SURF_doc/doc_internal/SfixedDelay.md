# Entity: sfixedDelay

- **File**: SfixedDelay.vhd
## Diagram

![Diagram](SfixedDelay.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type    | Value             | Description                                                  |
| ------------- | ------- | ----------------- | ------------------------------------------------------------ |
| TPD_G         | time    | 1 ns              |                                                              |
| XIL_DEVICE_G  | string  | "ULTRASCALE_PLUS" |                                                              |
| USER_WIDTH_G  | integer | 0                 |                                                              |
| DELAY_STYLE_G | string  | "srl_reg"         | "reg", "srl", "srl_reg", "reg_srl", "reg_srl_reg" or "block" |
| DELAY_G       | integer | 256               |                                                              |
## Ports

| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| clk       | in        | sl                           |             |
| validIn   | in        | sl                           |             |
| userIn    | in        | slv(USER_WIDTH_G-1 downto 0) |             |
| din       | in        | sfixed                       |             |
| validOut  | out       | sl                           |             |
| userOut   | out       | slv(USER_WIDTH_G-1 downto 0) |             |
| dout      | out       | sfixed                       |             |
## Signals

| Name        | Type                      | Description |
| ----------- | ------------------------- | ----------- |
| slvDelayIn  | slv(SLV_LEN_C-1 downto 0) |             |
| slvDelayOut | slv(SLV_LEN_C-1 downto 0) |             |
## Constants

| Name      | Type    | Value                          | Description |
| --------- | ------- | ------------------------------ | ----------- |
| SLV_LEN_C | integer |  din'length + 1 + USER_WIDTH_G |             |
## Instantiations

- U_SLV_DELAY: surf.SlvFixedDelay
