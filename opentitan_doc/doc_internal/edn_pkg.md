# Package: edn_pkg

- **File**: edn_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0



## Signals

| Name    | Type       | Description |
| ------- | ---------- | ----------- |
| edn_pkg | endpackage |             |
## Constants

| Name                    | Type         | Value | Description                     |
| ----------------------- | ------------ | ----- | ------------------------------- |
| ENDPOINT_BUS_WIDTH      | int unsigned | 32    |                                 |
| FIPS_ENDPOINT_BUS_WIDTH | int unsigned |       |                                 |
| edn_req_t               | edn_req_t    | '0    |                                 |
| edn_rsp_t               | edn_rsp_t    | '0    |                                 |
| EDN_MODE_WIDTH          | int          | 4     |  Sparse four-value signal type  |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                                                          | Description             |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| edn_req_t | struct packed {<br><span style="padding-left:20px">     logic                                 edn_req;<br><span style="padding-left:20px">   }                                                                                                                                                                                |  EDN request interface  |
| edn_rsp_t | struct packed {<br><span style="padding-left:20px">     logic                                 edn_ack;<br><span style="padding-left:20px">     logic                                 edn_fips;<br><span style="padding-left:20px">     logic [ENDPOINT_BUS_WIDTH-1:0]        edn_bus;<br><span style="padding-left:20px">   } |                         |
| edn_enb_e | enum logic [EDN_MODE_WIDTH-1:0] {<br><span style="padding-left:20px">     EDN_FIELD_ON = 4'b1010   }                                                                                                                                                                                                                          |                         |
