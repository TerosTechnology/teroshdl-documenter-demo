# Entity: CRC32Rtl

## Diagram

![Diagram](CRC32Rtl.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
VHDL source file for CRC32 calculation to replace macro of Virtex5 in Virtex6 and Spartan6.
assuming clock positive edge, reset positive edge, LSB first, data width is 32,
polynomial CRC32 IEEE802.3 type X32+X26+X23+x22+x16+X12+X11+X10+X8+X7+X5+X4+X2+X1+1
with CRCRESETial value of 0xffffffff
similar equation can be derived from
http://www.xilinx.com/support/documentation/application_notes/xapp209.pdf
and related app notes
http://www.xilinx.com/support/documentation/application_notes/xapp562.pdf
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type             | Value       | Description |
| ------------ | ---------------- | ----------- | ----------- |
| CRC_INIT     | slv(31 downto 0) | x"FFFFFFFF" |             |
## Ports

| Port name    | Direction | Type             | Description                                              |
| ------------ | --------- | ---------------- | -------------------------------------------------------- |
| CRCOUT       | out       | slv(31 downto 0) | CRC output                                               |
| CRCCLK       | in        | sl               | system clock                                             |
| CRCCLKEN     | in        | sl               | system clock enable                                      |
| CRCDATAVALID | in        | sl               | indicate that new data arrived and CRC can be computed   |
| CRCDATAWIDTH | in        | slv(2 downto 0)  | indicate width in bytes minus 1, 0 - 1 byte, 1 - 2 bytes |
| CRCIN        | in        | slv(31 downto 0) | input data for CRC calculation                           |
| CRCINIT      | in        | slv(31 downto 0) |                                                          |
| CRCRESET     | in        | sl               |                                                          |
## Signals

| Name           | Type             | Description |
| -------------- | ---------------- | ----------- |
| data           | slv(31 downto 0) |             |
| crc            | slv(31 downto 0) |             |
| CRCDATAVALID_d | sl               |             |
| CRCDATAWIDTH_d | slv(2 downto 0)  |             |
| MSBVect        | fb_array         |             |
|  TempXOR       | fb_array         |             |
## Constants

| Name    | Type             | Value        | Description                   |
| ------- | ---------------- | ------------ | ----------------------------- |
| Polyval | slv(31 downto 0) |  X"04C11DB7" |                               |
| tpd     | time             |  0.5 ns      | Register delay for simulation |
## Types

| Name     | Type | Description |
| -------- | ---- | ----------- |
| fb_array |      |             |
## Processes
- unnamed: ( CRCCLK, CRCCLKEN )
- CRCP: ( CRCCLK )
