# Package: rgmii_bfm_pkg
## Constants
| Name                       | Type               | Value                                                                                                                                                                                                                                               | Description |
| -------------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_SCOPE                    | string             |  "RGMII BFM"                                                                                                                                                                                                                                        |             |
| C_RGMII_BFM_CONFIG_DEFAULT | t_rgmii_bfm_config |  (     max_wait_cycles          => 10,     max_wait_cycles_severity => ERROR,     clock_period             => -1 ns,     rx_clock_skew            => -1 ns,     match_strictness         => MATCH_EXACT,     id_for_bfm               => ID_BFM   ) |             |
## Types
| Name               | Type | Description |
| ------------------ | ---- | ----------- |
| t_rgmii_tx_if      |      |             |
| t_rgmii_rx_if      |      |             |
| t_rgmii_bfm_config |      |             |
## Functions
- init_rgmii_if_signals <font id="function_arguments">()</font> <font id="function_return">return t_rgmii_tx_if</font>
- init_rgmii_if_signals <font id="function_arguments">()</font> <font id="function_return">return t_rgmii_rx_if</font>
- rgmii_write <font id="function_arguments">(    constant data_array   : in    t_byte_array;
    constant msg          : in    string             := "";
    signal   rgmii_tx_if  : inout t_rgmii_tx_if;
    constant scope        : in    string             := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel     := shared_msg_id_panel;
    constant config       : in    t_rgmii_bfm_config := C_RGMII_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
- rgmii_read <font id="function_arguments">(    variable data_array    : out   t_byte_array;
    variable data_len      : out   natural;
    constant msg           : in    string             := "";
    signal   rgmii_rx_if   : inout t_rgmii_rx_if;
    constant scope         : in    string             := C_SCOPE;
    constant msg_id_panel  : in    t_msg_id_panel     := shared_msg_id_panel;
    constant config        : in    t_rgmii_bfm_config := C_RGMII_BFM_CONFIG_DEFAULT;
    constant ext_proc_call : in    string := ""   External proc_call. Overwrite if called from another BFM procedure
  )</font> <font id="function_return">return ()</font>
- rgmii_expect <font id="function_arguments">(    constant data_exp     : in    t_byte_array;
    constant msg          : in    string             := "";
    signal   rgmii_rx_if  : inout t_rgmii_rx_if;
    constant alert_level  : in    t_alert_level      := ERROR;
    constant scope        : in    string             := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel     := shared_msg_id_panel;
    constant config       : in    t_rgmii_bfm_config := C_RGMII_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
