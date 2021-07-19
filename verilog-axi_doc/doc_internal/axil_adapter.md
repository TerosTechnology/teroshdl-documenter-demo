# Entity: axil_adapter

- **File**: axil_adapter.v
## Diagram

![Diagram](axil_adapter.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name | Type | Value     | Description                                                            |
| ------------ | ---- | --------- | ---------------------------------------------------------------------- |
| ADDR_WIDTH   |      | 32        | Width of address bus in bits                                           |
| S_DATA_WIDTH |      | 32        | Width of input (slave) interface data bus in bits                      |
| S_STRB_WIDTH |      | undefined | Width of input (slave) interface wstrb (width of data bus in words)    |
| M_DATA_WIDTH |      | 32        | Width of output (master) interface data bus in bits                    |
| M_STRB_WIDTH |      | undefined | Width of output (master) interface wstrb (width of data bus in words)  |
## Ports

| Port name      | Direction | Type                    | Description |
| -------------- | --------- | ----------------------- | ----------- |
| clk            | input     | wire                    |             |
| rst            | input     | wire                    |             |
| s_axil_awaddr  | input     | wire [ADDR_WIDTH-1:0]   |             |
| s_axil_awprot  | input     | wire [2:0]              |             |
| s_axil_awvalid | input     | wire                    |             |
| s_axil_awready | output    | wire                    |             |
| s_axil_wdata   | input     | wire [S_DATA_WIDTH-1:0] |             |
| s_axil_wstrb   | input     | wire [S_STRB_WIDTH-1:0] |             |
| s_axil_wvalid  | input     | wire                    |             |
| s_axil_wready  | output    | wire                    |             |
| s_axil_bresp   | output    | wire [1:0]              |             |
| s_axil_bvalid  | output    | wire                    |             |
| s_axil_bready  | input     | wire                    |             |
| s_axil_araddr  | input     | wire [ADDR_WIDTH-1:0]   |             |
| s_axil_arprot  | input     | wire [2:0]              |             |
| s_axil_arvalid | input     | wire                    |             |
| s_axil_arready | output    | wire                    |             |
| s_axil_rdata   | output    | wire [S_DATA_WIDTH-1:0] |             |
| s_axil_rresp   | output    | wire [1:0]              |             |
| s_axil_rvalid  | output    | wire                    |             |
| s_axil_rready  | input     | wire                    |             |
| m_axil_awaddr  | output    | wire [ADDR_WIDTH-1:0]   |             |
| m_axil_awprot  | output    | wire [2:0]              |             |
| m_axil_awvalid | output    | wire                    |             |
| m_axil_awready | input     | wire                    |             |
| m_axil_wdata   | output    | wire [M_DATA_WIDTH-1:0] |             |
| m_axil_wstrb   | output    | wire [M_STRB_WIDTH-1:0] |             |
| m_axil_wvalid  | output    | wire                    |             |
| m_axil_wready  | input     | wire                    |             |
| m_axil_bresp   | input     | wire [1:0]              |             |
| m_axil_bvalid  | input     | wire                    |             |
| m_axil_bready  | output    | wire                    |             |
| m_axil_araddr  | output    | wire [ADDR_WIDTH-1:0]   |             |
| m_axil_arprot  | output    | wire [2:0]              |             |
| m_axil_arvalid | output    | wire                    |             |
| m_axil_arready | input     | wire                    |             |
| m_axil_rdata   | input     | wire [M_DATA_WIDTH-1:0] |             |
| m_axil_rresp   | input     | wire [1:0]              |             |
| m_axil_rvalid  | input     | wire                    |             |
| m_axil_rready  | output    | wire                    |             |
## Instantiations

- axil_adapter_wr_inst: axil_adapter_wr
- axil_adapter_rd_inst: axil_adapter_rd
