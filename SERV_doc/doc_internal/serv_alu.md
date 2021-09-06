# Entity: serv_alu

- **File**: serv_alu.v
## Diagram

![Diagram](serv_alu.svg "Diagram")
## Ports

| Port name | Direction | Type       | Description |
| --------- | --------- | ---------- | ----------- |
| clk       | input     | wire       |             |
| i_en      | input     | wire       | State       |
| i_cnt0    | input     | wire       |             |
| o_cmp     | output    | wire       |             |
| i_sub     | input     | wire       | Control     |
| i_bool_op | input     | wire [1:0] |             |
| i_cmp_eq  | input     | wire       |             |
| i_cmp_sig | input     | wire       |             |
| i_rd_sel  | input     | wire [2:0] |             |
| i_rs1     | input     | wire       | Data        |
| i_op_b    | input     | wire       |             |
| i_buf     | input     | wire       |             |
| o_rd      | output    | wire       |             |
## Signals

| Name        | Type | Description                                                                                                                                                                                                                                                                                                                            |
| ----------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| result_add  | wire |                                                                                                                                                                                                                                                                                                                                        |
| cmp_r       | reg  |                                                                                                                                                                                                                                                                                                                                        |
| add_cy      | wire |                                                                                                                                                                                                                                                                                                                                        |
| add_cy_r    | reg  |                                                                                                                                                                                                                                                                                                                                        |
| rs1_sx      | wire | Sign-extended operands                                                                                                                                                                                                                                                                                                                 |
| op_b_sx     | wire |                                                                                                                                                                                                                                                                                                                                        |
| add_b       | wire |                                                                                                                                                                                                                                                                                                                                        |
| result_lt   | wire |                                                                                                                                                                                                                                                                                                                                        |
| result_eq   | wire |                                                                                                                                                                                                                                                                                                                                        |
| result_bool | wire |      The result_bool expression implements the following operations between     i_rs1 and i_op_b depending on the value of i_bool_op<br>     00 xor     01 0     10 or     11 and<br>     i_bool_op will be 01 during shift operations, so by outputting zero under     this condition we can safely or result_bool with i_buf     */  |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
