# Package: usbdev_env_pkg

- **File**: usbdev_env_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Constants

| Name           | Type   | Value                                               | Description        |
| -------------- | ------ | --------------------------------------------------- | ------------------ |
| uint           | uint   | 1                                                   | parameters alerts  |
| LIST_OF_ALERTS | string | {<br><span style="padding-left:20px">"fatal_fault"} |                    |
## Types

| Name          | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| usbdev_intr_e | enum {<br><span style="padding-left:20px">     IntrPktReceived = 0,<br><span style="padding-left:20px">     IntrPktSent = 1,<br><span style="padding-left:20px">     IntrDisconnected = 2,<br><span style="padding-left:20px">     IntrHostLost = 3,<br><span style="padding-left:20px">     IntrLinkReset = 4,<br><span style="padding-left:20px">     IntrLinkSuspend = 5,<br><span style="padding-left:20px">     IntrLinkResume = 6,<br><span style="padding-left:20px">     IntrAvEmpty = 7,<br><span style="padding-left:20px">     IntrRxFull = 8,<br><span style="padding-left:20px">     IntrAvOverflow = 9,<br><span style="padding-left:20px">     IntrLinkInErr = 10,<br><span style="padding-left:20px">     IntrRxCrcErr = 11,<br><span style="padding-left:20px">     IntrRxPidErr = 12,<br><span style="padding-left:20px">     IntrRxBitstuffErr = 13,<br><span style="padding-left:20px">     IntrFrame = 14,<br><span style="padding-left:20px">     IntrConnected = 15,<br><span style="padding-left:20px">     NumUsbdevInterrupts   } | types       |
