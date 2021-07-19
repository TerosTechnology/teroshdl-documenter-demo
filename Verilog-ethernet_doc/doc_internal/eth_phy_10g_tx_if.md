# Entity: eth_phy_10g_tx_if

- **File**: eth_phy_10g_tx_if.v
## Diagram

![Diagram](eth_phy_10g_tx_if.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name      | Type | Value | Description |
| ----------------- | ---- | ----- | ----------- |
| DATA_WIDTH        |      | 64    |             |
| HDR_WIDTH         |      | 2     |             |
| BIT_REVERSE       |      | 0     |             |
| SCRAMBLER_DISABLE |      | 0     |             |
| PRBS31_ENABLE     |      | 0     |             |
| SERDES_PIPELINE   |      | 0     |             |
## Ports

| Port name        | Direction | Type                  | Description |
| ---------------- | --------- | --------------------- | ----------- |
| clk              | input     | wire                  |             |
| rst              | input     | wire                  |             |
| encoded_tx_data  | input     | wire [DATA_WIDTH-1:0] |             |
| encoded_tx_hdr   | input     | wire [HDR_WIDTH-1:0]  |             |
| serdes_tx_data   | output    | wire [DATA_WIDTH-1:0] |             |
| serdes_tx_hdr    | output    | wire [HDR_WIDTH-1:0]  |             |
| tx_prbs31_enable | input     | wire                  |             |
## Signals

| Name                | Type                            | Description |
| ------------------- | ------------------------------- | ----------- |
| scrambler_state_reg | reg [57:0]                      |             |
| scrambler_state     | wire [57:0]                     |             |
| scrambled_data      | wire [DATA_WIDTH-1:0]           |             |
| prbs31_state_reg    | reg [30:0]                      |             |
| prbs31_state        | wire [30:0]                     |             |
| prbs31_data         | wire [DATA_WIDTH+HDR_WIDTH-1:0] |             |
| serdes_tx_data_reg  | reg [DATA_WIDTH-1:0]            |             |
| serdes_tx_hdr_reg   | reg [HDR_WIDTH-1:0]             |             |
| serdes_tx_data_int  | wire [DATA_WIDTH-1:0]           |             |
| serdes_tx_hdr_int   | wire [HDR_WIDTH-1:0]            |             |
## Processes
- unnamed: ( @(posedge clk) )
## Instantiations

- scrambler_inst: lfsr
- prbs31_gen_inst: lfsr
