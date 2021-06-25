# Entity: otp_ctrl_scrmbl
## Diagram
![Diagram](otp_ctrl_scrmbl.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 This module contains the scrambling datapath for the OTP controller. It basically consists of
 two single-round PRESENT primitives (one for encryption and one for decryption mode), a counter
 with a simple FSM and four working registers, as listed below.
 key_state_q (128bit): working register to hold the round key (needed for the key schedule).
 data_state_q (64bit): working register to hold the data state in between rounds.
 data_shadow_q (64bit): shadow register for holding a second 64bit block of input data. This is
                        used to form a 128bit data block for the digest mode, which has a block
                        size of 128bit.
 digest_state_q (64bit): register to hold the digest state in between digest updates. Technically,
                         this is not needed when the data for the digest is fed into this block
                         back-to-back. However, the partition integrity checks require that it is
                         possible to interleave encryption operations and digest update steps,
                         hence an additional state register is needed, as otherwise the digest
                         state would be lost.
 The scrambling datapath is arranged such that it can also be used for calculating a digest using
 the encryption primitive in a Merkle-Damgard construction. To that end, the PRESENT block cipher
 is turned into a one way function according to the Davies-Meyer scheme. Note however that this
 makes the digest block size 128bit wide, since the Merkle-Damgard construction leverages the
 cipher key input to ingest data.
 The scrambling datapath exposes a few simple commands and the FSM hides the complexity
 of steering the appropriate muxes and keeping track of the cipher rounds. These commands are
 briefly explained below.
 Decrypt: This decrypts the data block provided via data_i with the key at index sel_i.
 Encrypt: This encrypts the data block provided via data_i with the key at index sel_i.
          In addition, this command copies the prvious result into a shadow register before
          the first encryption round for later use in the digest (see description further below).
          This enables interleaved encrypt/digest operation needed for the integrity checks of
          the secret partitions.
 LoadShadow: In "StandardMode", the LoadShadow command loads the data provided via data_i into a
             shadow register that is mapped to the lower 64bit of the 128bit digest input data
             block. In "ChainedMode", this command copies the contents of the data state register
             into the shadow register.
 DigestInit: This ensures that the digest initialization vector (IV) is selected upon the next
             call of the Digest command. Also, mode_i can be used to set the digest mode. If
             mode_i is set to "StandardMode", the data to be digested has to be provided via
             data_i and LoadShadow. If mode_i is set to "ChainedMode", the digest input is formed
             by concatenating the results of the revious two encryption commands.
 Digest: In "StandardMode", this command concatenates the data input supplied via data_i with
         the shadow register in order to form a 128bit block ({data_i, data_shadow_q}). This block
         is then used to encrypt the digest state. In "ChainedMode" digest mode, the 128bit block
         to be digested is formed by concatenating {data_state_q, data_shadow_q}. If a DigestInit
         command has been executed right before calling Digest, the IV selected with sel_i is
         used to initialize the state.
 DigestFinalize: This command encrypts the digest state with the finalization constant selected
                 by sel_i in order to form the final digest.
 References: - https://docs.opentitan.org/hw/ip/otp_ctrl/doc/index.html#design-details
             - https://docs.opentitan.org/hw/ip/prim/doc/prim_present/
             - https://en.wikipedia.org/wiki/Merkle-Damgard_construction
             - https://en.wikipedia.org/wiki/One-way_compression_function#Davies%E2%80%93Meyer
             - https://en.wikipedia.org/wiki/PRESENT
             - http://www.lightweightcrypto.org/present/present_ches2007.pdf
 
## Ports
| Port name     | Direction | Type                   | Description                               |
| ------------- | --------- | ---------------------- | ----------------------------------------- |
| clk_i         | input     |                        |                                           |
| rst_ni        | input     |                        |                                           |
| cmd_i         | input     | otp_scrmbl_cmd_e       | input data and command                    |
| mode_i        | input     | digest_mode_e          |                                           |
| sel_i         | input     | [ConstSelWidth-1:0]    |                                           |
| data_i        | input     | [ScrmblBlockWidth-1:0] |                                           |
| valid_i       | input     |                        |                                           |
| ready_o       | output    |                        |                                           |
| data_o        | output    | [ScrmblBlockWidth-1:0] | output data                               |
| valid_o       | output    |                        |                                           |
| escalate_en_i | input     |                        | escalation input and FSM error indication |
| fsm_err_o     | output    |                        |                                           |
## Signals
| Name                 | Type                                                       | Description                                                                                                                |
| -------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| otp_enc_key_lut      | logic [2**$clog2(NumScrmblKeys)-1:0][ScrmblKeyWidth-1:0]   | Align these arrays to power of 2's to prevent X's in the muxing operations further below.                                  |
| otp_dec_key_lut      | logic [2**$clog2(NumScrmblKeys)-1:0][ScrmblKeyWidth-1:0]   |                                                                                                                            |
| digest_const_lut     | logic [2**$clog2(NumDigestSets)-1:0][ScrmblKeyWidth-1:0]   |                                                                                                                            |
| digest_iv_lut        | logic [2**$clog2(NumDigestSets)-1:0][ScrmblBlockWidth-1:0] |                                                                                                                            |
| idx_state_d          | logic [4:0]                                                |                                                                                                                            |
| idx_state_q          | logic [4:0]                                                |                                                                                                                            |
| key_state_d          | logic [ScrmblKeyWidth-1:0]                                 |                                                                                                                            |
| key_state_q          | logic [ScrmblKeyWidth-1:0]                                 |                                                                                                                            |
| data_state_d         | logic [ScrmblBlockWidth-1:0]                               |                                                                                                                            |
| data_state_q         | logic [ScrmblBlockWidth-1:0]                               |                                                                                                                            |
| data_shadow_q        | logic [ScrmblBlockWidth-1:0]                               |                                                                                                                            |
| digest_state_d       | logic [ScrmblBlockWidth-1:0]                               |                                                                                                                            |
| digest_state_q       | logic [ScrmblBlockWidth-1:0]                               |                                                                                                                            |
| enc_data_out         | logic [ScrmblBlockWidth-1:0]                               |                                                                                                                            |
| enc_data_out_xor     | logic [ScrmblBlockWidth-1:0]                               |                                                                                                                            |
| dec_data_out         | logic [ScrmblBlockWidth-1:0]                               |                                                                                                                            |
| dec_key_out          | logic [ScrmblKeyWidth-1:0]                                 |                                                                                                                            |
| enc_key_out          | logic [ScrmblKeyWidth-1:0]                                 |                                                                                                                            |
| dec_idx_out          | logic [4:0]                                                |                                                                                                                            |
| enc_idx_out          | logic [4:0]                                                |                                                                                                                            |
| otp_digest_const_mux | logic [ScrmblKeyWidth-1:0]                                 |                                                                                                                            |
| otp_enc_key_mux      | logic [ScrmblKeyWidth-1:0]                                 |                                                                                                                            |
| otp_dec_key_mux      | logic [ScrmblKeyWidth-1:0]                                 |                                                                                                                            |
| otp_digest_iv_mux    | logic [ScrmblBlockWidth-1:0]                               |                                                                                                                            |
| digest_init          | logic                                                      |                                                                                                                            |
| data_state_sel       | data_state_sel_e                                           |                                                                                                                            |
| key_state_sel        | key_state_sel_e                                            |                                                                                                                            |
| data_state_en        | logic                                                      |                                                                                                                            |
| data_shadow_copy     | logic                                                      |                                                                                                                            |
| data_shadow_load     | logic                                                      |                                                                                                                            |
| digest_state_en      | logic                                                      |                                                                                                                            |
| key_state_en         | logic                                                      |                                                                                                                            |
| digest_mode_d        | digest_mode_e                                              |                                                                                                                            |
| digest_mode_q        | digest_mode_e                                              |                                                                                                                            |
| state_d              | state_e                                                    |                                                                                                                            |
| state_q              | state_e                                                    |                                                                                                                            |
| cnt_d                | logic [CntWidth-1:0]                                       |                                                                                                                            |
| cnt_q                | logic [CntWidth-1:0]                                       |                                                                                                                            |
| cnt_clr              | logic                                                      |                                                                                                                            |
| cnt_en               | logic                                                      |                                                                                                                            |
| valid_d              | logic                                                      |                                                                                                                            |
| valid_q              | logic                                                      |                                                                                                                            |
| state_raw_q          | logic [StateWidth-1:0]                                     | This primitive is used to place a size-only constraint on the flops in order to prevent FSM state encoding optimizations.  |
## Constants
| Name                | Type               | Value                      | Description |
| ------------------- | ------------------ | -------------------------- | ----------- |
| StateWidth          | int                | 9                          |             |
| CntWidth            | int                | $clog2(NumPresentRounds+1) |             |
| LastPresentRoundInt | int unsigned       | NumPresentRounds - 1       |             |
| LastPresentRound    | bit [CntWidth-1:0] | undefined                  |             |
## Types
| Name             | Type                                                                                                                                                                                                                                                                                                  | Description |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| data_state_sel_e | enum logic [2:0] {SelEncDataOut,                             SelDecDataOut,                             SelDigestState,                             SelEncDataOutXor,                             SelDataInput}                                                                                       |             |
| key_state_sel_e  | enum logic [2:0] {SelDecKeyOut,                             SelEncKeyOut,                             SelDecKeyInit,                             SelEncKeyInit,                             SelDigestConst,                             SelDigestInput,                             SelDigestChained} |             |
| state_e          | enum logic [StateWidth-1:0] {     IdleSt    = 9'b100010111,     DecryptSt = 9'b001010000,     EncryptSt = 9'b011001011,     DigestSt  = 9'b100101000,     ErrorSt   = 9'b010111101   }                                                                                                                |             |
## Processes
- p_luts: _(  )_

- p_fsm: _(  )_

- p_regs: _( @(posedge clk_i or negedge rst_ni) )_

## Instantiations
- u_prim_present_enc: prim_present
- u_prim_present_dec: prim_present
- u_state_regs: prim_flop
