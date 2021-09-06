# Entity: serv_rf_ram

- **File**: serv_rf_ram.v
## Diagram

![Diagram](serv_rf_ram.svg "Diagram")
## Generics

| Generic name | Type | Value                  | Description |
| ------------ | ---- | ---------------------- | ----------- |
| width        |      | 0                      |             |
| csr_regs     |      | 4                      |             |
| depth        |      | 32*(32+csr_regs)/width |             |
## Ports

| Port name | Direction | Type                     | Description |
| --------- | --------- | ------------------------ | ----------- |
| i_clk     | input     | wire                     |             |
| i_waddr   | input     | wire [$clog2(depth)-1:0] |             |
| i_wdata   | input     | wire [width-1:0]         |             |
| i_wen     | input     | wire                     |             |
| i_raddr   | input     | wire [$clog2(depth)-1:0] |             |
| o_rdata   | output    | wire [width-1:0]         |             |
## Signals

| Name    | Type            | Description                                                                                                                                                                                                                                                                                                                                      |
| ------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| memory  | reg [width-1:0] |                                                                                                                                                                                                                                                                                                                                                  |
| rdata   | reg [width-1:0] |                                                                                                                                                                                                                                                                                                                                                  |
| regzero | reg             |  Reads from reg x0 needs to return 0     Check that the part of the read address corresponding to the register     is zero and gate the output     width LSB of reg index $clog2(width)     2     4                1     4     3                2     8     2                3     16    1                4     32    0                5     */  |
| i       | integer         |                                                                                                                                                                                                                                                                                                                                                  |
## Processes
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
