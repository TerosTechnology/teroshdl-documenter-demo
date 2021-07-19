# Entity: axi_fifo_wr

- **File**: axi_fifo_wr.v
## Diagram

![Diagram](axi_fifo_wr.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name    | Type | Value                    | Description                                               |
| --------------- | ---- | ------------------------ | --------------------------------------------------------- |
| DATA_WIDTH      |      | 32                       | Width of data bus in bits                                 |
| ADDR_WIDTH      |      | 32                       | Width of address bus in bits                              |
| STRB_WIDTH      |      | undefined                | Width of wstrb (width of data bus in words)               |
| ID_WIDTH        |      | 8                        | Width of ID signal                                        |
| AWUSER_ENABLE   |      | 0                        | Propagate awuser signal                                   |
| AWUSER_WIDTH    |      | 1                        | Width of awuser signal                                    |
| WUSER_ENABLE    |      | 0                        | Propagate wuser signal                                    |
| WUSER_WIDTH     |      | 1                        | Width of wuser signal                                     |
| BUSER_ENABLE    |      | 0                        | Propagate buser signal                                    |
| BUSER_WIDTH     |      | 1                        | Width of buser signal                                     |
| FIFO_DEPTH      |      | 32                       | Write data FIFO depth (cycles)                            |
| FIFO_DELAY      |      | 0                        | Hold write address until write data in FIFO, if possible  |
| STRB_OFFSET     |      | DATA_WIDTH               |                                                           |
| LAST_OFFSET     |      | STRB_OFFSET + STRB_WIDTH |                                                           |
| WUSER_OFFSET    |      | LAST_OFFSET + 1          |                                                           |
| WWIDTH          |      | WUSER_OFFSET             |                                                           |
| FIFO_ADDR_WIDTH |      | $clog2(FIFO_DEPTH)       |                                                           |
## Ports

| Port name      | Direction | Type                    | Description |
| -------------- | --------- | ----------------------- | ----------- |
| clk            | input     | wire                    |             |
| rst            | input     | wire                    |             |
| s_axi_awid     | input     | wire [ID_WIDTH-1:0]     |             |
| s_axi_awaddr   | input     | wire [ADDR_WIDTH-1:0]   |             |
| s_axi_awlen    | input     | wire [7:0]              |             |
| s_axi_awsize   | input     | wire [2:0]              |             |
| s_axi_awburst  | input     | wire [1:0]              |             |
| s_axi_awlock   | input     | wire                    |             |
| s_axi_awcache  | input     | wire [3:0]              |             |
| s_axi_awprot   | input     | wire [2:0]              |             |
| s_axi_awqos    | input     | wire [3:0]              |             |
| s_axi_awregion | input     | wire [3:0]              |             |
| s_axi_awuser   | input     | wire [AWUSER_WIDTH-1:0] |             |
| s_axi_awvalid  | input     | wire                    |             |
| s_axi_awready  | output    | wire                    |             |
| s_axi_wdata    | input     | wire [DATA_WIDTH-1:0]   |             |
| s_axi_wstrb    | input     | wire [STRB_WIDTH-1:0]   |             |
| s_axi_wlast    | input     | wire                    |             |
| s_axi_wuser    | input     | wire [WUSER_WIDTH-1:0]  |             |
| s_axi_wvalid   | input     | wire                    |             |
| s_axi_wready   | output    | wire                    |             |
| s_axi_bid      | output    | wire [ID_WIDTH-1:0]     |             |
| s_axi_bresp    | output    | wire [1:0]              |             |
| s_axi_buser    | output    | wire [BUSER_WIDTH-1:0]  |             |
| s_axi_bvalid   | output    | wire                    |             |
| s_axi_bready   | input     | wire                    |             |
| m_axi_awid     | output    | wire [ID_WIDTH-1:0]     |             |
| m_axi_awaddr   | output    | wire [ADDR_WIDTH-1:0]   |             |
| m_axi_awlen    | output    | wire [7:0]              |             |
| m_axi_awsize   | output    | wire [2:0]              |             |
| m_axi_awburst  | output    | wire [1:0]              |             |
| m_axi_awlock   | output    | wire                    |             |
| m_axi_awcache  | output    | wire [3:0]              |             |
| m_axi_awprot   | output    | wire [2:0]              |             |
| m_axi_awqos    | output    | wire [3:0]              |             |
| m_axi_awregion | output    | wire [3:0]              |             |
| m_axi_awuser   | output    | wire [AWUSER_WIDTH-1:0] |             |
| m_axi_awvalid  | output    | wire                    |             |
| m_axi_awready  | input     | wire                    |             |
| m_axi_wdata    | output    | wire [DATA_WIDTH-1:0]   |             |
| m_axi_wstrb    | output    | wire [STRB_WIDTH-1:0]   |             |
| m_axi_wlast    | output    | wire                    |             |
| m_axi_wuser    | output    | wire [WUSER_WIDTH-1:0]  |             |
| m_axi_wvalid   | output    | wire                    |             |
| m_axi_wready   | input     | wire                    |             |
| m_axi_bid      | input     | wire [ID_WIDTH-1:0]     |             |
| m_axi_bresp    | input     | wire [1:0]              |             |
| m_axi_buser    | input     | wire [BUSER_WIDTH-1:0]  |             |
| m_axi_bvalid   | input     | wire                    |             |
| m_axi_bready   | output    | wire                    |             |
## Signals

| Name                     | Type                    | Description                                  |
| ------------------------ | ----------------------- | -------------------------------------------- |
| wr_ptr_reg               | reg [FIFO_ADDR_WIDTH:0] |                                              |
| wr_ptr_next              | reg [FIFO_ADDR_WIDTH:0] |                                              |
| wr_addr_reg              | reg [FIFO_ADDR_WIDTH:0] |                                              |
| rd_ptr_reg               | reg [FIFO_ADDR_WIDTH:0] |                                              |
| rd_ptr_next              | reg [FIFO_ADDR_WIDTH:0] |                                              |
| rd_addr_reg              | reg [FIFO_ADDR_WIDTH:0] |                                              |
| mem                      | reg [WWIDTH-1:0]        |                                              |
| mem_read_data_reg        | reg [WWIDTH-1:0]        |                                              |
| mem_read_data_valid_reg  | reg                     |                                              |
| mem_read_data_valid_next | reg                     |                                              |
| s_axi_w                  | wire [WWIDTH-1:0]       |                                              |
| m_axi_w_reg              | reg [WWIDTH-1:0]        |                                              |
| m_axi_wvalid_reg         | reg                     |                                              |
| m_axi_wvalid_next        | reg                     |                                              |
| full                     | wire                    | full when first MSB different but rest same  |
| empty                    | wire                    | empty when pointers match exactly            |
| hold                     | wire                    |                                              |
| write                    | reg                     | control signals                              |
| read                     | reg                     |                                              |
| store_output             | reg                     |                                              |
## Processes
- unnamed: ( @* )
**Description**
Write logic

- unnamed: ( @(posedge clk) )
- unnamed: ( @* )
**Description**
Read logic

- unnamed: ( @(posedge clk) )
- unnamed: ( @* )
**Description**
Output register

- unnamed: ( @(posedge clk) )
