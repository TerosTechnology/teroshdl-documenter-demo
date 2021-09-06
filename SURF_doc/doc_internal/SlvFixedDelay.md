# Entity: SlvFixedDelay

- **File**: SlvFixedDelay.vhd
## Diagram

![Diagram](SlvFixedDelay.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Shift Register Delay module for std_logic_vector
              Uses a counter and single port RAM (distributed, block, ultra)
              Single port RAM setup in read first mode
              Counter counts 0...maxCount
              Optional data out register (DO_REG_G) on the RAM

              delay = maxCount + ite(DO_REG_G, 3, 2)
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

| Generic name  | Type     | Value             | Description                                                   |
| ------------- | -------- | ----------------- | ------------------------------------------------------------- |
| TPD_G         | time     | 1 ns              |                                                               |
| XIL_DEVICE_G  | string   | "ULTRASCALE_PLUS" |                                                               |
| DELAY_STYLE_G | string   | "srl_reg"         |  "reg", "srl", "srl_reg", "reg_srl", "reg_srl_reg" or "block" |
| DELAY_G       | integer  | 256               |                                                               |
| WIDTH_G       | positive | 16                |                                                               |
## Ports

| Port name | Direction | Type                      | Description |
| --------- | --------- | ------------------------- | ----------- |
| clk       | in        | sl                        |             |
| din       | in        | slv(WIDTH_G - 1 downto 0) |             |
| dout      | out       | slv(WIDTH_G - 1 downto 0) |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                          | Description |
| ---------- | ------- | ---------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       shift => (others => (others => '0'))) |             |
## Types

| Name        | Type | Description |
| ----------- | ---- | ----------- |
| VectorArray |      |             |
| RegType     |      |             |
