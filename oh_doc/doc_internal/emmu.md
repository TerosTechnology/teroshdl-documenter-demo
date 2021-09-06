# Entity: emmu

- **File**: emmu.v
## Diagram

![Diagram](emmu.svg "Diagram")
## Description

 ###########################################################################
 # MEMORY TRANSACTION TRANSLATOR
 # 
 # This block uses the upper 12 bits [31:20] of a memory address as an index
 # to read an entry from a table.
 #
 # Writes are done from the register config interface
 #
 # The table can be configured as 12 bits wide or 44 bits wide.
 #
 # 32bit address output = {table_data[11:0],dstaddr[19:0]}
 # 64bit address output = {table_data[43:0],dstaddr[19:0]}
 #
 ############################################################################

## Generics

| Generic name | Type | Value | Description                              |
| ------------ | ---- | ----- | ---------------------------------------- |
| AW           |      | 32    |  address width                           |
| MW           |      | 48    |  width of table                          |
| MAW          |      | 12    |  memory addres width (entries = 1<<MAW)  |
## Ports

| Port name        | Direction | Type     | Description                      |
| ---------------- | --------- | -------- | -------------------------------- |
| nreset           | input     |          | async active low reset           |
| mmu_en           | input     |          | enables mmu (by config register) |
| wr_clk           | input     |          | single clock                     |
| reg_access       | input     |          | valid packet                     |
| reg_packet       | input     | [PW-1:0] | packet                           |
| reg_rdata        | output    | [31:0]   | readback data                    |
| rd_clk           | input     |          | single clock                     |
| emesh_access_in  | input     |          | valid packet                     |
| emesh_packet_in  | input     | [PW-1:0] | input packet                     |
| emesh_wait_in    | input     |          | pushback                         |
| emesh_access_out | output    |          | valid packet                     |
| emesh_packet_out | output    | [PW-1:0] | output packet                    |
## Signals

| Name              | Type          | Description                                                                                                                                                      |
| ----------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| emesh_access_out  | reg           | ##################################################################### # BODY ##################################################################### wires + regs  |
| emesh_packet_reg  | reg [PW-1:0]  |                                                                                                                                                                  |
| emesh_dstaddr_out | wire [63:0]   |                                                                                                                                                                  |
| emmu_lookup_data  | wire [MW-1:0] |                                                                                                                                                                  |
| mem_wem           | wire [MW-1:0] |                                                                                                                                                                  |
| mem_data          | wire [MW-1:0] |                                                                                                                                                                  |
| emesh_dstaddr_in  | wire [AW-1:0] |                                                                                                                                                                  |
| reg_ctrlmode      | wire [4:0]    | From pe2 of packet2emesh.v                                                                                                                                       |
| reg_data          | wire [AW-1:0] | From pe2 of packet2emesh.v                                                                                                                                       |
| reg_datamode      | wire [1:0]    | From pe2 of packet2emesh.v                                                                                                                                       |
| reg_dstaddr       | wire [AW-1:0] | From pe2 of packet2emesh.v                                                                                                                                       |
| reg_srcaddr       | wire [AW-1:0] | From pe2 of packet2emesh.v                                                                                                                                       |
| reg_write         | wire          | From pe2 of packet2emesh.v                                                                                                                                       |
## Constants

| Name | Type | Value   | Description   |
| ---- | ---- | ------- | ------------- |
| PW   |      | 2*AW+40 | packet width  |
## Processes
- unnamed: ( @ (posedge  rd_clk) )
  - **Type:** always
</br>**Description**
########################### # OUTPUT PACKET ###########################          pipeline (compensates for 1 cycle memory access) 
- unnamed: ( @ (posedge  rd_clk) )
  - **Type:** always
