# Entity: dc_rm

- **File**: dc_rm.v
## Diagram

![Diagram](dc_rm.svg "Diagram")
## Description

Xianjun jiao. putaoshu@msn.com; xianjun.jiao@imec.be;
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| DATA_WIDTH   |      | 16    |             |
## Ports

| Port name      | Direction | Type                           | Description |
| -------------- | --------- | ------------------------------ | ----------- |
| clk            | input     | wire                           |             |
| rstn           | input     | wire                           |             |
| ddc_i          | input     | wire signed [(DATA_WIDTH-1):0] |             |
| ddc_q          | input     | wire signed [(DATA_WIDTH-1):0] |             |
| ddc_iq_valid   | input     | wire                           |             |
| i_dc_rm        | output    | wire signed [(DATA_WIDTH-1):0] |             |
| q_dc_rm        | output    | wire signed [(DATA_WIDTH-1):0] |             |
| iq_dc_rm_valid | output    | wire                           |             |
## Signals

| Name                  | Type                      | Description |
| --------------------- | ------------------------- | ----------- |
| ddc_i_mv_avg          | wire [DATA_WIDTH-1:0]     |             |
| ddc_q_mv_avg          | wire [DATA_WIDTH-1:0]     |             |
| dc_rm_mv_avg_internal | wire [(2*DATA_WIDTH-1):0] |             |
| dc_rm_ready_internal  | wire                      |             |
## Instantiations

- mv_avg128_i: mv_avg128
