# Package: i2c_bfm_pkg
## Constants
| Name                     | Type             | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description |
| ------------------------ | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_SCOPE                  | string           |  "I2C BFM"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| C_READ_BIT               | std_logic        |  '1'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
| C_WRITE_BIT              | std_logic        |  '0'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
| C_I2C_BFM_CONFIG_DEFAULT | t_i2c_bfm_config |  (     enable_10_bits_addressing       => false,     master_sda_to_scl               => 20 ns,     master_scl_to_sda               => 20 ns,     master_stop_condition_hold_time => 20 ns,     max_wait_scl_change             => 10 ms,     max_wait_scl_change_severity    => failure,     max_wait_sda_change             => 10 ms,     max_wait_sda_change_severity    => failure,     i2c_bit_time                    => -1 ns,     i2c_bit_time_severity           => failure,     acknowledge_severity            => failure,     slave_mode_address              => "0000000000",     slave_mode_address_severity     => failure,     slave_rw_bit_severity           => failure,     reserved_address_severity       => warning,     match_strictness                => MATCH_EXACT,     id_for_bfm                      => ID_BFM,     id_for_bfm_wait                 => ID_BFM_WAIT,     id_for_bfm_poll                 => ID_BFM_POLL     ) |             |
## Types
| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| t_i2c_if         |      |             |
| t_i2c_bfm_config |      |             |
## Functions
- init_i2c_if_signals <font id="function_arguments">(    constant VOID : in t_void
    )</font> <font id="function_return">return t_i2c_if</font>
- i2c_master_transmit <font id="function_arguments">(    constant addr_value                   : in    unsigned;
    constant data                         : in    t_byte_array;
    constant msg                          : in    string;
    signal scl                            : inout std_logic;
    signal sda                            : inout std_logic;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_i2c_bfm_config               := C_I2C_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
- i2c_master_transmit <font id="function_arguments">(    constant addr_value                   : in    unsigned;
    constant data                         : in    t_byte_array;
    constant msg                          : in    string;
    signal i2c_if                         : inout t_i2c_if;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_i2c_bfm_config               := C_I2C_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
- i2c_master_transmit <font id="function_arguments">(    constant addr_value                   : in    unsigned;
    constant data                         : in    std_logic_vector;
    constant msg                          : in    string;
    signal i2c_if                         : inout t_i2c_if;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_i2c_bfm_config               := C_I2C_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
- i2c_slave_transmit <font id="function_arguments">(    constant data         : in    t_byte_array;
    constant msg          : in    string;
    signal scl            : inout std_logic;
    signal sda            : inout std_logic;
    constant scope        : in    string           := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config       : in    t_i2c_bfm_config := C_I2C_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
- i2c_slave_transmit <font id="function_arguments">(    constant data         : in    t_byte_array;
    constant msg          : in    string;
    signal i2c_if         : inout t_i2c_if;
    constant scope        : in    string           := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config       : in    t_i2c_bfm_config := C_I2C_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
- i2c_slave_transmit <font id="function_arguments">(    constant data         : in    std_logic_vector;
    constant msg          : in    string;
    signal i2c_if         : inout t_i2c_if;
    constant scope        : in    string           := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config       : in    t_i2c_bfm_config := C_I2C_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
- i2c_master_receive <font id="function_arguments">(    constant addr_value                   : in    unsigned;
    variable data                         : out   t_byte_array;
    constant msg                          : in    string;
    signal scl                            : inout std_logic;
    signal sda                            : inout std_logic;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_i2c_bfm_config               := C_I2C_BFM_CONFIG_DEFAULT;
    constant ext_proc_call                : in    string                         := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
- i2c_master_receive <font id="function_arguments">(    constant addr_value                   : in    unsigned;
    variable data                         : out   t_byte_array;
    constant msg                          : in    string;
    signal i2c_if                         : inout t_i2c_if;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_i2c_bfm_config               := C_I2C_BFM_CONFIG_DEFAULT;
    constant ext_proc_call                : in    string                         := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
- i2c_master_receive <font id="function_arguments">(    constant addr_value                   : in    unsigned;
    variable data                         : out   std_logic_vector;
    constant msg                          : in    string;
    signal i2c_if                         : inout t_i2c_if;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_i2c_bfm_config               := C_I2C_BFM_CONFIG_DEFAULT;
    constant ext_proc_call                : in    string                         := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
- i2c_slave_receive <font id="function_arguments">(    variable data          : out   t_byte_array;
    constant msg           : in    string;
    signal scl             : inout std_logic;
    signal sda             : inout std_logic;
    constant exp_rw_bit    : in    std_logic        := C_WRITE_BIT;
    constant scope         : in    string           := C_SCOPE;
    constant msg_id_panel  : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config        : in    t_i2c_bfm_config := C_I2C_BFM_CONFIG_DEFAULT;
    constant ext_proc_call : in    string           := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
- i2c_slave_receive <font id="function_arguments">(    variable data          : out   t_byte_array;
    constant msg           : in    string;
    signal i2c_if          : inout t_i2c_if;
    constant scope         : in    string           := C_SCOPE;
    constant msg_id_panel  : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config        : in    t_i2c_bfm_config := C_I2C_BFM_CONFIG_DEFAULT;
    constant ext_proc_call : in    string           := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
- i2c_slave_receive <font id="function_arguments">(    variable data          : out   std_logic_vector;
    constant msg           : in    string;
    signal i2c_if          : inout t_i2c_if;
    constant scope         : in    string           := C_SCOPE;
    constant msg_id_panel  : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config        : in    t_i2c_bfm_config := C_I2C_BFM_CONFIG_DEFAULT;
    constant ext_proc_call : in    string           := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
- i2c_master_check <font id="function_arguments">(    constant addr_value                   : in    unsigned;
    constant data_exp                     : in    t_byte_array;
    constant msg                          : in    string;
    signal scl                            : inout std_logic;
    signal sda                            : inout std_logic;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant alert_level                  : in    t_alert_level                  := error;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_i2c_bfm_config               := C_I2C_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
- i2c_master_check <font id="function_arguments">(    constant addr_value                   : in    unsigned;
    constant data_exp                     : in    t_byte_array;
    constant msg                          : in    string;
    signal i2c_if                         : inout t_i2c_if;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant alert_level                  : in    t_alert_level                  := error;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_i2c_bfm_config               := C_I2C_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
- i2c_master_check <font id="function_arguments">(    constant addr_value                   : in    unsigned;
    constant data_exp                     : in    std_logic_vector;
    constant msg                          : in    string;
    signal i2c_if                         : inout t_i2c_if;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant alert_level                  : in    t_alert_level                  := error;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_i2c_bfm_config               := C_I2C_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
- i2c_slave_check <font id="function_arguments">(    constant data_exp     : in    t_byte_array;
    constant msg          : in    string;
    signal scl            : inout std_logic;
    signal sda            : inout std_logic;
    constant exp_rw_bit   : in    std_logic        := C_WRITE_BIT;
    constant alert_level  : in    t_alert_level    := error;
    constant scope        : in    string           := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config       : in    t_i2c_bfm_config := C_I2C_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
- i2c_slave_check <font id="function_arguments">(    constant data_exp     : in    t_byte_array;
    constant msg          : in    string;
    signal i2c_if         : inout t_i2c_if;
    constant exp_rw_bit   : in    std_logic        := C_WRITE_BIT;
    constant alert_level  : in    t_alert_level    := error;
    constant scope        : in    string           := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config       : in    t_i2c_bfm_config := C_I2C_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
- i2c_slave_check <font id="function_arguments">(    constant data_exp     : in    std_logic_vector;
    constant msg          : in    string;
    signal i2c_if         : inout t_i2c_if;
    constant exp_rw_bit   : in    std_logic        := C_WRITE_BIT;
    constant alert_level  : in    t_alert_level    := error;
    constant scope        : in    string           := C_SCOPE;
    constant msg_id_panel : in    t_msg_id_panel   := shared_msg_id_panel;
    constant config       : in    t_i2c_bfm_config := C_I2C_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
- i2c_master_quick_command <font id="function_arguments">(    constant addr_value                   : in    unsigned;
    constant msg                          : in    string;
    signal i2c_if                         : inout t_i2c_if;
    constant rw_bit                       : in    std_logic                      := C_WRITE_BIT;
    constant exp_ack                      : in    boolean                        := true;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant alert_level                  : in    t_alert_level                  := error;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_i2c_bfm_config               := C_I2C_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
