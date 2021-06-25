# Entity: serv_rf_ram
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
| o_rdata   | output    | [width-1:0]              |             |
## Signals
| Name   | Type            | Description |
| ------ | --------------- | ----------- |
| memory | reg [width-1:0] |             |
| i      | integer         |             |
## Processes
- unnamed: _( @(posedge i_clk) )_

