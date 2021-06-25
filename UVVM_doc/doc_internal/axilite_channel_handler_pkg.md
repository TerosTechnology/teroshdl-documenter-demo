# Package: axilite_channel_handler_pkg
## Constants
| Name    | Type   | Value                      | Description |
| ------- | ------ | -------------------------- | ----------- |
| C_SCOPE | string |  "AXILITE_CHANNEL_HANDLER" |             |
## Functions
- write_address_channel_write <font id="function_arguments">(    constant awaddr_value : in    std_logic_vector;
    constant msg          : in    string;
    signal   clk          : in    std_logic;
    signal   awaddr       : inout std_logic_vector;
    signal   awvalid      : inout std_logic;
    signal   awprot       : inout std_logic_vector(2 downto 0);  [0: '0' - unpriviliged access, '1' - priviliged access; 1: '0' - secure access, '1' - non-secure access, 2: '0' - Data access, '1' - Instruction accesss]
    signal   awready      : in    std_logic;
    constant scope        : in    string                := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel        := shared_msg_id_panel;
    constant config       : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
This procedure writes adress on the write address channel- When the write is completed, a log message is issued with ID_CHANNEL_BFM
- write_data_channel_write <font id="function_arguments">(    constant wdata_value  : in    std_logic_vector;
    constant wstrb_value  : in    std_logic_vector;
    constant msg          : in    string;
    signal   clk          : in    std_logic;
    signal   wdata        : inout std_logic_vector;
    signal   wstrb        : inout std_logic_vector;
    signal   wvalid       : inout std_logic;
    signal   wready       : in    std_logic;
    constant scope        : in    string                := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel        := shared_msg_id_panel;
    constant config       : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
This procedure writes data on the write data channel- When the write is completed, a log message is issued with ID_CHANNEL_BFM
- write_response_channel_check <font id="function_arguments">(    constant msg          : in    string;
    signal   clk          : in    std_logic;
    signal   bready       : inout std_logic;
    signal   bresp        : in    std_logic_vector(1 downto 0);
    signal   bvalid       : in    std_logic;
    constant alert_level  : in    t_alert_level         := error;
    constant scope        : in    string                := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel        := shared_msg_id_panel;
    constant config       : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
This procedure checks the write response on the write response channel- If the received response was inconsistent with config.expected_response,   an alert with severity config.expected_response_severity is issued.- When completed, a log message with ID id_for_bfm is issued.
- read_address_channel_write <font id="function_arguments">(    constant araddr_value : in    std_logic_vector;
    constant msg          : in    string;
    signal   clk          : in    std_logic;
    signal   araddr       : inout std_logic_vector;
    signal   arvalid      : inout std_logic;
    signal   arprot       : inout std_logic_vector(2 downto 0);
    signal   arready      : in    std_logic;
    constant scope        : in    string                := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel        := shared_msg_id_panel;
    constant config       : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
This procedure writes adress on the read address channel- When the write is completed, a log message is issued with ID_CHANNEL_BFM
- read_data_channel_receive <font id="function_arguments">(    variable rdata_value    : out   std_logic_vector;
    constant msg            : in    string;
    signal   clk            : in    std_logic;
    signal   rready         : inout std_logic;
    signal   rdata          : in    std_logic_vector;
    signal   rresp          : in    std_logic_vector(1 downto 0);
    signal   rvalid         : in    std_logic;
    constant scope          : in    string                := C_SCOPE;
    constant msg_id_panel   : in    t_msg_id_panel        := shared_msg_id_panel;
    constant config         : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT;
    constant ext_proc_call  : in    string                := ""   External proc_call. Overwrite if called from another BFM procedure
  )</font> <font id="function_return">return ()</font>
**Description**
This procedure receives read data on the read data channel,and returns the read data- If the received response was inconsistent with config.expected_response,   an alert with severity config.expected_response_severity is issued.
- read_data_channel_check <font id="function_arguments">(    constant rdata_exp    : in    std_logic_vector;
    constant msg          : in    string;
    signal   clk          : in    std_logic;
    signal   rready       : inout std_logic;
    signal   rdata        : in    std_logic_vector;
    signal   rresp        : in    std_logic_vector(1 downto 0);
    signal   rvalid       : in    std_logic;
    constant alert_level  : in    t_alert_level         := error;
    constant scope        : in    string                := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel        := shared_msg_id_panel;
    constant config       : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
This procedure receives and checks read data and read response on the read data channel- If the received data is inconsistent with rdata_exp,   an alert with severity alert_level is issued.- If the received data is correct, a log message with ID id_for_bfm is issued.
