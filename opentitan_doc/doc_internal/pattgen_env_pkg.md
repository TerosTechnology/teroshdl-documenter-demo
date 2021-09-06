# Package: pattgen_env_pkg

- **File**: pattgen_env_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0


## Signals

| Name            | Type       | Description |
| --------------- | ---------- | ----------- |
| pattgen_env_pkg | endpackage |             |
## Constants

| Name           | Type   | Value                                               | Description |
| -------------- | ------ | --------------------------------------------------- | ----------- |
| uint           | uint   | 1                                                   |  alerts     |
| LIST_OF_ALERTS | string | {<br><span style="padding-left:20px">"fatal_fault"} |             |
## Types

| Name             | Type                                                                                                                                                                                                                                                                       | Description  |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| pattgen_intr_e   | enum int {<br><span style="padding-left:20px">     DoneCh0        = 0,<br><span style="padding-left:20px">     DoneCh1        = 1,<br><span style="padding-left:20px">     NumPattgenIntr = 2   }                                                                          |  parameters  |
| channel_select_e | enum bit[1:0] {<br><span style="padding-left:20px">     NoChannels   = 2'b00,<br><span style="padding-left:20px">     Channel0     = 2'b01,<br><span style="padding-left:20px">     Channel1     = 2'b10,<br><span style="padding-left:20px">     AllChannels  = 2'b11   } |              |
| channel_status_e | enum bit {<br><span style="padding-left:20px">     Enable      = 1'b1,<br><span style="padding-left:20px">     Disable     = 1'b0   }                                                                                                                                      |              |
