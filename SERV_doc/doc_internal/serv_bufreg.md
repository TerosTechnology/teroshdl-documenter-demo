# Entity: serv_bufreg

- **File**: serv_bufreg.v
## Diagram

![Diagram](serv_bufreg.svg "Diagram")
## Generics

| Generic name | Type  | Value | Description |
| ------------ | ----- | ----- | ----------- |
| MDU          | [0:0] | 0     |             |
## Ports

| Port name   | Direction | Type        | Description |
| ----------- | --------- | ----------- | ----------- |
| i_clk       | input     | wire        |             |
| i_cnt0      | input     | wire        | State       |
| i_cnt1      | input     | wire        |             |
| i_en        | input     | wire        |             |
| i_init      | input     | wire        |             |
| i_mdu_op    | input     | wire        |             |
| o_lsb       | output    | wire [1:0]  |             |
| i_rs1_en    | input     | wire        | Control     |
| i_imm_en    | input     | wire        |             |
| i_clr_lsb   | input     | wire        |             |
| i_sh_signed | input     | wire        |             |
| i_rs1       | input     | wire        | Data        |
| i_imm       | input     | wire        |             |
| o_q         | output    | wire        |             |
| o_dbus_adr  | output    | wire [31:0] | External    |
| o_ext_rs1   | output    | wire [31:0] | Extension   |
## Signals

| Name    | Type       | Description |
| ------- | ---------- | ----------- |
| c       | wire       |             |
| q       | wire       |             |
| c_r     | reg        |             |
| data    | reg [31:2] |             |
| lsb     | reg [1:0]  |             |
| clr_lsb | wire       |             |
## Processes
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
