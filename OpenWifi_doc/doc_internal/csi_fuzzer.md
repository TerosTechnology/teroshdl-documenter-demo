# Entity: csi_fuzzer

- **File**: csi_fuzzer.v
## Diagram

![Diagram](csi_fuzzer.svg "Diagram")
## Description

 Xianjun jiao. putaoshu@msn.com; xianjun.jiao@imec.be;

## Generics

| Generic name     | Type    | Value | Description |
| ---------------- | ------- | ----- | ----------- |
| CSI_FUZZER_WIDTH | integer | 6     |             |
| IQ_DATA_WIDTH    | integer | 16    |             |
## Ports

| Port name           | Direction | Type                                 | Description             |
| ------------------- | --------- | ------------------------------------ | ----------------------- |
| rstn                | input     | wire                                 |                         |
| clk                 | input     | wire                                 |                         |
| iq                  | input     | wire [(2*IQ_DATA_WIDTH-1):0]         |  input data             |
| iq_valid            | input     | wire                                 |                         |
| bb_gain1            | input     | wire signed [(CSI_FUZZER_WIDTH-1):0] |  FIR coef of the fuzzer |
| bb_gain1_rot90_flag | input     | wire                                 |                         |
| bb_gain2            | input     | wire signed [(CSI_FUZZER_WIDTH-1):0] |                         |
| bb_gain2_rot90_flag | input     | wire                                 |                         |
| iq_out              | output    | [(2*IQ_DATA_WIDTH-1):0]              |  output data            |
## Signals

| Name          | Type                                                | Description |
| ------------- | --------------------------------------------------- | ----------- |
| i0            | wire [(IQ_DATA_WIDTH-1) : 0]                        |             |
| q0            | wire [(IQ_DATA_WIDTH-1) : 0]                        |             |
| i1            | reg  signed [(IQ_DATA_WIDTH-1) : 0]                 |             |
| q1            | reg  signed [(IQ_DATA_WIDTH-1) : 0]                 |             |
| i2            | reg  signed [(IQ_DATA_WIDTH-1) : 0]                 |             |
| q2            | reg  signed [(IQ_DATA_WIDTH-1) : 0]                 |             |
| tap1_result_i | reg signed [(CSI_FUZZER_WIDTH+IQ_DATA_WIDTH-1) : 0] |             |
| tap1_result_q | reg signed [(CSI_FUZZER_WIDTH+IQ_DATA_WIDTH-1) : 0] |             |
| tap2_result_i | reg signed [(CSI_FUZZER_WIDTH+IQ_DATA_WIDTH-1) : 0] |             |
| tap2_result_q | reg signed [(CSI_FUZZER_WIDTH+IQ_DATA_WIDTH-1) : 0] |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
**Description**
 delay samples for different taps 
