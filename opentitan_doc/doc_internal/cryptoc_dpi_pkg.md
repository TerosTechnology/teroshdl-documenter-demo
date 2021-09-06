# Package: cryptoc_dpi_pkg

- **File**: cryptoc_dpi_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0


## Signals

| Name    | Type             | Description |
| ------- | ---------------- | ----------- |
| input   | bit[7:0]         |             |
| len     | longint unsigned |             |
| output  | longint unsigned |             |
| hash    | int unsigned     |             |
| input   | bit[7:0]         |             |
| len     | longint unsigned |             |
| output  | longint unsigned |             |
| hash    | int unsigned     |             |
| input   | bit[7:0]         |             |
| key_len | longint unsigned |             |
| input   | longint unsigned |             |
| input   | bit[7:0]         |             |
| msg_len | longint unsigned |             |
| output  | longint unsigned |             |
| hmac    | int unsigned     |             |
| input   | bit[7:0]         |             |
| key_len | longint unsigned |             |
| input   | longint unsigned |             |
| input   | bit[7:0]         |             |
| msg_len | longint unsigned |             |
| output  | longint unsigned |             |
| hmac    | int unsigned     |             |
## Functions
- sv_dpi_get_sha_digest <font id="function_arguments">(input bit[7:0] msg[],<br><span style="padding-left:20px">)</font> <font id="function_return">return (void)</font>
**Description**
 sv wrapper functions

- sv_dpi_get_sha256_digest <font id="function_arguments">(input bit[7:0] msg[],<br><span style="padding-left:20px">)</font> <font id="function_return">return (void)</font>
- sv_dpi_get_hmac_sha <font id="function_arguments">(input bit[31:0] key[],<br><span style="padding-left:20px">)</font> <font id="function_return">return (void)</font>
- sv_dpi_get_hmac_sha256 <font id="function_arguments">(input bit[31:0] key[],<br><span style="padding-left:20px">)</font> <font id="function_return">return (void)</font>
