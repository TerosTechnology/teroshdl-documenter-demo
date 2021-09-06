# Package: aes_sbox_canright_pkg

- **File**: aes_sbox_canright_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 AES Canright SBox package

 For details, see the following documents:
 - Canright, "A very compact Rijndael S-box", technical report
   available at https://hdl.handle.net/10945/25608
 - Canright, "A very compact 'perfectly masked' S-box for AES (corrected)", paper
   available at https://eprint.iacr.org/2009/011.pdf


## Constants

| Name | Type        | Value     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---- | ----------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A2X  | logic [7:0] | undefined |  Basis conversion matrices to convert between polynomial basis A, normal basis X  and basis S incorporating the bit matrix of the SBox. More specifically,  multiplication by X2X performs the transformation from normal basis X into  polynomial basis A, followed by the affine transformation (substep 2). Likewise,  multiplication by S2X performs the inverse affine transformation followed by the  transformation from polynomial basis A to normal basis X.  (see Appendix A of the technical report)  |
| X2A  | logic [7:0] | undefined |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| X2S  | logic [7:0] | undefined |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| S2X  | logic [7:0] | undefined |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
## Functions
- aes_mul_gf2p2 <font id="function_arguments">(logic [1:0] g,<br><span style="padding-left:20px"> logic [1:0])</font> <font id="function_return">return (logic [1:0])</font>
- aes_scale_omega2_gf2p2 <font id="function_arguments">(logic [1:0])</font> <font id="function_return">return (logic [1:0])</font>
**Description**
 Scale by Omega^2 = N in GF(2^2), using normal basis [Omega^2, Omega]
 (see Figure 16 in the technical report)

- aes_scale_omega_gf2p2 <font id="function_arguments">(logic [1:0])</font> <font id="function_return">return (logic [1:0])</font>
**Description**
 Scale by Omega = N^2 in GF(2^2), using normal basis [Omega^2, Omega]
 (see Figure 15 in the technical report)

- aes_square_gf2p2 <font id="function_arguments">(logic [1:0])</font> <font id="function_return">return (logic [1:0])</font>
**Description**
 Square in GF(2^2), using normal basis [Omega^2, Omega]
 (see Figures 8 and 10 in the technical report)

- aes_mul_gf2p4 <font id="function_arguments">(logic [3:0] gamma,<br><span style="padding-left:20px"> logic [3:0])</font> <font id="function_return">return (logic [3:0])</font>
**Description**
 Multiplication in GF(2^4), using normal basis [alpha^8, alpha^2]
 (see Figure 13 in the technical report)

- aes_square_scale_gf2p4_gf2p2 <font id="function_arguments">(logic [3:0])</font> <font id="function_return">return (logic [3:0])</font>
**Description**
 Square and scale by nu in GF(2^4)/GF(2^2), using normal basis [alpha^8, alpha^2]
 (see Figure 19 as well as Appendix A of the technical report)

