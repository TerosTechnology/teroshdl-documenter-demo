# Entity: LutFixedDelay

## Diagram

![Diagram](LutFixedDelay.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Manual instantation of RAM64X1S, RAM128X1S or RAM256X1S for
             LUT based delays
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type                     | Value             | Description                          |
| ------------ | ------------------------ | ----------------- | ------------------------------------ |
| TPD_G        | time                     | 1 ns              |                                      |
| XIL_DEVICE_G | string                   | "ULTRASCALE_PLUS" |                                      |
| DELAY_G      | natural  range 33 to 513 | 256               | default number of clock cycle delays |
| WIDTH_G      | positive                 | 16                |                                      |
## Ports

| Port name | Direction | Type                    | Description |
| --------- | --------- | ----------------------- | ----------- |
| clk       | in        | sl                      |             |
| din       | in        | slv(WIDTH_G-1 downto 0) |             |
| dout      | out       | slv(WIDTH_G-1 downto 0) |             |
## Signals

| Name  | Type                          | Description |
| ----- | ----------------------------- | ----------- |
| r     | RegType                       |             |
| rin   | RegType                       |             |
| q     | slv(WIDTH_G - 1 downto 0)     |             |
| addra | slv(ADDR_BITS_C - 1 downto 0) |             |
## Constants

| Name        | Type    | Value                                 | Description |
| ----------- | ------- | ------------------------------------- | ----------- |
| DELAY_C     | integer |  DELAY_G - 1                          |             |
| ADDR_BITS_C | integer |  log2(DELAY_C)                        |             |
| REG_INIT_C  | RegType |  (       addr     => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( q, r )
- seq: ( clk )
## Instantiations

- U_RAM_PRIM: surf.SinglePortRamPrimitive
