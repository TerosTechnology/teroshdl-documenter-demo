# Package: csrng_env_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Constants

| Name           | Type                  | Value                                                                           | Description |
| -------------- | --------------------- | ------------------------------------------------------------------------------- | ----------- |
| uint           | uint                  | 1                                                                               | parameters  |
| LIST_OF_ALERTS | string                | {<br><span style="padding-left:20px">"fatal_alert"}                             |             |
| uint           | uint                  | 1                                                                               |             |
| uint           | uint                  | 256                                                                             |             |
| uint           | uint                  | 128                                                                             |             |
| uint           | uint                  | 32                                                                              |             |
| uint           | uint                  | 32                                                                              |             |
| TL_DW          | bit [TL_DW-1:0] [3:0] | {<br><span style="padding-left:20px">32'h0,<br><span style="padding-left:20px"> |             |
## Types

| Name         | Type                                                                                                                                                                                                                                          | Description |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| csrng_intr_e | enum int {<br><span style="padding-left:20px">     CmdReqDone = 0,<br><span style="padding-left:20px">     EntropyReq = 1,<br><span style="padding-left:20px">     HwInstExc  = 2,<br><span style="padding-left:20px">     FifoErr    = 3   } | types       |
