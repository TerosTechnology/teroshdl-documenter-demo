# Entity: FirFilterTap

## Diagram

![Diagram](FirFilterTap.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Using Transpose Multiply-Accumulate for FIR engine stage
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| TPD_G        | time     | 1 ns  |             |
| WIDTH_G      | positive | 12    |             |
## Ports

| Port name | Direction | Type                    | Description                        |
| --------- | --------- | ----------------------- | ---------------------------------- |
| clk       | in        | sl                      | Clock Only (Infer into DSP)        |
| datain    | in        | slv(WIDTH_G-1 downto 0) | Data and tap coefficient Interface |
| coeffin   | in        | slv(WIDTH_G-1 downto 0) |                                    |
| cascin    | in        | slv(2*WIDTH_G downto 0) | Cascade Interface                  |
| cascout   | out       | slv(2*WIDTH_G downto 0) |                                    |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                              | Description |
| ---------- | ------- | ---------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       accum => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( cascin, coeffin, datain, r )
- seq: ( clk )
