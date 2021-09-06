# Entity: magnitude

- **File**: magnitude.v
## Diagram

![Diagram](magnitude.svg "Diagram")
## Description

-----------------------------------------------------------------------

## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| DATA_SIZE    |      | 16    |             |
## Ports

| Port name  | Direction | Type              | Description  |
| ---------- | --------- | ----------------- | ------------ |
| data_i_i   | input     | [DATA_SIZE-1:0]   |  input data  |
| data_q_i   | input     | [DATA_SIZE-1:0]   |              |
| data_en_i  | input     |                   |              |
| data_sof_i | input     |                   |              |
| data_eof_i | input     |                   |              |
| data_rst_i | input     |                   |              |
| data_clk_i | input     |                   |              |
| data_o     | output    | [2*DATA_SIZE-1:0] |  output data |
| data_en_o  | output    |                   |              |
| data_sof_o | output    |                   |              |
| data_eof_o | output    |                   |              |
| data_rst_o | output    |                   |              |
| data_clk_o | output    |                   |              |
## Signals

| Name   | Type                   | Description |
| ------ | ---------------------- | ----------- |
| data_s | wire [2*DATA_SIZE-1:0] |             |
## Processes
- unnamed: ( @(posedge data_clk_i) )
  - **Type:** always
