# Entity: eth_phy_10g_tx

## Diagram

![Diagram](eth_phy_10g_tx.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name      | Type | Value     | Description |
| ----------------- | ---- | --------- | ----------- |
| DATA_WIDTH        |      | 64        |             |
| CTRL_WIDTH        |      | undefined |             |
| HDR_WIDTH         |      | 2         |             |
| BIT_REVERSE       |      | 0         |             |
| SCRAMBLER_DISABLE |      | 0         |             |
| PRBS31_ENABLE     |      | 0         |             |
| SERDES_PIPELINE   |      | 0         |             |
## Ports

| Port name        | Direction | Type                  | Description |
| ---------------- | --------- | --------------------- | ----------- |
| clk              | input     | wire                  |             |
| rst              | input     | wire                  |             |
| xgmii_txd        | input     | wire [DATA_WIDTH-1:0] |             |
| xgmii_txc        | input     | wire [CTRL_WIDTH-1:0] |             |
| serdes_tx_data   | output    | wire [DATA_WIDTH-1:0] |             |
| serdes_tx_hdr    | output    | wire [HDR_WIDTH-1:0]  |             |
| tx_prbs31_enable | input     | wire                  |             |
## Signals

| Name            | Type                  | Description |
| --------------- | --------------------- | ----------- |
| encoded_tx_data | wire [DATA_WIDTH-1:0] |             |
| encoded_tx_hdr  | wire [HDR_WIDTH-1:0]  |             |
## Instantiations

- xgmii_baser_enc_inst: xgmii_baser_enc_64
- eth_phy_10g_tx_if_inst: eth_phy_10g_tx_if
