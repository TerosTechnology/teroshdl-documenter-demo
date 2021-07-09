# Entity: EthCrc32Parallel

## Diagram

![Diagram](EthCrc32Parallel.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Ethernet CRC32 Ethernet/AAL5 Module
Polynomial: x^32 + x^26 + x^23 + x^22 + x^16 + x^12 + x^11 + x^10 + x^8 + x^7 + x^5 + x^4 + x^2 + x^1 + 1
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type                   | Value       | Description            |
| ------------ | ---------------------- | ----------- | ---------------------- |
| TPD_G        | time                   | 1 ns        |                        |
| USE_DSP_G    | boolean                | false       | true is not tested yet |
| CRC_INIT_G   | slv(31 downto 0)       | x"FFFFFFFF" |                        |
| BYTE_WIDTH_G | positive range 1 to 16 | 16          |                        |
## Ports

| Port name    | Direction | Type                             | Description                                                               |
| ------------ | --------- | -------------------------------- | ------------------------------------------------------------------------- |
| crcClk       | in        | sl                               |                                                                           |
| crcReset     | in        | sl                               |                                                                           |
| crcDataValid | in        | sl                               |                                                                           |
| crcDataWidth | in        | slv(3 downto 0)                  | # of bytes minus 1 (example: 0 - 1 byte, 1 - 2 bytes ... , 15 - 16 bytes) |
| crcIn        | in        | slv((BYTE_WIDTH_G*8-1) downto 0) |                                                                           |
| crcOut       | out       | slv(31 downto 0)                 |                                                                           |
## Signals

| Name   | Type                     | Description |
| ------ | ------------------------ | ----------- |
| r      | RegType                  |             |
| rin    | RegType                  |             |
| dspInA | Slv96Array(31 downto 0)  |             |
| dspInB | Slv192Array(31 downto 0) |             |
| dspOut | slv(31 downto 0)         |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                         | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       valid     => '0',<br><span style="padding-left:20px">       byteWidth => (others => '0'),<br><span style="padding-left:20px">       data      => (others => '0'),<br><span style="padding-left:20px">       crc       => CRC_INIT_G) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( crcDataValid, crcDataWidth, crcIn, crcReset, dspOut, r )
- seq: ( crcClk )
