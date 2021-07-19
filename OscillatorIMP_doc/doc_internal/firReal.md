# Entity: firReal

- **File**: firReal.vhd
## Diagram

![Diagram](firReal.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2018/05/26
## Generics

| Generic name         | Type    | Value    | Description                                    |
| -------------------- | ------- | -------- | ---------------------------------------------- |
| ID                   | natural | 1        | Users to add parameters here                   |
| coeff_format         | string  | "signed" |                                                |
| NB_COEFF             | natural | 128      |                                                |
| COEFF_SIZE           | natural | 16       |                                                |
| DECIMATE_FACTOR      | natural | 10       |                                                |
| DATA_IN_SIZE         | natural | 16       |                                                |
| DATA_OUT_SIZE        | natural | 39       |                                                |
| C_S00_AXI_DATA_WIDTH | integer | 32       | Parameters of Axi Slave Bus Interface S00_AXI  |
| C_S00_AXI_ADDR_WIDTH | integer | 4        |                                                |
## Ports

| Port name       | Direction | Type                                                  | Description                                                                                       |
| --------------- | --------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| data_i          | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)             | input data                                                                                        |
| data_en_i       | in        | std_logic                                             |                                                                                                   |
| data_clk_i      | in        | std_logic                                             |                                                                                                   |
| data_rst_i      | in        | std_logic                                             |                                                                                                   |
| data_o          | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0)            | for the next component                                                                            |
| data_en_o       | out       | std_logic                                             |                                                                                                   |
| data_eof_o      | out       | std_logic                                             |                                                                                                   |
| data_clk_o      | out       | std_logic                                             |                                                                                                   |
| data_rst_o      | out       | std_logic                                             |                                                                                                   |
| tick_o          | out       | std_logic                                             | ctrl                                                                                              |
| s00_axi_aclk    | in        | std_logic                                             | User ports endsDo not modify the ports beyond this line Ports of Axi Slave Bus Interface S00_AXI  |
| s00_axi_reset   | in        | std_logic                                             |                                                                                                   |
| s00_axi_awaddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)     |                                                                                                   |
| s00_axi_awprot  | in        | std_logic_vector(2 downto 0)                          |                                                                                                   |
| s00_axi_awvalid | in        | std_logic                                             |                                                                                                   |
| s00_axi_awready | out       | std_logic                                             |                                                                                                   |
| s00_axi_wdata   | in        | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)     |                                                                                                   |
| s00_axi_wstrb   | in        | std_logic_vector((C_S00_AXI_DATA_WIDTH/8)-1 downto 0) |                                                                                                   |
| s00_axi_wvalid  | in        | std_logic                                             |                                                                                                   |
| s00_axi_wready  | out       | std_logic                                             |                                                                                                   |
| s00_axi_bresp   | out       | std_logic_vector(1 downto 0)                          |                                                                                                   |
| s00_axi_bvalid  | out       | std_logic                                             |                                                                                                   |
| s00_axi_bready  | in        | std_logic                                             |                                                                                                   |
| s00_axi_araddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)     |                                                                                                   |
| s00_axi_arprot  | in        | std_logic_vector(2 downto 0)                          |                                                                                                   |
| s00_axi_arvalid | in        | std_logic                                             |                                                                                                   |
| s00_axi_arready | out       | std_logic                                             |                                                                                                   |
| s00_axi_rdata   | out       | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)     |                                                                                                   |
| s00_axi_rresp   | out       | std_logic_vector(1 downto 0)                          |                                                                                                   |
| s00_axi_rvalid  | out       | std_logic                                             |                                                                                                   |
| s00_axi_rready  | in        | std_logic                                             |                                                                                                   |
## Signals

| Name           | Type                                       | Description |
| -------------- | ------------------------------------------ | ----------- |
| coeff_en_s     | std_logic                                  |             |
| coeff_val_s    | std_logic_vector(COEFF_SIZE-1 downto 0)    |             |
| coeff_addr_s   | std_logic_vector(COEFF_ADDR_SZ-1 downto 0) |             |
| addr_s         | std_logic_vector(1 downto 0)               |             |
| write_en_s     | std_logic                                  |             |
|  read_en_s     | std_logic                                  |             |
| r_coeff_addr_s | std_logic_vector(9 downto 0)               |             |
| r_coeff_val_s  | std_logic_vector(COEFF_SIZE-1 downto 0)    |             |
| data_en_s      | std_logic                                  |             |
## Constants

| Name                | Type    | Value                                | Description |
| ------------------- | ------- | ------------------------------------ | ----------- |
| COEFF_ADDR_SZ       | natural |  natural(ceil(log2(real(NB_COEFF)))) |             |
| INTERNAL_ADDR_WIDTH | natural |  2                                   |             |
## Instantiations

- firReal_axi_inst: work.firReal_axi
**Description**
Instantiation of Axi Bus Interface S00_AXI

- fir_top_inst: work.firReal_top
**Description**
Add user logic here

- handle_comm: work.firReal_handCom
**Description**
Instantiation of Axi Bus Interface S00_AXI

