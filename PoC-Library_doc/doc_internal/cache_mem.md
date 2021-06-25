# Entity: cache_mem
## Diagram
![Diagram](cache_mem.svg "Diagram")
## Generics
| Generic name       | Type     | Value | Description |
| ------------------ | -------- | ----- | ----------- |
| REPLACEMENT_POLICY | string   | "LRU" |             |
| CACHE_LINES        | positive |       |             |
| ASSOCIATIVITY      | positive |       |             |
| CPU_DATA_BITS      | positive |       |             |
| MEM_ADDR_BITS      | positive |       |             |
| MEM_DATA_BITS      | positive |       |             |
| OUTSTANDING_REQ    | positive | 2     |             |
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
| cpu_rdy   | out       | std_logic                                                                |             |
| cpu_rstb  | out       | std_logic                                                                |             |
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
| Name      | Type                                         | Description |
| --------- | -------------------------------------------- | ----------- |
| int_req   | std_logic                                    |             |
| int_write | std_logic                                    |             |
| int_addr  | unsigned(CPU_ADDR_BITS-1 downto 0)           |             |
| int_wdata | std_logic_vector(CPU_DATA_BITS-1 downto 0)   |             |
| int_wmask | std_logic_vector(CPU_DATA_BITS/8-1 downto 0) |             |
| int_got   | std_logic                                    |             |
| int_rdata | std_logic_vector(CPU_DATA_BITS-1 downto 0)   |             |
## Constants
| Name          | Type     | Value                                                | Description |
| ------------- | -------- | ---------------------------------------------------- | ----------- |
| CPU_ADDR_BITS | positive |  log2ceil(MEM_DATA_BITS/CPU_DATA_BITS)+MEM_ADDR_BITS |             |
## Instantiations
- cache_cpu_inst: work.cache_cpu
