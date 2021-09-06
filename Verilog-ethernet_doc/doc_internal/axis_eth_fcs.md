# Entity: axis_eth_fcs

- **File**: axis_eth_fcs.v
## Diagram

![Diagram](axis_eth_fcs.svg "Diagram")
## Description


 Language: Verilog 2001


## Generics

| Generic name | Type | Value     | Description                                                     |
| ------------ | ---- | --------- | --------------------------------------------------------------- |
| DATA_WIDTH   |      | 8         |  Width of AXI stream interfaces in bits                         |
| KEEP_ENABLE  |      | undefined |  Propagate tkeep signal  If disabled, tkeep assumed to be 1'b1  |
| KEEP_WIDTH   |      | undefined |  tkeep signal width (words per cycle)                           |
## Ports

| Port name        | Direction | Type                  | Description                |
| ---------------- | --------- | --------------------- | -------------------------- |
| clk              | input     | wire                  |                            |
| rst              | input     | wire                  |                            |
| s_axis_tdata     | input     | wire [DATA_WIDTH-1:0] |      * AXI input      */   |
| s_axis_tkeep     | input     | wire [KEEP_WIDTH-1:0] |                            |
| s_axis_tvalid    | input     | wire                  |                            |
| s_axis_tready    | output    | wire                  |                            |
| s_axis_tlast     | input     | wire                  |                            |
| s_axis_tuser     | input     | wire                  |                            |
| output_fcs       | output    | wire [31:0]           |      * FCS output      */  |
| output_fcs_valid | output    | wire                  |                            |
## Signals

| Name          | Type        | Description |
| ------------- | ----------- | ----------- |
| crc_state     | reg [31:0]  |             |
| fcs_reg       | reg [31:0]  |             |
| fcs_valid_reg | reg         |             |
| crc_next      | wire [31:0] |             |
| i             | integer     |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
