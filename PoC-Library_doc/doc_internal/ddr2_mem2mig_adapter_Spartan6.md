# Entity: ddr2_mem2mig_adapter_Spartan6
## Diagram
![Diagram](ddr2_mem2mig_adapter_Spartan6.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| D_BITS       | positive |       |             |
| MEM_A_BITS   | positive |       |             |
| APP_A_BITS   | positive |       |             |
## Ports
| Port name         | Direction | Type                                    | Description |
| ----------------- | --------- | --------------------------------------- | ----------- |
| mem_req           | in        | std_logic                               |             |
| mem_write         | in        | std_logic                               |             |
| mem_addr          | in        | unsigned(MEM_A_BITS-1 downto 0)         |             |
| mem_wdata         | in        | std_logic_vector(D_BITS-1 downto 0)     |             |
| mem_wmask         | in        | std_logic_vector(D_BITS/8-1 downto 0)   |             |
| mem_rdy           | out       | std_logic                               |             |
| mem_rstb          | out       | std_logic                               |             |
| mem_rdata         | out       | std_logic_vector(D_BITS-1 downto 0)     |             |
| mig_calib_done    | in        | std_logic                               |             |
| mig_cmd_full      | in        | std_logic                               |             |
| mig_wr_full       | in        | std_logic                               |             |
| mig_rd_empty      | in        | std_logic                               |             |
| mig_rd_data       | in        | std_logic_vector((D_BITS)-1 downto 0)   |             |
| mig_cmd_instr     | out       | std_logic_vector(2 downto 0)            |             |
| mig_cmd_en        | out       | std_logic                               |             |
| mig_cmd_bl        | out       | std_logic_vector(5 downto 0)            |             |
| mig_cmd_byte_addr | out       | std_logic_vector(APP_A_BITS-1 downto 0) |             |
| mig_wr_data       | out       | std_logic_vector((D_BITS)-1 downto 0)   |             |
| mig_wr_mask       | out       | std_logic_vector((D_BITS)/8-1 downto 0) |             |
| mig_wr_en         | out       | std_logic                               |             |
| mig_rd_en         | out       | std_logic                               |             |
## Signals
| Name      | Type      | Description |
| --------- | --------- | ----------- |
| mem_rdy_i | std_logic |             |
## Constants
| Name           | Type     | Value               | Description |
| -------------- | -------- | ------------------- | ----------- |
| BYTE_ADDR_BITS | positive |  log2ceil(D_BITS/8) |             |
## Processes
- unnamed: _( mem_addr )_

