# Entity: fft_axi

- **File**: fft_axi.vhd
## Diagram

![Diagram](fft_axi.svg "Diagram")
## Generics

| Generic name       | Type    | Value | Description              |
| ------------------ | ------- | ----- | ------------------------ |
| COEFF_SIZE         | natural | 16    |                          |
| ADDR_SIZE          | natural | 10    |                          |
| C_S_AXI_DATA_WIDTH | integer | 32    | Width of S_AXI data bus  |
## Ports

| Port name       | Direction | Type                                            | Description |
| --------------- | --------- | ----------------------------------------------- | ----------- |
| S_AXI_ACLK      | in        | std_logic                                       |             |
| reset           | in        | std_logic                                       |             |
| addr_i          | in        | std_logic_vector(1 downto 0)                    |             |
| write_en_i      | in        | std_logic                                       |             |
| writedata       | in        | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0) |             |
| read_en_i       | in        | std_logic                                       |             |
| read_ack_o      | out       | std_logic                                       |             |
| readdata        | out       | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0) | ;           |
| read_coeff_re_i | in        | std_logic_vector(COEFF_SIZE-1 downto 0)         |             |
| read_coeff_im_i | in        | std_logic_vector(COEFF_SIZE-1 downto 0)         |             |
| data_i          | in        | std_logic_vector(31 downto 0)                   |             |
| data_addr_o     | out       | std_logic_vector(ADDR_SIZE -1 downto 0)         |             |
| coeff_re_en_o   | out       | std_logic                                       | end of test |
| coeff_re_val_o  | out       | std_logic_vector(COEFF_SIZE-1 downto 0)         |             |
| coeff_re_addr_o | out       | std_logic_vector(ADDR_SIZE-1 downto 0)          |             |
| coeff_im_en_o   | out       | std_logic                                       |             |
| coeff_im_val_o  | out       | std_logic_vector(COEFF_SIZE-1 downto 0)         |             |
| coeff_im_addr_o | out       | std_logic_vector(ADDR_SIZE-1 downto 0)          |             |
## Signals

| Name                 | Type                                            | Description |
| -------------------- | ----------------------------------------------- | ----------- |
| readdata_s           | std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0) |             |
| coeff_re_en_s        | std_logic                                       |             |
|  coeff_im_en_s       | std_logic                                       |             |
| coeff_re_val_s       | std_logic_vector(COEFF_SIZE-1 downto 0)         |             |
| coeff_im_val_s       | std_logic_vector(COEFF_SIZE-1 downto 0)         |             |
| coeff_re_addr_s      | std_logic_vector(ADDR_SIZE-1 downto 0)          |             |
|  coeff_im_addr_s     | std_logic_vector(ADDR_SIZE-1 downto 0)          |             |
| coeff_re_addr_next_s | std_logic_vector(ADDR_SIZE-1 downto 0)          |             |
| coeff_im_addr_next_s | std_logic_vector(ADDR_SIZE-1 downto 0)          |             |
| read_addr_im_s       | std_logic_vector(ADDR_SIZE-1 downto 0)          |             |
|  read_addr_re_s      | std_logic_vector(ADDR_SIZE-1 downto 0)          |             |
| data_addr_s          | std_logic_vector(ADDR_SIZE-1 downto 0)          |             |
## Constants

| Name         | Type                         | Value | Description |
| ------------ | ---------------------------- | ----- | ----------- |
| REG_ID       | std_logic_vector(1 downto 0) |  "00" |             |
| REG_RE_COEFF | std_logic_vector(1 downto 0) |  "01" |             |
| REG_IM_COEFF | std_logic_vector(1 downto 0) |  "10" |             |
| REG_DATA     | std_logic_vector(1 downto 0) |  "11" |             |
## Processes
- write_process: ( S_AXI_ACLK )
- read_process: ( S_AXI_ACLK )
