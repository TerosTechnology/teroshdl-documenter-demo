# Entity: axil_reg_if_rd

- **File**: axil_reg_if_rd.v
## Diagram

![Diagram](axil_reg_if_rd.svg "Diagram")
## Description


 Language: Verilog 2001


## Generics

| Generic name  | Type | Value           | Description                                   |
| ------------- | ---- | --------------- | --------------------------------------------- |
| DATA_WIDTH    |      | 32              |  Width of data bus in bits                    |
| ADDR_WIDTH    |      | 32              |  Width of address bus in bits                 |
| STRB_WIDTH    |      | undefined       |  Width of wstrb (width of data bus in words)  |
| TIMEOUT       |      | 4               |  Timeout delay (cycles)                       |
| TIMEOUT_WIDTH |      | $clog2(TIMEOUT) |                                               |
## Ports

| Port name      | Direction | Type                  | Description                              |
| -------------- | --------- | --------------------- | ---------------------------------------- |
| clk            | input     | wire                  |                                          |
| rst            | input     | wire                  |                                          |
| s_axil_araddr  | input     | wire [ADDR_WIDTH-1:0] |      * AXI-Lite slave interface      */  |
| s_axil_arprot  | input     | wire [2:0]            |                                          |
| s_axil_arvalid | input     | wire                  |                                          |
| s_axil_arready | output    | wire                  |                                          |
| s_axil_rdata   | output    | wire [DATA_WIDTH-1:0] |                                          |
| s_axil_rresp   | output    | wire [1:0]            |                                          |
| s_axil_rvalid  | output    | wire                  |                                          |
| s_axil_rready  | input     | wire                  |                                          |
| reg_rd_addr    | output    | wire [ADDR_WIDTH-1:0] |      * Register interface      */        |
| reg_rd_en      | output    | wire                  |                                          |
| reg_rd_data    | input     | wire [DATA_WIDTH-1:0] |                                          |
| reg_rd_wait    | input     | wire                  |                                          |
| reg_rd_ack     | input     | wire                  |                                          |
## Signals

| Name                | Type                    | Description |
| ------------------- | ----------------------- | ----------- |
| timeout_count_reg   | reg [TIMEOUT_WIDTH-1:0] |             |
| timeout_count_next  | reg [TIMEOUT_WIDTH-1:0] |             |
| s_axil_araddr_reg   | reg [ADDR_WIDTH-1:0]    |             |
| s_axil_araddr_next  | reg [ADDR_WIDTH-1:0]    |             |
| s_axil_arvalid_reg  | reg                     |             |
| s_axil_arvalid_next | reg                     |             |
| s_axil_rdata_reg    | reg [DATA_WIDTH-1:0]    |             |
| s_axil_rdata_next   | reg [DATA_WIDTH-1:0]    |             |
| s_axil_rvalid_reg   | reg                     |             |
| s_axil_rvalid_next  | reg                     |             |
| reg_rd_en_reg       | reg                     |             |
| reg_rd_en_next      | reg                     |             |
## Processes
- unnamed: ( @* )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
