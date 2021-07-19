# Entity: Crc32Parallel

- **File**: Crc32Parallel.vhd
## Diagram

![Diagram](Crc32Parallel.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
This is an implementation of an 1-to-8-byte input CRC32 calculation.
The polynomial is fixed to 0x04C11DB7, the "standard CRC32 polynomial."
The initialization value is configurable, but defaults to 0xFFFFFFFF.
This implementation is direct, so no bytes need to be appended to the data.
Bytes are reversed on input before being used for the CRC calculation,
and the CRC register is reversed on output just before a final XOR with
0xFFFFFFFF.
This version utilizes parallel CRC calculations, and as a result generally
should meet much tighter timing constraints and run at higher frequencies.
(relative to Crc32.vhd and CRC32Rtl.vhd).
With a data input size of 4 bytes, this module is compatible with the
previous CRC32Rtl.vhdl module in the StdLib.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name     | Type             | Value       | Description |
| ---------------- | ---------------- | ----------- | ----------- |
| TPD_G            | time             | 1 ns        |             |
| BYTE_WIDTH_G     | positive         | 4           |             |
| INPUT_REGISTER_G | boolean          | true        |             |
| CRC_INIT_G       | slv(31 downto 0) | x"FFFFFFFF" |             |
## Ports

| Port name    | Direction | Type                             | Description                                                                |
| ------------ | --------- | -------------------------------- | -------------------------------------------------------------------------- |
| crcOut       | out       | slv(31 downto 0)                 | CRC output                                                                 |
| crcRem       | out       | slv(31 downto 0)                 | CRC interim remainder                                                      |
| crcClk       | in        | sl                               | system clock                                                               |
| crcDataValid | in        | sl                               | indicate that new data arrived and CRC can be computed                     |
| crcDataWidth | in        | slv(2 downto 0)                  | indicate width in bytes minus 1, 0 - 1 byte, 1 - 2 bytes ... , 7 - 8 bytes |
| crcIn        | in        | slv((BYTE_WIDTH_G*8-1) downto 0) | input data for CRC calculation                                             |
| crcInit      | in        | slv(31 downto 0)                 | optional override of CRC_INIT_G                                            |
| crcReset     | in        | sl                               |                                                                            |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                     | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       crc       => CRC_INIT_G,<br><span style="padding-left:20px">       data      => (others => '0'),<br><span style="padding-left:20px">       valid     => '0',<br><span style="padding-left:20px">       reset     => '0',<br><span style="padding-left:20px">       byteWidth => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( crcDataValid, crcDataWidth, crcIn, crcInit, crcReset, r )
- seq: ( crcClk )
