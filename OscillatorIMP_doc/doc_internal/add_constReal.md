# Entity: add_constReal

## Diagram

![Diagram](add_constReal.svg "Diagram")
## Generics

| Generic name         | Type    | Value    | Description                                    |
| -------------------- | ------- | -------- | ---------------------------------------------- |
| id                   | natural | 1        |                                                |
| format               | string  | "signed" |                                                |
| add_val              | integer | 0        |                                                |
| DATA_OUT_SIZE        | natural | 18       |                                                |
| DATA_IN_SIZE         | natural | 16       |                                                |
| C_S00_AXI_DATA_WIDTH | integer | 32       | Parameters of Axi Slave Bus Interface S00_AXI  |
| C_S00_AXI_ADDR_WIDTH | integer | 4        |                                                |
## Ports

| Port name       | Direction | Type                                                  | Description      |
| --------------- | --------- | ----------------------------------------------------- | ---------------- |
| s00_axi_aclk    | in        | std_logic                                             |                  |
| s00_axi_reset   | in        | std_logic                                             |                  |
| s00_axi_awaddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)     | Wishbone signals |
| s00_axi_awprot  | in        | std_logic_vector(2 downto 0)                          |                  |
| s00_axi_awvalid | in        | std_logic                                             |                  |
| s00_axi_awready | out       | std_logic                                             |                  |
| s00_axi_wdata   | in        | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)     |                  |
| s00_axi_wstrb   | in        | std_logic_vector((C_S00_AXI_DATA_WIDTH/8)-1 downto 0) |                  |
| s00_axi_wvalid  | in        | std_logic                                             |                  |
| s00_axi_wready  | out       | std_logic                                             |                  |
| s00_axi_bresp   | out       | std_logic_vector(1 downto 0)                          |                  |
| s00_axi_bvalid  | out       | std_logic                                             |                  |
| s00_axi_bready  | in        | std_logic                                             |                  |
| s00_axi_araddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)     |                  |
| s00_axi_arprot  | in        | std_logic_vector(2 downto 0)                          |                  |
| s00_axi_arvalid | in        | std_logic                                             |                  |
| s00_axi_arready | out       | std_logic                                             |                  |
| s00_axi_rdata   | out       | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)     |                  |
| s00_axi_rresp   | out       | std_logic_vector(1 downto 0)                          |                  |
| s00_axi_rvalid  | out       | std_logic                                             |                  |
| s00_axi_rready  | in        | std_logic                                             |                  |
| data_en_i       | in        | std_logic                                             | in               |
| data_clk_i      | in        | std_logic                                             |                  |
| data_rst_i      | in        | std_logic                                             |                  |
| data_i          | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)             |                  |
| data_en_o       | out       | std_logic                                             | out              |
| data_clk_o      | out       | std_logic                                             |                  |
| data_rst_o      | out       | std_logic                                             |                  |
| data_o          | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0)            |                  |
## Signals

| Name          | Type                                      | Description |
| ------------- | ----------------------------------------- | ----------- |
| addr_s        | std_logic_vector(1 downto 0)              |             |
| write_en_s    | std_logic                                 |             |
|  read_en_s    | std_logic                                 |             |
| offset_s      | std_logic_vector(DATA_IN_SIZE-1 downto 0) |             |
| offset_sync_s | std_logic_vector(DATA_IN_SIZE-1 downto 0) |             |
## Constants

| Name                | Type    | Value | Description |
| ------------------- | ------- | ----- | ----------- |
| INTERNAL_ADDR_WIDTH | natural |  2    |             |
## Instantiations

- add_constRealLogic: work.add_constReal_logic
- offset_syn: work.add_constReal_synchronizer_vector
**Description**
synchro --

- wb_add_constReal_inst: work.wb_add_constReal
- add_constRealHandComm: work.add_constReal_handComm
