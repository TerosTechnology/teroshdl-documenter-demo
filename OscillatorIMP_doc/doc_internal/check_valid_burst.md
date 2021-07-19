# Entity: check_valid_burst

- **File**: check_valid_burst.vhd
## Diagram

![Diagram](check_valid_burst.svg "Diagram")
## Description

 warning !!!! --------------------
 cpt_max_val is the last value  --
 allowed (ie the addr)          --
consequently for 2048 sample the--
last value is 2047 since 0 is   --
an valid offset                 --
## Generics

| Generic name         | Type    | Value | Description                                    |
| -------------------- | ------- | ----- | ---------------------------------------------- |
| ACCUM_SIZE           | natural | 32    |                                                |
| DATA_SIZE            | natural | 14    |                                                |
| ADDR_SIZE            | natural | 10    |                                                |
| DFLT_START_OFFSET    | natural | 500   |                                                |
| DFLT_STOP_OFFSET     | natural | 1024  |                                                |
| DFLT_LIMIT           | natural | 10000 |                                                |
| id                   | natural | 1     |                                                |
| C_S00_AXI_DATA_WIDTH | integer | 32    | Parameters of Axi Slave Bus Interface S00_AXI  |
| C_S00_AXI_ADDR_WIDTH | integer | 4     |                                                |
## Ports

| Port name       | Direction | Type                                              | Description      |
| --------------- | --------- | ------------------------------------------------- | ---------------- |
| s00_axi_aclk    | in        | std_logic                                         |                  |
| s00_axi_reset   | in        | std_logic                                         |                  |
| s00_axi_awaddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0) | Wishbone signals |
| s00_axi_awvalid | in        | std_logic                                         |                  |
| s00_axi_awready | out       | std_logic                                         |                  |
| s00_axi_wdata   | in        | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0) |                  |
| s00_axi_wvalid  | in        | std_logic                                         |                  |
| s00_axi_wready  | out       | std_logic                                         |                  |
| s00_axi_bresp   | out       | std_logic_vector(1 downto 0)                      |                  |
| s00_axi_bvalid  | out       | std_logic                                         |                  |
| s00_axi_bready  | in        | std_logic                                         |                  |
| s00_axi_araddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0) |                  |
| s00_axi_arvalid | in        | std_logic                                         |                  |
| s00_axi_arready | out       | std_logic                                         |                  |
| s00_axi_rdata   | out       | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0) |                  |
| s00_axi_rresp   | out       | std_logic_vector(1 downto 0)                      |                  |
| s00_axi_rvalid  | out       | std_logic                                         |                  |
| s00_axi_rready  | in        | std_logic                                         |                  |
| data_en_i       | in        | std_logic                                         |                  |
| data_eof_i      | in        | std_logic                                         |                  |
| data_clk_i      | in        | std_logic                                         |                  |
| data_rst_i      | in        | std_logic                                         |                  |
| data_i_i        | in        | std_logic_vector(DATA_SIZE-1 downto 0)            |                  |
| data_q_i        | in        | std_logic_vector(DATA_SIZE-1 downto 0)            |                  |
| data_en_o       | out       | std_logic                                         |                  |
| data_eof_o      | out       | std_logic                                         |                  |
| data_clk_o      | out       | std_logic                                         |                  |
| data_rst_o      | out       | std_logic                                         |                  |
| data_i_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0)            |                  |
| data_q_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0)            |                  |
## Signals

| Name                | Type                                    | Description |
| ------------------- | --------------------------------------- | ----------- |
| start_mean_offset_s | std_logic_vector(ADDR_SIZE-1 downto 0)  |             |
| max_allowed_val_s   | std_logic_vector(ACCUM_SIZE-1 downto 0) |             |
| cpt_max_s           | std_logic_vector(ADDR_SIZE-1 downto 0)  |             |
| addr_s              | std_logic_vector(1 downto 0)            | comm        |
| write_en_s          | std_logic                               |             |
|  read_en_s          | std_logic                               |             |
## Instantiations

- cvbLogic: work.cvb_logic
- wb_cvb_inst: work.wb_cvb
- cvbHandComm: work.cvb_handComm
