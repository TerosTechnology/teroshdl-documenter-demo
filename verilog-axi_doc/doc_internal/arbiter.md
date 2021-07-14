# Entity: arbiter

## Diagram

![Diagram](arbiter.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name          | Type | Value | Description                                                        |
| --------------------- | ---- | ----- | ------------------------------------------------------------------ |
| PORTS                 |      | 4     |                                                                    |
| ARB_TYPE_ROUND_ROBIN  |      | 0     | select round robin arbitration                                     |
| ARB_BLOCK             |      | 0     | blocking arbiter enable                                            |
| ARB_BLOCK_ACK         |      | 1     | block on acknowledge assert when nonzero, request deassert when 0  |
| ARB_LSB_HIGH_PRIORITY |      | 0     | LSB priority selection                                             |
## Ports

| Port name     | Direction | Type                     | Description |
| ------------- | --------- | ------------------------ | ----------- |
| clk           | input     | wire                     |             |
| rst           | input     | wire                     |             |
| request       | input     | wire [PORTS-1:0]         |             |
| acknowledge   | input     | wire [PORTS-1:0]         |             |
| grant         | output    | wire [PORTS-1:0]         |             |
| grant_valid   | output    | wire                     |             |
| grant_encoded | output    | wire [$clog2(PORTS)-1:0] |             |
## Signals

| Name                 | Type                     | Description |
| -------------------- | ------------------------ | ----------- |
| grant_reg            | reg [PORTS-1:0]          |             |
| grant_next           | reg [PORTS-1:0]          |             |
| grant_valid_reg      | reg                      |             |
| grant_valid_next     | reg                      |             |
| grant_encoded_reg    | reg [$clog2(PORTS)-1:0]  |             |
| grant_encoded_next   | reg [$clog2(PORTS)-1:0]  |             |
| request_valid        | wire                     |             |
| request_index        | wire [$clog2(PORTS)-1:0] |             |
| request_mask         | wire [PORTS-1:0]         |             |
| mask_reg             | reg [PORTS-1:0]          |             |
| mask_next            | reg [PORTS-1:0]          |             |
| masked_request_valid | wire                     |             |
| masked_request_index | wire [$clog2(PORTS)-1:0] |             |
| masked_request_mask  | wire [PORTS-1:0]         |             |
## Processes
- unnamed: ( @* )
- unnamed: ( @(posedge clk) )
## Instantiations

- priority_encoder_inst: priority_encoder
- priority_encoder_masked: priority_encoder
