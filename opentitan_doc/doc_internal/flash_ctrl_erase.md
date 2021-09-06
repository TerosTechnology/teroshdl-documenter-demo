# Entity: flash_ctrl_erase

- **File**: flash_ctrl_erase.sv
## Diagram

![Diagram](flash_ctrl_erase.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Faux Flash Erase Control


## Ports

| Port name     | Direction | Type           | Description            |
| ------------- | --------- | -------------- | ---------------------- |
| op_start_i    | input     |                |  Software Interface    |
| op_type_i     | input     | flash_erase_e  |                        |
| op_addr_i     | input     | [BusAddrW-1:0] |                        |
| op_addr_oob_i | input     |                |                        |
| op_done_o     | output    |                |                        |
| op_err_o      | output    |                |                        |
| flash_req_o   | output    |                |  Flash Macro Interface |
| flash_addr_o  | output    | [BusAddrW-1:0] |                        |
| flash_op_o    | output    | flash_erase_e  |                        |
| flash_done_i  | input     |                |                        |
| flash_error_i | input     |                |                        |
## Signals

| Name          | Type                      | Description                                                                 |
| ------------- | ------------------------- | --------------------------------------------------------------------------- |
| oob_err       | logic                     |  out of bounds condition, the initial starting address is beyond the flash  |
| unused_addr_i | logic [WordsBitWidth-1:0] |  unused bus                                                                 |
## Constants

| Name          | Type                | Value                            | Description                                                                                                                                                                                                                                             |
| ------------- | ------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WordsBitWidth | int                 | $clog2(BusWordsPerPage)          |                                                                                                                                                                                                                                                         |
| PagesBitWidth | int                 | $clog2(PagesPerBank)             |                                                                                                                                                                                                                                                         |
| PageAddrMask  | logic[BusAddrW-1:0] | ~(('h1 << WordsBitWidth) - 1'b1) |  The *AddrMask below masks out the bits that are not required  e.g, assume we have an address 0x5_0004_345C  0x5 represents bank address  0x0004 represents page address  PageAddrMask would be 0xF_FFFF_0000  BankAddrMask would be 0xF_0000_0000<br>  |
| BankAddrMask  | logic[BusAddrW-1:0] | undefined                        |                                                                                                                                                                                                                                                         |
