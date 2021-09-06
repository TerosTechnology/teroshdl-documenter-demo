# Entity: gen_radar_prog

- **File**: gen_radar_prog.vhd
## Diagram

![Diagram](gen_radar_prog.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 2013-2018
-------------------------------------------------------------------------
## Generics

| Generic name         | Type    | Value | Description                                         |
| -------------------- | ------- | ----- | --------------------------------------------------- |
| ID                   | natural | 1     |                                                     |
| C_S00_AXI_DATA_WIDTH | integer | 32    |                                                     |
| C_S00_AXI_ADDR_WIDTH | integer | 4     |                                                     |
| DATA_SIZE            | natural | 16    | req_in : natural := 200;  -- ADC clock rate en MHz  |
| BURST_SIZE           | natural | 1024  |                                                     |
| RXOFF                | natural | 2     |  exprime' en cycle                                  |
| TXON                 | natural | 8     |  idem                                               |
## Ports

| Port name       | Direction | Type                                                  | Description    |
| --------------- | --------- | ----------------------------------------------------- | -------------- |
| switch_o        | out       | std_logic                                             | Syscon signals |
| switchn_o       | out       | std_logic                                             |                |
| data_i_i        | in        | std_logic_vector(DATA_SIZE-1 downto 0)                | rocessing      |
| data_q_i        | in        | std_logic_vector(DATA_SIZE-1 downto 0)                |                |
| data_en_i       | in        | std_logic                                             |                |
| data_clk_i      | in        | std_logic                                             |                |
| data_rst_i      | in        | std_logic                                             |                |
| data_i_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0)                |                |
| data_q_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0)                |                |
| data_en_o       | out       | std_logic                                             |                |
| data_clk_o      | out       | std_logic                                             |                |
| data_rst_o      | out       | std_logic                                             |                |
| data_eof_o      | out       | std_logic                                             |                |
| s00_axi_aclk    | in        | std_logic                                             | axi            |
| s00_axi_reset   | in        | std_logic                                             |                |
| s00_axi_awaddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)     |                |
| s00_axi_awprot  | in        | std_logic_vector(2 downto 0)                          |                |
| s00_axi_awvalid | in        | std_logic                                             |                |
| s00_axi_awready | out       | std_logic                                             |                |
| s00_axi_wdata   | in        | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)     |                |
| s00_axi_wstrb   | in        | std_logic_vector((C_S00_AXI_DATA_WIDTH/8)-1 downto 0) |                |
| s00_axi_wvalid  | in        | std_logic                                             |                |
| s00_axi_wready  | out       | std_logic                                             |                |
| s00_axi_bresp   | out       | std_logic_vector(1 downto 0)                          |                |
| s00_axi_bvalid  | out       | std_logic                                             |                |
| s00_axi_bready  | in        | std_logic                                             |                |
| s00_axi_araddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)     |                |
| s00_axi_arprot  | in        | std_logic_vector(2 downto 0)                          |                |
| s00_axi_arvalid | in        | std_logic                                             |                |
| s00_axi_arready | out       | std_logic                                             |                |
| s00_axi_rdata   | out       | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)     |                |
| s00_axi_rresp   | out       | std_logic_vector(1 downto 0)                          |                |
| s00_axi_rvalid  | out       | std_logic                                             |                |
| s00_axi_rready  | in        | std_logic                                             |                |
## Signals

| Name           | Type                          | Description |
| -------------- | ----------------------------- | ----------- |
| rxoff_s        | std_logic_vector(15 downto 0) |             |
|  txon_s        | std_logic_vector(15 downto 0) |             |
| addr_s         | std_logic_vector(1 downto 0)  |             |
| write_en_s     | std_logic                     |             |
|  read_en_s     | std_logic                     |             |
| point_period_s | std_logic_vector(15 downto 0) |             |
## Instantiations

- gr_logic_inst: work.gen_radar_prog_logic
- wb_inst: work.wb_gen_radar_prog
- handle_comm: work.gen_radar_prog_handComm
</br>**Description**
 Instantiation of Axi Bus Interface S00_AXI

