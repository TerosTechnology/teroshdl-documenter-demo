# Entity: sbi_fifo

- **File**: sbi_fifo.vhd
## Diagram

![Diagram](sbi_fifo.svg "Diagram")
## Description

================================================================================================================================
 Copyright 2020 Bitvis
 Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
 You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.

 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
 an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and limitations under the License.
================================================================================================================================
 Note : Any functionality not explicitly described in the documentation is subject to change at any time
--------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
 Description   : See library quick reference (under 'doc') and README-file(s)
----------------------------------------------------------------------------------------
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

| Name                  | Type    | Value       | Description      |
| --------------------- | ------- | ----------- | ---------------- |
| C_SCOPE               | string  |  "SBI_FIFO" |                  |
| C_BUFFER_INDEX_1      | natural |  1          |                  |
| C_BUFFER_INDEX_2      | natural |  2          |                  |
| C_BUFFER_SIZE_1       | natural |  256        |                  |
| C_BUFFER_SIZE_2       | natural |  256        |                  |
| C_ADDR_FIFO_PUT       | integer |  0          |  Register map :  |
| C_ADDR_FIFO_GET       | integer |  1          |                  |
| C_ADDR_FIFO_COUNT     | integer |  2          |                  |
| C_ADDR_FIFO_PEEK      | integer |  3          |                  |
| C_ADDR_FIFO_FLUSH     | integer |  4          |                  |
| C_ADDR_FIFO_MAX_COUNT | integer |  5          |                  |
## Processes
- p_init: (  )
- p_fifo_ready: ( clk )
- p_read_reg_sbi_1: ( sbi_if_1.cs, sbi_if_1.rena, sbi_if_1.addr, fifo_ready_1 )
**Description**
 Read registers for SBI IF 1 
- p_write_reg_sbi_1: ( clk )
**Description**
 Write registers for SBI IF 1 
- p_read_reg_sbi_2: ( sbi_if_2.cs, sbi_if_2.rena, sbi_if_2.addr, fifo_ready_2 )
**Description**
 Read registers for SBI IF 2 
- p_write_reg_sbi_2: ( clk )
**Description**
 Write registers for SBI IF 2 
