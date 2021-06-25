# Entity: usb_fs_tx_mux
## Diagram
![Diagram](usb_fs_tx_mux.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Copyright ETH Zurich.
 Copyright Luke Valenty (TinyFPGA project, https://github.com/tinyfpga/TinyFPGA-Bootloader).
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Ports
| Port name          | Direction | Type  | Description                      |
| ------------------ | --------- | ----- | -------------------------------- |
| in_tx_pkt_start_i  | input     |       | interface to IN Protocol Engine  |
| in_tx_pid_i        | input     | [3:0] |                                  |
| out_tx_pkt_start_i | input     |       | interface to OUT Protocol Engine |
| out_tx_pid_i       | input     | [3:0] |                                  |
| tx_pkt_start_o     | output    |       | interface to tx module           |
| tx_pid_o           | output    | [3:0] |                                  |
