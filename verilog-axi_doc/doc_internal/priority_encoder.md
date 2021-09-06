# Entity: priority_encoder

- **File**: priority_encoder.v
## Diagram

![Diagram](priority_encoder.svg "Diagram")
## Description


 Language: Verilog 2001


## Generics

| Generic name      | Type | Value         | Description              |
| ----------------- | ---- | ------------- | ------------------------ |
| WIDTH             |      | 4             |                          |
| LSB_HIGH_PRIORITY |      | 0             |  LSB priority selection  |
| LEVELS            |      | $clog2(WIDTH) |                          |
| W                 |      | 2**LEVELS     |                          |
## Ports

| Port name        | Direction | Type                     | Description |
| ---------------- | --------- | ------------------------ | ----------- |
| input_unencoded  | input     | wire [WIDTH-1:0]         |             |
| output_valid     | output    | wire                     |             |
| output_encoded   | output    | wire [$clog2(WIDTH)-1:0] |             |
| output_unencoded | output    | wire [WIDTH-1:0]         |             |
## Signals

| Name         | Type           | Description                      |
| ------------ | -------------- | -------------------------------- |
| input_padded | wire [W-1:0]   |  pad input to even power of two  |
| stage_valid  | wire [W/2-1:0] |                                  |
| stage_enc    | wire [W/2-1:0] |                                  |
