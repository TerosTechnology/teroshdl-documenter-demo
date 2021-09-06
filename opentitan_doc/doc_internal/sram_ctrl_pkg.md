# Package: sram_ctrl_pkg

- **File**: sram_ctrl_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0



## Signals

| Name          | Type       | Description |
| ------------- | ---------- | ----------- |
| sram_ctrl_pkg | endpackage |             |
## Constants

| Name         | Type                       | Value                                 | Description                                                                                                                 |
| ------------ | -------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| DataWidth    | int                        | 32 + tlul_pkg::DataIntgWidth          |                                                                                                                             |
| NonceWidth   | int                        | 64                                    |                                                                                                                             |
| otp_ctrl_pkg | otp_ctrl_pkg::sram_key_t   | 128'hbecda03b34bc0418a30a33861a610f71 | ///////////  RndCnst // ///////////                                                                                         |
| otp_ctrl_pkg | otp_ctrl_pkg::sram_nonce_t | 128'h22f296f8f95efb84a75cd435a5541e9f |                                                                                                                             |
| LfsrWidth    | int                        | 32                                    |  These LFSR parameters have been generated with  $ ./util/design/gen-lfsr-seed.py --width 32 --seed 3296833456 --prefix ""  |
| lfsr_seed_t  | lfsr_seed_t                | 32'h10a81ea5                          |                                                                                                                             |
| lfsr_perm_t  | lfsr_perm_t                |                                       |                                                                                                                             |
## Types

| Name        | Type                                         | Description |
| ----------- | -------------------------------------------- | ----------- |
| lfsr_seed_t | logic [LfsrWidth-1:0]                        |             |
| lfsr_perm_t | logic [LfsrWidth-1:0][$clog2(LfsrWidth)-1:0] |             |
