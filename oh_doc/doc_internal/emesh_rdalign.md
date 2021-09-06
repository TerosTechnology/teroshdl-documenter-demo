# Entity: emesh_rdalign

- **File**: emesh_rdalign.v
## Diagram

![Diagram](emesh_rdalign.svg "Diagram")
## Description

Byte Mode:
ADDR[2:0]   B7 B6 B5 B4  B3 B2 B1 B0
x00         0  0  0  MB0 0  0  0  MB0
x01         0  0  0  MB1 0  0  0  MB1
x10         0  0  0  MB2 0  0  0  MB2
x11         0  0  0  MB3 0  0  0  MB3
Short Mode:
ADDR[2:0]   B7 B6 B5  B4  B3 B2 B1  B0
x00         0  0  MB1 MB0 0  0  MB1 MB0
x10         0  0  MB3 MB2 0  0  MB3 MB2
Word Mode:
ADDR[2:0]   B7  B6  B5  B4  B3  B2  B1  B0
x00         MB3 MB2 MB1 MB0 MB3 MB2 MB1 MB0
Double Mode:
ADDR[2:0]   B7  B6  B5  B4  B3  B2  B1  B0
000         MB7 MB6 MB5 MB4 MB3 MB2 MB1 MB0
so..
B0=MB0|MB1|MB2|MB3
B1=MB1|MB3|0
B2=MB2|0
B3=MB3|0
A

## Ports

| Port name | Direction | Type   | Description |
| --------- | --------- | ------ | ----------- |
| addr      | input     | [2:0]  | Inputs      |
| datamode  | input     | [1:0]  |             |
| data_in   | input     | [63:0] |             |
| data_out  | output    | [63:0] | Outputs     |
## Signals

| Name         | Type        | Description |
| ------------ | ----------- | ----------- |
| byte0_sel    | wire [3:0]  | wires       |
| data_mux     | wire [31:0] |             |
| data_aligned | wire [31:0] |             |
| byte1_sel1   | wire        |             |
| byte1_sel0   | wire        |             |
| byte2_en     | wire        |             |
| byte3_en     | wire        |             |
