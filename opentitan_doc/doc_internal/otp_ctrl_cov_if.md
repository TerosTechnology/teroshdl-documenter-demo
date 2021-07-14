# Package: otp_ctrl_reg_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Implements functional coverage for OTP_CTRL
 

## Signals

| Name             | Type                                 | Description |
| ---------------- | ------------------------------------ | ----------- |
| lc_escalate_en_i | covergroup                           |             |
| data_req         | lc_esc_during_flash_data_req         |             |
| addr_req         | lc_esc_during_flash_addr_req         |             |
| sram_otp_key_i   | lc_esc_during_sram_0_req             |             |
| req              | lc_esc_during_sram_0_req             |             |
| sram_otp_key_i   | lc_esc_during_sram_1_req             |             |
| req              | lc_esc_during_sram_1_req             |             |
| req              | lc_esc_during_otbn_req               |             |
| otp_idle         | lc_esc_during_otp_idle               |             |
| req              | lc_esc_during_lc_otp_prog_req        |             |
| covergroup       | endgroup                             |             |
| data_req         | flash_data_req_condition_cg          |             |
| lc_esc_on        | flash_data_req_during_lc_esc         |             |
| lc_esc_off       | bins                                 |             |
| addr_req         | flash_data_req_during_flash_addr_req |             |
| sram_otp_key_i   | flash_data_req_during_sram_0_req     |             |
| req              | flash_data_req_during_sram_0_req     |             |
| sram_otp_key_i   | flash_data_req_during_sram_1_req     |             |
| req              | flash_data_req_during_sram_1_req     |             |
| req              | flash_data_req_during_otbn_req       |             |
| otp_idle         | flash_data_req_during_otp_idle       |             |
| covergroup       | endgroup                             |             |
| addr_req         | flash_addr_req_condition_cg          |             |
| lc_esc_on        | flash_addr_req_during_lc_esc         |             |
| lc_esc_off       | bins                                 |             |
| data_req         | flash_addr_req_during_flash_data_req |             |
| sram_otp_key_i   | flash_addr_req_during_sram_0_req     |             |
| req              | flash_addr_req_during_sram_0_req     |             |
| sram_otp_key_i   | flash_addr_req_during_sram_1_req     |             |
| req              | flash_addr_req_during_sram_1_req     |             |
| req              | flash_addr_req_during_otbn_req       |             |
| otp_idle         | flash_addr_req_during_otp_idle       |             |
| covergroup       | endgroup                             |             |
| sram_otp_key_i   | sram_0_req_condition_cg              |             |
| req              | sram_0_req_condition_cg              |             |
| lc_esc_on        | sram_0_req_during_lc_esc             |             |
| lc_esc_off       | bins                                 |             |
| addr_req         | sram_0_req_during_flash_addr_req     |             |
| data_req         | sram_0_req_during_flash_data_req     |             |
| sram_otp_key_i   | sram_0_req_during_sram_1_req         |             |
| req              | sram_0_req_during_sram_1_req         |             |
| req              | sram_0_req_during_otbn_req           |             |
| otp_idle         | sram_0_req_during_otp_idle           |             |
| covergroup       | endgroup                             |             |
| sram_otp_key_i   | sram_1_req_condition_cg              |             |
| req              | sram_1_req_condition_cg              |             |
| lc_esc_on        | sram_1_req_during_lc_esc             |             |
| lc_esc_off       | bins                                 |             |
| addr_req         | sram_1_req_during_flash_addr_req     |             |
| data_req         | sram_1_req_during_flash_data_req     |             |
| sram_otp_key_i   | sram_1_req_during_sram_0_req         |             |
| req              | sram_1_req_during_sram_0_req         |             |
| req              | sram_1_req_during_otbn_req           |             |
| otp_idle         | sram_1_req_during_otp_idle           |             |
| covergroup       | endgroup                             |             |
| req              | otbn_req_condition_cg                |             |
| lc_esc_on        | otbn_req_during_lc_esc               |             |
| lc_esc_off       | bins                                 |             |
| addr_req         | otbn_req_during_flash_addr_req       |             |
| data_req         | otbn_req_during_flash_data_req       |             |
| sram_otp_key_i   | otbn_req_during_sram_0_req           |             |
| req              | otbn_req_during_sram_0_req           |             |
| sram_otp_key_i   | otbn_req_during_sram_1_req           |             |
| req              | otbn_req_during_sram_1_req           |             |
| otp_idle         | otbn_req_during_otp_idle             |             |
| covergroup       | endgroup                             |             |
| req              | lc_prog_req_condition_cg             |             |
| lc_esc_on        | lc_prog_req_during_lc_esc            |             |
| lc_esc_off       | bins                                 |             |
| addr_req         | lc_prog_req_during_flash_addr_req    |             |
| data_req         | lc_prog_req_during_flash_data_req    |             |
| sram_otp_key_i   | lc_prog_req_during_sram_0_req        |             |
| req              | lc_prog_req_during_sram_0_req        |             |
| sram_otp_key_i   | lc_prog_req_during_sram_1_req        |             |
| req              | lc_prog_req_during_sram_1_req        |             |
| req              | lc_prog_req_during_otbn_req          |             |
| otp_idle         | lc_prog_req_during_otp_idle          |             |
