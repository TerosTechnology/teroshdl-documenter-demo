# Package: sbi_bfm_pkg
## Constants
| Name                     | Type             | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description |
| ------------------------ | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_SCOPE                  | string           |  "SBI BFM"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| C_SBI_BFM_CONFIG_DEFAULT | t_sbi_bfm_config |  (     max_wait_cycles             => 10,     max_wait_cycles_severity    => failure,     use_fixed_wait_cycles_read  => false,     fixed_wait_cycles_read      => 0,     clock_period                => -1 ns,     clock_period_margin         => 0 ns,     clock_margin_severity       => TB_ERROR,     setup_time                  => -1 ns,     hold_time                   => -1 ns,     bfm_sync                    => SYNC_ON_CLOCK_ONLY,     match_strictness            => MATCH_EXACT,     id_for_bfm                  => ID_BFM,     id_for_bfm_wait             => ID_BFM_WAIT,     id_for_bfm_poll             => ID_BFM_POLL,     use_ready_signal            => true     ) |             |
## Types
| Name             | Type | Description                                              |
| ---------------- | ---- | -------------------------------------------------------- |
| t_sbi_if         |      |                                                          |
| t_sbi_bfm_config |      | Configuration record to be assigned in the test harness. |
## Functions
- init_sbi_if_signals <font id="function_arguments">(    addr_width : natural;
    data_width : natural
    )</font> <font id="function_return">return t_sbi_if</font>
**Description**
- This function returns an SBI interface with initialized signals.- All SBI input signals are initialized to 0- All SBI output signals are initialized to Z
- sbi_write <font id="function_arguments">(    constant addr_value   : in    unsigned;
    constant data_value   : in    std_logic_vector;
    constant msg          : in    string;
    signal clk            : in    std_logic;
    signal cs             : inout std_logic;
    signal addr           : inout unsigned;
    signal rena           : inout std_logic;
    signal wena           : inout std_logic;
    signal ready          : in    std_logic;
    signal wdata          : inout std_logic_vector;
    constant scope        : in    string           := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config       : in    t_sbi_bfm_config := C_SBI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
- This procedure writes data to the SBI DUT- The SBI interface in this procedure is given as individual signals
- sbi_write <font id="function_arguments">(    constant addr_value   : in    unsigned;
    constant data_value   : in    std_logic_vector;
    constant msg          : in    string;
    signal clk            : in    std_logic;
    signal sbi_if         : inout t_sbi_if;
    constant scope        : in    string           := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config       : in    t_sbi_bfm_config := C_SBI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
- This procedure writes data 'data_value' to the SBI DUT address 'addr_value'- The SBI interface in this procedure is given as a t_sbi_if signal record
- sbi_read <font id="function_arguments">(    constant addr_value    : in    unsigned;
    variable data_value    : out   std_logic_vector;
    constant msg           : in    string;
    signal clk             : in    std_logic;
    signal cs              : inout std_logic;
    signal addr            : inout unsigned;
    signal rena            : inout std_logic;
    signal wena            : inout std_logic;
    signal ready           : in    std_logic;
    signal rdata           : in    std_logic_vector;
    constant scope         : in    string           := C_SCOPE;
    constant msg_id_panel  : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config        : in    t_sbi_bfm_config := C_SBI_BFM_CONFIG_DEFAULT;
    constant ext_proc_call : in    string           := ""   External proc_call. Overwrite if called from another BFM procedure

    )</font> <font id="function_return">return ()</font>
**Description**
- This procedure reads data from the SBI DUT address 'addr_value' and  returns the read data in the output 'data_value'- The SBI interface in this procedure is given as individual signals
- sbi_read <font id="function_arguments">(    constant addr_value    : in    unsigned;
    variable data_value    : out   std_logic_vector;
    constant msg           : in    string;
    signal clk             : in    std_logic;
    signal sbi_if          : inout t_sbi_if;
    constant scope         : in    string           := C_SCOPE;
    constant msg_id_panel  : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config        : in    t_sbi_bfm_config := C_SBI_BFM_CONFIG_DEFAULT;
    constant ext_proc_call : in    string           := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
**Description**
- This procedure reads data from the SBI DUT address 'addr_value' and returns  the read data in the output 'data_value'- The SBI interface in this procedure is given as a t_sbi_if signal record
- sbi_check <font id="function_arguments">(    constant addr_value   : in    unsigned;
    constant data_exp     : in    std_logic_vector;
    constant msg          : in    string;
    signal clk            : in    std_logic;
    signal cs             : inout std_logic;
    signal addr           : inout unsigned;
    signal rena           : inout std_logic;
    signal wena           : inout std_logic;
    signal ready          : in    std_logic;
    signal rdata          : in    std_logic_vector;
    constant alert_level  : in    t_alert_level    := error;
    constant scope        : in    string           := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config       : in    t_sbi_bfm_config := C_SBI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
- This procedure reads data from the SBI DUT address 'addr_value' and  compares the read data to the expected data in 'data_exp'.- If the read data is inconsistent with the expected data, an alert with  severity 'alert_level' is triggered.- The SBI interface in this procedure is given as individual signals
- sbi_check <font id="function_arguments">(    constant addr_value   : in    unsigned;
    constant data_exp     : in    std_logic_vector;
    constant msg          : in    string;
    signal clk            : in    std_logic;
    signal sbi_if         : inout t_sbi_if;
    constant alert_level  : in    t_alert_level    := error;
    constant scope        : in    string           := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config       : in    t_sbi_bfm_config := C_SBI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
- This procedure reads data from the SBI DUT address 'addr_value' and  compares the read data to the expected data in 'data_exp'.- If the read data is inconsistent with the expected data, an alert with  severity 'alert_level' is triggered.- The SBI interface in this procedure is given as a t_sbi_if signal record
- sbi_poll_until <font id="function_arguments">(    constant addr_value   : in    unsigned;
    constant data_exp     : in    std_logic_vector;
    constant max_polls    : in    integer          := 1;
    constant timeout      : in    time             := 0 ns;
    constant msg          : in    string;
    signal clk            : in    std_logic;
    signal cs             : inout std_logic;
    signal addr           : inout unsigned;
    signal rena           : inout std_logic;
    signal wena           : inout std_logic;
    signal ready          : in    std_logic;
    signal rdata          : in    std_logic_vector;
    signal terminate_loop : in    std_logic;
    constant alert_level  : in    t_alert_level    := error;
    constant scope        : in    string           := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config       : in    t_sbi_bfm_config := C_SBI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
- This procedure reads data from the SBI DUT address 'addr_value' and  compares the read data to the expected data in 'data_exp'.- If the read data is inconsistent with the expected data, a new read  will be performed, and the new read data will be compared with the  'data_exp'. This process will continue until one of the following  conditions are met:    a) The read data is equal to the expected data    b) The number of reads equal 'max_polls'    c) The time spent polling is equal to the 'timeout'- If 'timeout' is set to 0, it will be interpreted as no timeout- If 'max_polls' is set to 0, it will be interpreted as no limitation on number of polls- The SBI interface in this procedure is given as individual signals
- sbi_poll_until <font id="function_arguments">(    constant addr_value   : in    unsigned;
    constant data_exp     : in    std_logic_vector;
    constant max_polls    : in    integer          := 1;
    constant timeout      : in    time             := 0 ns;
    constant msg          : in    string;
    signal clk            : in    std_logic;
    signal sbi_if         : inout t_sbi_if;
    signal terminate_loop : in    std_logic;
    constant alert_level  : in    t_alert_level    := error;
    constant scope        : in    string           := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config       : in    t_sbi_bfm_config := C_SBI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
- This procedure reads data from the SBI DUT address 'addr_value' and  compares the read data to the expected data in 'data_exp'.- If the read data is inconsistent with the expected data, a new read  will be performed, and the new read data will be compared with the  'data_exp'. This process will continue until one of the following  conditions are met:    a) The read data is equal to the expected data    b) The number of reads equal 'max_polls'    c) The time spent polling is equal to the 'timeout'- If 'timeout' is set to 0, it will be interpreted as no timeout- If 'max_polls' is set to 0, it will be interpreted as no limitation on number of polls- The SBI interface in this procedure is given as a t_sbi_if signal record
