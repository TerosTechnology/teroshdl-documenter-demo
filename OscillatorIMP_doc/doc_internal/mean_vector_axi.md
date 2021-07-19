# Entity: mean_vector_axi

- **File**: mean_vector_axi.vhd
## Diagram

![Diagram](mean_vector_axi.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
2013-2019
## Generics

| Generic name         | Type    | Value | Description                                    |
| -------------------- | ------- | ----- | ---------------------------------------------- |
| id                   | natural | 1     |                                                |
| MAX_NB_ACCUM         | natural | 1024  |                                                |
| DATA_SIZE            | natural | 14    |                                                |
| ADDR_SIZE            | natural | 10    |                                                |
| C_S00_AXI_DATA_WIDTH | integer | 32    | Parameters of Axi Slave Bus Interface S00_AXI  |
| C_S00_AXI_ADDR_WIDTH | integer | 4     |                                                |
## Ports

| Port name       | Direction | Type                                              | Description      |
| --------------- | --------- | ------------------------------------------------- | ---------------- |
| s00_axi_aclk    | in        | std_logic                                         | Wishbone signals |
| s00_axi_reset   | in        | std_logic                                         |                  |
| s00_axi_awaddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0) |                  |
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
| data_i_i        | in        | std_logic_vector(DATA_SIZE-1 downto 0)            | input            |
| data_q_i        | in        | std_logic_vector(DATA_SIZE-1 downto 0)            |                  |
| data_en_i       | in        | std_logic                                         |                  |
| data_eof_i      | in        | std_logic                                         |                  |
| data_rst_i      | in        | std_logic                                         |                  |
| data_clk_i      | in        | std_logic                                         |                  |
| data_q_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0)            | output           |
| data_i_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0)            |                  |
| data_en_o       | out       | std_logic                                         |                  |
| data_eof_o      | out       | std_logic                                         |                  |
| data_rst_o      | out       | std_logic                                         |                  |
| data_clk_o      | out       | std_logic                                         |                  |
## Signals

| Name             | Type                                    | Description |
| ---------------- | --------------------------------------- | ----------- |
| nb_iter_s        | std_logic_vector(ACCUM_SIZE-1 downto 0) |             |
| nb_iter_sync_s   | std_logic_vector(ACCUM_SIZE-1 downto 0) |             |
| shift_val_s      | std_logic_vector(SHIFT_SIZE-1 downto 0) |             |
| shift_val_sync_s | std_logic_vector(SHIFT_SIZE-1 downto 0) |             |
| addr_s           | std_logic_vector(1 downto 0)            | comm        |
| write_en_s       | std_logic                               |             |
|  read_en_s       | std_logic                               |             |
## Constants

| Name       | Type    | Value                                    | Description                                                                                |
| ---------- | ------- | ---------------------------------------- | ------------------------------------------------------------------------------------------ |
| ACCUM_SIZE | natural |  natural(ceil(log2(real(MAX_NB_ACCUM)))) |                                                                                            |
| SHIFT_SIZE | natural |  natural(ceil(log2(real(ACCUM_SIZE))))   | we need to describe the shift sizedivide by 1024 is >> 10 => 10 must be used with 2^4 = 16 |
## Instantiations

- logic_inst1: work.mean_vector_axi_logic
- nb_iter_syn: work.mva_synchronizer_vector
**Description**
synchro --

- shift_syn: work.mva_synchronizer_vector
- wb_shift_inst: work.wb_mean_vector_axi
- handle_comm: work.mean_vector_axi_handcomm
**Description**
Instantiation of Axi Bus Interface S00_AXI

