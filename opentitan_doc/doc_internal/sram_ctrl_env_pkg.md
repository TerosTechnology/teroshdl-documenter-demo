# Package: sram_ctrl_env_pkg

- **File**: sram_ctrl_env_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Constants

| Name                             | Type   | Value                                                                                                               | Description                                                                                                                                        |
| -------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| LIST_OF_ALERTS                   | string | {<br><span style="padding-left:20px"> "fatal_intg_error",<br><span style="padding-left:20px"> "fatal_parity_error"} | parameters                                                                                                                                         |
| uint                             | uint   | 2                                                                                                                   |                                                                                                                                                    |
| KDI_DATA_SIZE                    | int    | 1 + otp_ctrl_pkg::SramKeyWidth + otp_ctrl_pkg::SramNonceWidth                                                       | Number of bits in the otp_ctrl_pkg::sram_otp_key_rsp_t struct: 1 bit for valid, SramKeyWidth bits for the key, SramNonceWidth bits for the nonce.  |
| KDI_PROPAGATION_CYCLES           | int    | 4                                                                                                                   | after a kDI transaction is copmleted, it needs 4 cycles in the SRAM clock domain to be properly synchronized and propagated through the DUT        |
| LC_ESCALATION_PROPAGATION_CYCLES | int    | 3                                                                                                                   | a LC escalation request needs 3 cycles to be fully propagated through the DUT                                                                      |
## Types

| Name               | Type                                                                                                                                                                                                                                                                                                    | Description |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| lc_vif             | virtual sram_ctrl_lc_if                                                                                                                                                                                                                                                                                 | types       |
| exec_vif           | virtual sram_ctrl_exec_if                                                                                                                                                                                                                                                                               |             |
| sram_ctrl_e        | enum bit {<br><span style="padding-left:20px">     SramCtrlRenewScrKey = 0,<br><span style="padding-left:20px">     SramCtrlInit        = 1   }                                                                                                                                                         |             |
| sram_ctrl_status_e | enum bit [1:0] {<br><span style="padding-left:20px">     SramCtrlError           = 0,<br><span style="padding-left:20px">     SramCtrlEscalated       = 1,<br><span style="padding-left:20px">     SramCtrlScrKeyValid     = 2,<br><span style="padding-left:20px">     SramCtrlScrKeySeedValid = 3   } |             |
