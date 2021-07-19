# Entity: prim_esc_sender

- **File**: prim_esc_sender.sv
## Diagram

![Diagram](prim_esc_sender.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 This module differentially encodes an escalation enable pulse
 of arbitrary width.
 The module supports in-band ping testing of the escalation
 wires. This is accomplished by sending out a single, differentially
 encoded pulse on esc_p/n which will be interpreted as a ping
 request by the escalation receiver. Note that ping_req_i shall
 be held high until either ping_ok_o or integ_fail_o is asserted.
 Native escalation enable pulses are differentiated from ping
 requests by making sure that these pulses are always longer than 1 cycle.
 If there is a differential encoding error, integ_fail_o
 will be asserted.
 See also: prim_esc_receiver, prim_diff_decode, alert_handler
 
## Ports

| Port name    | Direction | Type     | Description                                                              |
| ------------ | --------- | -------- | ------------------------------------------------------------------------ |
| clk_i        | input     |          |                                                                          |
| rst_ni       | input     |          |                                                                          |
| ping_req_i   | input     |          | this triggers a ping test. keep asserted until ping_ok_o is pulsed high. |
| ping_ok_o    | output    |          |                                                                          |
| integ_fail_o | output    |          | asserted if signal integrity issue detected                              |
| esc_req_i    | input     |          | escalation request signal                                                |
| esc_rx_i     | input     | esc_rx_t | escalation / ping response                                               |
| esc_tx_o     | output    | esc_tx_t | escalation output diff pair                                              |
## Signals

| Name            | Type    | Description                                                                   |
| --------------- | ------- | ----------------------------------------------------------------------------- |
| resp            | logic   |                                                                               |
| resp_n          | logic   |                                                                               |
| resp_p          | logic   |                                                                               |
| sigint_detected | logic   |                                                                               |
| ping_req_d      | logic   |                                                                               |
| ping_req_q      | logic   |                                                                               |
| esc_req_d       | logic   |                                                                               |
| esc_req_q       | logic   |                                                                               |
| esc_req_q1      | logic   |                                                                               |
| esc_p           | logic   | ping enable is 1 cycle pulse escalation pulse is always longer than 2 cycles  |
| state_d         | fsm_e   |                                                                               |
| state_q         | fsm_e   |                                                                               |
| integ_fail_o    | state_q |                                                                               |
| clk_i           | state_q |                                                                               |
| !rs             | state_q |                                                                               |
## Types

| Name  | Type                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| fsm_e | enum logic [2:0] {<br><span style="padding-left:20px">Idle,<br><span style="padding-left:20px"> CheckEscRespLo,<br><span style="padding-left:20px"> CheckEscRespHi,<br><span style="padding-left:20px">     CheckPingResp0,<br><span style="padding-left:20px"> CheckPingResp1,<br><span style="padding-left:20px"> CheckPingResp2,<br><span style="padding-left:20px"> CheckPingResp3} |             |
## Processes
- p_fsm: (  )
- p_regs: ( @(posedge clk_i or negedge rst_ni) )
## Instantiations

- u_prim_buf_resp: prim_buf
**Description**
This prevents further tool optimizations of the differential signal.

- u_decode_resp: prim_diff_decode
- u_prim_buf_esc: prim_buf
**Description**
This prevents further tool optimizations of the differential signal.

