# Entity: rtc_clock

## Diagram

![Diagram](rtc_clock.svg "Diagram")
## Description

Copyright 2018 ETH Zurich and University of Bologna.
 Copyright and related rights are licensed under the Solderpad Hardware
 License, Version 0.51 (the "License"); you may not use this file except in
 compliance with the License.  You may obtain a copy of the License at
 http://solderpad.org/licenses/SHL-0.51. Unless required by applicable law
 or agreed to in writing, software, hardware and materials distributed under
 this License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
 CONDITIONS OF ANY KIND, either express or implied. See the License for the
 specific language governing permissions and limitations under the License.
 
## Ports

| Port name      | Direction | Type   | Description |
| -------------- | --------- | ------ | ----------- |
| clk_i          | input     |        |             |
| rstn_i         | input     |        |             |
| clock_update_i | input     |        |             |
| clock_o        | output    | [21:0] |             |
| clock_i        | input     | [21:0] |             |
| init_sec_cnt_i | input     | [9:0]  |             |
| timer_update_i | input     |        |             |
| timer_enable_i | input     |        |             |
| timer_retrig_i | input     |        |             |
| timer_target_i | input     | [16:0] |             |
| timer_value_o  | output    | [16:0] |             |
| alarm_enable_i | input     |        |             |
| alarm_update_i | input     |        |             |
| alarm_clock_i  | input     | [21:0] |             |
| alarm_clock_o  | output    | [21:0] |             |
| event_o        | output    |        |             |
| update_day_o   | output    |        |             |
## Signals

| Name             | Type         | Description |
| ---------------- | ------------ | ----------- |
| r_seconds        | logic [7:0]  |             |
| r_minutes        | logic [7:0]  |             |
| r_hours          | logic [6:0]  |             |
| s_seconds        | logic [7:0]  |             |
| s_minutes        | logic [7:0]  |             |
| s_hours          | logic [6:0]  |             |
| r_alarm_seconds  | logic [7:0]  |             |
| r_alarm_minutes  | logic [7:0]  |             |
| r_alarm_hours    | logic [6:0]  |             |
| r_alarm_enable   | logic        |             |
| s_alarm_seconds  | logic [7:0]  |             |
| s_alarm_minutes  | logic [7:0]  |             |
| s_alarm_hours    | logic [5:0]  |             |
| r_sec_counter    | logic [14:0] |             |
| s_update_seconds | logic        |             |
| s_update_minutes | logic        |             |
| s_update_hours   | logic        |             |
| s_alarm_match    | logic        |             |
| r_alarm_match    | logic        |             |
| s_alarm_event    | logic        |             |
| s_timer_event    | logic        |             |
| r_timer          | logic [16:0] |             |
| r_timer_target   | logic [16:0] |             |
| r_timer_en       | logic        |             |
| r_timer_retrig   | logic        |             |
## Processes
- unnamed: ( @ (posedge clk_i or negedge rstn_i) )
- unnamed: ( @ (posedge clk_i or negedge rstn_i) )
- unnamed: ( @ (posedge clk_i or negedge rstn_i) )
- unnamed: ( @ (posedge clk_i or negedge rstn_i) )
- unnamed: ( @(posedge clk_i or negedge rstn_i) )
