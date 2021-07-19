# Entity: flash_ctrl_wrapper

- **File**: flash_ctrl_wrapper.sv
## Diagram

![Diagram](flash_ctrl_wrapper.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Ports

| Port name                  | Direction | Type                                | Description                               |
| -------------------------- | --------- | ----------------------------------- | ----------------------------------------- |
| clk_i                      | input     |                                     | Clock and Reset                           |
| rst_ni                     | input     |                                     |                                           |
| clk_otp_i                  | input     |                                     |                                           |
| rst_otp_ni                 | input     |                                     |                                           |
| flash_ctrl_tl_i            | input     |                                     | Bus Interface                             |
| flash_ctrl_tl_o            | output    |                                     |                                           |
| eflash_tl_i                | input     |                                     |                                           |
| eflash_tl_o                | output    |                                     |                                           |
| flash_power_ready_h_i      | input     |                                     | Analog Interface                          |
| flash_power_down_h_i       | input     |                                     |                                           |
| flash_bist_enable_i        | input     |                                     | DFT Interface                             |
| otp_i                      | input     |                                     | OTP interface                             |
| otp_o                      | output    |                                     |                                           |
| lc_creator_seed_sw_rw_en_i | input     |                                     |                                           |
| lc_owner_seed_sw_rw_en_i   | input     |                                     |                                           |
| lc_iso_part_sw_rd_en_i     | input     |                                     |                                           |
| lc_iso_part_sw_wr_en_i     | input     |                                     |                                           |
| lc_seed_hw_rd_en_i         | input     |                                     |                                           |
| lc_nvm_debug_en_i          | input     |                                     |                                           |
| lc_escalate_en_i           | input     |                                     |                                           |
| pwrmgr_o                   | output    |                                     |                                           |
| rma_req_i                  | input     |                                     |                                           |
| rma_seed_i                 | input     |                                     |                                           |
| rma_ack_o                  | output    |                                     |                                           |
| intr_prog_empty_o          | output    |                                     | Program fifo is empty                     |
| intr_prog_lvl_o            | output    |                                     | Program fifo is empty                     |
| intr_rd_full_o             | output    |                                     | Read fifo is full                         |
| intr_rd_lvl_o              | output    |                                     | Read fifo is full                         |
| intr_op_done_o             | output    |                                     | Requested flash operation (wr/erase) done |
| intr_err_o                 | output    |                                     | ERR_CODE is non-zero                      |
| alert_rx_i                 | input     | [flash_ctrl_reg_pkg::NumAlerts-1:0] |                                           |
| alert_tx_o                 | output    | [flash_ctrl_reg_pkg::NumAlerts-1:0] |                                           |
## Signals

| Name                 | Type                                 | Description                  |
| -------------------- | ------------------------------------ | ---------------------------- |
| flash_ctrl_flash_req | flash_ctrl_pkg::flash_req_t          | define inter-module signals  |
| flash_ctrl_flash_rsp | flash_ctrl_pkg::flash_rsp_t          |                              |
| flash_host_req       | logic                                | host to flash communication  |
| flash_host_req_type  | tlul_pkg::tl_type_e                  |                              |
| flash_host_req_rdy   | logic                                |                              |
| flash_host_req_done  | logic                                |                              |
| flash_host_intg_err  | logic                                |                              |
| flash_host_rdata     | logic [flash_ctrl_pkg::BusWidth-1:0] |                              |
| flash_host_addr      | logic [flash_ctrl_pkg::BusAddrW-1:0] |                              |
## Instantiations

- u_flash_ctrl: flash_ctrl
- u_tl_adapter_eflash: tlul_adapter_sram
- u_flash_eflash: flash_phy
