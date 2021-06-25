# Entity: sbi_fifo
## Diagram
![Diagram](sbi_fifo.svg "Diagram")
## Generics
| Generic name    | Type                   | Value | Description |
| --------------- | ---------------------- | ----- | ----------- |
| GC_DATA_WIDTH_1 | integer range 1 to 128 | 8     |             |
| GC_ADDR_WIDTH_1 | integer range 1 to 128 | 8     |             |
| GC_DATA_WIDTH_2 | integer range 1 to 128 | 8     |             |
| GC_ADDR_WIDTH_2 | integer range 1 to 128 | 8     |             |
## Ports
| Port name | Direction | Type                                                                                                             | Description |
| --------- | --------- | ---------------------------------------------------------------------------------------------------------------- | ----------- |
| clk       | in        | std_logic                                                                                                        |             |
| sbi_if_1  | inout     | t_sbi_if(addr(GC_ADDR_WIDTH_1-1 downto 0), wdata(GC_DATA_WIDTH_1-1 downto 0), rdata(GC_DATA_WIDTH_1-1 downto 0)) |             |
| sbi_if_2  | inout     | t_sbi_if(addr(GC_ADDR_WIDTH_2-1 downto 0), wdata(GC_DATA_WIDTH_2-1 downto 0), rdata(GC_DATA_WIDTH_2-1 downto 0)) |             |
## Signals
| Name          | Type      | Description |
| ------------- | --------- | ----------- |
| fifo_ready_1  | std_logic |             |
| fifo_ready_2  | std_logic |             |
| write_ready_1 | std_logic |             |
| write_ready_2 | std_logic |             |
| read_ready_1  | std_logic |             |
| read_ready_2  | std_logic |             |
## Constants
| Name                  | Type    | Value       | Description |
| --------------------- | ------- | ----------- | ----------- |
| C_SCOPE               | string  |  "SBI_FIFO" |             |
| C_BUFFER_INDEX_1      | natural |  1          |             |
| C_BUFFER_INDEX_2      | natural |  2          |             |
| C_BUFFER_SIZE_1       | natural |  256        |             |
| C_BUFFER_SIZE_2       | natural |  256        |             |
| C_ADDR_FIFO_PUT       | integer |  0          |             |
| C_ADDR_FIFO_GET       | integer |  1          |             |
| C_ADDR_FIFO_COUNT     | integer |  2          |             |
| C_ADDR_FIFO_PEEK      | integer |  3          |             |
| C_ADDR_FIFO_FLUSH     | integer |  4          |             |
| C_ADDR_FIFO_MAX_COUNT | integer |  5          |             |
## Processes
- p_init: _(  )_

- p_fifo_ready: _( clk )_

- p_read_reg_sbi_1: _( sbi_if_1.cs, sbi_if_1.rena, sbi_if_1.addr, fifo_ready_1 )_

- p_write_reg_sbi_1: _( clk )_

- p_read_reg_sbi_2: _( sbi_if_2.cs, sbi_if_2.rena, sbi_if_2.addr, fifo_ready_2 )_

- p_write_reg_sbi_2: _( clk )_

