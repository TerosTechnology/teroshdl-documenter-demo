# Entity: eth_phy_10g_rx

- **File**: eth_phy_10g_rx.v
## Diagram

![Diagram](eth_phy_10g_rx.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name        | Type | Value      | Description |
| ------------------- | ---- | ---------- | ----------- |
| DATA_WIDTH          |      | 64         |             |
| CTRL_WIDTH          |      | undefined  |             |
| HDR_WIDTH           |      | 2          |             |
| BIT_REVERSE         |      | 0          |             |
| SCRAMBLER_DISABLE   |      | 0          |             |
| PRBS31_ENABLE       |      | 0          |             |
| SERDES_PIPELINE     |      | 0          |             |
| BITSLIP_HIGH_CYCLES |      | 1          |             |
| BITSLIP_LOW_CYCLES  |      | 8          |             |
| COUNT_125US         |      | 125000/6.4 |             |
## Ports

| Port name         | Direction | Type                  | Description |
| ----------------- | --------- | --------------------- | ----------- |
| clk               | input     | wire                  |             |
| rst               | input     | wire                  |             |
| xgmii_rxd         | output    | wire [DATA_WIDTH-1:0] |             |
| xgmii_rxc         | output    | wire [CTRL_WIDTH-1:0] |             |
| serdes_rx_data    | input     | wire [DATA_WIDTH-1:0] |             |
| serdes_rx_hdr     | input     | wire [HDR_WIDTH-1:0]  |             |
| serdes_rx_bitslip | output    | wire                  |             |
| rx_error_count    | output    | wire [6:0]            |             |
| rx_bad_block      | output    | wire                  |             |
| rx_block_lock     | output    | wire                  |             |
| rx_high_ber       | output    | wire                  |             |
| rx_prbs31_enable  | input     | wire                  |             |
## Signals

| Name            | Type                  | Description |
| --------------- | --------------------- | ----------- |
| encoded_rx_data | wire [DATA_WIDTH-1:0] |             |
| encoded_rx_hdr  | wire [HDR_WIDTH-1:0]  |             |
## Instantiations

- eth_phy_10g_rx_if_inst: eth_phy_10g_rx_if
- xgmii_baser_dec_inst: xgmii_baser_dec_64
