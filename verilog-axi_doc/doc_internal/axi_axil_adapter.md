# Entity: axi_axil_adapter

- **File**: axi_axil_adapter.v
## Diagram

![Diagram](axi_axil_adapter.svg "Diagram")
## Description


 Language: Verilog 2001


## Generics

| Generic name         | Type | Value     | Description                                                                                                  |
| -------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------ |
| ADDR_WIDTH           |      | 32        |  Width of address bus in bits                                                                                |
| AXI_DATA_WIDTH       |      | 32        |  Width of input (slave) AXI interface data bus in bits                                                       |
| AXI_STRB_WIDTH       |      | undefined |  Width of input (slave) AXI interface wstrb (width of data bus in words)                                     |
| AXI_ID_WIDTH         |      | 8         |  Width of AXI ID signal                                                                                      |
| AXIL_DATA_WIDTH      |      | 32        |  Width of output (master) AXI lite interface data bus in bits                                                |
| AXIL_STRB_WIDTH      |      | undefined |  Width of output (master) AXI lite interface wstrb (width of data bus in words)                              |
| CONVERT_BURST        |      | 1         |  When adapting to a wider bus, re-pack full-width burst instead of passing through narrow burst if possible  |
| CONVERT_NARROW_BURST |      | 0         |  When adapting to a wider bus, re-pack all bursts instead of passing through narrow burst if possible        |
## Ports

| Port name      | Direction | Type                       | Description                               |
| -------------- | --------- | -------------------------- | ----------------------------------------- |
| clk            | input     | wire                       |                                           |
| rst            | input     | wire                       |                                           |
| s_axi_awid     | input     | wire [AXI_ID_WIDTH-1:0]    |      * AXI slave interface      */        |
| s_axi_awaddr   | input     | wire [ADDR_WIDTH-1:0]      |                                           |
| s_axi_awlen    | input     | wire [7:0]                 |                                           |
| s_axi_awsize   | input     | wire [2:0]                 |                                           |
| s_axi_awburst  | input     | wire [1:0]                 |                                           |
| s_axi_awlock   | input     | wire                       |                                           |
| s_axi_awcache  | input     | wire [3:0]                 |                                           |
| s_axi_awprot   | input     | wire [2:0]                 |                                           |
| s_axi_awvalid  | input     | wire                       |                                           |
| s_axi_awready  | output    | wire                       |                                           |
| s_axi_wdata    | input     | wire [AXI_DATA_WIDTH-1:0]  |                                           |
| s_axi_wstrb    | input     | wire [AXI_STRB_WIDTH-1:0]  |                                           |
| s_axi_wlast    | input     | wire                       |                                           |
| s_axi_wvalid   | input     | wire                       |                                           |
| s_axi_wready   | output    | wire                       |                                           |
| s_axi_bid      | output    | wire [AXI_ID_WIDTH-1:0]    |                                           |
| s_axi_bresp    | output    | wire [1:0]                 |                                           |
| s_axi_bvalid   | output    | wire                       |                                           |
| s_axi_bready   | input     | wire                       |                                           |
| s_axi_arid     | input     | wire [AXI_ID_WIDTH-1:0]    |                                           |
| s_axi_araddr   | input     | wire [ADDR_WIDTH-1:0]      |                                           |
| s_axi_arlen    | input     | wire [7:0]                 |                                           |
| s_axi_arsize   | input     | wire [2:0]                 |                                           |
| s_axi_arburst  | input     | wire [1:0]                 |                                           |
| s_axi_arlock   | input     | wire                       |                                           |
| s_axi_arcache  | input     | wire [3:0]                 |                                           |
| s_axi_arprot   | input     | wire [2:0]                 |                                           |
| s_axi_arvalid  | input     | wire                       |                                           |
| s_axi_arready  | output    | wire                       |                                           |
| s_axi_rid      | output    | wire [AXI_ID_WIDTH-1:0]    |                                           |
| s_axi_rdata    | output    | wire [AXI_DATA_WIDTH-1:0]  |                                           |
| s_axi_rresp    | output    | wire [1:0]                 |                                           |
| s_axi_rlast    | output    | wire                       |                                           |
| s_axi_rvalid   | output    | wire                       |                                           |
| s_axi_rready   | input     | wire                       |                                           |
| m_axil_awaddr  | output    | wire [ADDR_WIDTH-1:0]      |      * AXI lite master interface      */  |
| m_axil_awprot  | output    | wire [2:0]                 |                                           |
| m_axil_awvalid | output    | wire                       |                                           |
| m_axil_awready | input     | wire                       |                                           |
| m_axil_wdata   | output    | wire [AXIL_DATA_WIDTH-1:0] |                                           |
| m_axil_wstrb   | output    | wire [AXIL_STRB_WIDTH-1:0] |                                           |
| m_axil_wvalid  | output    | wire                       |                                           |
| m_axil_wready  | input     | wire                       |                                           |
| m_axil_bresp   | input     | wire [1:0]                 |                                           |
| m_axil_bvalid  | input     | wire                       |                                           |
| m_axil_bready  | output    | wire                       |                                           |
| m_axil_araddr  | output    | wire [ADDR_WIDTH-1:0]      |                                           |
| m_axil_arprot  | output    | wire [2:0]                 |                                           |
| m_axil_arvalid | output    | wire                       |                                           |
| m_axil_arready | input     | wire                       |                                           |
| m_axil_rdata   | input     | wire [AXIL_DATA_WIDTH-1:0] |                                           |
| m_axil_rresp   | input     | wire [1:0]                 |                                           |
| m_axil_rvalid  | input     | wire                       |                                           |
| m_axil_rready  | output    | wire                       |                                           |
## Instantiations

- axi_axil_adapter_wr_inst: axi_axil_adapter_wr
- axi_axil_adapter_rd_inst: axi_axil_adapter_rd
