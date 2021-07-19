# Entity: ssio_sdr_in

- **File**: ssio_sdr_in.v
## Diagram

![Diagram](ssio_sdr_in.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name      | Type | Value     | Description                                                                                                                                       |
| ----------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| TARGET            |      | "GENERIC" | target ("SIM", "GENERIC", "XILINX", "ALTERA")                                                                                                     |
| CLOCK_INPUT_STYLE |      | "BUFIO2"  | Clock input style ("BUFG", "BUFR", "BUFIO", "BUFIO2") Use BUFR for Virtex-5, Virtex-6, 7-series Use BUFG for Ultrascale Use BUFIO2 for Spartan-6  |
| WIDTH             |      | 1         | Width of register in bits                                                                                                                         |
## Ports

| Port name  | Direction | Type             | Description |
| ---------- | --------- | ---------------- | ----------- |
| input_clk  | input     | wire             |             |
| input_d    | input     | wire [WIDTH-1:0] |             |
| output_clk | output    | wire             |             |
| output_q   | output    | wire [WIDTH-1:0] |             |
## Signals

| Name         | Type            | Description |
| ------------ | --------------- | ----------- |
| clk_int      | wire            |             |
| clk_io       | wire            |             |
| output_q_reg | reg [WIDTH-1:0] |             |
## Processes
- unnamed: ( @(posedge clk_io) )
