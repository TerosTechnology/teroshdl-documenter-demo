# Entity: alert_handler_ping_timer_fpv

- **File**: alert_handler_ping_timer_fpv.sv
## Diagram

![Diagram](alert_handler_ping_timer_fpv.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Testbench module for ping timer in alert handler. Intended to use with
 a formal tool.
 
## Ports

| Port name          | Direction | Type              | Description |
| ------------------ | --------- | ----------------- | ----------- |
| clk_i              | input     |                   |             |
| rst_ni             | input     |                   |             |
| edn_req_o          | output    |                   |             |
| edn_ack_i          | input     |                   |             |
| edn_data_i         | input     | [LfsrWidth-1:0]   |             |
| en_i               | input     |                   |             |
| alert_ping_en_i    | input     | [NAlerts-1:0]     |             |
| ping_timeout_cyc_i | input     | [PING_CNT_DW-1:0] |             |
| wait_cyc_mask_i    | input     | [PING_CNT_DW-1:0] |             |
| alert_ping_req_o   | output    | [NAlerts-1:0]     |             |
| esc_ping_req_o     | output    | [N_ESC_SEV-1:0]   |             |
| alert_ping_ok_i    | input     | [NAlerts-1:0]     |             |
| esc_ping_ok_i      | input     | [N_ESC_SEV-1:0]   |             |
| alert_ping_fail_o  | output    |                   |             |
| esc_ping_fail_o    | output    |                   |             |
## Instantiations

- i_alert_handler_ping_timer: alert_handler_ping_timer
