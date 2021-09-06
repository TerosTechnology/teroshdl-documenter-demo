# Package: prim_ram_1p_pkg

- **File**: prim_ram_1p_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0



## Constants

| Name         | Type         | Value | Description |
| ------------ | ------------ | ----- | ----------- |
| ram_1p_cfg_t | ram_1p_cfg_t | '0    |             |
## Types

| Name         | Type                                                                                                                                                                         | Description |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| cfg_t        | struct packed {<br><span style="padding-left:20px">     logic       cfg_en;<br><span style="padding-left:20px">     logic [3:0] cfg;<br><span style="padding-left:20px">   } |             |
| ram_1p_cfg_t | struct packed {<br><span style="padding-left:20px">     cfg_t ram_cfg;<br><span style="padding-left:20px">       cfg_t rf_cfg;<br><span style="padding-left:20px">      }    |             |
