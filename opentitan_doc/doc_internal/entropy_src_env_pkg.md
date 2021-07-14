# Package: entropy_src_env_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Constants

| Name           | Type                  | Value                                                                                                 | Description |
| -------------- | --------------------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| TL_DW          | bit [11:0][TL_DW-1:0] | {<br><span style="padding-left:20px">32'h4836cb5a,<br><span style="padding-left:20px">                | parameters  |
| LIST_OF_ALERTS | string                | {<br><span style="padding-left:20px">"recov_alert",<br><span style="padding-left:20px">"fatal_alert"} |             |
| uint           | uint                  | 2                                                                                                     |             |
## Types

| Name               | Type                                                                                                                                                                                                                                                                  | Description |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| entropy_src_intr_e | enum int {<br><span style="padding-left:20px">     EntropyValid     = 0,<br><span style="padding-left:20px">     HealthTestFailed = 1,<br><span style="padding-left:20px">     ObserveFifoReady = 2,<br><span style="padding-left:20px">     FifoErr          = 3   } | types       |
| mode_e             | enum int {<br><span style="padding-left:20px">     Disabled  = 0,<br><span style="padding-left:20px">     PtrngMode = 1,<br><span style="padding-left:20px">     LfsrMode  = 2   }                                                                                    |             |
