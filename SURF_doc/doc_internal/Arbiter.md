# Entity: Arbiter

- **File**: Arbiter.vhd
## Diagram

![Diagram](Arbiter.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Example Arbiter Module
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

| Generic name   | Type     | Value | Description                                  |
| -------------- | -------- | ----- | -------------------------------------------- |
| TPD_G          | time     | 1 ns  |                                              |
| RST_POLARITY_G | sl       | '1'   |  '1' for active high rst, '0' for active low |
| RST_ASYNC_G    | boolean  | false |  Reset is asynchronous                       |
| REQ_SIZE_G     | positive | 16    |                                              |
## Ports

| Port name | Direction | Type                                  | Description     |
| --------- | --------- | ------------------------------------- | --------------- |
| clk       | in        | sl                                    |                 |
| rst       | in        | sl                                    |  Optional reset |
| req       | in        | slv(REQ_SIZE_G-1 downto 0)            |                 |
| selected  | out       | slv(bitSize(REQ_SIZE_G-1)-1 downto 0) |                 |
| valid     | out       | sl                                    |                 |
| ack       | out       | slv(REQ_SIZE_G-1 downto 0)            |                 |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name            | Type    | Value                                                                                                                                                  | Description |
| --------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| SELECTED_SIZE_C | integer |  bitSize(REQ_SIZE_G-1)                                                                                                                                 |             |
| REG_RESET_C     | RegType |        (lastSelected => (others => '0'),<br><span style="padding-left:20px"> valid => '0',<br><span style="padding-left:20px"> ack => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( r, req, rst )
- seq: ( clk, rst )
