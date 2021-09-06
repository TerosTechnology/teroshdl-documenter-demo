# Entity: RssiChksum

- **File**: RssiChksum.vhd
## Diagram

![Diagram](RssiChksum.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : RSSI Protocol: https://confluence.slac.stanford.edu/x/1IyfD
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Calculates and checks the RUDP packet checksum.
              Checksum for IP/UDP/TCP/RUDP.
              Works with 64-bit word
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

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| TPD_G        | time     | 1 ns  |             |
| DATA_WIDTH_G | positive | 64    |             |
| CSUM_WIDTH_G | positive | 16    |             |
## Ports

| Port name | Direction | Type                         | Description                                                                                                                                                                                  |
| --------- | --------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| clk_i     | in        | sl                           |                                                                                                                                                                                              |
| rst_i     | in        | sl                           |                                                                                                                                                                                              |
| enable_i  | in        | sl                           | Enables and initializes the calculations.enable_i <= '1' enables the calculation.                 the checksum value holds as long as enabled. enable_i <= '0' initializes the calculation.  |
| strobe_i  | in        | sl                           | Has to indicate valid data and defines the number of calculation clock cycles.                                                                                                               |
| length_i  | in        | positive                     | Length of checksumed data                                                                                                                                                                    |
| init_i    | in        | slv(CSUM_WIDTH_G-1 downto 0) | Initial value of the sumCalculation: init_i = (others=>'0') Validation:  init_i = Checksum value                                                                                             |
| data_i    | in        | slv(DATA_WIDTH_G-1 downto 0) | Fixed to 2 octets (standard specification)                                                                                                                                                   |
| chksum_o  | out       | slv(CSUM_WIDTH_G-1 downto 0) | Direct out 1 c-c delay                                                                                                                                                                       |
| valid_o   | out       | sl                           | Indicates when the module is ready and the checksum is valid                                                                                                                                 |
| check_o   | out       | sl                           | Indicates if the calculated checksum is ok (valid upon valid_o='1')                                                                                                                          |
## Signals

| Name          | Type                         | Description |
| ------------- | ---------------------------- | ----------- |
| r             | RegType                      |             |
| rin           | RegType                      |             |
| s_dataWordSum | slv(CSUM_WIDTH_G+1 downto 0) |             |
## Constants

| Name       | Type     | Value                                                                                                                                                                                                                            | Description |
| ---------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| RATIO_C    | positive |  DATA_WIDTH_G/CSUM_WIDTH_G                                                                                                                                                                                                       |             |
| REG_INIT_C | RegType  |  (       sum      => (others=>'0'),<br><span style="padding-left:20px">       chksum   => (others=>'0'),<br><span style="padding-left:20px">       lenCnt   => 0,<br><span style="padding-left:20px">       valid    => '0'    ) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( r, rst_i, enable_i, init_i, data_i, strobe_i, length_i, s_dataWordSum )
- seq: ( clk_i )
