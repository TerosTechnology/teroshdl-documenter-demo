# Entity: axil_crossbar_rd

- **File**: axil_crossbar_rd.v
## Diagram

![Diagram](axil_crossbar_rd.svg "Diagram")
## Description


 Language: Verilog 2001


## Generics

| Generic name  | Type | Value              | Description                                                                                                                                                                  |
| ------------- | ---- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S_COUNT       |      | 4                  |  Number of AXI inputs (slave interfaces)                                                                                                                                     |
| M_COUNT       |      | 4                  |  Number of AXI outputs (master interfaces)                                                                                                                                   |
| DATA_WIDTH    |      | 32                 |  Width of data bus in bits                                                                                                                                                   |
| ADDR_WIDTH    |      | 32                 |  Width of address bus in bits                                                                                                                                                |
| STRB_WIDTH    |      | undefined          |  Width of wstrb (width of data bus in words)                                                                                                                                 |
| S_ACCEPT      |      | undefined          |  Number of concurrent operations for each slave interface  S_COUNT concatenated fields of 32 bits                                                                            |
| M_REGIONS     |      | 1                  |  Number of regions per master interface                                                                                                                                      |
| M_BASE_ADDR   |      | 0                  |  Master interface base addresses  M_COUNT concatenated fields of M_REGIONS concatenated fields of ADDR_WIDTH bits  set to zero for default addressing based on M_ADDR_WIDTH  |
| M_ADDR_WIDTH  |      | undefined          |  Master interface address widths  M_COUNT concatenated fields of M_REGIONS concatenated fields of 32 bits                                                                    |
| M_CONNECT     |      | undefined          |  Read connections between interfaces  M_COUNT concatenated fields of S_COUNT bits                                                                                            |
| M_ISSUE       |      | undefined          |  Number of concurrent operations for each master interface  M_COUNT concatenated fields of 32 bits                                                                           |
| M_SECURE      |      | undefined          |  Secure master (fail operations based on awprot/arprot)  M_COUNT bits                                                                                                        |
| S_AR_REG_TYPE |      | undefined          |  Slave interface AR channel register type (input)  0 to bypass, 1 for simple buffer, 2 for skid buffer                                                                       |
| S_R_REG_TYPE  |      | undefined          |  Slave interface R channel register type (output)  0 to bypass, 1 for simple buffer, 2 for skid buffer                                                                       |
| M_AR_REG_TYPE |      | undefined          |  Master interface AR channel register type (output)  0 to bypass, 1 for simple buffer, 2 for skid buffer                                                                     |
| M_R_REG_TYPE  |      | undefined          |  Master interface R channel register type (input)  0 to bypass, 1 for simple buffer, 2 for skid buffer                                                                       |
| CL_S_COUNT    |      | $clog2(S_COUNT)    |                                                                                                                                                                              |
| CL_M_COUNT    |      | $clog2(M_COUNT)    |                                                                                                                                                                              |
| M_COUNT_P1    |      | M_COUNT+1          |                                                                                                                                                                              |
| CL_M_COUNT_P1 |      | $clog2(M_COUNT_P1) |                                                                                                                                                                              |
## Ports

| Port name      | Direction | Type                          | Description                                |
| -------------- | --------- | ----------------------------- | ------------------------------------------ |
| clk            | input     | wire                          |                                            |
| rst            | input     | wire                          |                                            |
| s_axil_araddr  | input     | wire [S_COUNT*ADDR_WIDTH-1:0] |      * AXI lite slave interfaces      */   |
| s_axil_arprot  | input     | wire [S_COUNT*3-1:0]          |                                            |
| s_axil_arvalid | input     | wire [S_COUNT-1:0]            |                                            |
| s_axil_arready | output    | wire [S_COUNT-1:0]            |                                            |
| s_axil_rdata   | output    | wire [S_COUNT*DATA_WIDTH-1:0] |                                            |
| s_axil_rresp   | output    | wire [S_COUNT*2-1:0]          |                                            |
| s_axil_rvalid  | output    | wire [S_COUNT-1:0]            |                                            |
| s_axil_rready  | input     | wire [S_COUNT-1:0]            |                                            |
| m_axil_araddr  | output    | wire [M_COUNT*ADDR_WIDTH-1:0] |      * AXI lite master interfaces      */  |
| m_axil_arprot  | output    | wire [M_COUNT*3-1:0]          |                                            |
| m_axil_arvalid | output    | wire [M_COUNT-1:0]            |                                            |
| m_axil_arready | input     | wire [M_COUNT-1:0]            |                                            |
| m_axil_rdata   | input     | wire [M_COUNT*DATA_WIDTH-1:0] |                                            |
| m_axil_rresp   | input     | wire [M_COUNT*2-1:0]          |                                            |
| m_axil_rvalid  | input     | wire [M_COUNT-1:0]            |                                            |
| m_axil_rready  | output    | wire [M_COUNT-1:0]            |                                            |
## Signals

| Name               | Type                          | Description |
| ------------------ | ----------------------------- | ----------- |
| i                  | integer                       |             |
| int_s_axil_araddr  | wire [S_COUNT*ADDR_WIDTH-1:0] |             |
| int_s_axil_arprot  | wire [S_COUNT*3-1:0]          |             |
| int_s_axil_arvalid | wire [S_COUNT-1:0]            |             |
| int_s_axil_arready | wire [S_COUNT-1:0]            |             |
| int_axil_arvalid   | wire [S_COUNT*M_COUNT-1:0]    |             |
| int_axil_arready   | wire [M_COUNT*S_COUNT-1:0]    |             |
| int_m_axil_rdata   | wire [M_COUNT*DATA_WIDTH-1:0] |             |
| int_m_axil_rresp   | wire [M_COUNT*2-1:0]          |             |
| int_m_axil_rvalid  | wire [M_COUNT-1:0]            |             |
| int_m_axil_rready  | wire [M_COUNT-1:0]            |             |
| int_axil_rvalid    | wire [M_COUNT*S_COUNT-1:0]    |             |
| int_axil_rready    | wire [S_COUNT*M_COUNT-1:0]    |             |
