# Package: edn_env_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Constants

| Name           | Type   | Value                                               | Description |
| -------------- | ------ | --------------------------------------------------- | ----------- |
| uint           | uint   | 1                                                   | parameters  |
| LIST_OF_ALERTS | string | {<br><span style="padding-left:20px">"fatal_alert"} |             |
| uint           | uint   | 1                                                   |             |
## Types

| Name          | Type                                                                                                                            | Description |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| edn_intr_e    | enum int {<br><span style="padding-left:20px">     CmdReqDone = 0,<br><span style="padding-left:20px">     FifoErr    = 1   }   | types       |
| hw_req_mode_e | enum int {<br><span style="padding-left:20px">     AutoReqMode = 1,<br><span style="padding-left:20px">     BootReqMode = 2   } |             |
