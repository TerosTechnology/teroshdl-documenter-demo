# Entity: cache_cpu
## Diagram
![Diagram](cache_cpu.svg "Diagram")
## Generics
| Generic name       | Type     | Value | Description |
| ------------------ | -------- | ----- | ----------- |
| REPLACEMENT_POLICY | string   | "LRU" |             |
| CACHE_LINES        | positive |       |             |
| ASSOCIATIVITY      | positive |       |             |
| CPU_DATA_BITS      | positive |       |             |
| MEM_ADDR_BITS      | positive |       |             |
| MEM_DATA_BITS      | positive |       |             |
## Ports
| Port name | Direction | Type                                                                     | Description |
| --------- | --------- | ------------------------------------------------------------------------ | ----------- |
| clk       | in        | std_logic                                                                |             |
| rst       | in        | std_logic                                                                |             |
| cpu_req   | in        | std_logic                                                                |             |
| cpu_write | in        | std_logic                                                                |             |
| cpu_addr  | in        | unsigned(log2ceil(MEM_DATA_BITS/CPU_DATA_BITS)+MEM_ADDR_BITS-1 downto 0) |             |
| cpu_wdata | in        | std_logic_vector(CPU_DATA_BITS-1 downto 0)                               |             |
| cpu_wmask | in        | std_logic_vector(CPU_DATA_BITS/8-1 downto 0)                             |             |
| cpu_got   | out       | std_logic                                                                |             |
| cpu_rdata | out       | std_logic_vector(CPU_DATA_BITS-1 downto 0)                               |             |
| mem_req   | out       | std_logic                                                                |             |
| mem_write | out       | std_logic                                                                |             |
| mem_addr  | out       | unsigned(MEM_ADDR_BITS-1 downto 0)                                       |             |
| mem_wdata | out       | std_logic_vector(MEM_DATA_BITS-1 downto 0)                               |             |
| mem_wmask | out       | std_logic_vector(MEM_DATA_BITS/8-1 downto 0)                             |             |
| mem_rdy   | in        | std_logic                                                                |             |
| mem_rstb  | in        | std_logic                                                                |             |
| mem_rdata | in        | std_logic_vector(MEM_DATA_BITS-1 downto 0)                               |             |
## Signals
| Name             | Type                                         | Description |
| ---------------- | -------------------------------------------- | ----------- |
| cpu_wdata_wide   | std_logic_vector(MEM_DATA_BITS-1 downto 0)   |             |
| cpu_wmask_wide   | std_logic_vector(MEM_DATA_BITS/8-1 downto 0) |             |
| cache_Request    | std_logic                                    |             |
| cache_ReadWrite  | std_logic                                    |             |
| cache_Writemask  | std_logic_vector(MEM_DATA_BITS/8-1 downto 0) |             |
| cache_Invalidate | std_logic                                    |             |
| cache_Replace    | std_logic                                    |             |
| cache_Address    | std_logic_vector(MEM_ADDR_BITS-1 downto 0)   |             |
| cache_LineIn     | std_logic_vector(MEM_DATA_BITS-1 downto 0)   |             |
| cache_LineOut    | std_logic_vector(MEM_DATA_BITS-1 downto 0)   |             |
| cache_Hit        | std_logic                                    |             |
| cache_Miss       | std_logic                                    |             |
| fsm_cs           | T_FSM                                        |             |
| fsm_ns           | T_FSM                                        |             |
## Constants
| Name            | Type     | Value                        | Description |
| --------------- | -------- | ---------------------------- | ----------- |
| RATIO           | positive |  MEM_DATA_BITS/CPU_DATA_BITS |             |
| LOWER_ADDR_BITS | natural  |  log2ceil(RATIO)             |             |
## Types
| Name  | Type                                      | Description |
| ----- | ----------------------------------------- | ----------- |
| T_FSM | (READY, ACCESS_MEM, READING_MEM, UNKNOWN) |             |
## Processes
- unnamed: _( fsm_cs, cpu_req, cpu_write, cache_Hit, cache_Miss, mem_rdy, mem_rstb )_

- unnamed: _( clk )_

## Instantiations
- cache_inst: work.cache_par2
