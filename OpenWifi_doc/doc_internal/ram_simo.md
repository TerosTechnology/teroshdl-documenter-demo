# Entity: ram_simo

- **File**: ram_simo.v
## Diagram

![Diagram](ram_simo.svg "Diagram")
## Description



## Ports

| Port name | Direction | Type                       | Description |
| --------- | --------- | -------------------------- | ----------- |
| clk       | input     | wire                       |             |
| waddr     | input     | wire [$clog2(DEPTH*8)-1:0] |             |
| raddr     | input     | wire [$clog2(DEPTH)-1:0]   |             |
| wen       | input     | wire                       |             |
| data_i    | input     | wire                       |             |
| data_o    | output    | wire [5:0]                 |             |
## Signals

| Name | Type               | Description |
| ---- | ------------------ | ----------- |
| mem  | reg  [DEPTH*8-1:0] |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
**Description**
 Data is latched on the positive edge of the clock 
