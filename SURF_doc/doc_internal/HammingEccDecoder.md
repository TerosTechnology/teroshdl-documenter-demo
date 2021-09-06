# Entity: HammingEccDecoder

- **File**: HammingEccDecoder.vhd
## Diagram

![Diagram](HammingEccDecoder.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : Hamming-ECC: https://en.wikipedia.org/wiki/Hamming_code
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Hamming-ECC Decoder Module
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

| Generic name   | Type     | Value | Description |
| -------------- | -------- | ----- | ----------- |
| TPD_G          | time     | 1 ns  |             |
| RST_POLARITY_G | sl       | '1'   |             |
| RST_ASYNC_G    | boolean  | false |             |
| FLOW_CTRL_EN_G | boolean  | false |             |
| DATA_WIDTH_G   | positive | 8     |             |
## Ports

| Port name | Direction | Type                                            | Description                          |
| --------- | --------- | ----------------------------------------------- | ------------------------------------ |
| clk       | in        | sl                                              | Clock and Reset                      |
| clkEn     | in        | sl                                              |  Optional Clock Enable               |
| rst       | in        | sl                                              |  Optional Reset                      |
| ibValid   | in        | sl                                              | Inbound Interface                    |
| ibReady   | out       | sl                                              |                                      |
| ibData    | in        | slv(hammingEccDataWidth(DATA_WIDTH_G) downto 0) |  +1 for the "extended parity bit"    |
| obValid   | out       | sl                                              | Outbound Interface                   |
| obReady   | in        | sl                                              |                                      |
| obData    | out       | slv(DATA_WIDTH_G-1 downto 0)                    |                                      |
| obErrSbit | out       | sl                                              |  Only 1 bit error that was corrected |
| obErrDbit | out       | sl                                              |                                      |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name            | Type     | Value                                                                                                                                                                                                                                                                                  | Description |
| --------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| IB_DATA_WIDTH_C | positive |  hammingEccDataWidth(DATA_WIDTH_G)                                                                                                                                                                                                                                                     |             |
| REG_INIT_C      | RegType  |  (       ibReady   => '0',<br><span style="padding-left:20px">       obValid   => '0',<br><span style="padding-left:20px">       obData    => (others => '0'),<br><span style="padding-left:20px">       obErrSbit => '0',<br><span style="padding-left:20px">       obErrDbit => '0') |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( ibData, ibValid, obReady, r, rst )
- seq: ( clk, rst )
