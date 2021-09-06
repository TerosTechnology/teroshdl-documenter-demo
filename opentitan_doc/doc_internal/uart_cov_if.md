# Package: uvm_pkg

- **File**: uart_cov_if.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Implements functional coverage for UART.


## Signals

| Name               | Type                 | Description                                                                      |
| ------------------ | -------------------- | -------------------------------------------------------------------------------- |
| en_full_cov        | bit                  |                                                                                  |
| en_intg_cov        | bit                  |                                                                                  |
| en_intg_cov_loc    | bit                  |  If en_full_cov is set, then en_intg_cov must also be set since it is a subset.  |
| en_intg_cov_loc    | assign               |                                                                                  |
| uart_cov_vifs_wrap | endclass             |                                                                                  |
| begin              | initial              |                                                                                  |
| get_vifs           | m_uart_cov_vifs_wrap |                                                                                  |
| covergroup         | end                  |                                                                                  |
| clk_i              | uart_op_cg           |                                                                                  |
| name               | option               |                                                                                  |
| comment            | option               |                                                                                  |
| per_instance       | option               |                                                                                  |
| tx_enable          | cp_tx_enable         |                                                                                  |
| rx_enable          | cp_rx_enable         |                                                                                  |
| cp_tx_enable       | cr_tx_rx_enable      |                                                                                  |
| cp_rx_enable       | cr_tx_rx_enable      |                                                                                  |
