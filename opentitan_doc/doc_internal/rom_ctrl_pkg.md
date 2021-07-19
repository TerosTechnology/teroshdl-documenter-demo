# Package: rom_ctrl_pkg

- **File**: rom_ctrl_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Constants

| Name          | Type          | Value     | Description |
| ------------- | ------------- | --------- | ----------- |
| AlertFatal    | int           | 0         |             |
| pwrmgr_data_t | pwrmgr_data_t | undefined |             |
## Types

| Name          | Type                                                                                                                                                                             | Description |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| pwrmgr_data_t | struct packed {<br><span style="padding-left:20px">     logic done;<br><span style="padding-left:20px">     logic good;<br><span style="padding-left:20px">   }                  |             |
| keymgr_data_t | struct packed {<br><span style="padding-left:20px">     logic [255:0] data;<br><span style="padding-left:20px">     logic         valid;<br><span style="padding-left:20px">   } |             |
