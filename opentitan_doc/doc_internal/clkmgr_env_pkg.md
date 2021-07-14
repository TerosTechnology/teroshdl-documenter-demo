# Package: clkmgr_env_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Constants

| Name           | Type   | Value                                               | Description |
| -------------- | ------ | --------------------------------------------------- | ----------- |
| NUM_PERI       | int    | 4                                                   | parameters  |
| NUM_TRANS      | int    | 4                                                   |             |
| uint           | uint   | 1                                                   | alerts      |
| LIST_OF_ALERTS | string | {<br><span style="padding-left:20px">"fatal_fault"} |             |
## Types

| Name        | Type                                                                                                                                                                                                 | Description                                                       |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| clkmgr_vif  | virtual clkmgr_if                                                                                                                                                                                    |                                                                   |
| clk_rst_vif | virtual clk_rst_if                                                                                                                                                                                   |                                                                   |
| peri_e      | enum int {<br><span style="padding-left:20px">PeriDiv4,<br><span style="padding-left:20px"> PeriDiv2,<br><span style="padding-left:20px"> PeriIo,<br><span style="padding-left:20px"> PeriUsb}       | types The enum values for these match the bit order in the CSRs.  |
| trans_e     | enum int {<br><span style="padding-left:20px">TransAes,<br><span style="padding-left:20px"> TransHmac,<br><span style="padding-left:20px"> TransKmac,<br><span style="padding-left:20px"> TransOtbn} |                                                                   |
