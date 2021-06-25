# Entity: ddr3_mem2mig_adapter_Series7
## Diagram
![Diagram](ddr3_mem2mig_adapter_Series7.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| D_BITS       | positive |       |             |
| DQ_BITS      | positive |       |             |
| MEM_A_BITS   | positive |       |             |
| APP_A_BITS   | positive |       |             |
## Ports
| Port name           | Direction | Type                                    | Description |
| ------------------- | --------- | --------------------------------------- | ----------- |
| mem_req             | in        | std_logic                               |             |
| mem_write           | in        | std_logic                               |             |
| mem_addr            | in        | unsigned(MEM_A_BITS-1 downto 0)         |             |
| mem_wdata           | in        | std_logic_vector(D_BITS-1 downto 0)     |             |
| mem_wmask           | in        | std_logic_vector(D_BITS/8-1 downto 0)   |             |
| mem_rdy             | out       | std_logic                               |             |
| mem_rstb            | out       | std_logic                               |             |
| mem_rdata           | out       | std_logic_vector(D_BITS-1 downto 0)     |             |
| init_calib_complete | in        | std_logic                               |             |
| app_rd_data         | in        | std_logic_vector((D_BITS)-1 downto 0)   |             |
| app_rd_data_end     | in        | std_logic                               |             |
| app_rd_data_valid   | in        | std_logic                               |             |
| app_rdy             | in        | std_logic                               |             |
| app_wdf_rdy         | in        | std_logic                               |             |
| app_addr            | out       | std_logic_vector(APP_A_BITS-1 downto 0) |             |
| app_cmd             | out       | std_logic_vector(2 downto 0)            |             |
| app_en              | out       | std_logic                               |             |
| app_wdf_data        | out       | std_logic_vector((D_BITS)-1 downto 0)   |             |
| app_wdf_end         | out       | std_logic                               |             |
| app_wdf_mask        | out       | std_logic_vector((D_BITS)/8-1 downto 0) |             |
| app_wdf_wren        | out       | std_logic                               |             |
## Signals
| Name      | Type      | Description |
| --------- | --------- | ----------- |
| mem_rdy_i | std_logic |             |
## Constants
| Name    | Type     | Value             | Description |
| ------- | -------- | ----------------- | ----------- |
| BL      | positive |  D_BITS / DQ_BITS |             |
| BL_BITS | natural  |  log2ceil(BL)     |             |
## Processes
- unnamed: _( mem_addr )_

