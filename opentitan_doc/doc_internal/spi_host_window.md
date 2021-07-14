# Entity: spi_host_window

## Diagram

![Diagram](spi_host_window.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Module to manage TX FIFO window for Serial Peripheral Interface (SPI) host IP.
 
## Ports

| Port name  | Direction | Type   | Description |
| ---------- | --------- | ------ | ----------- |
| clk_i      | input     |        |             |
| rst_ni     | input     |        |             |
| win_i      | input     |        |             |
| win_o      | output    |        |             |
| tx_data_o  | output    | [31:0] |             |
| tx_be_o    | output    | [3:0]  |             |
| tx_valid_o | output    |        |             |
| rx_data_i  | input     | [31:0] |             |
| rx_ready_o | output    |        |             |
## Signals

| Name      | Type           | Description                                        |
| --------- | -------------- | -------------------------------------------------- |
| addr      | logic [AW-1:0] |                                                    |
| win_error | logic          | Only support reads/writes to the data fifo window  |
## Constants

| Name | Type | Value                     | Description |
| ---- | ---- | ------------------------- | ----------- |
| AW   | int  | spi_host_reg_pkg::BlockAw |             |
| DW   | int  | 32                        |             |
## Instantiations

- u_adapter: tlul_adapter_reg
