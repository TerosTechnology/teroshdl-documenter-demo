# Entity: GtpRxCommaAligner

- **File**: GtpRxCommaAligner.vhd
## Diagram

![Diagram](GtpRxCommaAligner.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Pgp2 Gtp Word aligner
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name       | Direction | Type                          | Description              |
| --------------- | --------- | ----------------------------- | ------------------------ |
| gtpRxUsrClk2    | in        | std_logic                     |                          |
| gtpRxUsrClk2Rst | in        | std_logic                     |                          |
| gtpRxData       | in        | std_logic_vector(19 downto 0) |                          |
| codeErr         | in        | std_logic_vector(1 downto 0)  |                          |
| dispErr         | in        | std_logic_vector(1 downto 0)  |                          |
| gtpRxUsrClk2Sel | out       | std_logic                     |  Select phase of usrclk2 |
| gtpRxSlide      | out       | std_logic                     |                          |
| gtpRxCdrReset   | out       | std_logic                     |                          |
| aligned         | out       | std_logic                     |                          |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
|  rin | RegType |             |
## Constants

| Name        | Type                         | Value         | Description |
| ----------- | ---------------------------- | ------------- | ----------- |
| RAW_COMMA_C | std_logic_vector(9 downto 0) |  "0101111100" |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                                            | Description |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | (SEARCH_S,<br><span style="padding-left:20px"> RESET_S,<br><span style="padding-left:20px"> SLIDE_S,<br><span style="padding-left:20px"> SLIDE_WAIT_0_S,<br><span style="padding-left:20px"> SLIDE_WAIT_1_S,<br><span style="padding-left:20px"> WAIT_SETTLE_S,<br><span style="padding-left:20px"> ALIGNED_S)  |             |
| RegType   |                                                                                                                                                                                                                                                                                                                 |             |
## Processes
- seq: ( gtpRxUsrClk2, gtpRxUsrClk2Rst )
- comb: ( r, gtpRxData, codeErr, dispErr )
