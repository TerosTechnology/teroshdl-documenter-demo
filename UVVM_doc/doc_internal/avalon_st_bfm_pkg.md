# Package: avalon_st_bfm_pkg
## Constants
| Name                           | Type                   | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                   |
| ------------------------------ | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| C_SCOPE                        | string                 |  "AVALON_ST BFM"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                               |
| C_MAX_BITS_PER_SYMBOL          | positive               |  512                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Recommended maximum in protocol specification (MNL-AVABUSREF) |
| C_MAX_SYMBOLS_PER_BEAT         | positive               |  32                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Recommended maximum in protocol specification (MNL-AVABUSREF) |
| C_AVALON_ST_BFM_CONFIG_DEFAULT | t_avalon_st_bfm_config |  (     max_wait_cycles             => 100,     max_wait_cycles_severity    => ERROR,     clock_period                => -1 ns,     clock_period_margin         => 0 ns,     clock_margin_severity       => TB_ERROR,     setup_time                  => -1 ns,     hold_time                   => -1 ns,     bfm_sync                    => SYNC_ON_CLOCK_ONLY,     match_strictness            => MATCH_EXACT,     symbol_width                => 8,     first_symbol_in_msb         => true,     max_channel                 => 0,     use_packet_transfer         => true,     id_for_bfm                  => ID_BFM   ) | Define the default value for the BFM config                   |
## Types
| Name                   | Type | Description                                              |
| ---------------------- | ---- | -------------------------------------------------------- |
| t_avalon_st_if         |      | Interface record for BFM signals                         |
| t_avalon_st_bfm_config |      | Configuration record to be assigned in the test harness. |
## Functions
- init_avalon_st_if_signals <font id="function_arguments">(    is_master        : boolean;  When true, this BFM drives data signals
    channel_width    : natural;
    data_width       : natural;
    data_error_width : natural;
    empty_width      : natural
  )</font> <font id="function_return">return t_avalon_st_if</font>
**Description**
This function returns an Avalon-ST interface with initialized signals.All input signals are initialized to 0All output signals are initialized to Z
- avalon_st_transmit <font id="function_arguments">(    constant channel_value    : in    std_logic_vector;
    constant data_array       : in    t_slv_array;
    constant msg              : in    string                 := "";
    signal   clk              : in    std_logic;
    signal   avalon_st_if     : inout t_avalon_st_if;
    constant scope            : in    string                 := C_SCOPE;
    constant msg_id_panel     : in    t_msg_id_panel         := shared_msg_id_panel;
    constant config           : in    t_avalon_st_bfm_config := C_AVALON_ST_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
- avalon_st_transmit <font id="function_arguments">(    constant data_array       : in    t_slv_array;
    constant msg              : in    string                 := "";
    signal   clk              : in    std_logic;
    signal   avalon_st_if     : inout t_avalon_st_if;
    constant scope            : in    string                 := C_SCOPE;
    constant msg_id_panel     : in    t_msg_id_panel         := shared_msg_id_panel;
    constant config           : in    t_avalon_st_bfm_config := C_AVALON_ST_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
- avalon_st_receive <font id="function_arguments">(    variable channel_value    : out   std_logic_vector;
    variable data_array       : out   t_slv_array;
    constant msg              : in    string                 := "";
    signal   clk              : in    std_logic;
    signal   avalon_st_if     : inout t_avalon_st_if;
    constant scope            : in    string                 := C_SCOPE;
    constant msg_id_panel     : in    t_msg_id_panel         := shared_msg_id_panel;
    constant config           : in    t_avalon_st_bfm_config := C_AVALON_ST_BFM_CONFIG_DEFAULT;
    constant ext_proc_call    : in    string := ""   External proc_call. Overwrite if called from another BFM procedure
  )</font> <font id="function_return">return ()</font>
- avalon_st_receive <font id="function_arguments">(    variable data_array       : out   t_slv_array;
    constant msg              : in    string                 := "";
    signal   clk              : in    std_logic;
    signal   avalon_st_if     : inout t_avalon_st_if;
    constant scope            : in    string                 := C_SCOPE;
    constant msg_id_panel     : in    t_msg_id_panel         := shared_msg_id_panel;
    constant config           : in    t_avalon_st_bfm_config := C_AVALON_ST_BFM_CONFIG_DEFAULT;
    constant ext_proc_call    : in    string := ""   External proc_call. Overwrite if called from another BFM procedure
  )</font> <font id="function_return">return ()</font>
- avalon_st_expect <font id="function_arguments">(    constant channel_exp      : in    std_logic_vector;
    constant data_exp         : in    t_slv_array;
    constant msg              : in    string                 := "";
    signal   clk              : in    std_logic;
    signal   avalon_st_if     : inout t_avalon_st_if;
    constant alert_level      : in    t_alert_level          := error;
    constant scope            : in    string                 := C_SCOPE;
    constant msg_id_panel     : in    t_msg_id_panel         := shared_msg_id_panel;
    constant config           : in    t_avalon_st_bfm_config := C_AVALON_ST_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
- avalon_st_expect <font id="function_arguments">(    constant data_exp         : in    t_slv_array;
    constant msg              : in    string                 := "";
    signal   clk              : in    std_logic;
    signal   avalon_st_if     : inout t_avalon_st_if;
    constant alert_level      : in    t_alert_level          := error;
    constant scope            : in    string                 := C_SCOPE;
    constant msg_id_panel     : in    t_msg_id_panel         := shared_msg_id_panel;
    constant config           : in    t_avalon_st_bfm_config := C_AVALON_ST_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
