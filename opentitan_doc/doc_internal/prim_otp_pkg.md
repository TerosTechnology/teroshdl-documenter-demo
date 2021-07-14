# Package: prim_otp_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Common interface definitions for OTP primitives.
 

## Signals

| Name         | Type       | Description |
| ------------ | ---------- | ----------- |
| prim_otp_pkg | endpackage |             |
## Constants

| Name     | Type | Value | Description |
| -------- | ---- | ----- | ----------- |
| CmdWidth | int  | 2     |             |
| ErrWidth | int  | 3     |             |
## Types

| Name  | Type                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| cmd_e | enum logic [CmdWidth-1:0] {<br><span style="padding-left:20px">     Read  = 2'b00,<br><span style="padding-left:20px">     Write = 2'b01,<br><span style="padding-left:20px">     Init  = 2'b11   }                                                                                                                                                                                     |             |
| err_e | enum logic [ErrWidth-1:0] {<br><span style="padding-left:20px">     NoError              = 3'h0,<br><span style="padding-left:20px">     MacroError           = 3'h1,<br><span style="padding-left:20px">     MacroEccCorrError    = 3'h2,<br><span style="padding-left:20px">     MacroEccUncorrError  = 3'h3,<br><span style="padding-left:20px">     MacroWriteBlankError = 3'h4   } |             |
