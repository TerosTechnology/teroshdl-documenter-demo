# Entity: ssio_sdr_in_diff

## Diagram

![Diagram](ssio_sdr_in_diff.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name      | Type | Value     | Description                                                                                                                                       |
| ----------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| TARGET            |      | "GENERIC" | target ("SIM", "GENERIC", "XILINX", "ALTERA")                                                                                                     |
| CLOCK_INPUT_STYLE |      | "BUFIO2"  | Clock input style ("BUFG", "BUFR", "BUFIO", "BUFIO2") Use BUFR for Virtex-5, Virtex-6, 7-series Use BUFG for Ultrascale Use BUFIO2 for Spartan-6  |
| WIDTH             |      | 1         | Width of register in bits                                                                                                                         |
## Ports

| Port name   | Direction | Type             | Description |
| ----------- | --------- | ---------------- | ----------- |
| input_clk_p | input     | wire             |             |
| input_clk_n | input     | wire             |             |
| input_d_p   | input     | wire [WIDTH-1:0] |             |
| input_d_n   | input     | wire [WIDTH-1:0] |             |
| output_clk  | output    | wire             |             |
| output_q    | output    | wire [WIDTH-1:0] |             |
## Signals

| Name      | Type             | Description |
| --------- | ---------------- | ----------- |
| input_clk | wire             |             |
| input_d   | wire [WIDTH-1:0] |             |
## Instantiations

- ssio_ddr_in_inst: ssio_sdr_in
