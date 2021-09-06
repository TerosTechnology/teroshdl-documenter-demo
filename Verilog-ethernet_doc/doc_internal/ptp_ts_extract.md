# Entity: ptp_ts_extract

- **File**: ptp_ts_extract.v
## Diagram

![Diagram](ptp_ts_extract.svg "Diagram")
## Description


 Language: Verilog 2001


## Generics

| Generic name | Type | Value              | Description |
| ------------ | ---- | ------------------ | ----------- |
| TS_WIDTH     |      | 96                 |             |
| TS_OFFSET    |      | 1                  |             |
| USER_WIDTH   |      | TS_WIDTH+TS_OFFSET |             |
## Ports

| Port name       | Direction | Type                  | Description                      |
| --------------- | --------- | --------------------- | -------------------------------- |
| clk             | input     | wire                  |                                  |
| rst             | input     | wire                  |                                  |
| s_axis_tvalid   | input     | wire                  |      * AXI stream input      */  |
| s_axis_tlast    | input     | wire                  |                                  |
| s_axis_tuser    | input     | wire [USER_WIDTH-1:0] |                                  |
| m_axis_ts       | output    | wire [TS_WIDTH-1:0]   |      * Timestamp output      */  |
| m_axis_ts_valid | output    | wire                  |                                  |
## Signals

| Name      | Type | Description |
| --------- | ---- | ----------- |
| frame_reg | reg  |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
