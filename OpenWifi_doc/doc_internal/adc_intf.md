# Entity: adc_intf

- **File**: adc_intf.v
## Diagram

![Diagram](adc_intf.svg "Diagram")
## Description

 Xianjun jiao. putaoshu@msn.com; xianjun.jiao@imec.be;

## Generics

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| IQ_DATA_WIDTH | integer | 16    |             |
## Ports

| Port name    | Direction | Type                           | Description          |
| ------------ | --------- | ------------------------------ | -------------------- |
| adc_rst      | input     | wire                           |                      |
| adc_clk      | input     | wire                           |                      |
| adc_data     | input     | wire [(4*IQ_DATA_WIDTH-1) : 0] |                      |
| adc_valid    | input     | wire                           | input wire adc_sync, |
| acc_clk      | input     | wire                           |                      |
| acc_rstn     | input     | wire                           |                      |
| bb_gain      | input     | wire [2:0]                     |                      |
| data_to_bb   | output    | [(4*IQ_DATA_WIDTH-1) : 0]      |                      |
| emptyn_to_bb | output    | wire                           |                      |
| bb_ask_data  | input     | wire                           |                      |
## Signals

| Name                 | Type                           | Description           |
| -------------------- | ------------------------------ | --------------------- |
| FULL_internal        | wire                           |                       |
| EMPTY_internal       | wire                           |                       |
| data_to_acc_internal | wire [(4*IQ_DATA_WIDTH-1) : 0] |   wire RST_internal;  |
| adc_data_delay       | reg [(4*IQ_DATA_WIDTH-1) : 0]  |                       |
| adc_valid_count      | reg                            |                       |
| adc_valid_decimate   | wire                           |                       |
## Processes
- unnamed: ( @( bb_gain, data_to_acc_internal) )
  - **Type:** always
- unnamed: ( @( posedge adc_clk ) )
  - **Type:** always
</br>**Description**
decimate input by 2: 40Msps --> 20Msps 
## Instantiations

- xpm_fifo_async_adc_intf: xpm_fifo_async
</br>**Description**
 fifo32_2clk_dep32 fifo32_2clk_dep32_i
        (.DATAO(data_to_acc_internal),
         .DI(adc_data_delay),
         .EMPTY(EMPTY_internal),
         .FULL(FULL_internal),
         .RDCLK(acc_clk),
         .RDEN(bb_ask_data),
         .RD_DATA_COUNT(),
         .RST(RST_internal),
         .WRCLK(adc_clk),
         .WREN(adc_valid_decimate),
         .WR_DATA_COUNT());

