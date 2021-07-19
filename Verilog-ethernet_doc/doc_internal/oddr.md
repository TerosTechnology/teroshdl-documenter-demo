# Entity: oddr

- **File**: oddr.v
## Diagram

![Diagram](oddr.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name | Type | Value     | Description                                                                                                                |
| ------------ | ---- | --------- | -------------------------------------------------------------------------------------------------------------------------- |
| TARGET       |      | "GENERIC" | target ("SIM", "GENERIC", "XILINX", "ALTERA")                                                                              |
| IODDR_STYLE  |      | "IODDR2"  | IODDR style ("IODDR", "IODDR2") Use IODDR for Virtex-4, Virtex-5, Virtex-6, 7 Series, Ultrascale Use IODDR2 for Spartan-6  |
| WIDTH        |      | 1         | Width of register in bits                                                                                                  |
## Ports

| Port name | Direction | Type             | Description |
| --------- | --------- | ---------------- | ----------- |
| clk       | input     | wire             |             |
| d1        | input     | wire [WIDTH-1:0] |             |
| d2        | input     | wire [WIDTH-1:0] |             |
| q         | output    | wire [WIDTH-1:0] |             |
