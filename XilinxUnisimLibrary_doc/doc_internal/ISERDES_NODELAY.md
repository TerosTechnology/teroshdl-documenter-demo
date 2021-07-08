# Entity: ISERDES_NODELAY

## Diagram

![Diagram](ISERDES_NODELAY.svg "Diagram")
## Description

   Copyright (c) 1995/2005 Xilinx, Inc.
 
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
 
        http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
   ____  ____
  /   /\/   /
 /___/  \  /    Vendor : Xilinx
 \   \   \/     Version : 10.1
  \   \         Description : Xilinx Functional Simulation Library Component
  /   /                  Source Synchronous Input Deserializer without delay element
 /___/   /\     Filename : ISERDES_NODELAY.v
 \   \  /  \    Timestamp : Fri Oct 21 10:31:45 PDT 2005
  \___\/\___\
 Revision:
    10/21/05 - Initial version.
    02/28/06 - CR 226003 -- Added Parameter Types (integer/real)
    06/16/06 - Added new port CLKB
    10/13/06 - Fixed CR 426606
    07/07/07 - Added wire declaration for internal signals
    09/10/07 - CR 447760 Added Strict DRC for BITSLIP and INTERFACE_TYPE combinations
    12/03/07 - CR 454107 Added DRC warnings for INTERFACE_TYPE, DATA_RATE and DATA_WIDTH combinations
    01/12/11 - CR 589496 changed some internal parameters to localparams
    12/13/11 - Added `celldefine and `endcelldefine (CR 524859).
    10/22/14 - Added #1 to $finish (CR 808642).
 End Revision
 
## Generics

| Generic name   | Type    | Value    | Description |
| -------------- | ------- | -------- | ----------- |
| BITSLIP_ENABLE |         | "FALSE"  |             |
| DATA_RATE      |         | "DDR"    |             |
| DATA_WIDTH     | integer | 4        |             |
| INIT_Q1        |         | 1'b0     |             |
| INIT_Q2        |         | 1'b0     |             |
| INIT_Q3        |         | 1'b0     |             |
| INIT_Q4        |         | 1'b0     |             |
| INTERFACE_TYPE |         | "MEMORY" |             |
| NUM_CE         | integer | 2        |             |
| SERDES_MODE    |         | "MASTER" |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| Q1        | output    |      |             |
| Q2        | output    |      |             |
| Q3        | output    |      |             |
| Q4        | output    |      |             |
| Q5        | output    |      |             |
| Q6        | output    |      |             |
| SHIFTOUT1 | output    |      |             |
| SHIFTOUT2 | output    |      |             |
| BITSLIP   | input     |      |             |
| CE1       | input     |      |             |
| CE2       | input     |      |             |
| CLK       | input     |      |             |
| CLKB      | input     |      |             |
| CLKDIV    | input     |      |             |
| D         | input     |      |             |
| OCLK      | input     |      |             |
| RST       | input     |      |             |
| SHIFTIN1  | input     |      |             |
| SHIFTIN2  | input     |      |             |
## Signals

| Name                 | Type       | Description          |
| -------------------- | ---------- | -------------------- |
| GSR                  | tri0       |                      |
| sel                  | reg [1:0]  |                      |
| data_width_int       | reg [3:0]  |                      |
| bts_q1               | reg        |                      |
| bts_q2               | reg        |                      |
| bts_q3               | reg        |                      |
| c23                  | reg        |                      |
| c45                  | reg        |                      |
| c67                  | reg        |                      |
| ce1r                 | reg        |                      |
| ce2r                 | reg        |                      |
| dataq1rnk2           | reg        |                      |
| dataq2rnk2           | reg        |                      |
| dataq3rnk2           | reg        |                      |
| dataq3rnk1           | reg        |                      |
| dataq4rnk1           | reg        |                      |
| dataq5rnk1           | reg        |                      |
| dataq6rnk1           | reg        |                      |
| dataq4rnk2           | reg        |                      |
| dataq5rnk2           | reg        |                      |
| dataq6rnk2           | reg        |                      |
| ice                  | reg        |                      |
| memmux               | reg        |                      |
| q2pmux               | reg        |                      |
| mux                  | reg        |                      |
| mux1                 | reg        |                      |
| muxc                 | reg        |                      |
| notifier             | reg        |                      |
| clkdiv_int           | reg        |                      |
| clkdivmux            | reg        |                      |
| o_out                | reg        |                      |
| q1_out               | reg        |                      |
| q2_out               | reg        |                      |
| q3_out               | reg        |                      |
| q4_out               | reg        |                      |
| q5_out               | reg        |                      |
| q6_out               | reg        |                      |
| q1rnk2               | reg        |                      |
| q2rnk2               | reg        |                      |
| q3rnk2               | reg        |                      |
| q4rnk2               | reg        |                      |
| q5rnk2               | reg        |                      |
| q6rnk2               | reg        |                      |
| q1rnk3               | reg        |                      |
| q2rnk3               | reg        |                      |
| q3rnk3               | reg        |                      |
| q4rnk3               | reg        |                      |
| q5rnk3               | reg        |                      |
| q6rnk3               | reg        |                      |
| q4rnk1               | reg        |                      |
| q5rnk1               | reg        |                      |
| q6rnk1               | reg        |                      |
| q6prnk1              | reg        |                      |
| num_ce_int           | reg        |                      |
| qr1                  | reg        |                      |
| qr2                  | reg        |                      |
| qhc1                 | reg        |                      |
| qhc2                 | reg        |                      |
| qlc1                 | reg        |                      |
| qlc2                 | reg        |                      |
| shiftn2_in           | reg        |                      |
| shiftn1_in           | reg        |                      |
| q1rnk1               | reg        |                      |
| q2nrnk1              | reg        |                      |
| q1prnk1              | reg        |                      |
| q2prnk1              | reg        |                      |
| q3rnk1               | reg        |                      |
| serdes_mode_int      | reg        |                      |
| data_rate_int        | reg        |                      |
| bitslip_enable_int   | reg        |                      |
| o_delay              | wire       |                      |
| rev_in               | reg        |                      |
| shiftout1_out        | wire       |                      |
| shiftout2_out        | wire       |                      |
| sel1                 | wire [1:0] |                      |
| bsmux                | wire [2:0] |                      |
| selrnk3              | wire [3:0] |                      |
| bitslip_in           | wire       |                      |
| ce1_in               | wire       |                      |
| ce2_in               | wire       |                      |
| clk_in               | wire       |                      |
| clkb_in              | wire       |                      |
| clkdiv_in            | wire       |                      |
| d_in                 | wire       |                      |
| dlyce_in             | wire       |                      |
| dlyinc_in            | wire       |                      |
| dlyrst_in            | wire       |                      |
| gsr_in               | wire       |                      |
| oclk_in              | wire       |                      |
| sr_in                | wire       |                      |
| shiftin1_in          | wire       |                      |
| shiftin2_in          | wire       |                      |
| rev_in_AND_NOT_sr_in | wire       | workaround for XSIM  |
| NOT_rev_in_AND_sr_in | wire       |                      |
## Constants

| Name      | Type | Value | Description                                                                                                                                            |
| --------- | ---- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SRVAL_Q1  |      | 1'b0  |                                                                                                                                                        |
| SRVAL_Q2  |      | 1'b0  |                                                                                                                                                        |
| SRVAL_Q3  |      | 1'b0  |                                                                                                                                                        |
| SRVAL_Q4  |      | 1'b0  |                                                                                                                                                        |
| ffinp     |      | 300   | WARNING !!!: This model may not work properly if the following parameters are changed. xilinx_internal_parameter on Parameter declarations for delays  |
| mxinp1    |      | 60    |                                                                                                                                                        |
| mxinp2    |      | 120   |                                                                                                                                                        |
| ffice     |      | 300   | Delay parameters                                                                                                                                       |
| mxice     |      | 60    |                                                                                                                                                        |
| ffbsc     |      | 300   | Delay parameter assignment                                                                                                                             |
| mxbsc     |      | 60    |                                                                                                                                                        |
| mxinp1_my |      | 0     |                                                                                                                                                        |
## Processes
- unnamed: ( @(gsr_in) )
**Description**
GSR

- unnamed: ( @(posedge clk_in or posedge rev_in or posedge sr_in or posedge rev_in_AND_NOT_sr_in or posedge NOT_rev_in_AND_sr_in) )
**Description**
1st rank of registers
Asynchronous Operation

- unnamed: ( @(posedge clk_in or posedge sr_in) )
**Description**
always @ (posedge clk_in or posedge rev_in or posedge sr_in or posedge rev_in_AND_NOT_sr_in or posedge NOT_rev_in_AND_sr_in)

- unnamed: ( @(posedge clkb_in or posedge sr_in or posedge rev_in or posedge rev_in_AND_NOT_sr_in or posedge NOT_rev_in_AND_sr_in) )
**Description**
always @ (posedge clk_in or sr_in)
2nd flop in rank 1
Asynchronous Operation

- unnamed: ( @(posedge q2pmux or posedge sr_in or posedge rev_in or posedge rev_in_AND_NOT_sr_in or posedge NOT_rev_in_AND_sr_in) )
**Description**
always @ (posedge clkb_in or posedge sr_in or posedge rev_in or posedge rev_in_AND_NOT_sr_in or posedge NOT_rev_in_AND_sr_in)
4th flop in rank 1 operating on the posedge for networking
Asynchronous Operation

- unnamed: ( @(posedge memmux or posedge sr_in or posedge rev_in or posedge rev_in_AND_NOT_sr_in or posedge NOT_rev_in_AND_sr_in) )
**Description**
always @ (posedge q2pmux or posedge sr_in or posedge rev_in or posedge rev_in_AND_NOT_sr_in or posedge NOT_rev_in_AND_sr_in)
3rd flop in 2nd rank which is full featured and has
a choice of being clocked by oclk or clk
Asynchronous Operation

- unnamed: ( @(posedge memmux or posedge sr_in) )
**Description**
always @ (posedge memmux or posedge sr_in or posedge rev_in or posedge rev_in_AND_NOT_sr_in or posedge NOT_rev_in_AND_sr_in)
5th and 6th flops in rank 1 which are not full featured but can be clocked
by either clk or oclk

- unnamed: ( @ (memmux) )
**Description**
Optional inverter for q2p (4th flop in rank1)

- unnamed: ( @(clk_in or oclk_in) )
**Description**
always @ (memmux)
4 clock muxs in first rank

- unnamed: ( @(sel1 or q1prnk1 or shiftin1_in or shiftin2_in) )
**Description**
always @(clk_in or oclk_in)
data input mux for q3, q4, q5 and q6

- unnamed: ( @(sel1 or q2prnk1 or q3rnk1 or shiftin1_in) )
**Description**
always @(sel1 or q1prnk1 or SHIFTIN1 or SHIFTIN2)

- unnamed: ( @(data_rate_int or q3rnk1 or q4rnk1) )
**Description**
always @(sel1 or q2prnk1 or q3rnk1 or SHIFTIN1)

- unnamed: ( @(data_rate_int or q4rnk1 or q5rnk1) )
- unnamed: ( @(bitslip_enable_int or clkdiv_int or clkdiv_in) )
**Description**
2nd rank of registers
clkdivmux to pass clkdiv_int or CLKDIV to rank 2

- unnamed: ( @(posedge clkdivmux or posedge sr_in) )
**Description**
always @(clkdiv_int or clkdiv_in)
Asynchronous Operation

- unnamed: ( @(bsmux or q1rnk1 or q1prnk1 or q2prnk1) )
**Description**
always @ (posedge clkdivmux or sr_in)
Data mux for 2nd rank of flops
Delay for mux set to 120

- unnamed: ( @(bsmux or q1prnk1 or q4rnk1) )
**Description**
always @(bsmux or q1rnk1 or q1prnk1 or q2prnk1)

- unnamed: ( @(bsmux or q3rnk1 or q4rnk1) )
**Description**
always @(bsmux or q1prnk1 or q4rnk1)

- unnamed: ( @(bsmux or q3rnk1 or q4rnk1 or q6rnk1) )
**Description**
always @(bsmux or q3rnk1 or q4rnk1)

- unnamed: ( @(bsmux or q5rnk1 or q6rnk1) )
**Description**
always @(bsmux or q3rnk1 or q4rnk1 or q6rnk1)

- unnamed: ( @(bsmux or q5rnk1 or q6rnk1 or q6prnk1) )
**Description**
always @(bsmux or q5rnk1 or q6rnk1)

- unnamed: ( @(posedge clkdiv_in or posedge sr_in) )
**Description**
always @(bsmux or q5rnk1 or q6rnk1 or q6prnk1)
3rd rank of registers
Asynchronous Operation

- unnamed: ( @(selrnk3 or q1rnk1 or q1prnk1 or q1rnk2 or q1rnk3) )
- unnamed: ( @(selrnk3 or q2nrnk1 or q2prnk1 or q2rnk2 or q2rnk3) )
**Description**
always @(selrnk3 or q1rnk1 or q1prnk1 or q1rnk2 or q1rnk3)

- unnamed: ( @(bitslip_enable_int or q3rnk2 or q3rnk3) )
**Description**
always @(selrnk3 or q2nrnk1 or q2prnk1 or q2rnk2 or q2rnk3)

- unnamed: ( @(bitslip_enable_int or q4rnk2 or q4rnk3) )
**Description**
always @ (q3rnk2 or q3rnk3)

- unnamed: ( @(bitslip_enable_int or q5rnk2 or q5rnk3) )
**Description**
always @ (q4rnk2 or q4rnk3)

- unnamed: ( @(bitslip_enable_int or q6rnk2 or q6rnk3) )
**Description**
always @ (q5rnk2 or q5rnk3)

- unnamed: ( @(data_rate_int or data_width_int) )
**Description**
always @ (q6rnk2 or q6rnk3)
Set value of counter in bitslip controller

- unnamed: ( @ (posedge qr2 or negedge clk_in) )
**Description**
Divide by 2 - 8 counter
Asynchronous Operation

- unnamed: ( @ (negedge clk_in) )
**Description**
always @ (posedge qr2 or negedge clk_in)
Synchronous Operation

- unnamed: ( @ (sel or c23 or c45 or c67 or clkdiv_int or bts_q1 or bts_q2 or bts_q3) )
**Description**
always @ (negedge clk_in)
4:1 selector mux and divider selections

- unnamed: ( @ (posedge qr1 or posedge clkdiv_in) )
**Description**
always @ (sel or c23 or c45 or c67 or clkdiv_int or bts_q1 or bts_q2 or bts_q3)
Bitslip control logic
Low speed control flop
Asynchronous Operation

- unnamed: ( @ (data_rate_int or qlc1) )
**Description**
always @ (posedge qr1 or posedge clkdiv_in)
Mux to select between sdr "1" and ddr "0"

- unnamed: ( @ (posedge qr2 or negedge clk_in) )
**Description**
High speed control flop
Asynchronous Operation

- unnamed: ( @ (data_rate_int or mux1) )
- unnamed: ( @ (posedge sr_in or posedge clkdiv_in) )
**Description**
Asynchronous set flops
Low speed reset flop
Asynchronous Operation

- unnamed: ( @ (posedge sr_in or negedge clk_in) )
**Description**
always @ (posedge sr_in or posedge clkdiv_in)
High speed reset flop
Asynchronous Operation

- unnamed: ( @ (posedge clkdiv_in or posedge sr_in) )
**Description**
Asynchronous Operation

- unnamed: ( @ (num_ce_int or clkdiv_in or ce1_in or ce1r or ce2r) )
**Description**
always @ (posedge clkdiv_in or posedge sr_in)
Output mux ice

