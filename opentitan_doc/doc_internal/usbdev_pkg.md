# Package: usbdev_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name       | Type       | Description |
| ---------- | ---------- | ----------- |
| usbdev_pkg | endpackage |             |
## Types

| Name        | Type                                                                                                                                                                                                                                                                                                                                                | Description |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| awk_state_e | enum logic [2:0] {<br><span style="padding-left:20px">     AwkIdle     = 3'b000,<br><span style="padding-left:20px">     AwkTrigUon  = 3'b011,<br><span style="padding-left:20px">       AwkTrigUoff = 3'b010,<br><span style="padding-left:20px">       AwkWokenUon = 3'b001,<br><span style="padding-left:20px">       AwkWoken    = 3'b100     } |             |
| awk_state_t | awk_state_e                                                                                                                                                                                                                                                                                                                                         |             |
