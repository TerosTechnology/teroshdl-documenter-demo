# Package: rom_ctrl_env_pkg

- **File**: rom_ctrl_env_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Constants

| Name               | Type        | Value                                         | Description                                                                                                                |
| ------------------ | ----------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| RND_CNST_SCR_NONCE | bit [63:0]  | 64'h0123456789ABCDEF                          | parameters                                                                                                                 |
| RND_CNST_SCR_KEY   | bit [127:0] | 128'hFEDCBA9876543210FEDCBA9876543210         |                                                                                                                            |
| LIST_OF_ALERTS     | string      | {<br><span style="padding-left:20px">"fatal"} |                                                                                                                            |
| uint               | uint        | 1                                             |                                                                                                                            |
| uint               | uint        | 256                                           | The top bytes in memory hold the digest KMAC's max digest size is larger than what is required, so declare the size here.  |
| MAX_CHECK_ADDR     | uint        | rom_ctrl_reg_pkg::ROM_CTRL_ROM_SIZE           |                                                                                                                            |
| KMAC_DATA_SIZE     | uint        | MAX_CHECK_ADDR                                | The data for each line in rom up to the digest is padded out to the kmac message width                                     |
| uint               | uint        | 39                                            | The rom width in bits                                                                                                      |
## Types

| Name         | Type                | Description |
| ------------ | ------------------- | ----------- |
| rom_ctrl_vif | virtual rom_ctrl_if | types       |
