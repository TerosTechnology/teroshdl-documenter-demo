# Entity: iq_abs_avg

## Diagram

![Diagram](iq_abs_avg.svg "Diagram")
## Description

Xianjun jiao. putaoshu@msn.com; xianjun.jiao@imec.be;
 
## Generics

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| IQ_DATA_WIDTH | integer | 16    |             |
## Ports

| Port name     | Direction | Type                              | Description                  |
| ------------- | --------- | --------------------------------- | ---------------------------- |
| clk           | input     | wire                              |                              |
| rstn          | input     | wire                              |                              |
| ddc_i         | input     | wire signed [(IQ_DATA_WIDTH-1):0] | Ports to receive IQ from DDC |
| ddc_q         | input     | wire signed [(IQ_DATA_WIDTH-1):0] |                              |
| ddc_iq_valid  | input     | wire                              |                              |
| iq_rssi       | output    | wire signed [(IQ_DATA_WIDTH-1):0] | result outputs               |
| iq_rssi_valid | output    | wire                              |                              |
## Signals

| Name                      | Type                         | Description |
| ------------------------- | ---------------------------- | ----------- |
| i_dc_rm                   | wire [(IQ_DATA_WIDTH-1):0]   |             |
| q_dc_rm                   | wire [(IQ_DATA_WIDTH-1):0]   |             |
| iq_dc_rm_valid            | wire                         |             |
| i_abs                     | wire [(IQ_DATA_WIDTH-1):0]   |             |
| q_abs                     | wire [(IQ_DATA_WIDTH-1):0]   |             |
| iq_abs_mv_avg             | wire [(2*IQ_DATA_WIDTH-1):0] |             |
| iq_abs_avg_ready_internal | wire                         |             |
## Instantiations

- dc_rm_i: dc_rm
- mv_avg32_i: mv_avg32
