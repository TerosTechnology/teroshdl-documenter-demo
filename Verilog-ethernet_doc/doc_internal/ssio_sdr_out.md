# Entity: ssio_sdr_out

## Diagram

![Diagram](ssio_sdr_out.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name | Type | Value     | Description                                                                                                                |
| ------------ | ---- | --------- | -------------------------------------------------------------------------------------------------------------------------- |
| TARGET       |      | "GENERIC" | target ("SIM", "GENERIC", "XILINX", "ALTERA")                                                                              |
| IODDR_STYLE  |      | "IODDR2"  | IODDR style ("IODDR", "IODDR2") Use IODDR for Virtex-4, Virtex-5, Virtex-6, 7 Series, Ultrascale Use IODDR2 for Spartan-6  |
| WIDTH        |      | 1         | Width of register in bits                                                                                                  |
## Ports

| Port name  | Direction | Type             | Description |
| ---------- | --------- | ---------------- | ----------- |
| clk        | input     | wire             |             |
| input_d    | input     | wire [WIDTH-1:0] |             |
| output_clk | output    | wire             |             |
| output_q   | output    | wire [WIDTH-1:0] |             |
## Signals

| Name         | Type            | Description |
| ------------ | --------------- | ----------- |
| output_q_reg | reg [WIDTH-1:0] |             |
## Processes
- unnamed: ( @(posedge clk) )
## Instantiations

- clk_oddr_inst: oddr
