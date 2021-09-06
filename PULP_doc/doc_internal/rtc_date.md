# Entity: rtc_date

- **File**: rtc_date.sv
## Diagram

![Diagram](rtc_date.svg "Diagram")
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

| Port name     | Direction | Type   | Description |
| ------------- | --------- | ------ | ----------- |
| clk_i         | input     |        |             |
| rstn_i        | input     |        |             |
| date_update_i | input     |        |             |
| date_i        | input     | [31:0] |             |
| date_o        | output    | [31:0] |             |
| new_day_i     | input     |        |             |
## Signals

| Name           | Type           | Description |
| -------------- | -------------- | ----------- |
| s_day          | logic	[5:0]    |             |
| s_month        | logic	[4:0]    |             |
| s_year         | logic	[13:0]   |             |
| r_day          | logic   [5:0]  |             |
| r_month        | logic   [4:0]  |             |
| r_year         | logic   [13:0] |             |
| s_end_of_month | logic          |             |
| s_end_of_year  | logic          |             |
| s_year_century | logic          |             |
| s_year_400     | logic          |             |
| s_year_leap    | logic          |             |
| s_year_div_4   | logic          |             |
## Processes
- unnamed: (  )
  - **Type:** always_comb
- proc_r_day: ( @(posedge clk_i or negedge rstn_i) )
  - **Type:** always_ff
**Description**
 Adjust the day of month 
- proc_r_month: ( @(posedge clk_i or negedge rstn_i) )
  - **Type:** always_ff
- proc_r_year: ( @(posedge clk_i or negedge rstn_i) )
  - **Type:** always_ff
**Description**
 proc_r_month 
