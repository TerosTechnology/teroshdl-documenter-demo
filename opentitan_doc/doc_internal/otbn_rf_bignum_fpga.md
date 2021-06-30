# Entity: otbn_rf_bignum_fpga

## Diagram

![Diagram](otbn_rf_bignum_fpga.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Ports

| Port name   | Direction | Type          | Description |
| ----------- | --------- | ------------- | ----------- |
| clk_i       | input     |               |             |
| rst_ni      | input     |               |             |
| wr_addr_i   | input     | [WdrAw-1:0]   |             |
| wr_en_i     | input     | [1:0]         |             |
| wr_data_i   | input     | [ExtWLEN-1:0] |             |
| rd_addr_a_i | input     | [WdrAw-1:0]   |             |
| rd_data_a_o | output    | [ExtWLEN-1:0] |             |
| rd_addr_b_i | input     | [WdrAw-1:0]   |             |
| rd_data_b_o | output    | [ExtWLEN-1:0] |             |
## Signals

| Name          | Type                | Description                                           |
| ------------- | ------------------- | ----------------------------------------------------- |
| rf            | logic [ExtWLEN-1:0] |                                                       |
| unused_rst_ni | logic               | The reset is not used in this register file version.  |
