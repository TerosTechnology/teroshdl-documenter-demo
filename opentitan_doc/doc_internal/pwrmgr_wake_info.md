# Entity: pwrmgr_wake_info

- **File**: pwrmgr_wake_info.sv
## Diagram

![Diagram](pwrmgr_wake_info.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Power Manager Wake Information


## Ports

| Port name       | Direction | Type                          | Description |
| --------------- | --------- | ----------------------------- | ----------- |
| clk_i           | input     |                               |             |
| rst_ni          | input     |                               |             |
| wr_i            | input     |                               |             |
| data_i          | input     | [TotalWakeWidth-1:0]          |             |
| start_capture_i | input     |                               |             |
| record_dis_i    | input     |                               |             |
| wakeups_i       | input     | [NumWkups-1:0]                |             |
| fall_through_i  | input     |                               |             |
| abort_i         | input     |                               |             |
| info_o          | output    | pwrmgr_hw2reg_wake_info_reg_t |             |
## Signals

| Name             | Type                       | Description                             |
| ---------------- | -------------------------- | --------------------------------------- |
| record_en        | logic                      |                                         |
| start_capture_q1 | logic                      |  detect rising edge of start_capture_i  |
| start_capture    | logic                      |  detect rising edge of start_capture_i  |
| info             | logic [TotalWakeWidth-1:0] |                                         |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
**Description**
 generate the record enbale signal  HW enables the recording  Software can suppress the recording or disable it 
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
