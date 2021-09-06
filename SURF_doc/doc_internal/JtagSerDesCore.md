# Entity: JtagSerDesCore

- **File**: JtagSerDesCore.vhd
## Diagram

![Diagram](JtagSerDesCore.svg "Diagram")
## Description

 Title      : JTAG Support
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: JTAG serializer/deserializer with parallel word interface
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
 Serialize a TMS/TDI word pair into JTAG signals and deserialize
 TDO into a paralle output word.
## Generics

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| TPD_G        | time     | 1 ns  |             |
| WIDTH_G      | positive | 32    |             |
| CLK_DIV2_G   | positive | 8     |             |
## Ports

| Port name    | Direction | Type                           | Description |
| ------------ | --------- | ------------------------------ | ----------- |
| clk          | in        | sl                             |             |
| rst          | in        | sl                             |             |
| numBits      | in        | natural range 0 to WIDTH_G - 1 |             |
| dataInTms    | in        | slv(WIDTH_G - 1 downto 0)      |             |
| dataInTdi    | in        | slv(WIDTH_G - 1 downto 0)      |             |
| dataInValid  | in        | sl                             |             |
| dataInReady  | out       | sl                             |             |
| dataOut      | out       | slv(WIDTH_G - 1 downto 0)      |             |
| dataOutValid | out       | sl                             |             |
| dataOutReady | in        | sl                             |             |
| tck          | out       | sl                             |             |
| tdi          | out       | sl                             |             |
| tms          | out       | sl                             |             |
| tdo          | in        | sl                             |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| REG_INIT_C | RegType |  (       cnt     => -1,<br><span style="padding-left:20px">       div     => 0,<br><span style="padding-left:20px">       tms     => (others => '0'),<br><span style="padding-left:20px">       tdi     => (others => '0'),<br><span style="padding-left:20px">       tdo     => (others => '0'),<br><span style="padding-left:20px">       tck     => '0',<br><span style="padding-left:20px">       lastBit => false,<br><span style="padding-left:20px">       oValid  => '0',<br><span style="padding-left:20px">       iReady  => '1',<br><span style="padding-left:20px">       state   => IDLE_S    ) |             |
## Types

| Name      | Type                                                                                              | Description |
| --------- | ------------------------------------------------------------------------------------------------- | ----------- |
| StateType | (IDLE_S,<br><span style="padding-left:20px"> SHIFT_S,<br><span style="padding-left:20px"> WAI_S)  |             |
| RegType   |                                                                                                   |             |
## Processes
- P_COMB: ( r, numBits,  dataInTms, dataInTdi, dataInValid, dataOutReady, tdo )
- P_SEQ: ( clk )
