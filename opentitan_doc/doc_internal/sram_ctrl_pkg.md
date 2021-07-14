# Package: sram_ctrl_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name          | Type       | Description |
| ------------- | ---------- | ----------- |
| sram_ctrl_pkg | endpackage |             |
## Constants

| Name         | Type                       | Value                                         | Description                                                                  |
| ------------ | -------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------- |
| Width        | int                        | 32                                            |                                                                              |
| AddrWidth    | int                        | 32                                            | This is later on pruned to the correct width at the SRAM wrapper interface.  |
| RandInitSeed | int                        | 32                                            |                                                                              |
| NonceWidth   | int                        | 64                                            |                                                                              |
| otp_ctrl_pkg | otp_ctrl_pkg::sram_key_t   | 128'hbecda03b34bc0418a30a33861a610f71         |                                                                              |
| otp_ctrl_pkg | otp_ctrl_pkg::sram_nonce_t | 128'h22f296f8f95efb84a75cd435a5541e9f         |                                                                              |
| lfsr_perm_t  | lfsr_perm_t                | 160'h8c24f71703eda8a2378916b6bf80c76651ebcea1 |                                                                              |
## Types

| Name                | Type                                                                                                                                                                                                                                                                                                                               | Description |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| lfsr_perm_t         | logic [RandInitSeed-1:0][$clog2(RandInitSeed)-1:0]                                                                                                                                                                                                                                                                                 |             |
| sram_scr_req_t      | struct packed {<br><span style="padding-left:20px">          logic                                    valid;<br><span style="padding-left:20px">     logic [otp_ctrl_pkg::SramKeyWidth-1:0]   key;<br><span style="padding-left:20px">     logic [NonceWidth-1:0]                   nonce;<br><span style="padding-left:20px">   } |             |
| sram_scr_init_req_t | struct packed {<br><span style="padding-left:20px">     logic                                    req;<br><span style="padding-left:20px">     logic [RandInitSeed-1:0]                 seed;<br><span style="padding-left:20px">   }                                                                                               |             |
| sram_scr_rsp_t      | struct packed {<br><span style="padding-left:20px">     logic [1:0]           rerror;<br><span style="padding-left:20px">      logic [AddrWidth-1:0] raddr;<br><span style="padding-left:20px">     }                                                                                                                              |             |
| sram_scr_init_rsp_t | struct packed {<br><span style="padding-left:20px">     logic                  ack;<br><span style="padding-left:20px">   }                                                                                                                                                                                                        |             |
