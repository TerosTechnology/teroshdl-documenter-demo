# Entity: rom_ctrl

- **File**: rom_ctrl.sv
## Diagram

![Diagram](rom_ctrl.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Generics

| Generic name         | Type                  | Value     | Description                                                                                                                                                                                                                            |
| -------------------- | --------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BootRomInitFile      |                       | ""        |                                                                                                                                                                                                                                        |
| NumAlerts            | logic [NumAlerts-1:0] | undefined |                                                                                                                                                                                                                                        |
| RndCnstScrNonce      | bit [63:0]            | '0        |                                                                                                                                                                                                                                        |
| RndCnstScrKey        | bit [127:0]           | '0        |                                                                                                                                                                                                                                        |
| SecDisableScrambling | bit                   | 1'b0      | Disable all (de)scrambling operation. This disables both the scrambling block and the boot-time checker. Don't use this in a real chip, but it's handy for small FPGA targets where we don't want to spend area on unused scrambling.  |
## Ports

| Port name     | Direction | Type            | Description                  |
| ------------- | --------- | --------------- | ---------------------------- |
| clk_i         | input     |                 |                              |
| rst_ni        | input     |                 |                              |
| rom_cfg_i     | input     | rom_cfg_t       | ROM configuration parameters |
| rom_tl_i      | input     |                 |                              |
| rom_tl_o      | output    |                 |                              |
| regs_tl_i     | input     |                 |                              |
| regs_tl_o     | output    |                 |                              |
| alert_rx_i    | input     | [NumAlerts-1:0] | Alerts                       |
| alert_tx_o    | output    | [NumAlerts-1:0] |                              |
| pwrmgr_data_o | output    |                 | Connections to other blocks  |
| keymgr_data_o | output    |                 |                              |
| kmac_data_i   | input     |                 |                              |
| kmac_data_o   | output    |                 |                              |
## Signals

| Name                    | Type                      | Description                                                                  |
| ----------------------- | ------------------------- | ---------------------------------------------------------------------------- |
| rom_select              | logic                     |                                                                              |
| rom_index               | logic [RomIndexWidth-1:0] |                                                                              |
| rom_req                 | logic                     |                                                                              |
| rom_scr_rdata           | logic [DataWidth-1:0]     |                                                                              |
| rom_clr_rdata           | logic [DataWidth-1:0]     |                                                                              |
| rom_rvalid              | logic                     |                                                                              |
| bus_rom_index           | logic [RomIndexWidth-1:0] |                                                                              |
| bus_rom_req             | logic                     |                                                                              |
| bus_rom_gnt             | logic                     |                                                                              |
| bus_rom_rdata           | logic [DataWidth-1:0]     |                                                                              |
| bus_rom_rvalid          | logic                     |                                                                              |
| checker_rom_index       | logic [RomIndexWidth-1:0] |                                                                              |
| checker_rom_req         | logic                     |                                                                              |
| checker_rom_rdata       | logic [DataWidth-1:0]     |                                                                              |
| kmac_rom_data           | logic [63:0]              | Pack / unpack kmac connection data ========================================  |
| kmac_rom_rdy            | logic                     |                                                                              |
| kmac_rom_vld            | logic                     |                                                                              |
| kmac_rom_last           | logic                     |                                                                              |
| kmac_done               | logic                     |                                                                              |
| kmac_digest             | logic [255:0]             |                                                                              |
| tl_rom_h2d              | tlul_pkg::tl_h2d_t        | TL interface ==============================================================  |
| tl_rom_d2h              | tlul_pkg::tl_d2h_t        |                                                                              |
| rom_reg_integrity_error | logic                     |                                                                              |
| rom_integrity_error     | logic                     | Bus -> ROM adapter ========================================================  |
| mux_alert               | logic                     | The mux ===================================================================  |
| reg2hw                  | rom_ctrl_regs_reg2hw_t    | Register block ============================================================  |
| hw2reg                  | rom_ctrl_regs_hw2reg_t    |                                                                              |
| reg_integrity_error     | logic                     |                                                                              |
| digest_q                | logic [255:0]             | The checker FSM ===========================================================  |
| exp_digest_q            | logic [255:0]             | The checker FSM ===========================================================  |
| digest_d                | logic [255:0]             |                                                                              |
| digest_de               | logic                     |                                                                              |
| exp_digest_word_d       | logic [31:0]              |                                                                              |
| exp_digest_de           | logic                     |                                                                              |
| exp_digest_idx          | logic [2:0]               |                                                                              |
| checker_alert           | logic                     |                                                                              |
| bus_integrity_error     | logic                     |                                                                              |
| alert_test              | logic [NumAlerts-1:0]     | Alert generation ==========================================================  |
| alerts                  | logic [NumAlerts-1:0]     |                                                                              |
## Constants

| Name          | Type         | Value                          | Description                                                                                                                                                                                            |
| ------------- | ------------ | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| RomSizeByte   | int unsigned | ROM_CTRL_ROM_SIZE              | ROM_CTRL_ROM_SIZE is auto-generated by regtool and comes from the bus window size, measured in bytes of content (i.e. 4 times the number of 32 bit words).                                             |
| RomSizeWords  | int unsigned | RomSizeByte >> 2               |                                                                                                                                                                                                        |
| RomIndexWidth | int unsigned | vbits(RomSizeWords)            |                                                                                                                                                                                                        |
| DataWidth     | int unsigned | SecDisableScrambling ? 32 : 39 | DataWidth is normally 39, representing 32 bits of actual data plus 7 ECC check bits. If scrambling is disabled ("insecure mode"), we store a raw 32-bit image and generate ECC check bits on the fly.  |
## Instantiations

- u_rom_top: rom_ctrl_rom_reg_top
- u_tl_adapter_rom: tlul_adapter_sram
- u_mux: rom_ctrl_mux
- u_reg_regs: rom_ctrl_regs_reg_top
