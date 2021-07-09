# Entity: delayTempoReal_axi

## Diagram

![Diagram](delayTempoReal_axi.svg "Diagram")
## Generics

| Generic name         | Type    | Value | Description                                    |
| -------------------- | ------- | ----- | ---------------------------------------------- |
| DATA_SIZE            | natural | 16    |                                                |
| MAX_NB_DELAY         | natural | 6     |                                                |
| DEFAULT_DELAY        | natural | 0     |                                                |
| C_S00_AXI_DATA_WIDTH | integer | 32    | Parameters of Axi Slave Bus Interface S00_AXI  |
| C_S00_AXI_ADDR_WIDTH | integer | 3     |                                                |
## Ports

| Port name       | Direction | Type                                              | Description                              |
| --------------- | --------- | ------------------------------------------------- | ---------------------------------------- |
| data_i          | in        | std_logic_vector(DATA_SIZE-1 downto 0)            | input data                               |
| data_en_i       | in        | std_logic                                         |                                          |
| data_eof_i      | in        | std_logic                                         |                                          |
| data_clk_i      | in        | std_logic                                         |                                          |
| data_rst_i      | in        | std_logic                                         |                                          |
| data_o          | out       | std_logic_vector(DATA_SIZE-1 downto 0)            | output data                              |
| data_en_o       | out       | std_logic                                         |                                          |
| data_eof_o      | out       | std_logic                                         |                                          |
| data_clk_o      | out       | std_logic                                         |                                          |
| data_rst_o      | out       | std_logic                                         |                                          |
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

| Name          | Type                                             | Description |
| ------------- | ------------------------------------------------ | ----------- |
| addr_s        | std_logic_vector(INTERNAL_ADDR_WIDTH-1 downto 0) |             |
| write_en_s    | std_logic                                        |             |
|  read_en_s    | std_logic                                        |             |
| delay_s       | std_logic_vector(DELAY_ADDR_SZ-1 downto 0)       |             |
|  delay_sync_s | std_logic_vector(DELAY_ADDR_SZ-1 downto 0)       |             |
## Constants

| Name                | Type    | Value                                    | Description |
| ------------------- | ------- | ---------------------------------------- | ----------- |
| INTERNAL_ADDR_WIDTH | natural |  1                                       |             |
| DELAY_ADDR_SZ       | natural |  natural(ceil(log2(real(MAX_NB_DELAY)))) |             |
## Instantiations

- delay_logic_inst: work.delayTempoReal_axi_logic
- sync_delay_inst: work.delayTempoReal_axi_sync_slv
- delayTempoReal_axi_comm_inst: work.delayTempoReal_axi_comm
**Description**
Instantiation of Axi Bus Interface S00_AXI

- handle_comm: work.delayTempoReal_axi_handCom
**Description**
Instantiation of Axi Bus Interface S00_AXI

