# Package: crypto_dpi_prince_pkg

- **File**: crypto_dpi_prince_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name             | Type             | Description |
| ---------------- | ---------------- | ----------- |
| data             | longint unsigned |             |
| input            | longint unsigned |             |
| key0             | longint unsigned |             |
| input            | longint unsigned |             |
| key1             | longint unsigned |             |
| input            | longint unsigned |             |
| num_half_rounds  | int unsigned     |             |
| input            | int unsigned     |             |
| new_key_schedule | int unsigned     |             |
| data             | longint unsigned |             |
| input            | longint unsigned |             |
| key0             | longint unsigned |             |
| input            | longint unsigned |             |
| key1             | longint unsigned |             |
| input            | longint unsigned |             |
| num_half_rounds  | int unsigned     |             |
| input            | int unsigned     |             |
| new_key_schedule | int unsigned     |             |
## Constants

| Name          | Type         | Value | Description |
| ------------- | ------------ | ----- | ----------- |
| NumRoundsHalf | int unsigned | 5     |             |
## Functions
- sv_dpi_prince_encrypt <font id="function_arguments">(input bit [63:0]                      plaintext,<br><span style="padding-left:20px">)</font> <font id="function_return">return (void)</font>
- sv_dpi_prince_decrypt <font id="function_arguments">(input bit [NumRoundsHalf-1:0][63:0]   ciphertex)</font> <font id="function_return">return (void)</font>
