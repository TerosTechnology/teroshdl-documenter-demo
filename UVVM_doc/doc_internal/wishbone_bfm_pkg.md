# Package: wishbone_bfm_pkg
## Constants
| Name                          | Type                  | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description                                 |
| ----------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| C_SCOPE                       | string                |  "WISHBONE BFM"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                             |
| C_WISHBONE_BFM_CONFIG_DEFAULT | t_wishbone_bfm_config |  (     max_wait_cycles             => 10,     max_wait_cycles_severity    => failure,     clock_period                => -1 ns,     clock_period_margin         => 0 ns,     clock_margin_severity       => TB_ERROR,     setup_time                  => -1 ns,     hold_time                   => -1 ns,     match_strictness            => MATCH_EXACT,     id_for_bfm                  => ID_BFM,     id_for_bfm_wait             => ID_BFM_WAIT,     id_for_bfm_poll             => ID_BFM_POLL   ) | Define the default value for the BFM config |
## Types
| Name                  | Type | Description                                              |
| --------------------- | ---- | -------------------------------------------------------- |
| t_wishbone_if         |      |                                                          |
| t_wishbone_bfm_config |      | Configuration record to be assigned in the test harness. |
## Functions
- init_wishbone_if_signals <font id="function_arguments">(    addr_width : natural;
    data_width : natural
    )</font> <font id="function_return">return t_wishbone_if</font>
- wishbone_write <font id="function_arguments">(    constant addr_value       : in  unsigned;
    constant data_value       : in  std_logic_vector;
    constant msg              : in  string;
    signal clk                : in  std_logic;
    signal wishbone_if        : inout t_wishbone_if;
    constant scope            : in  string                    := C_SCOPE;
    constant msg_id_panel     : in  t_msg_id_panel            := shared_msg_id_panel;
    constant config           : in  t_wishbone_bfm_config     := C_WISHBONE_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
- wishbone_read <font id="function_arguments">(    constant addr_value       : in  unsigned;
    variable data_value       : out std_logic_vector;
    constant msg              : in  string;
    signal clk                : in  std_logic;
    signal wishbone_if        : inout t_wishbone_if;
    constant scope            : in  string                    := C_SCOPE;
    constant msg_id_panel     : in  t_msg_id_panel            := shared_msg_id_panel;
    constant config           : in  t_wishbone_bfm_config     := C_WISHBONE_BFM_CONFIG_DEFAULT;
    constant ext_proc_call    : in  string                    := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
- wishbone_check <font id="function_arguments">(    constant addr_value       : in  unsigned;
    constant data_exp         : in  std_logic_vector;
    constant msg              : in  string;
    signal clk                : in  std_logic;
    signal wishbone_if        : inout t_wishbone_if;
    constant alert_level      : in  t_alert_level             := error;
    constant scope            : in  string                    := C_SCOPE;
    constant msg_id_panel     : in  t_msg_id_panel            := shared_msg_id_panel;
    constant config           : in  t_wishbone_bfm_config     := C_WISHBONE_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
