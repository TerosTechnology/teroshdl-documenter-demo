# Entity: alert_handler_accu
## Diagram
![Diagram](alert_handler_accu.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 This module accumulates incoming alert triggers. Once the current accumulator
 value is greater or equal the accumulator threshold, the next occurence of
 class_trig_i will trigger escalation.
 Note that the accumulator is implemented using a saturation counter which
 does not wrap around.
 
## Ports
| Port name    | Direction | Type            | Description                                        |
| ------------ | --------- | --------------- | -------------------------------------------------- |
| clk_i        | input     |                 |                                                    |
| rst_ni       | input     |                 |                                                    |
| class_en_i   | input     |                 | class enable                                       |
| clr_i        | input     |                 | clear the accumulator                              |
| class_trig_i | input     |                 | increments the accu                                |
| thresh_i     | input     | [AccuCntDw-1:0] | escalation trigger threshold                       |
| accu_cnt_o   | output    | [AccuCntDw-1:0] | output of current accu value                       |
| accu_trig_o  | output    |                 | escalation trigger output                          |
| accu_fail_o  | output    |                 | asserted if the tandem accu counters are not equal |
## Signals
| Name             | Type                       | Description                                                                                                                                                                                                                                                                                                       |
| ---------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| trig_gated_unbuf | logic                      |                                                                                                                                                                                                                                                                                                                   |
| accu_q           | logic [1:0][AccuCntDw-1:0] | We employ two redundant counters to guard against FI attacks. If any of the two is glitched and the two counter states do not agree, the check_fail_o signal is asserted which will move the corresponding escalation FSM into a terminal error state where all escalation actions will be permanently asserted.  |
