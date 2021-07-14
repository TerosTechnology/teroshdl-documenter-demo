# Entity: axi_axil_adapter_rd

## Diagram

![Diagram](axi_axil_adapter_rd.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name         | Type | Value                                     | Description                                                                                                 |
| -------------------- | ---- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| ADDR_WIDTH           |      | 32                                        | Width of address bus in bits                                                                                |
| AXI_DATA_WIDTH       |      | 32                                        | Width of input (slave) AXI interface data bus in bits                                                       |
| AXI_STRB_WIDTH       |      | undefined                                 | Width of input (slave) AXI interface wstrb (width of data bus in words)                                     |
| AXI_ID_WIDTH         |      | 8                                         | Width of AXI ID signal                                                                                      |
| AXIL_DATA_WIDTH      |      | 32                                        | Width of output (master) AXI lite interface data bus in bits                                                |
| AXIL_STRB_WIDTH      |      | undefined                                 | Width of output (master) AXI lite interface wstrb (width of data bus in words)                              |
| CONVERT_BURST        |      | 1                                         | When adapting to a wider bus, re-pack full-width burst instead of passing through narrow burst if possible  |
| CONVERT_NARROW_BURST |      | 0                                         | When adapting to a wider bus, re-pack all bursts instead of passing through narrow burst if possible        |
| AXI_ADDR_BIT_OFFSET  |      | $clog2(AXI_STRB_WIDTH)                    |                                                                                                             |
| AXIL_ADDR_BIT_OFFSET |      | $clog2(AXIL_STRB_WIDTH)                   |                                                                                                             |
| AXI_WORD_WIDTH       |      | AXI_STRB_WIDTH                            |                                                                                                             |
| AXIL_WORD_WIDTH      |      | AXIL_STRB_WIDTH                           |                                                                                                             |
| AXI_WORD_SIZE        |      | AXI_DATA_WIDTH/AXI_WORD_WIDTH             |                                                                                                             |
| AXIL_WORD_SIZE       |      | AXIL_DATA_WIDTH/AXIL_WORD_WIDTH           |                                                                                                             |
| AXI_BURST_SIZE       |      | $clog2(AXI_STRB_WIDTH)                    |                                                                                                             |
| AXIL_BURST_SIZE      |      | $clog2(AXIL_STRB_WIDTH)                   |                                                                                                             |
| EXPAND               |      | AXIL_STRB_WIDTH > AXI_STRB_WIDTH          | output bus is wider                                                                                         |
| DATA_WIDTH           |      | EXPAND ? AXIL_DATA_WIDTH : AXI_DATA_WIDTH |                                                                                                             |
| STRB_WIDTH           |      | EXPAND ? AXIL_STRB_WIDTH : AXI_STRB_WIDTH |                                                                                                             |
| SEGMENT_COUNT        |      | undefined                                 | required number of segments in wider bus                                                                    |
| SEGMENT_DATA_WIDTH   |      | DATA_WIDTH / SEGMENT_COUNT                | data width and keep width per segment                                                                       |
| SEGMENT_STRB_WIDTH   |      | STRB_WIDTH / SEGMENT_COUNT                |                                                                                                             |
## Ports

| Port name      | Direction | Type                       | Description |
| -------------- | --------- | -------------------------- | ----------- |
| clk            | input     | wire                       |             |
| rst            | input     | wire                       |             |
| s_axi_arid     | input     | wire [AXI_ID_WIDTH-1:0]    |             |
| s_axi_araddr   | input     | wire [ADDR_WIDTH-1:0]      |             |
| s_axi_arlen    | input     | wire [7:0]                 |             |
| s_axi_arsize   | input     | wire [2:0]                 |             |
| s_axi_arburst  | input     | wire [1:0]                 |             |
| s_axi_arlock   | input     | wire                       |             |
| s_axi_arcache  | input     | wire [3:0]                 |             |
| s_axi_arprot   | input     | wire [2:0]                 |             |
| s_axi_arvalid  | input     | wire                       |             |
| s_axi_arready  | output    | wire                       |             |
| s_axi_rid      | output    | wire [AXI_ID_WIDTH-1:0]    |             |
| s_axi_rdata    | output    | wire [AXI_DATA_WIDTH-1:0]  |             |
| s_axi_rresp    | output    | wire [1:0]                 |             |
| s_axi_rlast    | output    | wire                       |             |
| s_axi_rvalid   | output    | wire                       |             |
| s_axi_rready   | input     | wire                       |             |
| m_axil_araddr  | output    | wire [ADDR_WIDTH-1:0]      |             |
| m_axil_arprot  | output    | wire [2:0]                 |             |
| m_axil_arvalid | output    | wire                       |             |
| m_axil_arready | input     | wire                       |             |
| m_axil_rdata   | input     | wire [AXIL_DATA_WIDTH-1:0] |             |
| m_axil_rresp   | input     | wire [1:0]                 |             |
| m_axil_rvalid  | input     | wire                       |             |
| m_axil_rready  | output    | wire                       |             |
## Signals

| Name                   | Type                     | Description |
| ---------------------- | ------------------------ | ----------- |
| state_reg              | reg [1:0]                |             |
| state_next             | reg [1:0]                |             |
| id_reg                 | reg [AXI_ID_WIDTH-1:0]   |             |
| id_next                | reg [AXI_ID_WIDTH-1:0]   |             |
| addr_reg               | reg [ADDR_WIDTH-1:0]     |             |
| addr_next              | reg [ADDR_WIDTH-1:0]     |             |
| data_reg               | reg [DATA_WIDTH-1:0]     |             |
| data_next              | reg [DATA_WIDTH-1:0]     |             |
| resp_reg               | reg [1:0]                |             |
| resp_next              | reg [1:0]                |             |
| burst_reg              | reg [7:0]                |             |
| burst_next             | reg [7:0]                |             |
| burst_size_reg         | reg [2:0]                |             |
| burst_size_next        | reg [2:0]                |             |
| master_burst_reg       | reg [7:0]                |             |
| master_burst_next      | reg [7:0]                |             |
| master_burst_size_reg  | reg [2:0]                |             |
| master_burst_size_next | reg [2:0]                |             |
| s_axi_arready_reg      | reg                      |             |
| s_axi_arready_next     | reg                      |             |
| s_axi_rid_reg          | reg [AXI_ID_WIDTH-1:0]   |             |
| s_axi_rid_next         | reg [AXI_ID_WIDTH-1:0]   |             |
| s_axi_rdata_reg        | reg [AXI_DATA_WIDTH-1:0] |             |
| s_axi_rdata_next       | reg [AXI_DATA_WIDTH-1:0] |             |
| s_axi_rresp_reg        | reg [1:0]                |             |
| s_axi_rresp_next       | reg [1:0]                |             |
| s_axi_rlast_reg        | reg                      |             |
| s_axi_rlast_next       | reg                      |             |
| s_axi_rvalid_reg       | reg                      |             |
| s_axi_rvalid_next      | reg                      |             |
| m_axil_araddr_reg      | reg [ADDR_WIDTH-1:0]     |             |
| m_axil_araddr_next     | reg [ADDR_WIDTH-1:0]     |             |
| m_axil_arprot_reg      | reg [2:0]                |             |
| m_axil_arprot_next     | reg [2:0]                |             |
| m_axil_arvalid_reg     | reg                      |             |
| m_axil_arvalid_next    | reg                      |             |
| m_axil_rready_reg      | reg                      |             |
| m_axil_rready_next     | reg                      |             |
## Constants

| Name             | Type  | Value | Description |
| ---------------- | ----- | ----- | ----------- |
| STATE_IDLE       | [1:0] | 2'd0  |             |
| STATE_DATA       | [1:0] | 2'd1  |             |
| STATE_DATA_READ  | [1:0] | 2'd2  |             |
| STATE_DATA_SPLIT | [1:0] | 2'd3  |             |
## Processes
- unnamed: ( @* )
- unnamed: ( @(posedge clk) )
