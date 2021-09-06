# Package: prim_subreg_pkg

- **File**: prim_subreg_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0


## Types

| Name        | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| sw_access_e | enum logic [2:0] {<br><span style="padding-left:20px">     SwAccessRW  = 3'd0,<br><span style="padding-left:20px">      SwAccessRO  = 3'd1,<br><span style="padding-left:20px">      SwAccessWO  = 3'd2,<br><span style="padding-left:20px">      SwAccessW1C = 3'd3,<br><span style="padding-left:20px">      SwAccessW1S = 3'd4,<br><span style="padding-left:20px">      SwAccessW0C = 3'd5,<br><span style="padding-left:20px">      SwAccessRC  = 3'd6     } |             |
