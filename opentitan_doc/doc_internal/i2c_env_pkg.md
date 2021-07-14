# Package: i2c_env_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name        | Type       | Description |
| ----------- | ---------- | ----------- |
| i2c_env_pkg | endpackage |             |
## Constants

| Name           | Type   | Value                                               | Description |
| -------------- | ------ | --------------------------------------------------- | ----------- |
| uint           | uint   | i2c_reg_pkg::FifoDepth                              |             |
| uint           | uint   | i2c_reg_pkg::FifoDepth                              |             |
| uint           | uint   | i2c_reg_pkg::FifoDepth                              |             |
| uint           | uint   | i2c_reg_pkg::FifoDepth                              |             |
| uint           | uint   | 1                                                   | alerts      |
| LIST_OF_ALERTS | string | {<br><span style="padding-left:20px">"fatal_fault"} |             |
## Types

| Name        | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| i2c_intr_e  | enum int {<br><span style="padding-left:20px">     FmtWatermark   = 0,<br><span style="padding-left:20px">     RxWatermark    = 1,<br><span style="padding-left:20px">     FmtOverflow    = 2,<br><span style="padding-left:20px">     RxOverflow     = 3,<br><span style="padding-left:20px">     Nak            = 4,<br><span style="padding-left:20px">     SclInference   = 5,<br><span style="padding-left:20px">     SdaInference   = 6,<br><span style="padding-left:20px">     StretchTimeout = 7,<br><span style="padding-left:20px">     SdaUnstable    = 8,<br><span style="padding-left:20px">     TransComplete  = 9,<br><span style="padding-left:20px">     TxEmpty        = 10,<br><span style="padding-left:20px">     TxNonEmpty     = 11,<br><span style="padding-left:20px">     TxOverflow     = 12,<br><span style="padding-left:20px">     AcqOverflow    = 13,<br><span style="padding-left:20px">     AckStop        = 14,<br><span style="padding-left:20px">     HostTimeout    = 15,<br><span style="padding-left:20px">     NumI2cIntr     = 16   } | parameters  |
| tran_type_e | enum int {<br><span style="padding-left:20px">     ReadOnly  = 0,<br><span style="padding-left:20px">     WriteOnly = 1,<br><span style="padding-left:20px">     ReadWrite = 2   }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
