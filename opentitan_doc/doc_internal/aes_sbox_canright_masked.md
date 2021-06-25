# Entity: aes_masked_inverse_gf2p4
## Diagram
![Diagram](aes_sbox_canright_masked.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 AES Masked Canright SBox with Mask Re-Use
 For details, see the following paper:
 Canright, "A very compact 'perfectly masked' S-box for AES (corrected)"
 available at https://eprint.iacr.org/2009/011.pdf
 Note: This module implements the masked inversion algorithm with re-using masks.
 For details, see Section 2.3 of the paper. Re-using masks may make the implementation more
 vulnerable to higher-order differential side-channel analysis, but it remains secure against
 first-order attacks. This implementation is commonly referred to as THE Canright Masked SBox.
 A formal analysis using REBECCA (stable and transient mode) shows that this implementation is
 not secure. It's usage is thus discouraged. It's included here mainly for reference.
 For details on the REBECCA tool, see the following paper:
 Bloem, "Formal verification of masked hardware implementations in the presence of glitches"
 available at https://eprint.iacr.org/2017/897.pdf
 IMPORTANT NOTE:                                                                               //
                            DO NOT USE THIS FOR SYNTHESIS BLINDLY!                             //
                                                                                               //
 This implementation relies on primitive cells like prim_buf/xor2 containing tool-specific     //
 synthesis attributes to enforce the correct ordering of operations and avoid aggressive       //
 optimization. Without the proper primitives, synthesis tools might heavily optimize the       //
 design. The result is likely insecure. Use with care.                                         //
 Masked inverse in GF(2^4), using normal basis [z^4, z]
 (see Formulas 6, 13, 14, 15, 21, 22, 23, 24 in the paper)
 
## Ports
| Port name | Direction | Type  | Description |
| --------- | --------- | ----- | ----------- |
| b         | input     | [3:0] |             |
| q         | input     | [3:0] |             |
| r         | input     | [1:0] |             |
| m1        | input     | [3:0] |             |
| b_inv     | output    | [3:0] |             |
## Signals
| Name               | Type        | Description                                                                                                                                                                                                                                                                                  |
| ------------------ | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| b1                 | logic [1:0] |                                                                                                                                                                                                                                                                                              |
| b0                 | logic [1:0] |                                                                                                                                                                                                                                                                                              |
| q1                 | logic [1:0] |                                                                                                                                                                                                                                                                                              |
| q0                 | logic [1:0] |                                                                                                                                                                                                                                                                                              |
| c_inv              | logic [1:0] |                                                                                                                                                                                                                                                                                              |
| r_sq               | logic [1:0] |                                                                                                                                                                                                                                                                                              |
| m11                | logic [1:0] |                                                                                                                                                                                                                                                                                              |
| m10                | logic [1:0] |                                                                                                                                                                                                                                                                                              |
| mul_b0_q1          | logic [1:0] | Get re-usable intermediate results.                                                                                                                                                                                                                                                          |
| mul_b1_q0          | logic [1:0] | Get re-usable intermediate results.                                                                                                                                                                                                                                                          |
| mul_q1_q0          | logic [1:0] | Get re-usable intermediate results.                                                                                                                                                                                                                                                          |
| mul_b0_q1_buf      | logic [1:0] | Avoid aggressive synthesis optimizations.                                                                                                                                                                                                                                                    |
| mul_b1_q0_buf      | logic [1:0] | Avoid aggressive synthesis optimizations.                                                                                                                                                                                                                                                    |
| mul_q1_q0_buf      | logic [1:0] | Avoid aggressive synthesis optimizations.                                                                                                                                                                                                                                                    |
| scale_omega2_b     | logic [1:0] | IMPORTANT: The following ops must be executed in order (left to right): c = r ^ aes_scale_omega2_gf2p2(aes_square_gf2p2(b1 ^ b0)) ^ aes_scale_omega2_gf2p2(aes_square_gf2p2(q1 ^ q0)) ^ aes_mul_gf2p2(b1, b0) ^ mul_b1_q0 ^ mul_b0_q1 ^ mul_q0_q1; Get intermediate terms.                   |
| scale_omega2_q     | logic [1:0] | IMPORTANT: The following ops must be executed in order (left to right): c = r ^ aes_scale_omega2_gf2p2(aes_square_gf2p2(b1 ^ b0)) ^ aes_scale_omega2_gf2p2(aes_square_gf2p2(q1 ^ q0)) ^ aes_mul_gf2p2(b1, b0) ^ mul_b1_q0 ^ mul_b0_q1 ^ mul_q0_q1; Get intermediate terms.                   |
| mul_b1_b0          | logic [1:0] |                                                                                                                                                                                                                                                                                              |
| scale_omega2_b_buf | logic [1:0] | These terms are added to other terms that depend on the same inputs. Avoid aggressive synthesis optimizations.                                                                                                                                                                               |
| scale_omega2_q_buf | logic [1:0] | These terms are added to other terms that depend on the same inputs. Avoid aggressive synthesis optimizations.                                                                                                                                                                               |
| mul_b1_b0_buf      | logic [1:0] |                                                                                                                                                                                                                                                                                              |
| c                  | logic [1:0] | Generate c step by step.                                                                                                                                                                                                                                                                     |
| c_buf              | logic [1:0] |                                                                                                                                                                                                                                                                                              |
| xor_q1_r_sq        | logic [1:0] | Re-masking c_inv IMPORTANT: First combine the masks (ops in parens) then apply to c_inv: c_inv  = c_inv ^ (q1 ^ r_sq); c2_inv = c_inv ^ (q0 ^ q1); Get intermediate terms.                                                                                                                   |
| xor_q0_q1          | logic [1:0] | Re-masking c_inv IMPORTANT: First combine the masks (ops in parens) then apply to c_inv: c_inv  = c_inv ^ (q1 ^ r_sq); c2_inv = c_inv ^ (q0 ^ q1); Get intermediate terms.                                                                                                                   |
| c1_inv             | logic [1:0] | Re-masking c_inv IMPORTANT: First combine the masks (ops in parens) then apply to c_inv: c_inv  = c_inv ^ (q1 ^ r_sq); c2_inv = c_inv ^ (q0 ^ q1); Get intermediate terms.                                                                                                                   |
| c2_inv             | logic [1:0] | Re-masking c_inv IMPORTANT: First combine the masks (ops in parens) then apply to c_inv: c_inv  = c_inv ^ (q1 ^ r_sq); c2_inv = c_inv ^ (q0 ^ q1); Get intermediate terms.                                                                                                                   |
| mul_b0_c1_inv      | logic [1:0] | IMPORTANT: The following ops must be executed in order (left to right): b1_inv = m11 ^ aes_mul_gf2p2(b0, c1_inv) ^ mul_b0_q1 ^ aes_mul_gf2p2(q0, c1_inv) ^ mul_q0_q1; b0_inv = m10 ^ aes_mul_gf2p2(b1, c2_inv) ^ mul_b1_q0 ^ aes_mul_gf2p2(q1, c2_inv) ^ mul_q0_q1; Get intermediate terms.  |
| mul_q0_c1_inv      | logic [1:0] | IMPORTANT: The following ops must be executed in order (left to right): b1_inv = m11 ^ aes_mul_gf2p2(b0, c1_inv) ^ mul_b0_q1 ^ aes_mul_gf2p2(q0, c1_inv) ^ mul_q0_q1; b0_inv = m10 ^ aes_mul_gf2p2(b1, c2_inv) ^ mul_b1_q0 ^ aes_mul_gf2p2(q1, c2_inv) ^ mul_q0_q1; Get intermediate terms.  |
| mul_b1_c2_inv      | logic [1:0] | IMPORTANT: The following ops must be executed in order (left to right): b1_inv = m11 ^ aes_mul_gf2p2(b0, c1_inv) ^ mul_b0_q1 ^ aes_mul_gf2p2(q0, c1_inv) ^ mul_q0_q1; b0_inv = m10 ^ aes_mul_gf2p2(b1, c2_inv) ^ mul_b1_q0 ^ aes_mul_gf2p2(q1, c2_inv) ^ mul_q0_q1; Get intermediate terms.  |
| mul_q1_c2_inv      | logic [1:0] | IMPORTANT: The following ops must be executed in order (left to right): b1_inv = m11 ^ aes_mul_gf2p2(b0, c1_inv) ^ mul_b0_q1 ^ aes_mul_gf2p2(q0, c1_inv) ^ mul_q0_q1; b0_inv = m10 ^ aes_mul_gf2p2(b1, c2_inv) ^ mul_b1_q0 ^ aes_mul_gf2p2(q1, c2_inv) ^ mul_q0_q1; Get intermediate terms.  |
| mul_b0_c1_inv_buf  | logic [1:0] | The multiplier outputs are added to terms that depend on the same inputs. Avoid aggressive synthesis optimizations.                                                                                                                                                                          |
| mul_q0_c1_inv_buf  | logic [1:0] | The multiplier outputs are added to terms that depend on the same inputs. Avoid aggressive synthesis optimizations.                                                                                                                                                                          |
| mul_b1_c2_inv_buf  | logic [1:0] | The multiplier outputs are added to terms that depend on the same inputs. Avoid aggressive synthesis optimizations.                                                                                                                                                                          |
| mul_q1_c2_inv_buf  | logic [1:0] | The multiplier outputs are added to terms that depend on the same inputs. Avoid aggressive synthesis optimizations.                                                                                                                                                                          |
| b1_inv             | logic [1:0] | Generate b1_inv and b0_inv step by step.                                                                                                                                                                                                                                                     |
| b1_inv_buf         | logic [1:0] |                                                                                                                                                                                                                                                                                              |
| b0_inv             | logic [1:0] |                                                                                                                                                                                                                                                                                              |
| b0_inv_buf         | logic [1:0] |                                                                                                                                                                                                                                                                                              |
## Instantiations
- u_prim_buf_mul_bq01: prim_buf
- u_prim_buf_scale_omega2_bq: prim_buf
- u_prim_buf_mul_b1_b0: prim_buf
- u_prim_xor_q1_r_sq: prim_xor2
- u_prim_xor_q0_q1: prim_xor2
- u_prim_c1_inv: prim_xor2
**Description**
Generate c1_inv and c2_inv.

- u_prim_c2_inv: prim_xor2
- u_prim_buf_mul_bq01_c12_inv: prim_buf
