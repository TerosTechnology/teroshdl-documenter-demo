# Entity: axis_eth_fcs_insert

- **File**: axis_eth_fcs_insert.v
## Diagram

![Diagram](axis_eth_fcs_insert.svg "Diagram")
## Description

Language: Verilog 2001
 
## Generics

| Generic name     | Type | Value | Description |
| ---------------- | ---- | ----- | ----------- |
| ENABLE_PADDING   |      | 0     |             |
| MIN_FRAME_LENGTH |      | 64    |             |
## Ports

| Port name     | Direction | Type       | Description |
| ------------- | --------- | ---------- | ----------- |
| clk           | input     | wire       |             |
| rst           | input     | wire       |             |
| s_axis_tdata  | input     | wire [7:0] |             |
| s_axis_tvalid | input     | wire       |             |
| s_axis_tready | output    | wire       |             |
| s_axis_tlast  | input     | wire       |             |
| s_axis_tuser  | input     | wire       |             |
| m_axis_tdata  | output    | wire [7:0] |             |
| m_axis_tvalid | output    | wire       |             |
| m_axis_tready | input     | wire       |             |
| m_axis_tlast  | output    | wire       |             |
| m_axis_tuser  | output    | wire       |             |
| busy          | output    | wire       |             |
## Signals

| Name                      | Type        | Description               |
| ------------------------- | ----------- | ------------------------- |
| state_reg                 | reg [1:0]   |                           |
| state_next                | reg [1:0]   |                           |
| reset_crc                 | reg         | datapath control signals  |
| update_crc                | reg         |                           |
| frame_ptr_reg             | reg [15:0]  |                           |
| frame_ptr_next            | reg [15:0]  |                           |
| busy_reg                  | reg         |                           |
| s_axis_tready_reg         | reg         |                           |
| s_axis_tready_next        | reg         |                           |
| crc_state                 | reg [31:0]  |                           |
| crc_next                  | wire [31:0] |                           |
| m_axis_tdata_int          | reg [7:0]   | internal datapath         |
| m_axis_tvalid_int         | reg         |                           |
| m_axis_tready_int_reg     | reg         |                           |
| m_axis_tlast_int          | reg         |                           |
| m_axis_tuser_int          | reg         |                           |
| m_axis_tready_int_early   | wire        |                           |
| m_axis_tdata_reg          | reg [7:0]   | output datapath logic     |
| m_axis_tvalid_reg         | reg         |                           |
| m_axis_tvalid_next        | reg         |                           |
| m_axis_tlast_reg          | reg         |                           |
| m_axis_tuser_reg          | reg         |                           |
| temp_m_axis_tdata_reg     | reg [7:0]   |                           |
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
| STATE_PAD     | [1:0] | 2'd2  |             |
| STATE_FCS     | [1:0] | 2'd3  |             |
## Processes
- unnamed: ( @* )
- unnamed: ( @(posedge clk) )
- unnamed: ( @* )
- unnamed: ( @(posedge clk) )
## Instantiations

- eth_crc_8: lfsr
