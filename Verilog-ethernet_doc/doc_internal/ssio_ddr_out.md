# Entity: ssio_ddr_out

- **File**: ssio_ddr_out.v
## Diagram

![Diagram](ssio_ddr_out.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name | Type | Value     | Description                                                                                                                |
| ------------ | ---- | --------- | -------------------------------------------------------------------------------------------------------------------------- |
| TARGET       |      | "GENERIC" | target ("SIM", "GENERIC", "XILINX", "ALTERA")                                                                              |
| IODDR_STYLE  |      | "IODDR2"  | IODDR style ("IODDR", "IODDR2") Use IODDR for Virtex-4, Virtex-5, Virtex-6, 7 Series, Ultrascale Use IODDR2 for Spartan-6  |
| USE_CLK90    |      | "TRUE"    | Use 90 degree clock for transmit ("TRUE", "FALSE")                                                                         |
| WIDTH        |      | 1         | Width of register in bits                                                                                                  |
## Ports

| Port name  | Direction | Type             | Description |
| ---------- | --------- | ---------------- | ----------- |
| clk        | input     | wire             |             |
| clk90      | input     | wire             |             |
| input_d1   | input     | wire [WIDTH-1:0] |             |
| input_d2   | input     | wire [WIDTH-1:0] |             |
| output_clk | output    | wire             |             |
| output_q   | output    | wire [WIDTH-1:0] |             |
## Signals

| Name    | Type | Description |
| ------- | ---- | ----------- |
| ref_clk | wire |             |
## Instantiations

- clk_oddr_inst: oddr
- data_oddr_inst: oddr
