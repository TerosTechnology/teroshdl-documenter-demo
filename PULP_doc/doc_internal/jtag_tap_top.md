# Entity: jtag_tap_top
## Diagram
![Diagram](jtag_tap_top.svg "Diagram")
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
| Port name          | Direction | Type  | Description |
| ------------------ | --------- | ----- | ----------- |
| tck_i              | input     |       |             |
| trst_ni            | input     |       |             |
| tms_i              | input     |       |             |
| td_i               | input     |       |             |
| td_o               | output    |       |             |
| test_clk_i         | input     |       |             |
| test_rstn_i        | input     |       |             |
| soc_jtag_reg_i     | input     | [7:0] |             |
| soc_jtag_reg_o     | output    | [7:0] |             |
| sel_fll_clk_o      | output    |       |             |
| jtag_shift_dr_o    | output    |       | tap         |
| jtag_update_dr_o   | output    |       |             |
| jtag_capture_dr_o  | output    |       |             |
| axireg_sel_o       | output    |       |             |
| dbg_axi_scan_in_o  | output    |       |             |
| dbg_axi_scan_out_i | input     |       |             |
## Signals
| Name                | Type        | Description |
| ------------------- | ----------- | ----------- |
| s_scan_i            | logic       |             |
| s_confreg           | logic [8:0] |             |
| confscan            | logic       |             |
| confreg_sel         | logic       |             |
| td_o_int            | logic       |             |
| r_soc_reg0          | logic [7:0] |             |
| r_soc_reg1          | logic [7:0] |             |
| s_soc_jtag_reg_sync | logic [7:0] |             |
## Processes
- unnamed: _( @(posedge tck_i or negedge trst_ni) )_

## Instantiations
- tap_top_i: tap_top
**Description**
jtag tap controller

- confreg: jtagreg
**Description**
pulp configuration register

