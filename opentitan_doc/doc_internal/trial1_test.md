# Entity: trial1_test

- **File**: trial1_test.sv
## Diagram

![Diagram](trial1_test.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

## Ports

| Port name | Direction | Type            | Description |
| --------- | --------- | --------------- | ----------- |
| clk       | input     |                 |             |
| rst_n     | input     |                 |             |
| tl_h2d    | output    | tl_h2d_t        |             |
| tl_d2h    | input     | tl_d2h_t        |             |
| reg2hw    | input     | trial1_reg2hw_t |             |
| hw2reg    | output    | trial1_hw2reg_t |             |
## Signals

| Name            | Type         | Description                                                                                                                                                                                                                                                                                                                                      |
| --------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| errorcount      | int          |                                                                                                                                                                                                                                                                                                                                                  |
| DEBUG           | logic        |                                                                                                                                                                                                                                                                                                                                                  |
| rwtype5_capture | logic [31:0] |  these registers need capturers to see the qe effect                                                                                                                                                                                                                                                                                             |
| rwtype6_capture | logic [31:0] |                                                                                                                                                                                                                                                                                                                                                  |
| rotype1_capture | logic [31:0] |                                                                                                                                                                                                                                                                                                                                                  |
| my_rotype1_d    | logic [31:0] |                                                                                                                                                                                                                                                                                                                                                  |
| my_rotype1_de   | logic        |                                                                                                                                                                                                                                                                                                                                                  |
| hold_wd         | logic [31:0] |  so far just these registers we need to drive back into  RWTYPE2[31:0]  RWTYPE3.FIELD0[15:0]  RWTYPE3.FIELD1[15:0]  ROTYPE0[31:0]  W1CTYPE2[31:0]  W1STYPE2[31:0]  W0CTYPE2[31:0]  R0W1CTYPE2[31:0]  RCTYPE0[31:0]  MIXTYPE0.FIELD1[3:0]  MIXTYPE0.FIELD3[3:0]  MIXTYPE0.FIELD4[3:0]  MIXTYPE0.FIELD5[3:0]  MIXTYPE0.FIELD6[3:0]  RWTYPE5[31:0]  |
| hold_q          | logic [31:0] |  so far just these registers we need to drive back into  RWTYPE2[31:0]  RWTYPE3.FIELD0[15:0]  RWTYPE3.FIELD1[15:0]  ROTYPE0[31:0]  W1CTYPE2[31:0]  W1STYPE2[31:0]  W0CTYPE2[31:0]  R0W1CTYPE2[31:0]  RCTYPE0[31:0]  MIXTYPE0.FIELD1[3:0]  MIXTYPE0.FIELD3[3:0]  MIXTYPE0.FIELD4[3:0]  MIXTYPE0.FIELD5[3:0]  MIXTYPE0.FIELD6[3:0]  RWTYPE5[31:0]  |
## Processes
- unnamed: ( @(posedge clk or negedge rst_n) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk or negedge rst_n) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk or negedge rst_n) )
  - **Type:** always_ff
