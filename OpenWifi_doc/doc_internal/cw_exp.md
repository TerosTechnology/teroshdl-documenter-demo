# Entity: cw_exp

- **File**: cw_exp.v
## Diagram

![Diagram](cw_exp.svg "Diagram")
## Description

`define DEBUG_PREFIX (*mark_debug="true",DONT_TOUCH="TRUE"*)
 
## Ports

| Port name       | Direction | Type        | Description |
| --------------- | --------- | ----------- | ----------- |
| clk             | input     | wire        |             |
| rstn            | input     | wire        |             |
| tx_try_complete | input     | wire        |             |
| cw_combined     | input     | wire [31:0] |             |
| start_retrans   | input     | wire        |             |
| tx_queue_idx    | input     | wire [1:0]  |             |
| cw_exp          | input     | [3:0]       |             |
## Signals

| Name             | Type      | Description |
| ---------------- | --------- | ----------- |
| cw_min           | reg [3:0] |             |
| cw_max           | reg [3:0] |             |
| tx_queue_idx_reg | reg [1:0] |             |
| cw_update        | reg       |             |
## Processes
- unnamed: ( @(tx_queue_idx,cw_combined) )
- unnamed: ( @( posedge clk ) )
- unnamed: ( @( posedge clk ) )
