# Package: pwrmgr_env_pkg

- **File**: pwrmgr_env_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0


## Constants

| Name           | Type   | Value                                               | Description          |
| -------------- | ------ | --------------------------------------------------- | -------------------- |
| uint           | uint   | 1                                                   |  parameters  alerts  |
| LIST_OF_ALERTS | string | {<br><span style="padding-left:20px">"fatal_fault"} |                      |
## Types

| Name          | Type                                                                                                                                                                                                                                                                                                                                                               | Description |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| clk_enables_t | struct packed {<br><span style="padding-left:20px">     logic core_clk_en;<br><span style="padding-left:20px">     logic io_clk_en;<br><span style="padding-left:20px">     logic usb_clk_en_lp;<br><span style="padding-left:20px">     logic usb_clk_en_active;<br><span style="padding-left:20px">     logic main_pd_n;<br><span style="padding-left:20px">   } |  types      |
