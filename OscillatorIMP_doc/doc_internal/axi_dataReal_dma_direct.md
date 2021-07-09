# Entity: axi_dataReal_dma_direct

## Diagram

![Diagram](axi_dataReal_dma_direct.svg "Diagram")
## Generics

| Generic name         | Type    | Value | Description |
| -------------------- | ------- | ----- | ----------- |
| NB_INPUT             | natural | 1     |             |
| STOP_ON_EOF          | boolean | false |             |
| DATA_SIZE            | natural | 32    |             |
| NB_SAMPLE            | natural | 32    |             |
| C_M_AXIS_TDATA_WIDTH | integer | 32    |             |
## Ports

| Port name           | Direction | Type                                                  | Description       |
| ------------------- | --------- | ----------------------------------------------------- | ----------------- |
| reset               | in        | std_logic                                             | Syscon signals    |
| clk                 | in        | std_logic                                             |                   |
| M_AXIS_TVALID       | out       | std_logic                                             | axi signals       |
| M_AXIS_TDATA        | out       | std_logic_vector(C_M_AXIS_TDATA_WIDTH-1 downto 0)     |                   |
| M_AXIS_TSTRB        | out       | std_logic_vector((C_M_AXIS_TDATA_WIDTH/8)-1 downto 0) |                   |
| M_AXIS_TLAST        | out       | std_logic                                             |                   |
| M_AXIS_TREADY       | in        | std_logic                                             |                   |
| start_acquisition_i | in        | std_logic                                             | config/control    |
| busy_o              | out       | std_logic                                             |                   |
| data_en_i           | in        | std_logic                                             | input data stream |
| data_sof_i          | in        | std_logic                                             |                   |
| data_eof_i          | in        | std_logic                                             |                   |
| data1_i             | in        | std_logic_vector(DATA_SIZE-1 downto 0)                |                   |
| data2_i             | in        | std_logic_vector(DATA_SIZE-1 downto 0)                |                   |
## Signals

| Name               | Type                                              | Description |
| ------------------ | ------------------------------------------------- | ----------- |
| axis_tvalid_delay  | std_logic                                         |             |
| tlast_next_s       | std_logic                                         |             |
| axis_tlast_delay   | std_logic                                         |             |
| stream_data_out    | std_logic_vector(C_M_AXIS_TDATA_WIDTH-1 downto 0) |             |
| stop_acquisition_s | std_logic                                         | new         |
| busy_s             | std_logic                                         |             |
| data_en_s          | std_logic                                         |             |
| cpt_s              | unsigned(CPT_SIZE-1 downto 0)                     |             |
| sec_part           | natural range 0 to 1                              |             |
| data2_s            | std_logic_vector(31 downto 0)                     |             |
| ready_s            | std_logic                                         |             |
|  ready_next_s      | std_logic                                         |             |
| enable_s           | std_logic                                         |             |
| data_eof_s         | std_logic                                         |             |
| end_recv_s         | std_logic                                         |             |
## Constants

| Name     | Type    | Value                                 | Description |
| -------- | ------- | ------------------------------------- | ----------- |
| CPT_SIZE | natural |  natural(ceil(log2(real(NB_SAMPLE)))) |             |
## Processes
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
