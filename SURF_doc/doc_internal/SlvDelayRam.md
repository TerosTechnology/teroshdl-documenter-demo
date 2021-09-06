# Entity: SlvDelayRam

- **File**: SlvDelayRam.vhd
## Diagram

![Diagram](SlvDelayRam.svg "Diagram")
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

| Generic name   | Type                       | Value   | Description                                                   |
| -------------- | -------------------------- | ------- | ------------------------------------------------------------- |
| TPD_G          | time                       | 1 ns    |                                                               |
| RST_POLARITY_G | sl                         | '1'     |  '1' for active high rst, '0' for active low                  |
| MEMORY_TYPE_G  | string                     | "block" |                                                               |
| DO_REG_G       | boolean                    | true    |                                                               |
| DELAY_G        | integer range 3 to (2**24) | 3       | max number of clock cycle delays. MAX delay stages when using |
| WIDTH_G        | positive                   | 1       |                                                               |
## Ports

| Port name | Direction | Type                                                  | Description                    |
| --------- | --------- | ----------------------------------------------------- | ------------------------------ |
| clk       | in        | sl                                                    |                                |
| rst       | in        | sl                                                    |                                |
| en        | in        | sl                                                    |  Optional clock enable         |
| maxCount  | in        | slv(log2(DELAY_G - ite(DO_REG_G, 2, 1)) - 1 downto 0) |  Optional runtime configurable |
| din       | in        | slv(WIDTH_G - 1 downto 0)                             |                                |
| dout      | out       | slv(WIDTH_G - 1 downto 0)                             |                                |
## Signals

| Name    | Type                      | Description |
| ------- | ------------------------- | ----------- |
| mem     | mem_type                  |             |
| r       | RegType                   |             |
| rin     | RegType                   |             |
| doutInt | slv(WIDTH_G - 1 downto 0) |             |
## Constants

| Name             | Type                    | Value                                                                                                                                          | Description |
| ---------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| XST_BRAM_STYLE_C | string                  |  MEMORY_TYPE_G                                                                                                                                 |             |
| INIT_C           | slv(WIDTH_G-1 downto 0) |  slvZero(WIDTH_G)                                                                                                                              |             |
| REG_INIT_C       | RegType                 |  (       addr     => 0,<br><span style="padding-left:20px">       maxCount => 0,<br><span style="padding-left:20px">       doutReg  => INIT_C) |             |
## Types

| Name     | Type | Description |
| -------- | ---- | ----------- |
| mem_type |      |             |
| RegType  |      |             |
## Processes
- comb: ( en, maxCount, doutInt, rst, r )
- seq: ( clk )
- MEM_PROC: ( clk, rst )
**Description**
 read before write single port RAM 
