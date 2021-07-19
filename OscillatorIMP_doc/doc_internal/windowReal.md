# Entity: windowReal

- **File**: windowReal.vhd
## Diagram

![Diagram](windowReal.svg "Diagram")
## Generics

| Generic name         | Type    | Value | Description                                    |
| -------------------- | ------- | ----- | ---------------------------------------------- |
| DATA_SIZE            | natural | 32    |                                                |
| COEFF_ADDR_SIZE      | natural | 8     |                                                |
| COEFF_SIZE           | natural | 16    |                                                |
| id                   | natural | 1     |                                                |
| C_S00_AXI_DATA_WIDTH | integer | 32    | Parameters of Axi Slave Bus Interface S00_AXI  |
| C_S00_AXI_ADDR_WIDTH | integer | 4     |                                                |
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
| data_en_i       | in        | std_logic                                             |                  |
| data_clk_i      | in        | std_logic                                             |                  |
| data_rst_i      | in        | std_logic                                             |                  |
| data_i          | in        | std_logic_vector(DATA_SIZE-1 downto 0)                |                  |
| data_en_o       | out       | std_logic                                             |                  |
| data_eof_o      | out       | std_logic                                             |                  |
| data_clk_o      | out       | std_logic                                             |                  |
| data_rst_o      | out       | std_logic                                             |                  |
| data_o          | out       | std_logic_vector(DATA_SIZE-1 downto 0)                |                  |
## Signals

| Name         | Type                                         | Description |
| ------------ | -------------------------------------------- | ----------- |
| coeff_en_s   | std_logic                                    |             |
| coeff_s      | std_logic_vector(COEFF_SIZE downto 0)        |             |
| coeff_addr_s | std_logic_vector(COEFF_ADDR_SIZE-1 downto 0) |             |
| addr_s       | std_logic_vector(1 downto 0)                 | comm        |
| write_en_s   | std_logic                                    |             |
|  read_en_s   | std_logic                                    |             |
## Instantiations

- windowRealLogic: work.windowReal_logic
- wb_windowReal_inst: work.wb_windowReal
- windowRealHandComm: work.windowReal_handComm
