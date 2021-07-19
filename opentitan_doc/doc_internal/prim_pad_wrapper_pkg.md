# Package: prim_pad_wrapper_pkg

- **File**: prim_pad_wrapper_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name                 | Type       | Description |
| -------------------- | ---------- | ----------- |
| prim_pad_wrapper_pkg | endpackage |             |
## Constants

| Name       | Type | Value             | Description                           |
| ---------- | ---- | ----------------- | ------------------------------------- |
| DriveStrDw | int  | 4                 | Pad attributes                        |
| SlewRateDw | int  | 2                 |                                       |
| AttrDw     | int  | $bits(pad_attr_t) |                                       |
| PokDw      | int  | 8                 | Power OK signals (library dependent)  |
## Types

| Name        | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| pad_type_e  | enum logic [2:0] {<br><span style="padding-left:20px">     BidirStd = 3'h0,<br><span style="padding-left:20px">       BidirTol = 3'h1,<br><span style="padding-left:20px">       BidirOd = 3'h2,<br><span style="padding-left:20px">        InputStd = 3'h3,<br><span style="padding-left:20px">       AnalogIn0 = 3'h4,<br><span style="padding-left:20px">      AnalogIn1 = 3'h5     }                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| scan_role_e | enum logic [1:0] {<br><span style="padding-left:20px">     NoScan = 2'h0,<br><span style="padding-left:20px">     ScanIn = 2'h1,<br><span style="padding-left:20px">     ScanOut = 2'h2   }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |             |
| pad_attr_t  | struct packed {<br><span style="padding-left:20px">     logic [DriveStrDw-1:0] drive_strength;<br><span style="padding-left:20px">      logic [SlewRateDw-1:0] slew_rate;<br><span style="padding-left:20px">           logic od_en;<br><span style="padding-left:20px">                                logic schmitt_en;<br><span style="padding-left:20px">                           logic keep_en;<br><span style="padding-left:20px">                              logic pull_select;<br><span style="padding-left:20px">                          logic pull_en;<br><span style="padding-left:20px">                              logic virt_od_en;<br><span style="padding-left:20px">                           logic invert;<br><span style="padding-left:20px">                             } |             |
| pad_pok_t   | logic [PokDw-1:0]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |             |
