# Entity: ClkOutBufDiff

- **File**: ClkOutBufDiff.vhd
## Diagram

![Diagram](ClkOutBufDiff.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Special buffer for outputting a clock on Xilinx FPGA pins.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type    | Value     | Description                                           |
| -------------- | ------- | --------- | ----------------------------------------------------- |
| TPD_G          | time    | 1 ns      |                                                       |
| XIL_DEVICE_G   | string  | "7SERIES" | Either "7SERIES" or "ULTRASCALE" or "ULTRASCALE_PLUS" |
| RST_POLARITY_G | sl      | '1'       |                                                       |
| INVERT_G       | boolean | false     |                                                       |
## Ports

| Port name | Direction | Type | Description                                        |
| --------- | --------- | ---- | -------------------------------------------------- |
| rstIn     | in        | sl   | Optional reset                                     |
| outEnL    | in        | sl   | optional tristate (0 = enabled, 1 = high z output) |
| clkIn     | in        | sl   | Input clock                                        |
| clkOutP   | out       | sl   | differential output buffer                         |
| clkOutN   | out       | sl   |                                                    |
## Signals

| Name   | Type | Description |
| ------ | ---- | ----------- |
| clkDdr | sl   |             |
| rst    | sl   |             |
## Instantiations

- OBUFDS_I: OBUFTDS
**Description**
Differential output buffer

