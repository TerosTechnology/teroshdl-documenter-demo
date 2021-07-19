# Entity: slv_to_sl_axi

- **File**: slv_to_sl_axi.vhd
## Diagram

![Diagram](slv_to_sl_axi.svg "Diagram")
## Generics

| Generic name         | Type    | Value | Description                                    |
| -------------------- | ------- | ----- | ---------------------------------------------- |
| SLV_SIZE             | natural | 16    |                                                |
| DEFAULT_BIT_OFFSET   | natural | 0     |                                                |
| C_S00_AXI_DATA_WIDTH | integer | 32    | Parameters of Axi Slave Bus Interface S00_AXI  |
| C_S00_AXI_ADDR_WIDTH | integer | 3     |                                                |
## Ports

| Port name       | Direction | Type                                              | Description                              |
| --------------- | --------- | ------------------------------------------------- | ---------------------------------------- |
| ref_clk_i       | in        | std_logic                                         |                                          |
| ref_rst_i       | in        | std_logic                                         |                                          |
| slv_i           | in        | std_logic_vector(SLV_SIZE-1 downto 0)             | input data                               |
| sl_o            | out       | std_logic                                         | output data                              |
| s00_axi_aclk    | in        | std_logic                                         | Ports of Axi Slave Bus Interface S00_AXI |
| s00_axi_reset   | in        | std_logic                                         |                                          |
| s00_axi_awaddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0) |                                          |
| s00_axi_awvalid | in        | std_logic                                         |                                          |
| s00_axi_awready | out       | std_logic                                         |                                          |
| s00_axi_wdata   | in        | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0) |                                          |
| s00_axi_wvalid  | in        | std_logic                                         |                                          |
| s00_axi_wready  | out       | std_logic                                         |                                          |
| s00_axi_bresp   | out       | std_logic_vector(1 downto 0)                      |                                          |
| s00_axi_bvalid  | out       | std_logic                                         |                                          |
| s00_axi_bready  | in        | std_logic                                         |                                          |
| s00_axi_araddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0) |                                          |
| s00_axi_arvalid | in        | std_logic                                         |                                          |
| s00_axi_arready | out       | std_logic                                         |                                          |
| s00_axi_rdata   | out       | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0) |                                          |
| s00_axi_rresp   | out       | std_logic_vector(1 downto 0)                      |                                          |
| s00_axi_rvalid  | out       | std_logic                                         |                                          |
| s00_axi_rready  | in        | std_logic                                         |                                          |
## Signals

| Name           | Type                                             | Description |
| -------------- | ------------------------------------------------ | ----------- |
| addr_s         | std_logic_vector(INTERNAL_ADDR_WIDTH-1 downto 0) |             |
| write_en_s     | std_logic                                        |             |
|  read_en_s     | std_logic                                        |             |
| offset_s       | std_logic_vector(OFFSET_ADDR_SZ-1 downto 0)      |             |
|  offset_sync_s | std_logic_vector(OFFSET_ADDR_SZ-1 downto 0)      |             |
| sl_s           | std_logic                                        |             |
## Constants

| Name                | Type    | Value                                | Description |
| ------------------- | ------- | ------------------------------------ | ----------- |
| INTERNAL_ADDR_WIDTH | natural |  1                                   |             |
| OFFSET_ADDR_SZ      | natural |  natural(ceil(log2(real(SLV_SIZE)))) |             |
## Processes
- unnamed: ( ref_clk_i )
## Instantiations

- sync_offset_inst: work.slv_to_sl_axi_sync_slv
- slv_to_sl_axi_comm_inst: work.slv_to_sl_axi_comm
**Description**
Instantiation of Axi Bus Interface S00_AXI

- handle_comm: work.slv_to_sl_axi_handCom
**Description**
Instantiation of Axi Bus Interface S00_AXI

