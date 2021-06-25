# Package: axi_bfm_pkg
## Constants
| Name                     | Type                            | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description |
| ------------------------ | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_SCOPE                  | string                          |  "AXI_BFM"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |             |
| C_EMPTY_SLV_ARRAY        | t_slv_array(0 to 0)(0 downto 0) |  (others=>"U")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
| C_EMPTY_XRESP_ARRAY      | t_xresp_array(0 to 0)           |  (others=>ILLEGAL)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |             |
| C_AXI_BFM_CONFIG_DEFAULT | t_axi_bfm_config                |  (     max_wait_cycles             => 1000,     max_wait_cycles_severity    => TB_FAILURE,     clock_period                => -1 ns,     clock_period_margin         => 0 ns,     clock_margin_severity       => TB_ERROR,     setup_time                  => -1 ns,     hold_time                   => -1 ns,     bfm_sync                    => SYNC_ON_CLOCK_ONLY,     match_strictness            => MATCH_EXACT,     num_aw_pipe_stages          => 1,     num_w_pipe_stages           => 1,     num_ar_pipe_stages          => 1,     num_r_pipe_stages           => 1,     num_b_pipe_stages           => 1,     id_for_bfm                  => ID_BFM,     id_for_bfm_wait             => ID_BFM_WAIT,     id_for_bfm_poll             => ID_BFM_POLL     ) |             |
## Types
| Name                         | Type                                                                                                                                                                                                                                                                                 | Description                                              |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| t_xresp                      | (     OKAY,     EXOKAY,     SLVERR,     DECERR,     ILLEGAL   )                                                                                                                                                                                                                      |                                                          |
| t_xresp_array                |                                                                                                                                                                                                                                                                                      |                                                          |
| t_axprot                     | (     UNPRIVILEGED_NONSECURE_DATA,     UNPRIVILEGED_NONSECURE_INSTRUCTION,     UNPRIVILEGED_SECURE_DATA,     UNPRIVILEGED_SECURE_INSTRUCTION,     PRIVILEGED_NONSECURE_DATA,     PRIVILEGED_NONSECURE_INSTRUCTION,     PRIVILEGED_SECURE_DATA,     PRIVILEGED_SECURE_INSTRUCTION   ) |                                                          |
| t_axburst                    | (     FIXED,     INCR,     WRAP   )                                                                                                                                                                                                                                                  |                                                          |
| t_axlock                     | (     NORMAL,     EXCLUSIVE   )                                                                                                                                                                                                                                                      |                                                          |
| t_axi_bfm_config             |                                                                                                                                                                                                                                                                                      | Configuration record to be assigned in the test harness. |
| t_axi_write_address_channel  |                                                                                                                                                                                                                                                                                      | AXI Interface signals                                    |
| t_axi_write_data_channel     |                                                                                                                                                                                                                                                                                      |                                                          |
| t_axi_write_response_channel |                                                                                                                                                                                                                                                                                      |                                                          |
| t_axi_read_address_channel   |                                                                                                                                                                                                                                                                                      |                                                          |
| t_axi_read_data_channel      |                                                                                                                                                                                                                                                                                      |                                                          |
| t_axi_if                     |                                                                                                                                                                                                                                                                                      |                                                          |
## Functions
- init_axi_if_signals <font id="function_arguments">(    addr_width : natural;
    data_width : natural;
    id_width   : natural;
    user_width : natural
    )</font> <font id="function_return">return t_axi_if</font>
**Description**
- This function returns an AXI interface with initialized signals.- All AXI input signals are initialized to 0- All AXI output signals are initialized to Z
- axprot_to_slv <font id="function_arguments">(    axprot : t_axprot
  )</font> <font id="function_return">return std_logic_vector</font>
- xresp_to_slv <font id="function_arguments">(    xresp : t_xresp
  )</font> <font id="function_return">return std_logic_vector</font>
- slv_to_xresp <font id="function_arguments">(    value : std_logic_vector(1 downto 0)
  )</font> <font id="function_return">return t_xresp</font>
- axburst_to_slv <font id="function_arguments">(    axburst : t_axburst
  )</font> <font id="function_return">return std_logic_vector</font>
- bytes_to_axsize <font id="function_arguments">(    constant bytes : positive
  )</font> <font id="function_return">return std_logic_vector</font>
- axlock_to_sl <font id="function_arguments">(    constant axlock : t_axlock
  )</font> <font id="function_return">return std_logic</font>
- axi_write <font id="function_arguments">(    constant awid_value         : in    std_logic_vector              := "";
    constant awaddr_value       : in    unsigned;
    constant awlen_value        : in    unsigned(7 downto 0)          := (others=>'0');
    constant awsize_value       : in    integer range 1 to 128        := 4;
    constant awburst_value      : in    t_axburst                     := INCR;
    constant awlock_value       : in    t_axlock                      := NORMAL;
    constant awcache_value      : in    std_logic_vector(3 downto 0)  := (others=>'0');
    constant awprot_value       : in    t_axprot                      := UNPRIVILEGED_NONSECURE_DATA;
    constant awqos_value        : in    std_logic_vector(3 downto 0)  := (others=>'0');
    constant awregion_value     : in    std_logic_vector(3 downto 0)  := (others=>'0');
    constant awuser_value       : in    std_logic_vector              := "";
    constant wdata_value        : in    t_slv_array;
    constant wstrb_value        : in    t_slv_array                   := C_EMPTY_SLV_ARRAY;
    constant wuser_value        : in    t_slv_array                   := C_EMPTY_SLV_ARRAY;
    variable buser_value        : out   std_logic_vector;
    variable bresp_value        : out   t_xresp;
    constant msg                : in    string;
    signal   clk                : in    std_logic;
    signal   axi_if             : inout t_axi_if;
    constant scope              : in    string                        := C_SCOPE;
    constant msg_id_panel       : in    t_msg_id_panel                := shared_msg_id_panel;
    constant config             : in    t_axi_bfm_config              := C_AXI_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
This procedure writes data to the AXI interface specified in axi_if- When the write is completed, a log message is issued with log ID id_for_bfm
- axi_read <font id="function_arguments">(    constant arid_value     : in    std_logic_vector              := "";
    constant araddr_value   : in    unsigned;
    constant arlen_value    : in    unsigned(7 downto 0)          := (others=>'0');
    constant arsize_value   : in    integer range 1 to 128        := 4;
    constant arburst_value  : in    t_axburst                     := INCR;
    constant arlock_value   : in    t_axlock                      := NORMAL;
    constant arcache_value  : in    std_logic_vector(3 downto 0)  := (others=>'0');
    constant arprot_value   : in    t_axprot                      := UNPRIVILEGED_NONSECURE_DATA;
    constant arqos_value    : in    std_logic_vector(3 downto 0)  := (others=>'0');
    constant arregion_value : in    std_logic_vector(3 downto 0)  := (others=>'0');
    constant aruser_value   : in    std_logic_vector              := "";
    variable rdata_value    : out   t_slv_array;
    variable rresp_value    : out   t_xresp_array;
    variable ruser_value    : out   t_slv_array;
    constant msg            : in    string;
    signal   clk            : in    std_logic;
    signal   axi_if         : inout t_axi_if;
    constant scope          : in    string                        := C_SCOPE;
    constant msg_id_panel   : in    t_msg_id_panel                := shared_msg_id_panel;
    constant config         : in    t_axi_bfm_config              := C_AXI_BFM_CONFIG_DEFAULT;
    constant ext_proc_call  : in    string                        := ""   External proc_call. Overwrite if called from another BFM procedure
  )</font> <font id="function_return">return ()</font>
**Description**
This procedure reads data from the AXI interface specified in axi_if,and returns the read data in rdata_value.
- axi_check <font id="function_arguments">(    constant arid_value     : in    std_logic_vector              := "";
    constant araddr_value   : in    unsigned;
    constant arlen_value    : in    unsigned(7 downto 0)          := (others=>'0');
    constant arsize_value   : in    integer range 1 to 128        := 4;
    constant arburst_value  : in    t_axburst                     := INCR;
    constant arlock_value   : in    t_axlock                      := NORMAL;
    constant arcache_value  : in    std_logic_vector(3 downto 0)  := (others=>'0');
    constant arprot_value   : in    t_axprot                      := UNPRIVILEGED_NONSECURE_DATA;
    constant arqos_value    : in    std_logic_vector(3 downto 0)  := (others=>'0');
    constant arregion_value : in    std_logic_vector(3 downto 0)  := (others=>'0');
    constant aruser_value   : in    std_logic_vector              := "";
    constant rdata_exp      : in    t_slv_array;
    constant rresp_exp      : in    t_xresp_array                 := C_EMPTY_XRESP_ARRAY;
    constant ruser_exp      : in    t_slv_array                   := C_EMPTY_SLV_ARRAY;
    constant msg            : in    string;
    signal   clk            : in    std_logic;
    signal   axi_if         : inout t_axi_if;
    constant alert_level    : in    t_alert_level                 := error;
    constant scope          : in    string                        := C_SCOPE;
    constant msg_id_panel   : in    t_msg_id_panel                := shared_msg_id_panel;
    constant config         : in    t_axi_bfm_config              := C_AXI_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
This procedure reads data from the AXI interface specified in axi_if,and compares it to the data in data_exp.- If the received data inconsistent with data_exp, an alert with severity  alert_level is issued.- If the received data was correct, a log message with ID id_for_bfm is issued.
