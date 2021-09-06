# Package: aes_model_dpi_pkg

- **File**: aes_model_dpi_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0


## Signals

| Name      | Type               | Description                                            |
| --------- | ------------------ | ------------------------------------------------------ |
| impl_i    | bit                | 0 = C model, 1 = OpenSSL/BoringSSL                     |
| input     | bit                | 0 = C model, 1 = OpenSSL/BoringSSL                     |
| op_i      | bit                | 0 = encrypt, 1 = decrypt                               |
| input     | bit                | 0 = encrypt, 1 = decrypt                               |
| mode_i    | bit          [5:0] | 6'b00_0001 = ECB, 6'00_b0010 = CBC, 6'b00_0100 = CFB,  |
| input     | bit          [5:0] | 6'b00_0001 = ECB, 6'00_b0010 = CBC, 6'b00_0100 = CFB,  |
| iv_i      | bit[3:0][3:0][7:0] |                                                        |
| input     | bit[3:0][3:0][7:0] |                                                        |
| key_len_i | bit          [2:0] | 3'b001 = 128b, 3'b010 = 192b, 3'b100 = 256b            |
| input     | bit          [2:0] | 3'b001 = 128b, 3'b010 = 192b, 3'b100 = 256b            |
| key_i     | bit    [7:0][31:0] |                                                        |
| input     | bit    [7:0][31:0] |                                                        |
| data_i    | bit[3:0][3:0][7:0] |                                                        |
| output    | bit[3:0][3:0][7:0] |                                                        |
| data_o    | bit[3:0][3:0][7:0] |                                                        |
| impl_i    | bit                | 0 = C model, 1 = OpenSSL/BoringSSL                     |
| input     | bit                | 0 = C model, 1 = OpenSSL/BoringSSL                     |
| op_i      | bit                | 0 = encrypt, 1 = decrypt                               |
| input     | bit                | 0 = encrypt, 1 = decrypt                               |
| mode_i    | bit        [5:0]   | 6'b00_0001 = ECB, 6'00_b0010 = CBC, 6'b00_0100 = CFB,  |
| input     | bit        [5:0]   | 6'b00_0001 = ECB, 6'00_b0010 = CBC, 6'b00_0100 = CFB,  |
| iv_i      | bit  [3:0][31:0]   |                                                        |
| input     | bit  [3:0][31:0]   |                                                        |
| key_len_i | bit        [2:0]   | 3'b001 = 128b, 3'b010 = 192b, 3'b100 = 256b            |
| input     | bit        [2:0]   | 3'b001 = 128b, 3'b010 = 192b, 3'b100 = 256b            |
| key_i     | bit  [7:0][31:0]   |                                                        |
| input     | bit  [7:0][31:0]   |                                                        |
| output    | bit        [7:0]   |                                                        |
| op_i      | bit                | 0 = encrypt, 1 = decrypt                               |
| input     | bit                | 0 = encrypt, 1 = decrypt                               |
| data_i    | bit[3:0][3:0][7:0] |                                                        |
| output    | bit[3:0][3:0][7:0] |                                                        |
| data_o    | bit[3:0][3:0][7:0] |                                                        |
| op_i      | bit                | 0 = encrypt, 1 = decrypt                               |
| input     | bit                | 0 = encrypt, 1 = decrypt                               |
| data_i    | bit[3:0][3:0][7:0] |                                                        |
| output    | bit[3:0][3:0][7:0] |                                                        |
| data_o    | bit[3:0][3:0][7:0] |                                                        |
| op_i      | bit                | 0 = encrypt, 1 = decrypt                               |
| input     | bit                | 0 = encrypt, 1 = decrypt                               |
| data_i    | bit[3:0][3:0][7:0] |                                                        |
| output    | bit[3:0][3:0][7:0] |                                                        |
| data_o    | bit[3:0][3:0][7:0] |                                                        |
| op_i      | bit                | 0 = encrypt, 1 = decrypt                               |
| input     | bit                | 0 = encrypt, 1 = decrypt                               |
| rcon_i    | bit      [7:0]     |                                                        |
| input     | bit      [7:0]     |                                                        |
| round_i   | bit      [3:0]     |                                                        |
| input     | bit      [3:0]     |                                                        |
| key_len_i | bit      [2:0]     | 3'b001 = 128b, 3'b010 = 192b, 3'b100 = 256b            |
| input     | bit      [2:0]     | 3'b001 = 128b, 3'b010 = 192b, 3'b100 = 256b            |
| key_i     | bit[7:0][31:0]     |                                                        |
| output    | bit[7:0][31:0]     |                                                        |
| key_o     | bit[7:0][31:0]     |                                                        |
## Functions
- sv_dpi_aes_crypt_block <font id="function_arguments">(input  bit             impl_i)</font> <font id="function_return">return (void)</font>
</br>**Description**
 wrapper function that converts from register format (4x32bit)
 to the 4x4x8 format of the c functions and back
 this ensures that RTL and refence models have same input and output format.

