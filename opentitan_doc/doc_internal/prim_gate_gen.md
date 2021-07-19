# Entity: prim_gate_gen

- **File**: prim_gate_gen.sv
## Diagram

![Diagram](prim_gate_gen.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Simple parameterizable gate generator. Used to fill up the netlist with gates that cannot be
 optimized away.
 The module leverages 4bit SBoxes from the PRINCE cipher, and interleaves them with registers,
 resulting in a split of around 50/50 between logic and sequential cells.
 This generator has been tested with 32bit wide data, and produces the following results:
 -------------+-----------+----------
 requested GE | actual GE | GE error
 -------------+-----------+----------
 500          |  483      |  -17
 1000         |  964      |  -36
 1500         |  1447     |  -53
 2500         |  2892     |  392
 5000         |  5299     |  299
 7500         |  8030     |  530
 10000        |  10393    |  393
 15000        |  15575    |  575
 25000        |  26422    |  1422
 50000        |  52859    |  2859
 100000       |  105270   |  5270
 Note that the generator is not very accurate for smaller gate counts due to the generate loop
 granularity. Hence, do not use for fever than 500 GE.
 If valid_i constantly set to 1'b1, the gate generator produces around 2.5% smaller designs for
 the configurations listed in the table above.
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| DataWidth    | int  | 32    |             |
| NumGates     | int  | 1000  |             |
## Ports

| Port name | Direction | Type            | Description |
| --------- | --------- | --------------- | ----------- |
| clk_i     | input     |                 |             |
| rst_ni    | input     |                 |             |
| valid_i   | input     |                 |             |
| data_i    | input     | [DataWidth-1:0] |             |
| data_o    | output    | [DataWidth-1:0] |             |
| valid_o   | output    |                 |             |
## Signals

| Name    | Type                                      | Description |
| ------- | ----------------------------------------- | ----------- |
| regs_d  | logic [NumOuterRounds-1:0][DataWidth-1:0] |             |
| regs_q  | logic [NumOuterRounds-1:0][DataWidth-1:0] |             |
| valid_d | logic [NumOuterRounds-1:0]                |             |
| valid_q | logic [NumOuterRounds-1:0]                |             |
## Constants

| Name           | Type | Value          | Description                                                                                                                |
| -------------- | ---- | -------------- | -------------------------------------------------------------------------------------------------------------------------- |
| NumInnerRounds | int  | 2              | technology specific tuning, do not modify. an inner round is comprised of a 2bit rotation, followed by a 4bit SBox Layer.  |
| GatesPerRound  | int  | DataWidth * 14 |                                                                                                                            |
| NumOuterRounds | int  | GatesPerRound  | an outer round consists of NumInnerRounds, followed by a register.                                                         |
## Processes
- p_regs: ( @(posedge clk_i or negedge rst_ni) )
