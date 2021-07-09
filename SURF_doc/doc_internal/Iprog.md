# Entity: Iprog

## Diagram

![Diagram](Iprog.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Wrapper for the ICAP Module to issue IPROG command
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type     | Value     | Description                                           |
| -------------- | -------- | --------- | ----------------------------------------------------- |
| TPD_G          | time     | 1 ns      |                                                       |
| XIL_DEVICE_G   | string   | "7SERIES" | Either "7SERIES" or "ULTRASCALE" or "ULTRASCALE_PLUS" |
| USE_SLOWCLK_G  | boolean  | false     |                                                       |
| BUFR_CLK_DIV_G | positive | 8         |                                                       |
| RST_POLARITY_G | sl       | '1'       |                                                       |
## Ports

| Port name   | Direction | Type             | Description |
| ----------- | --------- | ---------------- | ----------- |
| clk         | in        | sl               |             |
| rst         | in        | sl               |             |
| slowClk     | in        | sl               |             |
| start       | in        | sl               |             |
| bootAddress | in        | slv(31 downto 0) |             |
