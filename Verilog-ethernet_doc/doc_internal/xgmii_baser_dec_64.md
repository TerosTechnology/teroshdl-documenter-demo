# Entity: xgmii_baser_dec_64

- **File**: xgmii_baser_dec_64.v
## Diagram

![Diagram](xgmii_baser_dec_64.svg "Diagram")
## Description


 Language: Verilog 2001


## Generics

| Generic name | Type | Value     | Description |
| ------------ | ---- | --------- | ----------- |
| DATA_WIDTH   |      | 64        |             |
| CTRL_WIDTH   |      | undefined |             |
| HDR_WIDTH    |      | 2         |             |
## Ports

| Port name       | Direction | Type                  | Description                             |
| --------------- | --------- | --------------------- | --------------------------------------- |
| clk             | input     | wire                  |                                         |
| rst             | input     | wire                  |                                         |
| encoded_rx_data | input     | wire [DATA_WIDTH-1:0] |      * 10GBASE-R encoded input      */  |
| encoded_rx_hdr  | input     | wire [HDR_WIDTH-1:0]  |                                         |
| xgmii_rxd       | output    | wire [DATA_WIDTH-1:0] |      * XGMII interface      */          |
| xgmii_rxc       | output    | wire [CTRL_WIDTH-1:0] |                                         |
| rx_bad_block    | output    | wire                  |      * Status      */                   |
## Signals

| Name              | Type                 | Description                  |
| ----------------- | -------------------- | ---------------------------- |
| decoded_ctrl      | reg [DATA_WIDTH-1:0] |     D6 D5 D4 D3 D2 D1 D0 BT  |
| decode_err        | reg [CTRL_WIDTH-1:0] |                              |
| xgmii_rxd_reg     | reg [DATA_WIDTH-1:0] |                              |
| xgmii_rxd_next    | reg [DATA_WIDTH-1:0] |                              |
| xgmii_rxc_reg     | reg [CTRL_WIDTH-1:0] |                              |
| xgmii_rxc_next    | reg [CTRL_WIDTH-1:0] |                              |
| rx_bad_block_reg  | reg                  |                              |
| rx_bad_block_next | reg                  |                              |
| i                 | integer              |                              |
## Constants

| Name                | Type  | Value | Description |
| ------------------- | ----- | ----- | ----------- |
| XGMII_IDLE          | [7:0] | 8'h07 |             |
| XGMII_LPI           | [7:0] | 8'h06 |             |
| XGMII_START         | [7:0] | 8'hfb |             |
| XGMII_TERM          | [7:0] | 8'hfd |             |
| XGMII_ERROR         | [7:0] | 8'hfe |             |
| XGMII_SEQ_OS        | [7:0] | 8'h9c |             |
| XGMII_RES_0         | [7:0] | 8'h1c |             |
| XGMII_RES_1         | [7:0] | 8'h3c |             |
| XGMII_RES_2         | [7:0] | 8'h7c |             |
| XGMII_RES_3         | [7:0] | 8'hbc |             |
| XGMII_RES_4         | [7:0] | 8'hdc |             |
| XGMII_RES_5         | [7:0] | 8'hf7 |             |
| XGMII_SIG_OS        | [7:0] | 8'h5c |             |
| CTRL_IDLE           | [6:0] | 7'h00 |             |
| CTRL_LPI            | [6:0] | 7'h06 |             |
| CTRL_ERROR          | [6:0] | 7'h1e |             |
| CTRL_RES_0          | [6:0] | 7'h2d |             |
| CTRL_RES_1          | [6:0] | 7'h33 |             |
| CTRL_RES_2          | [6:0] | 7'h4b |             |
| CTRL_RES_3          | [6:0] | 7'h55 |             |
| CTRL_RES_4          | [6:0] | 7'h66 |             |
| CTRL_RES_5          | [6:0] | 7'h78 |             |
| O_SEQ_OS            | [3:0] | 4'h0  |             |
| O_SIG_OS            | [3:0] | 4'hf  |             |
| SYNC_DATA           | [1:0] | 2'b10 |             |
| SYNC_CTRL           | [1:0] | 2'b01 |             |
| BLOCK_TYPE_CTRL     | [7:0] | 8'h1e |             |
| BLOCK_TYPE_OS_4     | [7:0] | 8'h2d |             |
| BLOCK_TYPE_START_4  | [7:0] | 8'h33 |             |
| BLOCK_TYPE_OS_START | [7:0] | 8'h66 |             |
| BLOCK_TYPE_OS_04    | [7:0] | 8'h55 |             |
| BLOCK_TYPE_START_0  | [7:0] | 8'h78 |             |
| BLOCK_TYPE_OS_0     | [7:0] | 8'h4b |             |
| BLOCK_TYPE_TERM_0   | [7:0] | 8'h87 |             |
| BLOCK_TYPE_TERM_1   | [7:0] | 8'h99 |             |
| BLOCK_TYPE_TERM_2   | [7:0] | 8'haa |             |
| BLOCK_TYPE_TERM_3   | [7:0] | 8'hb4 |             |
| BLOCK_TYPE_TERM_4   | [7:0] | 8'hcc |             |
| BLOCK_TYPE_TERM_5   | [7:0] | 8'hd2 |             |
| BLOCK_TYPE_TERM_6   | [7:0] | 8'he1 |             |
| BLOCK_TYPE_TERM_7   | [7:0] | 8'hff |             |
## Processes
- unnamed: ( @* )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
