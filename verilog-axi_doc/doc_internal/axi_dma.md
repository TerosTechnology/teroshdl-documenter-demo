# Entity: axi_dma

## Diagram

![Diagram](axi_dma.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name      | Type | Value          | Description                                                                        |
| ----------------- | ---- | -------------- | ---------------------------------------------------------------------------------- |
| AXI_DATA_WIDTH    |      | 32             | Width of AXI data bus in bits                                                      |
| AXI_ADDR_WIDTH    |      | 16             | Width of AXI address bus in bits                                                   |
| AXI_STRB_WIDTH    |      | undefined      | Width of AXI wstrb (width of data bus in words)                                    |
| AXI_ID_WIDTH      |      | 8              | Width of AXI ID signal                                                             |
| AXI_MAX_BURST_LEN |      | 16             | Maximum AXI burst length to generate                                               |
| AXIS_DATA_WIDTH   |      | AXI_DATA_WIDTH | Width of AXI stream interfaces in bits                                             |
| AXIS_KEEP_ENABLE  |      | undefined      | Use AXI stream tkeep signal                                                        |
| AXIS_KEEP_WIDTH   |      | undefined      | AXI stream tkeep signal width (words per cycle)                                    |
| AXIS_LAST_ENABLE  |      | 1              | Use AXI stream tlast signal                                                        |
| AXIS_ID_ENABLE    |      | 0              | Propagate AXI stream tid signal                                                    |
| AXIS_ID_WIDTH     |      | 8              | AXI stream tid signal width                                                        |
| AXIS_DEST_ENABLE  |      | 0              | Propagate AXI stream tdest signal                                                  |
| AXIS_DEST_WIDTH   |      | 8              | AXI stream tdest signal width                                                      |
| AXIS_USER_ENABLE  |      | 1              | Propagate AXI stream tuser signal                                                  |
| AXIS_USER_WIDTH   |      | 1              | AXI stream tuser signal width                                                      |
| LEN_WIDTH         |      | 20             | Width of length field                                                              |
| TAG_WIDTH         |      | 8              | Width of tag field                                                                 |
| ENABLE_SG         |      | 0              | Enable support for scatter/gather DMA (multiple descriptors per AXI stream frame)  |
| ENABLE_UNALIGNED  |      | 0              | Enable support for unaligned transfers                                             |
## Ports

| Port name                      | Direction | Type                       | Description |
| ------------------------------ | --------- | -------------------------- | ----------- |
| clk                            | input     | wire                       |             |
| rst                            | input     | wire                       |             |
| s_axis_read_desc_addr          | input     | wire [AXI_ADDR_WIDTH-1:0]  |             |
| s_axis_read_desc_len           | input     | wire [LEN_WIDTH-1:0]       |             |
| s_axis_read_desc_tag           | input     | wire [TAG_WIDTH-1:0]       |             |
| s_axis_read_desc_id            | input     | wire [AXIS_ID_WIDTH-1:0]   |             |
| s_axis_read_desc_dest          | input     | wire [AXIS_DEST_WIDTH-1:0] |             |
| s_axis_read_desc_user          | input     | wire [AXIS_USER_WIDTH-1:0] |             |
| s_axis_read_desc_valid         | input     | wire                       |             |
| s_axis_read_desc_ready         | output    | wire                       |             |
| m_axis_read_desc_status_tag    | output    | wire [TAG_WIDTH-1:0]       |             |
| m_axis_read_desc_status_valid  | output    | wire                       |             |
| m_axis_read_data_tdata         | output    | wire [AXIS_DATA_WIDTH-1:0] |             |
| m_axis_read_data_tkeep         | output    | wire [AXIS_KEEP_WIDTH-1:0] |             |
| m_axis_read_data_tvalid        | output    | wire                       |             |
| m_axis_read_data_tready        | input     | wire                       |             |
| m_axis_read_data_tlast         | output    | wire                       |             |
| m_axis_read_data_tid           | output    | wire [AXIS_ID_WIDTH-1:0]   |             |
| m_axis_read_data_tdest         | output    | wire [AXIS_DEST_WIDTH-1:0] |             |
| m_axis_read_data_tuser         | output    | wire [AXIS_USER_WIDTH-1:0] |             |
| s_axis_write_desc_addr         | input     | wire [AXI_ADDR_WIDTH-1:0]  |             |
| s_axis_write_desc_len          | input     | wire [LEN_WIDTH-1:0]       |             |
| s_axis_write_desc_tag          | input     | wire [TAG_WIDTH-1:0]       |             |
| s_axis_write_desc_valid        | input     | wire                       |             |
| s_axis_write_desc_ready        | output    | wire                       |             |
| m_axis_write_desc_status_len   | output    | wire [LEN_WIDTH-1:0]       |             |
| m_axis_write_desc_status_tag   | output    | wire [TAG_WIDTH-1:0]       |             |
| m_axis_write_desc_status_id    | output    | wire [AXIS_ID_WIDTH-1:0]   |             |
| m_axis_write_desc_status_dest  | output    | wire [AXIS_DEST_WIDTH-1:0] |             |
| m_axis_write_desc_status_user  | output    | wire [AXIS_USER_WIDTH-1:0] |             |
| m_axis_write_desc_status_valid | output    | wire                       |             |
| s_axis_write_data_tdata        | input     | wire [AXIS_DATA_WIDTH-1:0] |             |
| s_axis_write_data_tkeep        | input     | wire [AXIS_KEEP_WIDTH-1:0] |             |
| s_axis_write_data_tvalid       | input     | wire                       |             |
| s_axis_write_data_tready       | output    | wire                       |             |
| s_axis_write_data_tlast        | input     | wire                       |             |
| s_axis_write_data_tid          | input     | wire [AXIS_ID_WIDTH-1:0]   |             |
| s_axis_write_data_tdest        | input     | wire [AXIS_DEST_WIDTH-1:0] |             |
| s_axis_write_data_tuser        | input     | wire [AXIS_USER_WIDTH-1:0] |             |
| m_axi_awid                     | output    | wire [AXI_ID_WIDTH-1:0]    |             |
| m_axi_awaddr                   | output    | wire [AXI_ADDR_WIDTH-1:0]  |             |
| m_axi_awlen                    | output    | wire [7:0]                 |             |
| m_axi_awsize                   | output    | wire [2:0]                 |             |
| m_axi_awburst                  | output    | wire [1:0]                 |             |
| m_axi_awlock                   | output    | wire                       |             |
| m_axi_awcache                  | output    | wire [3:0]                 |             |
| m_axi_awprot                   | output    | wire [2:0]                 |             |
| m_axi_awvalid                  | output    | wire                       |             |
| m_axi_awready                  | input     | wire                       |             |
| m_axi_wdata                    | output    | wire [AXI_DATA_WIDTH-1:0]  |             |
| m_axi_wstrb                    | output    | wire [AXI_STRB_WIDTH-1:0]  |             |
| m_axi_wlast                    | output    | wire                       |             |
| m_axi_wvalid                   | output    | wire                       |             |
| m_axi_wready                   | input     | wire                       |             |
| m_axi_bid                      | input     | wire [AXI_ID_WIDTH-1:0]    |             |
| m_axi_bresp                    | input     | wire [1:0]                 |             |
| m_axi_bvalid                   | input     | wire                       |             |
| m_axi_bready                   | output    | wire                       |             |
| m_axi_arid                     | output    | wire [AXI_ID_WIDTH-1:0]    |             |
| m_axi_araddr                   | output    | wire [AXI_ADDR_WIDTH-1:0]  |             |
| m_axi_arlen                    | output    | wire [7:0]                 |             |
| m_axi_arsize                   | output    | wire [2:0]                 |             |
| m_axi_arburst                  | output    | wire [1:0]                 |             |
| m_axi_arlock                   | output    | wire                       |             |
| m_axi_arcache                  | output    | wire [3:0]                 |             |
| m_axi_arprot                   | output    | wire [2:0]                 |             |
| m_axi_arvalid                  | output    | wire                       |             |
| m_axi_arready                  | input     | wire                       |             |
| m_axi_rid                      | input     | wire [AXI_ID_WIDTH-1:0]    |             |
| m_axi_rdata                    | input     | wire [AXI_DATA_WIDTH-1:0]  |             |
| m_axi_rresp                    | input     | wire [1:0]                 |             |
| m_axi_rlast                    | input     | wire                       |             |
| m_axi_rvalid                   | input     | wire                       |             |
| m_axi_rready                   | output    | wire                       |             |
| read_enable                    | input     | wire                       |             |
| write_enable                   | input     | wire                       |             |
| write_abort                    | input     | wire                       |             |
## Instantiations

- axi_dma_rd_inst: axi_dma_rd
- axi_dma_wr_inst: axi_dma_wr
