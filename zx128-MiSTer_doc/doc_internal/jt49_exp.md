# Entity: jt49_exp

## Diagram

![Diagram](jt49_exp.svg "Diagram")
## Description

 Th
 Compression vs dynamic range
 0 -> 43.6dB
 1 -> 29.1
 2 -> 21.8
 3 -> 13.4
 
## Ports

| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| clk       | input     | wire      |             |
| comp      | input     | wire[1:0] | compression |
| din       | input     | wire[4:0] |             |
| dout      | output    | [7:0]     |             |
## Signals

| Name | Type       | Description |
| ---- | ---------- | ----------- |
| lut  | reg [7:0]  |             |
| addr | wire [6:0] |             |
## Processes
- unnamed: ( @(posedge clk) )
