# Entity: fft

- **File**: fft.vhd
## Diagram

![Diagram](fft.svg "Diagram")
## Generics

| Generic name         | Type    | Value | Description                                    |
| -------------------- | ------- | ----- | ---------------------------------------------- |
| USE_EOF              | boolean | false | Users to add parameters here                   |
| USE_FIRST_BUFF       | boolean | true  |                                                |
| USE_SEC_BUFF         | boolean | true  |                                                |
| LOG_2_N_FFT          | natural | 11    |                                                |
| SHIFT_VAL            | natural | 16    |                                                |
| DATA_SIZE            | natural | 32    |                                                |
| DATA_IN_SIZE         | natural | 16    |                                                |
| C_S00_AXI_DATA_WIDTH | integer | 32    | Parameters of Axi Slave Bus Interface S00_AXI  |
| C_S00_AXI_ADDR_WIDTH | integer | 4     |                                                |
## Ports

| Port name       | Direction | Type                                                  | Description                                                                                       |
| --------------- | --------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| test_o          | out       | std_logic                                             |                                                                                                   |
| test_eof_o      | out       | std_logic                                             |                                                                                                   |
| data_i          | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)             | input data                                                                                        |
| data_en_i       | in        | std_logic                                             |                                                                                                   |
| data_eof_i      | in        | std_logic                                             |                                                                                                   |
| data_clk_i      | in        | std_logic                                             |                                                                                                   |
| data_rst_i      | in        | std_logic                                             |                                                                                                   |
| data_re_o       | out       | std_logic_vector(DATA_SIZE-1 downto 0)                | for the next component                                                                            |
| data_im_o       | out       | std_logic_vector(DATA_SIZE-1 downto 0)                |                                                                                                   |
| data_en_o       | out       | std_logic                                             |                                                                                                   |
| data_eof_o      | out       | std_logic                                             |                                                                                                   |
| data_clk_o      | out       | std_logic                                             |                                                                                                   |
| data_rst_o      | out       | std_logic                                             |                                                                                                   |
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

| Name             | Type                                     | Description |
| ---------------- | ---------------------------------------- | ----------- |
| coeff_re_en_s    | std_logic                                |             |
|  coeff_im_en_s   | std_logic                                |             |
| coeff_re_val_s   | std_logic_vector(COEFF_SIZE-1 downto 0)  |             |
|  coeff_im_val_s  | std_logic_vector(COEFF_SIZE-1 downto 0)  |             |
| coeff_re_addr_s  | std_logic_vector(LOG_2_N_FFT-1 downto 0) |             |
|  coeff_im_addr_s | std_logic_vector(LOG_2_N_FFT-1 downto 0) |             |
| addr_s           | std_logic_vector(1 downto 0)             |             |
| write_en_s       | std_logic                                |             |
|  read_en_s       | std_logic                                |             |
| read_coeff_re_s  | std_logic_vector(COEFF_SIZE-1 downto 0)  |             |
| read_coeff_im_s  | std_logic_vector(COEFF_SIZE-1 downto 0)  |             |
| test_data_s      | std_logic_vector(31 downto 0)            |             |
| test_data_addr_s | std_logic_vector(LOG_2_N_FFT-1 downto 0) |             |
| rcp_data_s       | std_logic_vector(31 downto 0)            |             |
| rcp_data_addr_s  | std_logic_vector(LOG_2_N_FFT-1 downto 0) |             |
| data_eof_s       | std_logic                                |             |
| data_en_s        | std_logic                                |             |
## Constants

| Name       | Type    | Value          | Description |
| ---------- | ------- | -------------- | ----------- |
| COEFF_SIZE | natural |  SHIFT_VAL + 2 |             |
## Processes
- unnamed: ( data_clk_i )
## Instantiations

- fft_axi_inst: work.fft_axi
**Description**
Instantiation of Axi Bus Interface S00_AXI

- fir_top_inst: work.fft_top_logic
**Description**
Add user logic here

- handle_comm: work.fft_handCom
**Description**
Instantiation of Axi Bus Interface S00_AXI

- coeff_re_inst: work.fft_ram_coeff
