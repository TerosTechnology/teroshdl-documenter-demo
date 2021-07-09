# Entity: top_dut

## Diagram

![Diagram](top_dataDma.svg "Diagram")
## Ports

| Port name           | Direction | Type                                | Description |
| ------------------- | --------- | ----------------------------------- | ----------- |
| clk_i               | in        | std_logic                           |             |
| rst_i               | in        | std_logic                           |             |
| M_AXIS_TVALID       | out       | std_logic                           | axistream   |
| M_AXIS_TDATA        | out       | std_logic_vector(32-1 downto 0)     |             |
| M_AXIS_TSTRB        | out       | std_logic_vector((32/8)-1 downto 0) |             |
| M_AXIS_TLAST        | out       | std_logic                           |             |
| M_AXIS_TREADY       | in        | std_logic                           |             |
| data1_i             | in        | std_logic_vector(31 downto 0)       | data in     |
| data_en_i           | in        | std_logic                           |             |
| start_acquisition_i | in        | std_logic                           | config      |
| busy_o              | out       | std_logic                           |             |
## Signals

| Name           | Type                          | Description |
| -------------- | ----------------------------- | ----------- |
| mux_data1_s    | std_logic_vector(31 downto 0) |             |
| mux_data2_s    | std_logic_vector(31 downto 0) |             |
| mux_data_en_s  | std_logic                     |             |
| mux_data_sof_s | std_logic                     |             |
| mux_data_eof_s | std_logic                     |             |
## Instantiations

- dut_inst: work.axi_dataReal_dma_direct
