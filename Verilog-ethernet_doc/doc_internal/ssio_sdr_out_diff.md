# Entity: ssio_sdr_out_diff

- **File**: ssio_sdr_out_diff.v
## Diagram

![Diagram](ssio_sdr_out_diff.svg "Diagram")
## Description


 Language: Verilog 2001


## Generics

| Generic name | Type | Value     | Description                                                                                                                   |
| ------------ | ---- | --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| TARGET       |      | "GENERIC" |  target ("SIM", "GENERIC", "XILINX", "ALTERA")                                                                                |
| IODDR_STYLE  |      | "IODDR2"  |  IODDR style ("IODDR", "IODDR2")  Use IODDR for Virtex-4, Virtex-5, Virtex-6, 7 Series, Ultrascale  Use IODDR2 for Spartan-6  |
| WIDTH        |      | 1         |  Width of register in bits                                                                                                    |
## Ports

| Port name    | Direction | Type             | Description |
| ------------ | --------- | ---------------- | ----------- |
| clk          | input     | wire             |             |
| input_d      | input     | wire [WIDTH-1:0] |             |
| output_clk_p | output    | wire             |             |
| output_clk_n | output    | wire             |             |
| output_q_p   | output    | wire [WIDTH-1:0] |             |
| output_q_n   | output    | wire [WIDTH-1:0] |             |
## Signals

| Name       | Type             | Description |
| ---------- | ---------------- | ----------- |
| output_clk | wire             |             |
| output_q   | wire [WIDTH-1:0] |             |
## Instantiations

- ssio_ddr_out_inst: ssio_sdr_out
