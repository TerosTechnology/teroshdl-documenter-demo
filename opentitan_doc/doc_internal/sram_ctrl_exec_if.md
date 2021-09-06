# Package: lc_ctrl_pkg

- **File**: sram_ctrl_exec_if.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 LC escalation signal must be stable before reset ends


## Signals

| Name               | Type                   | Description |
| ------------------ | ---------------------- | ----------- |
| path               | string                 |             |
| lc_hw_debug_en     | lc_ctrl_pkg::lc_tx_t   |             |
| otp_en_sram_ifetch | otp_ctrl_pkg::otp_en_t |             |
