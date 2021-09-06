# Entity: convenc

- **File**: convenc.v
## Diagram

![Diagram](convenc.svg "Diagram")
## Description



## Ports

| Port name | Direction | Type       | Description |
| --------- | --------- | ---------- | ----------- |
| clk       | input     | wire       |             |
| rst       | input     | wire       |             |
| enc_en    | input     | wire       |             |
| bit_in    | input     | wire       |             |
| bits_out  | output    | wire [1:0] |             |
## Signals

| Name  | Type      | Description |
| ----- | --------- | ----------- |
| state | reg [5:0] |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
