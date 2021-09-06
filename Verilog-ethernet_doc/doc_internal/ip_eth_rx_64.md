# Entity: ip_eth_rx_64

- **File**: ip_eth_rx_64.v
## Diagram

![Diagram](ip_eth_rx_64.svg "Diagram")
## Description


 Language: Verilog 2001


## Ports

| Port name                       | Direction | Type        | Description                          |
| ------------------------------- | --------- | ----------- | ------------------------------------ |
| clk                             | input     | wire        |                                      |
| rst                             | input     | wire        |                                      |
| s_eth_hdr_valid                 | input     | wire        |      * Ethernet frame input      */  |
| s_eth_hdr_ready                 | output    | wire        |                                      |
| s_eth_dest_mac                  | input     | wire [47:0] |                                      |
| s_eth_src_mac                   | input     | wire [47:0] |                                      |
| s_eth_type                      | input     | wire [15:0] |                                      |
| s_eth_payload_axis_tdata        | input     | wire [63:0] |                                      |
| s_eth_payload_axis_tkeep        | input     | wire [7:0]  |                                      |
| s_eth_payload_axis_tvalid       | input     | wire        |                                      |
| s_eth_payload_axis_tready       | output    | wire        |                                      |
| s_eth_payload_axis_tlast        | input     | wire        |                                      |
| s_eth_payload_axis_tuser        | input     | wire        |                                      |
| m_ip_hdr_valid                  | output    | wire        |      * IP frame output      */       |
| m_ip_hdr_ready                  | input     | wire        |                                      |
| m_eth_dest_mac                  | output    | wire [47:0] |                                      |
| m_eth_src_mac                   | output    | wire [47:0] |                                      |
| m_eth_type                      | output    | wire [15:0] |                                      |
| m_ip_version                    | output    | wire [3:0]  |                                      |
| m_ip_ihl                        | output    | wire [3:0]  |                                      |
| m_ip_dscp                       | output    | wire [5:0]  |                                      |
| m_ip_ecn                        | output    | wire [1:0]  |                                      |
| m_ip_length                     | output    | wire [15:0] |                                      |
| m_ip_identification             | output    | wire [15:0] |                                      |
| m_ip_flags                      | output    | wire [2:0]  |                                      |
| m_ip_fragment_offset            | output    | wire [12:0] |                                      |
| m_ip_ttl                        | output    | wire [7:0]  |                                      |
| m_ip_protocol                   | output    | wire [7:0]  |                                      |
| m_ip_header_checksum            | output    | wire [15:0] |                                      |
| m_ip_source_ip                  | output    | wire [31:0] |                                      |
| m_ip_dest_ip                    | output    | wire [31:0] |                                      |
| m_ip_payload_axis_tdata         | output    | wire [63:0] |                                      |
| m_ip_payload_axis_tkeep         | output    | wire [7:0]  |                                      |
| m_ip_payload_axis_tvalid        | output    | wire        |                                      |
| m_ip_payload_axis_tready        | input     | wire        |                                      |
| m_ip_payload_axis_tlast         | output    | wire        |                                      |
| m_ip_payload_axis_tuser         | output    | wire        |                                      |
| busy                            | output    | wire        |      * Status signals      */        |
| error_header_early_termination  | output    | wire        |                                      |
| error_payload_early_termination | output    | wire        |                                      |
| error_invalid_header            | output    | wire        |                                      |
| error_invalid_checksum          | output    | wire        |                                      |
## Signals

| Name                                 | Type       | Description                |
| ------------------------------------ | ---------- | -------------------------- |
| state_reg                            | reg [2:0]  |                            |
| state_next                           | reg [2:0]  |                            |
| store_eth_hdr                        | reg        |  datapath control signals  |
| store_hdr_word_0                     | reg        |                            |
| store_hdr_word_1                     | reg        |                            |
| store_hdr_word_2                     | reg        |                            |
| store_last_word                      | reg        |                            |
| flush_save                           | reg        |                            |
| transfer_in_save                     | reg        |                            |
| hdr_ptr_reg                          | reg [5:0]  |                            |
| hdr_ptr_next                         | reg [5:0]  |                            |
| word_count_reg                       | reg [15:0] |                            |
| word_count_next                      | reg [15:0] |                            |
| hdr_sum_high_reg                     | reg [16:0] |                            |
| hdr_sum_low_reg                      | reg [16:0] |                            |
| hdr_sum_temp                         | reg [19:0] |                            |
| hdr_sum_reg                          | reg [19:0] |                            |
| hdr_sum_next                         | reg [19:0] |                            |
| check_hdr_reg                        | reg        |                            |
| check_hdr_next                       | reg        |                            |
| last_word_data_reg                   | reg [63:0] |                            |
| last_word_keep_reg                   | reg [7:0]  |                            |
| s_eth_hdr_ready_reg                  | reg        |                            |
| s_eth_hdr_ready_next                 | reg        |                            |
| s_eth_payload_axis_tready_reg        | reg        |                            |
| s_eth_payload_axis_tready_next       | reg        |                            |
| m_ip_hdr_valid_reg                   | reg        |                            |
| m_ip_hdr_valid_next                  | reg        |                            |
| m_eth_dest_mac_reg                   | reg [47:0] |                            |
| m_eth_src_mac_reg                    | reg [47:0] |                            |
| m_eth_type_reg                       | reg [15:0] |                            |
| m_ip_version_reg                     | reg [3:0]  |                            |
| m_ip_ihl_reg                         | reg [3:0]  |                            |
| m_ip_dscp_reg                        | reg [5:0]  |                            |
| m_ip_ecn_reg                         | reg [1:0]  |                            |
| m_ip_length_reg                      | reg [15:0] |                            |
| m_ip_identification_reg              | reg [15:0] |                            |
| m_ip_flags_reg                       | reg [2:0]  |                            |
| m_ip_fragment_offset_reg             | reg [12:0] |                            |
| m_ip_ttl_reg                         | reg [7:0]  |                            |
| m_ip_protocol_reg                    | reg [7:0]  |                            |
| m_ip_header_checksum_reg             | reg [15:0] |                            |
| m_ip_source_ip_reg                   | reg [31:0] |                            |
| m_ip_dest_ip_reg                     | reg [31:0] |                            |
| busy_reg                             | reg        |                            |
| error_header_early_termination_reg   | reg        |                            |
| error_header_early_termination_next  | reg        |                            |
| error_payload_early_termination_reg  | reg        |                            |
| error_payload_early_termination_next | reg        |                            |
| error_invalid_header_reg             | reg        |                            |
| error_invalid_header_next            | reg        |                            |
| error_invalid_checksum_reg           | reg        |                            |
| error_invalid_checksum_next          | reg        |                            |
| save_eth_payload_axis_tdata_reg      | reg [63:0] |                            |
| save_eth_payload_axis_tkeep_reg      | reg [7:0]  |                            |
| save_eth_payload_axis_tlast_reg      | reg        |                            |
| save_eth_payload_axis_tuser_reg      | reg        |                            |
| shift_eth_payload_axis_tdata         | reg [63:0] |                            |
| shift_eth_payload_axis_tkeep         | reg [7:0]  |                            |
| shift_eth_payload_axis_tvalid        | reg        |                            |
| shift_eth_payload_axis_tlast         | reg        |                            |
| shift_eth_payload_axis_tuser         | reg        |                            |
| shift_eth_payload_s_tready           | reg        |                            |
| shift_eth_payload_extra_cycle_reg    | reg        |                            |
| m_ip_payload_axis_tdata_int          | reg [63:0] |  internal datapath         |
| m_ip_payload_axis_tkeep_int          | reg [7:0]  |                            |
| m_ip_payload_axis_tvalid_int         | reg        |                            |
| m_ip_payload_axis_tready_int_reg     | reg        |                            |
| m_ip_payload_axis_tlast_int          | reg        |                            |
| m_ip_payload_axis_tuser_int          | reg        |                            |
| m_ip_payload_axis_tready_int_early   | wire       |                            |
| m_ip_payload_axis_tdata_reg          | reg [63:0] |  output datapath logic     |
| m_ip_payload_axis_tkeep_reg          | reg [7:0]  |                            |
| m_ip_payload_axis_tvalid_reg         | reg        |                            |
| m_ip_payload_axis_tvalid_next        | reg        |                            |
| m_ip_payload_axis_tlast_reg          | reg        |                            |
| m_ip_payload_axis_tuser_reg          | reg        |                            |
| temp_m_ip_payload_axis_tdata_reg     | reg [63:0] |                            |
| temp_m_ip_payload_axis_tkeep_reg     | reg [7:0]  |                            |
| temp_m_ip_payload_axis_tvalid_reg    | reg        |                            |
| temp_m_ip_payload_axis_tvalid_next   | reg        |                            |
| temp_m_ip_payload_axis_tlast_reg     | reg        |                            |
| temp_m_ip_payload_axis_tuser_reg     | reg        |                            |
| store_ip_payload_int_to_output       | reg        |  datapath control          |
| store_ip_payload_int_to_temp         | reg        |                            |
| store_ip_payload_axis_temp_to_output | reg        |                            |
## Constants

| Name                    | Type  | Value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| STATE_IDLE              | [2:0] | 3'd0  | <br> IP Frame<br>  Field                       Length  Destination MAC address     6 octets  Source MAC address          6 octets  Ethertype (0x0800)          2 octets  Version (4)                 4 bits  IHL (5-15)                  4 bits  DSCP (0)                    6 bits  ECN (0)                     2 bits  length                      2 octets  identification (0?)         2 octets  flags (010)                 3 bits  fragment offset (0)         13 bits  time to live (64?)          1 octet  protocol                    1 octet  header checksum             2 octets  source IP                   4 octets  destination IP              4 octets  options                     (IHL-5)*4 octets  payload                     length octets<br> This module receives an Ethernet frame with header fields in parallel and payload on an AXI stream interface, decodes and strips the IP header fields, then produces the header fields in parallel along with the IP payload in a separate AXI stream.<br> */  |
| STATE_READ_HEADER       | [2:0] | 3'd1  | <br> IP Frame<br>  Field                       Length  Destination MAC address     6 octets  Source MAC address          6 octets  Ethertype (0x0800)          2 octets  Version (4)                 4 bits  IHL (5-15)                  4 bits  DSCP (0)                    6 bits  ECN (0)                     2 bits  length                      2 octets  identification (0?)         2 octets  flags (010)                 3 bits  fragment offset (0)         13 bits  time to live (64?)          1 octet  protocol                    1 octet  header checksum             2 octets  source IP                   4 octets  destination IP              4 octets  options                     (IHL-5)*4 octets  payload                     length octets<br> This module receives an Ethernet frame with header fields in parallel and payload on an AXI stream interface, decodes and strips the IP header fields, then produces the header fields in parallel along with the IP payload in a separate AXI stream.<br> */  |
| STATE_READ_PAYLOAD      | [2:0] | 3'd2  | <br> IP Frame<br>  Field                       Length  Destination MAC address     6 octets  Source MAC address          6 octets  Ethertype (0x0800)          2 octets  Version (4)                 4 bits  IHL (5-15)                  4 bits  DSCP (0)                    6 bits  ECN (0)                     2 bits  length                      2 octets  identification (0?)         2 octets  flags (010)                 3 bits  fragment offset (0)         13 bits  time to live (64?)          1 octet  protocol                    1 octet  header checksum             2 octets  source IP                   4 octets  destination IP              4 octets  options                     (IHL-5)*4 octets  payload                     length octets<br> This module receives an Ethernet frame with header fields in parallel and payload on an AXI stream interface, decodes and strips the IP header fields, then produces the header fields in parallel along with the IP payload in a separate AXI stream.<br> */  |
| STATE_READ_PAYLOAD_LAST | [2:0] | 3'd3  | <br> IP Frame<br>  Field                       Length  Destination MAC address     6 octets  Source MAC address          6 octets  Ethertype (0x0800)          2 octets  Version (4)                 4 bits  IHL (5-15)                  4 bits  DSCP (0)                    6 bits  ECN (0)                     2 bits  length                      2 octets  identification (0?)         2 octets  flags (010)                 3 bits  fragment offset (0)         13 bits  time to live (64?)          1 octet  protocol                    1 octet  header checksum             2 octets  source IP                   4 octets  destination IP              4 octets  options                     (IHL-5)*4 octets  payload                     length octets<br> This module receives an Ethernet frame with header fields in parallel and payload on an AXI stream interface, decodes and strips the IP header fields, then produces the header fields in parallel along with the IP payload in a separate AXI stream.<br> */  |
| STATE_WAIT_LAST         | [2:0] | 3'd4  | <br> IP Frame<br>  Field                       Length  Destination MAC address     6 octets  Source MAC address          6 octets  Ethertype (0x0800)          2 octets  Version (4)                 4 bits  IHL (5-15)                  4 bits  DSCP (0)                    6 bits  ECN (0)                     2 bits  length                      2 octets  identification (0?)         2 octets  flags (010)                 3 bits  fragment offset (0)         13 bits  time to live (64?)          1 octet  protocol                    1 octet  header checksum             2 octets  source IP                   4 octets  destination IP              4 octets  options                     (IHL-5)*4 octets  payload                     length octets<br> This module receives an Ethernet frame with header fields in parallel and payload on an AXI stream interface, decodes and strips the IP header fields, then produces the header fields in parallel along with the IP payload in a separate AXI stream.<br> */  |
## Functions
- keep2count <font id="function_arguments">()</font> <font id="function_return">return ([3:0])</font>
- count2keep <font id="function_arguments">()</font> <font id="function_return">return ([7:0])</font>
## Processes
- unnamed: ( @* )
  - **Type:** always
- unnamed: ( @* )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @* )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
