# Entity: MUXcomplexNto1

- **File**: _MUXcomplexNto1.vhd
## Diagram

![Diagram](_MUXcomplexNto1.svg "Diagram")
## Generics

| Generic name         | Type     | Value | Description |
| -------------------- | -------- | ----- | ----------- |
| ID                   | NATURAL  | 1     |             |
| INPUTS               | positive | 4     |             |
| DEFAULT_INPUT        | natural  | 0     |             |
| DATA_SIZE            | natural  | 16    |             |
| C_S00_AXI_DATA_WIDTH | integer  | 32    |             |
| C_S00_AXI_ADDR_WIDTH | integer  | 4     |             |
## Ports

| Port name       | Direction | Type                                                              | Description                                                                   |
| --------------- | --------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| data_i_i        | in        | STD_LOGIC_VECTOR_ARRAY_T(0 to INPUTS - 1)(DATA_SIZE - 1 downto 0) | rocessing                                                                     |
| data_q_i        | in        | STD_LOGIC_VECTOR_ARRAY_T(0 to INPUTS - 1)(DATA_SIZE - 1 downto 0) |                                                                               |
| data_en_i       | in        | STD_LOGIC_ARRAY_T(INPUTS - 1 downto 0)                            |                                                                               |
| data_clk_i      | in        | STD_LOGIC_ARRAY_T(INPUTS - 1 downto 0)                            |                                                                               |
| data_eof_i      | in        | STD_LOGIC_ARRAY_T(INPUTS - 1 downto 0)                            |                                                                               |
| data_rst_i      | in        | STD_LOGIC_ARRAY_T(INPUTS - 1 downto 0)                            |                                                                               |
| data_i_o        | out       | STD_LOGIC_VECTOR(DATA_SIZE-1 downto 0)                            |  select_i    : in STD_LOGIC_VECTOR(integer(log2(real(INPUTS))) - 1 downto 0); |
| data_q_o        | out       | STD_LOGIC_VECTOR(DATA_SIZE-1 downto 0)                            |                                                                               |
| data_en_o       | out       | STD_LOGIC                                                         |                                                                               |
| data_clk_o      | out       | STD_LOGIC                                                         |                                                                               |
| data_eof_o      | out       | STD_LOGIC                                                         |                                                                               |
| data_rst_o      | out       | STD_LOGIC                                                         |                                                                               |
| s00_axi_aclk    | in        | std_logic                                                         |                                                                               |
| s00_axi_reset   | in        | std_logic                                                         |                                                                               |
| s00_axi_awaddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)                 |                                                                               |
| s00_axi_awvalid | in        | std_logic                                                         | 00_axi_awprot	: in std_logic_vector(2 downto 0);                              |
| s00_axi_awready | out       | std_logic                                                         |                                                                               |
| s00_axi_wdata   | in        | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)                 |                                                                               |
| s00_axi_wvalid  | in        | std_logic                                                         | 00_axi_wstrb	: in std_logic_vector((C_S00_AXI_DATA_WIDTH/8)-1 downto 0);      |
| s00_axi_wready  | out       | std_logic                                                         |                                                                               |
| s00_axi_bresp   | out       | std_logic_vector(1 downto 0)                                      |                                                                               |
| s00_axi_bvalid  | out       | std_logic                                                         |                                                                               |
| s00_axi_bready  | in        | std_logic                                                         |                                                                               |
| s00_axi_araddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)                 |                                                                               |
| s00_axi_arvalid | in        | std_logic                                                         | 00_axi_arprot	: in std_logic_vector(2 downto 0);                              |
| s00_axi_arready | out       | std_logic                                                         |                                                                               |
| s00_axi_rdata   | out       | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)                 |                                                                               |
| s00_axi_rresp   | out       | std_logic_vector(1 downto 0)                                      |                                                                               |
| s00_axi_rvalid  | out       | std_logic                                                         |                                                                               |
| s00_axi_rready  | in        | std_logic                                                         |                                                                               |
## Signals

| Name         | Type                                    | Description                  |
| ------------ | --------------------------------------- | ---------------------------- |
| addr_s       | std_logic_vector(1 downto 0)            |                              |
| write_en_s   | std_logic                               |                              |
|  read_en_s   | std_logic                               |                              |
| select_s     | std_logic_vector(SEL_SIZE - 1 downto 0) | signal witchIn : std_logic;  |
| witchIn_sync | std_logic                               |                              |
## Constants

| Name     | Type    | Value                              | Description |
| -------- | ------- | ---------------------------------- | ----------- |
| SEL_SIZE | integer |  integer(ceil(log2(real(INPUTS)))) |             |
## Instantiations

- switchComplexWb_inst: work.MUXcomplexNto1_wb
- handle_comm: work.MUXcomplex_handComm
**Description**
 Instantiation of Axi Bus Interface S00_AXI

