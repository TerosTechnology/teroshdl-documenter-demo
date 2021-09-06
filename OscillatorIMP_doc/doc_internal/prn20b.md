# Entity: prn20b

- **File**: prn20b.vhd
## Diagram

![Diagram](prn20b.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 Creation date : 2018/06/11
-------------------------------------------------------------------------
## Generics

| Generic name         | Type    | Value | Description                                    |
| -------------------- | ------- | ----- | ---------------------------------------------- |
| DFLT_PRESC           | natural | 15    |                                                |
| PRESC_SIZE           | natural | 16    |                                                |
| C_S00_AXI_DATA_WIDTH | integer | 32    | Parameters of Axi Slave Bus Interface S00_AXI  |
| C_S00_AXI_ADDR_WIDTH | integer | 3     |                                                |
## Ports

| Port name       | Direction | Type                                                  | Description                                   |
| --------------- | --------- | ----------------------------------------------------- | --------------------------------------------- |
| s00_axi_aclk    | in        | std_logic                                             | Ports of Axi Lite Slave Bus Interface S00_AXI |
| s00_axi_reset   | in        | std_logic                                             |                                               |
| s00_axi_awaddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)     |                                               |
| s00_axi_awprot  | in        | std_logic_vector(2 downto 0)                          |                                               |
| s00_axi_awvalid | in        | std_logic                                             |                                               |
| s00_axi_awready | out       | std_logic                                             |                                               |
| s00_axi_wdata   | in        | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)     |                                               |
| s00_axi_wstrb   | in        | std_logic_vector((C_S00_AXI_DATA_WIDTH/8)-1 downto 0) |                                               |
| s00_axi_wvalid  | in        | std_logic                                             |                                               |
| s00_axi_wready  | out       | std_logic                                             |                                               |
| s00_axi_bresp   | out       | std_logic_vector(1 downto 0)                          |                                               |
| s00_axi_bvalid  | out       | std_logic                                             |                                               |
| s00_axi_bready  | in        | std_logic                                             |                                               |
| s00_axi_araddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)     |                                               |
| s00_axi_arprot  | in        | std_logic_vector(2 downto 0)                          |                                               |
| s00_axi_arvalid | in        | std_logic                                             |                                               |
| s00_axi_arready | out       | std_logic                                             |                                               |
| s00_axi_rdata   | out       | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)     |                                               |
| s00_axi_rresp   | out       | std_logic_vector(1 downto 0)                          |                                               |
| s00_axi_rvalid  | out       | std_logic                                             |                                               |
| s00_axi_rready  | in        | std_logic                                             |                                               |
| ref_clk_i       | in        | std_logic                                             | specific signals                              |
| ref_rst_i       | in        | std_logic                                             |                                               |
| prn_full_o      | out       | std_logic_vector(19 downto 0)                         |                                               |
| prn_full_en_o   | out       | std_logic                                             |                                               |
| prn_full_clk_o  | out       | std_logic                                             |                                               |
| prn_full_rst_o  | out       | std_logic                                             |                                               |
| test_o          | out       | std_logic                                             |                                               |
| bit_o           | out       | std_logic                                             |                                               |
## Signals

| Name          | Type                                             | Description |
| ------------- | ------------------------------------------------ | ----------- |
| addr_s        | std_logic_vector(INTERNAL_ADDR_WIDTH-1 downto 0) |             |
| write_en_s    | std_logic                                        |             |
|  read_en_s    | std_logic                                        |             |
| prescaler_s   | std_logic_vector(PRESC_SIZE-1 downto 0)          |             |
|  presc_sync_s | std_logic_vector(PRESC_SIZE-1 downto 0)          |             |
| tick_s        | std_logic                                        |             |
| test_s        | std_logic                                        |             |
## Constants

| Name                | Type    | Value | Description |
| ------------------- | ------- | ----- | ----------- |
| INTERNAL_ADDR_WIDTH | natural |  1    |             |
## Processes
- unnamed: ( ref_clk_i )
## Instantiations

- logic_inst: work.prn20b_logic
- presc_inst: work.prn20b_presc
- prescSync: work.prn20b_vectSync
- wb_inst: work.wb_prn20b
- handle_comm: work.prn20b_handCom
</br>**Description**
 Instantiation of Axi Bus Interface S00_AXI

