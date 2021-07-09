# Entity: lfsr

## Diagram

![Diagram](lfsr.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name      | Type | Value        | Description                                         |
| ----------------- | ---- | ------------ | --------------------------------------------------- |
| LFSR_WIDTH        |      | 31           | width of LFSR                                       |
| LFSR_POLY         |      | 31'h10000001 | LFSR polynomial                                     |
| LFSR_CONFIG       |      | "FIBONACCI"  | LFSR configuration: "GALOIS", "FIBONACCI"           |
| LFSR_FEED_FORWARD |      | 0            | LFSR feed forward enable                            |
| REVERSE           |      | 0            | bit-reverse input and output                        |
| DATA_WIDTH        |      | 8            | width of data input                                 |
| STYLE             |      | "AUTO"       | implementation style: "AUTO", "LOOP", "REDUCTION"   |
| STYLE_INT         |      | "REDUCTION"  | "AUTO" style is "REDUCTION" for faster simulation   |
| STYLE_INT         |      | "LOOP"       | "AUTO" style is "LOOP" for better synthesis result  |
## Ports

| Port name | Direction | Type                  | Description |
| --------- | --------- | --------------------- | ----------- |
| data_in   | input     | wire [DATA_WIDTH-1:0] |             |
| state_in  | input     | wire [LFSR_WIDTH-1:0] |             |
| data_out  | output    | wire [DATA_WIDTH-1:0] |             |
| state_out | output    | wire [LFSR_WIDTH-1:0] |             |
## Signals

| Name              | Type                 | Description |
| ----------------- | -------------------- | ----------- |
| lfsr_mask_state   | reg [LFSR_WIDTH-1:0] |             |
| lfsr_mask_data    | reg [DATA_WIDTH-1:0] |             |
| output_mask_state | reg [LFSR_WIDTH-1:0] |             |
| output_mask_data  | reg [DATA_WIDTH-1:0] |             |
| state_val         | reg [LFSR_WIDTH-1:0] |             |
| data_val          | reg [DATA_WIDTH-1:0] |             |
| i                 | integer              |             |
| j                 | integer              |             |
| k                 | integer              |             |
