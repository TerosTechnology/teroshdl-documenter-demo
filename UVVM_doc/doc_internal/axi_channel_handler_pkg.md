# Package: axi_channel_handler_pkg
## Constants
| Name    | Type   | Value                  | Description |
| ------- | ------ | ---------------------- | ----------- |
| C_SCOPE | string |  "AXI_CHANNEL_HANDLER" |             |
## Functions
- write_address_channel_write <font id="function_arguments">(    constant awid_value     : in    std_logic_vector;
    constant awaddr_value   : in    unsigned;
    constant awlen_value    : in    unsigned(7 downto 0);
    constant awsize_value   : in    integer range 1 to 128;
    constant awburst_value  : in    t_axburst;
    constant awlock_value   : in    t_axlock;
    constant awcache_value  : in    std_logic_vector(3 downto 0);
    constant awprot_value   : in    t_axprot;
    constant awqos_value    : in    std_logic_vector(3 downto 0);
    constant awregion_value : in    std_logic_vector(3 downto 0);
    constant awuser_value   : in    std_logic_vector;
    constant msg            : in    string;
    signal   clk            : in    std_logic;
    signal   awid           : inout std_logic_vector;
    signal   awaddr         : inout std_logic_vector;
    signal   awlen          : inout std_logic_vector(7 downto 0);
    signal   awsize         : inout std_logic_vector(2 downto 0);
    signal   awburst        : inout std_logic_vector(1 downto 0);
    signal   awlock         : inout std_logic;
    signal   awcache        : inout std_logic_vector(3 downto 0);
    signal   awprot         : inout std_logic_vector(2 downto 0);
    signal   awqos          : inout std_logic_vector(3 downto 0);
    signal   awregion       : inout std_logic_vector(3 downto 0);
    signal   awuser         : inout std_logic_vector;
    signal   awvalid        : inout std_logic;
    signal   awready        : in    std_logic;
    constant scope          : in    string                := C_SCOPE;
    constant msg_id_panel   : in    t_msg_id_panel        := shared_msg_id_panel;
    constant config         : in    t_axi_bfm_config  := C_AXI_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
- write_data_channel_write <font id="function_arguments">(    constant wdata_value  : in    t_slv_array;
    constant wstrb_value  : in    t_slv_array;
    constant wuser_value  : in    t_slv_array;
    constant awlen_value  : in    unsigned(7 downto 0);
    constant msg          : in    string;
    signal   clk          : in    std_logic;
    signal   wdata        : inout std_logic_vector;
    signal   wstrb        : inout std_logic_vector;
    signal   wlast        : inout std_logic;
    signal   wuser        : inout std_logic_vector;
    signal   wvalid       : inout std_logic;
    signal   wready       : in    std_logic;
    constant scope        : in    string                := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel        := shared_msg_id_panel;
    constant config       : in    t_axi_bfm_config  := C_AXI_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
- write_response_channel_receive <font id="function_arguments">(    variable bid_value      : out   std_logic_vector;
    variable bresp_value    : out   t_xresp;
    variable buser_value    : out   std_logic_vector;
    constant msg            : in    string;
    signal   clk            : in    std_logic;
    signal   bid            : in    std_logic_vector;
    signal   bresp          : in    std_logic_vector(1 downto 0);
    signal   buser          : in    std_logic_vector;
    signal   bvalid         : in    std_logic;
    signal   bready         : inout std_logic;
    constant alert_level    : in    t_alert_level         := error;
    constant scope          : in    string                := C_SCOPE;
    constant msg_id_panel   : in    t_msg_id_panel        := shared_msg_id_panel;
    constant config         : in    t_axi_bfm_config      := C_AXI_BFM_CONFIG_DEFAULT;
    constant ext_proc_call  : in    string                := ""   External proc_call. Overwrite if called from another BFM procedure
  )</font> <font id="function_return">return ()</font>
- read_address_channel_write <font id="function_arguments">(    constant arid_value     : in    std_logic_vector;
    constant araddr_value   : in    unsigned;
    constant arlen_value    : in    unsigned(7 downto 0);
    constant arsize_value   : in    integer range 1 to 128;
    constant arburst_value  : in    t_axburst;
    constant arlock_value   : in    t_axlock;
    constant arcache_value  : in    std_logic_vector(3 downto 0);
    constant arprot_value   : in    t_axprot;
    constant arqos_value    : in    std_logic_vector(3 downto 0);
    constant arregion_value : in    std_logic_vector(3 downto 0);
    constant aruser_value   : in    std_logic_vector;
    constant msg            : in    string;
    signal   clk            : in    std_logic;
    signal   arid           : inout std_logic_vector;
    signal   araddr         : inout std_logic_vector;
    signal   arlen          : inout std_logic_vector(7 downto 0);
    signal   arsize         : inout std_logic_vector(2 downto 0);
    signal   arburst        : inout std_logic_vector(1 downto 0);
    signal   arlock         : inout std_logic;
    signal   arcache        : inout std_logic_vector(3 downto 0);
    signal   arprot         : inout std_logic_vector(2 downto 0);
    signal   arqos          : inout std_logic_vector(3 downto 0);
    signal   arregion       : inout std_logic_vector(3 downto 0);
    signal   aruser         : inout std_logic_vector;
    signal   arvalid        : inout std_logic;
    signal   arready        : in    std_logic;
    constant scope          : in    string                := C_SCOPE;
    constant msg_id_panel   : in    t_msg_id_panel        := shared_msg_id_panel;
    constant config         : in    t_axi_bfm_config      := C_AXI_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
- read_data_channel_receive <font id="function_arguments">(    variable read_result      : out   t_vvc_result;
    variable read_data_queue  : inout t_axi_read_data_queue;
    constant msg              : in    string;
    signal   clk              : in    std_logic;
    signal   rid              : in    std_logic_vector;
    signal   rdata            : in    std_logic_vector;
    signal   rresp            : in    std_logic_vector(1 downto 0);
    signal   rlast            : in    std_logic;
    signal   ruser            : in    std_logic_vector;
    signal   rvalid           : in    std_logic;
    signal   rready           : inout std_logic;
    constant scope            : in    string                := C_SCOPE;
    constant msg_id_panel     : in    t_msg_id_panel        := shared_msg_id_panel;
    constant config           : in    t_axi_bfm_config  := C_AXI_BFM_CONFIG_DEFAULT;
    constant ext_proc_call    : in    string                := ""   External proc_call. Overwrite if called from another BFM procedure
  )</font> <font id="function_return">return ()</font>
