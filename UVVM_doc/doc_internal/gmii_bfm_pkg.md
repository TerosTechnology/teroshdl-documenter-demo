# Package: gmii_bfm_pkg
## Constants
| Name                      | Type              | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description                                 |
| ------------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| C_SCOPE                   | string            |  "GMII BFM"                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                             |
| C_GMII_BFM_CONFIG_DEFAULT | t_gmii_bfm_config |  (     max_wait_cycles          => 12, -- Standard minimum interpacket gap (Gigabith Ethernet)     max_wait_cycles_severity => ERROR,     clock_period             => -1 ns,     clock_period_margin      => 0 ns,     clock_margin_severity    => TB_ERROR,     setup_time               => -1 ns,     hold_time                => -1 ns,     bfm_sync                 => SYNC_ON_CLOCK_ONLY,     match_strictness         => MATCH_EXACT,     id_for_bfm               => ID_BFM   ) | Define the default value for the BFM config |
## Types
| Name              | Type | Description                                              |
| ----------------- | ---- | -------------------------------------------------------- |
| t_gmii_tx_if      |      | Interface record for BFM signals to DUT                  |
| t_gmii_rx_if      |      | Interface record for BFM signals from DUT                |
| t_gmii_bfm_config |      | Configuration record to be assigned in the test harness. |
## Functions
- init_gmii_if_signals <font id="function_arguments">()</font> <font id="function_return">return t_gmii_tx_if</font>
**Description**
This function returns a GMII interface with initialized signals.All input signals are initialized to 0All output signals are initialized to Z
- init_gmii_if_signals <font id="function_arguments">()</font> <font id="function_return">return t_gmii_rx_if</font>
- gmii_write <font id="function_arguments">(    constant data_array   : in    t_slv_array;
    constant msg          : in    string            := "";
    signal   gmii_tx_if   : inout t_gmii_tx_if;
    constant scope        : in    string            := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel    := shared_msg_id_panel;
    constant config       : in    t_gmii_bfm_config := C_GMII_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
- gmii_read <font id="function_arguments">(    variable data_array    : out   t_slv_array;
    variable data_len      : out   natural;
    constant msg           : in    string            := "";
    signal   gmii_rx_if    : inout t_gmii_rx_if;
    constant scope         : in    string            := C_SCOPE;
    constant msg_id_panel  : in    t_msg_id_panel    := shared_msg_id_panel;
    constant config        : in    t_gmii_bfm_config := C_GMII_BFM_CONFIG_DEFAULT;
    constant ext_proc_call : in    string := ""   External proc_call. Overwrite if called from another BFM procedure
  )</font> <font id="function_return">return ()</font>
- gmii_expect <font id="function_arguments">(    constant data_exp     : in    t_slv_array;
    constant msg          : in    string            := "";
    signal   gmii_rx_if   : inout t_gmii_rx_if;
    constant alert_level  : in    t_alert_level     := ERROR;
    constant scope        : in    string            := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel    := shared_msg_id_panel;
    constant config       : in    t_gmii_bfm_config := C_GMII_BFM_CONFIG_DEFAULT
  )</font> <font id="function_return">return ()</font>
