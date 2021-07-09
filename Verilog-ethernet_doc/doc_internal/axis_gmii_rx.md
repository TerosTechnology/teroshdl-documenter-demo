# Entity: axis_gmii_rx

## Diagram

![Diagram](axis_gmii_rx.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name  | Type | Value | Description |
| ------------- | ---- | ----- | ----------- |
| DATA_WIDTH    |      | 8     |             |
| PTP_TS_ENABLE |      | 0     |             |
| PTP_TS_WIDTH  |      | 96    |             |
| USER_WIDTH    |      | + 1   |             |
## Ports

| Port name       | Direction | Type                    | Description |
| --------------- | --------- | ----------------------- | ----------- |
| clk             | input     | wire                    |             |
| rst             | input     | wire                    |             |
| gmii_rxd        | input     | wire [DATA_WIDTH-1:0]   |             |
| gmii_rx_dv      | input     | wire                    |             |
| gmii_rx_er      | input     | wire                    |             |
| m_axis_tdata    | output    | wire [DATA_WIDTH-1:0]   |             |
| m_axis_tvalid   | output    | wire                    |             |
| m_axis_tlast    | output    | wire                    |             |
| m_axis_tuser    | output    | wire [USER_WIDTH-1:0]   |             |
| ptp_ts          | input     | wire [PTP_TS_WIDTH-1:0] |             |
| clk_enable      | input     | wire                    |             |
| mii_select      | input     | wire                    |             |
| start_packet    | output    | wire                    |             |
| error_bad_frame | output    | wire                    |             |
| error_bad_fcs   | output    | wire                    |             |
## Signals

| Name                 | Type                   | Description               |
| -------------------- | ---------------------- | ------------------------- |
| state_reg            | reg [2:0]              |                           |
| state_next           | reg [2:0]              |                           |
| reset_crc            | reg                    | datapath control signals  |
| update_crc           | reg                    |                           |
| mii_odd              | reg                    |                           |
| mii_locked           | reg                    |                           |
| gmii_rxd_d0          | reg [DATA_WIDTH-1:0]   |                           |
| gmii_rxd_d1          | reg [DATA_WIDTH-1:0]   |                           |
| gmii_rxd_d2          | reg [DATA_WIDTH-1:0]   |                           |
| gmii_rxd_d3          | reg [DATA_WIDTH-1:0]   |                           |
| gmii_rxd_d4          | reg [DATA_WIDTH-1:0]   |                           |
| gmii_rx_dv_d0        | reg                    |                           |
| gmii_rx_dv_d1        | reg                    |                           |
| gmii_rx_dv_d2        | reg                    |                           |
| gmii_rx_dv_d3        | reg                    |                           |
| gmii_rx_dv_d4        | reg                    |                           |
| gmii_rx_er_d0        | reg                    |                           |
| gmii_rx_er_d1        | reg                    |                           |
| gmii_rx_er_d2        | reg                    |                           |
| gmii_rx_er_d3        | reg                    |                           |
| gmii_rx_er_d4        | reg                    |                           |
| m_axis_tdata_reg     | reg [DATA_WIDTH-1:0]   |                           |
| m_axis_tdata_next    | reg [DATA_WIDTH-1:0]   |                           |
| m_axis_tvalid_reg    | reg                    |                           |
| m_axis_tvalid_next   | reg                    |                           |
| m_axis_tlast_reg     | reg                    |                           |
| m_axis_tlast_next    | reg                    |                           |
| m_axis_tuser_reg     | reg                    |                           |
| m_axis_tuser_next    | reg                    |                           |
| start_packet_reg     | reg                    |                           |
| start_packet_next    | reg                    |                           |
| error_bad_frame_reg  | reg                    |                           |
| error_bad_frame_next | reg                    |                           |
| error_bad_fcs_reg    | reg                    |                           |
| error_bad_fcs_next   | reg                    |                           |
| ptp_ts_reg           | reg [PTP_TS_WIDTH-1:0] |                           |
| ptp_ts_next          | reg [PTP_TS_WIDTH-1:0] |                           |
| crc_state            | reg [31:0]             |                           |
| crc_next             | wire [31:0]            |                           |
## Constants

| Name            | Type  | Value | Description |
| --------------- | ----- | ----- | ----------- |
| ETH_PRE         | [7:0] | 8'h55 |             |
| ETH_SFD         | [7:0] | 8'hD5 |             |
| STATE_IDLE      | [2:0] | 3'd0  |             |
| STATE_PAYLOAD   | [2:0] | 3'd1  |             |
| STATE_WAIT_LAST | [2:0] | 3'd2  |             |
## Processes
- unnamed: ( @* )
- unnamed: ( @(posedge clk) )
## Instantiations

- eth_crc_8: lfsr
