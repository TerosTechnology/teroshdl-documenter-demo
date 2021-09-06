# Package: axilite_channel_handler_pkg

- **File**: axilite_channel_handler_pkg.vhd
## Description

=================================================================================================

## Constants

| Name    | Type   | Value                      | Description |
| ------- | ------ | -------------------------- | ----------- |
| C_SCOPE | string |  "AXILITE_CHANNEL_HANDLER" |             |
## Functions
- write_address_channel_write <font id="function_arguments">( constant awaddr_value : in    std_logic_vector;<br><span style="padding-left:20px"> constant msg          : in    string;<br><span style="padding-left:20px"> signal   clk          : in    std_logic;<br><span style="padding-left:20px"> signal   awaddr       : inout std_logic_vector;<br><span style="padding-left:20px"> signal   awvalid      : inout std_logic;<br><span style="padding-left:20px"> signal   awprot       : inout std_logic_vector(2 downto 0);<br><span style="padding-left:20px"> -- [0: '0' - unpriviliged access,<br><span style="padding-left:20px"> '1' - priviliged access;<br><span style="padding-left:20px"> 1: '0' - secure access,<br><span style="padding-left:20px"> '1' - non-secure access,<br><span style="padding-left:20px"> 2: '0' - Data access,<br><span style="padding-left:20px"> '1' - Instruction accesss] signal   awready      : in    std_logic;<br><span style="padding-left:20px"> constant scope        : in    string                := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel : in    t_msg_id_panel        := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config       : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
**Description**
===============================================================================================
 Procedures
===============================================================================================
----------------------------------------
 write_address_channel_write
----------------------------------------
 This procedure writes adress on the write address channel
 - When the write is completed, a log message is issued with ID_CHANNEL_BFM

- write_data_channel_write <font id="function_arguments">( constant wdata_value  : in    std_logic_vector;<br><span style="padding-left:20px"> constant wstrb_value  : in    std_logic_vector;<br><span style="padding-left:20px"> constant msg          : in    string;<br><span style="padding-left:20px"> signal   clk          : in    std_logic;<br><span style="padding-left:20px"> signal   wdata        : inout std_logic_vector;<br><span style="padding-left:20px"> signal   wstrb        : inout std_logic_vector;<br><span style="padding-left:20px"> signal   wvalid       : inout std_logic;<br><span style="padding-left:20px"> signal   wready       : in    std_logic;<br><span style="padding-left:20px"> constant scope        : in    string                := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel : in    t_msg_id_panel        := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config       : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
**Description**
----------------------------------------
 write_data_channel_write
----------------------------------------
 This procedure writes data on the write data channel
 - When the write is completed, a log message is issued with ID_CHANNEL_BFM

- write_response_channel_check <font id="function_arguments">( constant msg          : in    string;<br><span style="padding-left:20px"> signal   clk          : in    std_logic;<br><span style="padding-left:20px"> signal   bready       : inout std_logic;<br><span style="padding-left:20px"> signal   bresp        : in    std_logic_vector(1 downto 0);<br><span style="padding-left:20px"> signal   bvalid       : in    std_logic;<br><span style="padding-left:20px"> constant alert_level  : in    t_alert_level         := error;<br><span style="padding-left:20px"> constant scope        : in    string                := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel : in    t_msg_id_panel        := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config       : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
**Description**
----------------------------------------
 write_response_channel_check
----------------------------------------
 This procedure checks the write response on the write response channel
 - If the received response was inconsistent with config.expected_response, 
   an alert with severity config.expected_response_severity is issued.
 - When completed, a log message with ID id_for_bfm is issued.

- read_address_channel_write <font id="function_arguments">( constant araddr_value : in    std_logic_vector;<br><span style="padding-left:20px"> constant msg          : in    string;<br><span style="padding-left:20px"> signal   clk          : in    std_logic;<br><span style="padding-left:20px"> signal   araddr       : inout std_logic_vector;<br><span style="padding-left:20px"> signal   arvalid      : inout std_logic;<br><span style="padding-left:20px"> signal   arprot       : inout std_logic_vector(2 downto 0);<br><span style="padding-left:20px"> signal   arready      : in    std_logic;<br><span style="padding-left:20px"> constant scope        : in    string                := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel : in    t_msg_id_panel        := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config       : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
**Description**
----------------------------------------
 read_address_channel_write
----------------------------------------
 This procedure writes adress on the read address channel
 - When the write is completed, a log message is issued with ID_CHANNEL_BFM

- read_data_channel_receive <font id="function_arguments">( variable rdata_value    : out   std_logic_vector;<br><span style="padding-left:20px"> constant msg            : in    string;<br><span style="padding-left:20px"> signal   clk            : in    std_logic;<br><span style="padding-left:20px"> signal   rready         : inout std_logic;<br><span style="padding-left:20px"> signal   rdata          : in    std_logic_vector;<br><span style="padding-left:20px"> signal   rresp          : in    std_logic_vector(1 downto 0);<br><span style="padding-left:20px"> signal   rvalid         : in    std_logic;<br><span style="padding-left:20px"> constant scope          : in    string                := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel   : in    t_msg_id_panel        := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config         : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT;<br><span style="padding-left:20px"> constant ext_proc_call  : in    string                := ""  -- External proc_call. Overwrite if called from another BFM procedure ) </font> <font id="function_return">return ()</font>
**Description**
----------------------------------------
 read_data_channel_receive
----------------------------------------
 This procedure receives read data on the read data channel,
 and returns the read data
 - If the received response was inconsistent with config.expected_response, 
   an alert with severity config.expected_response_severity is issued.

- read_data_channel_check <font id="function_arguments">( constant rdata_exp    : in    std_logic_vector;<br><span style="padding-left:20px"> constant msg          : in    string;<br><span style="padding-left:20px"> signal   clk          : in    std_logic;<br><span style="padding-left:20px"> signal   rready       : inout std_logic;<br><span style="padding-left:20px"> signal   rdata        : in    std_logic_vector;<br><span style="padding-left:20px"> signal   rresp        : in    std_logic_vector(1 downto 0);<br><span style="padding-left:20px"> signal   rvalid       : in    std_logic;<br><span style="padding-left:20px"> constant alert_level  : in    t_alert_level         := error;<br><span style="padding-left:20px"> constant scope        : in    string                := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel : in    t_msg_id_panel        := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config       : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
**Description**
----------------------------------------
 read_data_channel_check
----------------------------------------
 This procedure receives and checks read data and 
 read response on the read data channel
 - If the received data is inconsistent with rdata_exp, 
   an alert with severity alert_level is issued.
 - If the received data is correct, a log message with ID id_for_bfm is issued.

