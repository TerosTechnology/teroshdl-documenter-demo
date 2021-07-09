# Entity: side_ch_s_axis

## Diagram

![Diagram](side_ch_s_axis.svg "Diagram")
## Description

based on Xilinx module template
 Xianjun jiao. putaoshu@msn.com; xianjun.jiao@imec.be;
 
## Generics

| Generic name           | Type    | Value | Description |
| ---------------------- | ------- | ----- | ----------- |
| C_S_AXIS_TDATA_WIDTH   | integer | 64    |             |
| MAX_NUM_DMA_SYMBOL     | integer | 8192  |             |
| MAX_BIT_NUM_DMA_SYMBOL | integer | 14    |             |
## Ports

| Port name             | Direction | Type                                  | Description |
| --------------------- | --------- | ------------------------------------- | ----------- |
| s_axis_endless_mode   | input     | wire                                  |             |
| S_AXIS_NUM_DMA_SYMBOL | input     | wire [MAX_BIT_NUM_DMA_SYMBOL-1 : 0]   |             |
| s_axis_state          | output    | wire                                  |             |
| data_to_pl            | output    | wire [C_S_AXIS_TDATA_WIDTH-1 : 0]     |             |
| pl_ask_data           | input     | wire                                  |             |
| s_axis_data_count     | output    | wire [MAX_BIT_NUM_DMA_SYMBOL-1 : 0]   |             |
| emptyn_to_pl          | output    | wire                                  |             |
| S_AXIS_ACLK           | input     | wire                                  |             |
| S_AXIS_ARESETN        | input     | wire                                  |             |
| S_AXIS_TREADY         | output    | wire                                  |             |
| S_AXIS_TDATA          | input     | wire [C_S_AXIS_TDATA_WIDTH-1 : 0]     |             |
| S_AXIS_TSTRB          | input     | wire [(C_S_AXIS_TDATA_WIDTH/8)-1 : 0] |             |
| S_AXIS_TLAST          | input     | wire                                  |             |
| S_AXIS_TVALID         | input     | wire                                  |             |
## Signals

| Name           | Type               | Description                             |
| -------------- | ------------------ | --------------------------------------- |
| mst_exec_state | reg                | In this state FIFO is written with the  |
| axis_tready    | wire               |                                         |
| fifo_wren      | wire               |                                         |
| write_pointer  | reg  [bit_num-1:0] |                                         |
| writes_done    | reg                |                                         |
| EMPTY          | wire               |                                         |
| FULL           | wire               |                                         |
## Constants

| Name       | Type    | Value                      | Description                    |
| ---------- | ------- | -------------------------- | ------------------------------ |
| bit_num    | integer | clogb2(MAX_NUM_DMA_SYMBOL) |                                |
| IDLE       | [1:0]   | 1'b0                       | This is the initial/idle state |
| WRITE_FIFO | [1:0]   | 1'b1                       | This is the initial/idle state |
## Functions
- clogb2 <font id="function_arguments">(input integer bit_depth)</font> <font id="function_return">return (integer)</font>
## Processes
- unnamed: ( @(posedge S_AXIS_ACLK) )
- unnamed: ( @(posedge S_AXIS_ACLK) )
## Instantiations

- fifo64_1clk_dep512_i: fifo64_1clk_dep512
## State machines

![Diagram_state_machine_0]( stm_side_ch_s_axis_00.svg "Diagram")