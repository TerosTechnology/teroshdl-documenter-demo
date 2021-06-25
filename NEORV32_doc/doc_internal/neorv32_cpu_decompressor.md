# Entity: neorv32_cpu_decompressor
## Diagram
![Diagram](neorv32_cpu_decompressor.svg "Diagram")
## Ports
| Port name    | Direction | Type                           | Description |
| ------------ | --------- | ------------------------------ | ----------- |
| ci_instr16_i | in        | std_ulogic_vector(15 downto 0) |             |
| ci_illegal_o | out       | std_ulogic                     |             |
| ci_instr32_o | out       | std_ulogic_vector(31 downto 0) |             |
## Constants
| Name            | Type    | Value | Description |
| --------------- | ------- | ----- | ----------- |
| ci_opcode_lsb_c | natural |   0   |             |
| ci_opcode_msb_c | natural |   1   |             |
| ci_rd_3_lsb_c   | natural |   2   |             |
| ci_rd_3_msb_c   | natural |   4   |             |
| ci_rd_5_lsb_c   | natural |   7   |             |
| ci_rd_5_msb_c   | natural |  11   |             |
| ci_rs1_3_lsb_c  | natural |   7   |             |
| ci_rs1_3_msb_c  | natural |   9   |             |
| ci_rs1_5_lsb_c  | natural |   7   |             |
| ci_rs1_5_msb_c  | natural |  11   |             |
| ci_rs2_3_lsb_c  | natural |   2   |             |
| ci_rs2_3_msb_c  | natural |   4   |             |
| ci_rs2_5_lsb_c  | natural |   2   |             |
| ci_rs2_5_msb_c  | natural |   6   |             |
| ci_funct3_lsb_c | natural |  13   |             |
| ci_funct3_msb_c | natural |  15   |             |
## Processes
- decompressor: _( ci_instr16_i )_

