# Package: jtag_pkg

- **File**: jtag_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0



## Signals

| Name     | Type       | Description |
| -------- | ---------- | ----------- |
| jtag_pkg | endpackage |             |
## Constants

| Name       | Type       | Value | Description |
| ---------- | ---------- | ----- | ----------- |
| jtag_req_t | jtag_req_t | '0    |             |
| jtag_rsp_t | jtag_rsp_t | '0    |             |
## Types

| Name       | Type                                                                                                                                                                                                                                                                   | Description |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| jtag_req_t | struct packed {<br><span style="padding-left:20px">     logic tck;<br><span style="padding-left:20px">     logic tms;<br><span style="padding-left:20px">     logic trst_n;<br><span style="padding-left:20px">     logic tdi;<br><span style="padding-left:20px">   } |             |
| jtag_rsp_t | struct packed {<br><span style="padding-left:20px">     logic tdo;<br><span style="padding-left:20px">     logic tdo_oe;<br><span style="padding-left:20px">   }                                                                                                       |             |
