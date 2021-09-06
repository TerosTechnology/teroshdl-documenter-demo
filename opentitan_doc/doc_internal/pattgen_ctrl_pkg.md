# Package: pattgen_ctrl_pkg

- **File**: pattgen_ctrl_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0


## Signals

| Name             | Type       | Description |
| ---------------- | ---------- | ----------- |
| pattgen_ctrl_pkg | endpackage |             |
## Types

| Name                | Type                                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| pattgen_chan_ctrl_t | struct packed {<br><span style="padding-left:20px">     logic        enable;<br><span style="padding-left:20px">     logic        polarity;<br><span style="padding-left:20px">     logic [31:0] prediv;<br><span style="padding-left:20px">     logic [63:0] data;<br><span style="padding-left:20px">     logic [5:0]  len;<br><span style="padding-left:20px">     logic [9:0]  reps;<br><span style="padding-left:20px">   } |             |
