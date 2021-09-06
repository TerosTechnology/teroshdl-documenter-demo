# Entity: tx_iq_intf

- **File**: tx_iq_intf.v
## Diagram

![Diagram](tx_iq_intf.svg "Diagram")
## Description

 Xianjun jiao. putaoshu@msn.com; xianjun.jiao@imec.be;

## Generics

| Generic name           | Type    | Value | Description |
| ---------------------- | ------- | ----- | ----------- |
| C_S00_AXIS_TDATA_WIDTH | integer | 64    |             |
| CSI_FUZZER_WIDTH       | integer | 6     |             |
| IQ_DATA_WIDTH          | integer | 16    |             |
## Ports

| Port name           | Direction | Type                                 | Description |
| ------------------- | --------- | ------------------------------------ | ----------- |
| rstn                | input     | wire                                 |             |
| clk                 | input     | wire                                 |             |
| wifi_iq_pack        | output    | wire [(2*IQ_DATA_WIDTH-1):0]         |             |
| wifi_iq_ready       | input     | wire                                 |             |
| wifi_iq_valid       | output    | wire                                 |             |
| tx_hold_threshold   | input     | wire [9:0]                           |             |
| bb_gain             | input     | wire signed [9:0]                    |             |
| bb_gain1            | input     | wire signed [(CSI_FUZZER_WIDTH-1):0] |             |
| bb_gain1_rot90_flag | input     | wire                                 |             |
| bb_gain2            | input     | wire signed [(CSI_FUZZER_WIDTH-1):0] |             |
| bb_gain2_rot90_flag | input     | wire                                 |             |
| rf_i                | input     | wire signed [(IQ_DATA_WIDTH-1) : 0]  |             |
| rf_q                | input     | wire signed [(IQ_DATA_WIDTH-1) : 0]  |             |
| rf_iq_valid         | input     | wire                                 |             |
| tx_iq_fifo_empty    | output    | wire                                 |  to lbt     |
| tx_hold             | output    | wire                                 |  to tx core |
## Signals

| Name                        | Type                                  | Description |
| --------------------------- | ------------------------------------- | ----------- |
| rf_i_tmp                    | reg signed [(10+IQ_DATA_WIDTH-1) : 0] |             |
| rf_q_tmp                    | reg signed [(10+IQ_DATA_WIDTH-1) : 0] |             |
| tx_iq_fifo_wren             | reg                                   |             |
| tx_iq_fifo_out_zero_padding | wire [(2*IQ_DATA_WIDTH-1):0]          |             |
| tx_iq_fifo_out              | wire [(2*IQ_DATA_WIDTH-1):0]          |             |
| tx_iq_fifo_in               | wire [(2*IQ_DATA_WIDTH-1):0]          |             |
| tx_iq_fifo_rden             | wire                                  |             |
| tx_iq_fifo_full             | wire                                  |             |
| data_count                  | wire [9:0]                            |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 gain module 
## Instantiations

- csi_fuzzer_i: csi_fuzzer
</br>**Description**
csi fuzzer at fifo out

- fifo32_1clk_dep512_i: xpm_fifo_sync
</br>**Description**
 fifo32_1clk_dep512 fifo32_1clk_dep512_i (
     .CLK(clk),
     .DATAO(tx_iq_fifo_out),
     .DI(tx_iq_fifo_in),
     .EMPTY(tx_iq_fifo_empty),
     .FULL(tx_iq_fifo_full),
     .RDEN(tx_iq_fifo_rden),
     .RST(~rstn),
     .WREN(tx_iq_fifo_wren),
     .data_count(data_count)
 );

