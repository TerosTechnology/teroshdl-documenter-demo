# Entity: otbn_rf_base_fpga

- **File**: otbn_rf_base_fpga.sv
## Diagram

![Diagram](otbn_rf_base_fpga.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
*

## Ports

| Port name   | Direction | Type                | Description |
| ----------- | --------- | ------------------- | ----------- |
| clk_i       | input     |                     |             |
| rst_ni      | input     |                     |             |
| wr_addr_i   | input     | [4:0]               |             |
| wr_en_i     | input     |                     |             |
| wr_data_i   | input     | [BaseIntgWidth-1:0] |             |
| rd_addr_a_i | input     | [4:0]               |             |
| rd_data_a_o | output    | [BaseIntgWidth-1:0] |             |
| rd_addr_b_i | input     | [4:0]               |             |
| rd_data_b_o | output    | [BaseIntgWidth-1:0] |             |
## Signals

| Name          | Type                      | Description                                            |
| ------------- | ------------------------- | ------------------------------------------------------ |
| rf_reg        | logic [BaseIntgWidth-1:0] |                                                        |
| wr_en         | logic                     |                                                        |
| unused_rst_ni | logic                     |  The reset is not used in this register file version.  |
## Processes
- g_rf_reg: ( @(posedge clk_i) )
  - **Type:** always_ff
**Description**
 Sync write 
