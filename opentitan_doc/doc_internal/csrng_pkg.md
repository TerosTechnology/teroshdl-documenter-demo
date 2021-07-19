# Package: csrng_pkg

- **File**: csrng_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name      | Type       | Description |
| --------- | ---------- | ----------- |
| csrng_pkg | endpackage |             |
## Constants

| Name                   | Type         | Value     | Description |
| ---------------------- | ------------ | --------- | ----------- |
| GENBITS_BUS_WIDTH      | int unsigned | 128       |             |
| CSRNG_CMD_WIDTH        | int unsigned | 32        |             |
| FIPS_GENBITS_BUS_WIDTH | int unsigned |           |             |
| csrng_req_t            | csrng_req_t  | undefined |             |
| csrng_rsp_t            | csrng_rsp_t  | undefined |             |
| CsKeymgrDivWidth       | int          | 384       |             |
## Types

| Name            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description              |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| csrng_req_t     | struct packed {<br><span style="padding-left:20px">     logic         csrng_req_valid;<br><span style="padding-left:20px">     logic [CSRNG_CMD_WIDTH-1:0]  csrng_req_bus;<br><span style="padding-left:20px">     logic         genbits_ready;<br><span style="padding-left:20px">   }                                                                                                                                                                                                              | instantiation interface  |
| csrng_rsp_t     | struct packed {<br><span style="padding-left:20px">     logic         csrng_req_ready;<br><span style="padding-left:20px">     logic         csrng_rsp_ack;<br><span style="padding-left:20px">     logic         csrng_rsp_sts;<br><span style="padding-left:20px">     logic         genbits_valid;<br><span style="padding-left:20px">     logic         genbits_fips;<br><span style="padding-left:20px">     logic [GENBITS_BUS_WIDTH-1:0] genbits_bus;<br><span style="padding-left:20px">   } |                          |
| acmd_e          | enum logic [2:0] {<br><span style="padding-left:20px">     INV = 3'h0,<br><span style="padding-left:20px">     INS = 3'h1,<br><span style="padding-left:20px">     RES = 3'h2,<br><span style="padding-left:20px">     GEN = 3'h3,<br><span style="padding-left:20px">     UPD = 3'h4,<br><span style="padding-left:20px">     UNI = 3'h5,<br><span style="padding-left:20px">     GENB = 3'h6,<br><span style="padding-left:20px">     GENU = 3'h7   }                                              |                          |
| cs_keymgr_div_t | logic [CsKeymgrDivWidth-1:0]                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                          |
