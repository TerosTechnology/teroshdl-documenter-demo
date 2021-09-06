# Entity: rx_iq_intf

- **File**: rx_iq_intf.v
## Diagram

![Diagram](rx_iq_intf.svg "Diagram")
## Description

 Xianjun jiao. putaoshu@msn.com; xianjun.jiao@imec.be;

## Generics

| Generic name           | Type    | Value | Description |
| ---------------------- | ------- | ----- | ----------- |
| C_S00_AXIS_TDATA_WIDTH | integer | 64    |             |
| IQ_DATA_WIDTH          | integer | 16    |             |
## Ports

| Port name              | Direction | Type                           | Description                                                                                                      |
| ---------------------- | --------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| rstn                   | input     | wire                           |  -------------debug purpose---------------- output reg trigger_out,  -------------debug purpose----------------  |
| clk                    | input     | wire                           |                                                                                                                  |
| bw20_i0                | input     | wire [(IQ_DATA_WIDTH-1):0]     |                                                                                                                  |
| bw20_q0                | input     | wire [(IQ_DATA_WIDTH-1):0]     |                                                                                                                  |
| bw20_i1                | input     | wire [(IQ_DATA_WIDTH-1):0]     |                                                                                                                  |
| bw20_q1                | input     | wire [(IQ_DATA_WIDTH-1):0]     |                                                                                                                  |
| bw20_iq_valid          | input     | wire                           |                                                                                                                  |
| fifo_in_en             | input     | wire                           |                                                                                                                  |
| fifo_out_en            | input     | wire                           |                                                                                                                  |
| bb_20M_en              | input     | wire                           |                                                                                                                  |
| rf_i0                  | output    | wire [(IQ_DATA_WIDTH-1) : 0]   |  to wifi receiver                                                                                                |
| rf_q0                  | output    | wire [(IQ_DATA_WIDTH-1) : 0]   |                                                                                                                  |
| rf_i1                  | output    | wire [(IQ_DATA_WIDTH-1) : 0]   |                                                                                                                  |
| rf_q1                  | output    | wire [(IQ_DATA_WIDTH-1) : 0]   |                                                                                                                  |
| rf_iq_valid            | output    | wire                           |                                                                                                                  |
| rf_iq_valid_delay_sel  | input     | wire                           |                                                                                                                  |
| rf_iq                  | output    | wire [((4*IQ_DATA_WIDTH)-1):0] |  to m_axis for loop back test                                                                                    |
| wifi_rx_iq_fifo_emptyn | output    | wire                           |                                                                                                                  |
## Signals

| Name             | Type                           | Description |
| ---------------- | ------------------------------ | ----------- |
| empty            | wire                           |             |
| full             | wire                           |             |
| rden             | wire                           |             |
| wren             | wire                           |             |
| bb_en            | wire                           |             |
| data_count       | wire [5:0]                     |             |
| data_selected    | wire [((4*IQ_DATA_WIDTH)-1):0] |             |
| wren_selected    | wire                           |             |
| counter          | reg [4:0]                      |             |
| counter_top      | reg [4:0]                      |             |
| rf_iq_valid_reg  | reg                            |             |
| fractional_flag  | wire                           |             |
| counter_top_flag | reg                            |             |
## Processes
- unnamed: ( @( posedge clk ) )
  - **Type:** always
**Description**
 rate control to make sure ofdm rx get I/Q as uniform as possible 
- unnamed: ( @( posedge clk ) )
  - **Type:** always
**Description**
 20MHz en 
- unnamed: ( @( posedge clk ) )
  - **Type:** always
**Description**
delay I/Q valid to wifi receiver for loop back mode 
## Instantiations

- xpm_fifo_sync_rx_iq_intf: xpm_fifo_sync
**Description**
 fifo32_1clk_dep32 fifo32_1clk_dep32_i (
     .CLK(clk),
     .DATAO(rf_iq),
     .DI(data_selected),
     .EMPTY(empty),
     .FULL(full),
     .RDEN(rden),
     .RST(~rstn),
     .WREN(wren),
     .data_count(data_count)
 );

