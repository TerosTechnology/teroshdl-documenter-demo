# Entity: axis_eth_fcs_check_64

- **File**: axis_eth_fcs_check_64.v
## Diagram

![Diagram](axis_eth_fcs_check_64.svg "Diagram")
## Description

Language: Verilog 2001
 
## Ports

| Port name     | Direction | Type        | Description |
| ------------- | --------- | ----------- | ----------- |
| clk           | input     | wire        |             |
| rst           | input     | wire        |             |
| s_axis_tdata  | input     | wire [63:0] |             |
| s_axis_tkeep  | input     | wire [7:0]  |             |
| s_axis_tvalid | input     | wire        |             |
| s_axis_tready | output    | wire        |             |
| s_axis_tlast  | input     | wire        |             |
| s_axis_tuser  | input     | wire        |             |
| m_axis_tdata  | output    | wire [63:0] |             |
| m_axis_tkeep  | output    | wire [7:0]  |             |
| m_axis_tvalid | output    | wire        |             |
| m_axis_tready | input     | wire        |             |
| m_axis_tlast  | output    | wire        |             |
| m_axis_tuser  | output    | wire        |             |
| busy          | output    | wire        |             |
| error_bad_fcs | output    | wire        |             |
## Signals

| Name                      | Type        | Description               |
| ------------------------- | ----------- | ------------------------- |
| state_reg                 | reg [1:0]   |                           |
| state_next                | reg [1:0]   |                           |
| reset_crc                 | reg         | datapath control signals  |
| update_crc                | reg         |                           |
| shift_in                  | reg         |                           |
| shift_reset               | reg         |                           |
| last_cycle_tkeep_reg      | reg [7:0]   |                           |
| last_cycle_tkeep_next     | reg [7:0]   |                           |
| last_cycle_tuser_reg      | reg         |                           |
| last_cycle_tuser_next     | reg         |                           |
| s_axis_tdata_d0           | reg [63:0]  |                           |
| s_axis_tkeep_d0           | reg [7:0]   |                           |
| s_axis_tvalid_d0          | reg         |                           |
| s_axis_tuser_d0           | reg         |                           |
| busy_reg                  | reg         |                           |
| error_bad_fcs_reg         | reg         |                           |
| error_bad_fcs_next        | reg         |                           |
| s_axis_tready_reg         | reg         |                           |
| s_axis_tready_next        | reg         |                           |
| crc_state                 | reg [31:0]  |                           |
| crc_state3                | reg [31:0]  |                           |
| crc_next0                 | wire [31:0] |                           |
| crc_next1                 | wire [31:0] |                           |
| crc_next2                 | wire [31:0] |                           |
| crc_next3                 | wire [31:0] |                           |
| crc_next7                 | wire [31:0] |                           |
| crc_valid0                | wire        |                           |
| crc_valid1                | wire        |                           |
| crc_valid2                | wire        |                           |
| crc_valid3                | wire        |                           |
| m_axis_tdata_int          | reg [63:0]  | internal datapath         |
| m_axis_tkeep_int          | reg [7:0]   |                           |
| m_axis_tvalid_int         | reg         |                           |
| m_axis_tready_int_reg     | reg         |                           |
| m_axis_tlast_int          | reg         |                           |
| m_axis_tuser_int          | reg         |                           |
| m_axis_tready_int_early   | wire        |                           |
| last_cycle                | wire        |                           |
| m_axis_tdata_reg          | reg [63:0]  | output datapath logic     |
| m_axis_tkeep_reg          | reg [7:0]   |                           |
| m_axis_tvalid_reg         | reg         |                           |
| m_axis_tvalid_next        | reg         |                           |
| m_axis_tlast_reg          | reg         |                           |
| m_axis_tuser_reg          | reg         |                           |
| temp_m_axis_tdata_reg     | reg [63:0]  |                           |
| temp_m_axis_tkeep_reg     | reg [7:0]   |                           |
| temp_m_axis_tvalid_reg    | reg         |                           |
| temp_m_axis_tvalid_next   | reg         |                           |
| temp_m_axis_tlast_reg     | reg         |                           |
| temp_m_axis_tuser_reg     | reg         |                           |
| store_axis_int_to_output  | reg         | datapath control          |
| store_axis_int_to_temp    | reg         |                           |
| store_axis_temp_to_output | reg         |                           |
## Constants

| Name          | Type  | Value | Description |
| ------------- | ----- | ----- | ----------- |
| STATE_IDLE    | [1:0] | 2'd0  |             |
| STATE_PAYLOAD | [1:0] | 2'd1  |             |
| STATE_LAST    | [1:0] | 2'd2  |             |
## Processes
- unnamed: ( @* )
- unnamed: ( @(posedge clk) )
- unnamed: ( @* )
- unnamed: ( @(posedge clk) )
## Instantiations

- eth_crc_8: lfsr
- eth_crc_16: lfsr
- eth_crc_24: lfsr
- eth_crc_32: lfsr
- eth_crc_64: lfsr
