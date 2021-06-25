# Package: spi_bfm_pkg
## Constants
| Name                     | Type             | Value                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_SCOPE                  | string           |  "SPI BFM"                                                                                                                                                                                                                                                                                                                                                                                        |             |
| C_SPI_BFM_CONFIG_DEFAULT | t_spi_bfm_config |  (     CPOL             => '0',     CPHA             => '0',     spi_bit_time     => -1 ns,  -- Make sure we notice if we forget to set bit time.     ss_n_to_sclk     => 20 ns,     sclk_to_ss_n     => 20 ns,     inter_word_delay => 0 ns,     match_strictness => MATCH_EXACT,     id_for_bfm       => ID_BFM,     id_for_bfm_wait  => ID_BFM_WAIT,     id_for_bfm_poll  => ID_BFM_POLL     ) |             |
## Types
| Name             | Type | Description                                              |
| ---------------- | ---- | -------------------------------------------------------- |
| t_spi_if         |      |                                                          |
| t_spi_bfm_config |      | Configuration record to be assigned in the test harness. |
## Functions
- init_spi_if_signals <font id="function_arguments">(    constant config      : in t_spi_bfm_config;
    constant master_mode : in boolean := true
    )</font> <font id="function_return">return t_spi_if</font>
**Description**
- This function returns an SPI interface with initialized signals.- master_mode = true:   - ss_n initialized to 'H'   - if config.CPOL = '1', sclk initialized to 'H',     otherwise sclk initialized to 'L'   - miso and mosi initialized to 'Z'- master_mode = false:   - all signals initialized to 'Z'
- spi_master_transmit_and_receive <font id="function_arguments">(    constant tx_data                      : in    std_logic_vector;
    variable rx_data                      : out   std_logic_vector;
    constant msg                          : in    string;
    signal sclk                           : inout std_logic;
    signal ss_n                           : inout std_logic;
    signal mosi                           : inout std_logic;
    signal miso                           : inout std_logic;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT;
    constant ext_proc_call                : in    string                         := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure transmits data 'tx_data' to the SPI slave DUTand receives 'rx_data' from the SPI slave DUT.
- spi_master_transmit_and_receive <font id="function_arguments">(    constant tx_data                      : in    std_logic_vector;
    variable rx_data                      : out   std_logic_vector;
    constant msg                          : in    string;
    signal spi_if                         : inout t_spi_if;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT;
    constant ext_proc_call                : in    string                         := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure transmits data 'tx_data' to the SPI slave DUTand receives 'rx_data' from the SPI slave DUT.The SPI interface in this procedure is given as a t_spi_if signal record
- spi_master_transmit_and_receive <font id="function_arguments">(    constant tx_data                      : in    t_slv_array;
    variable rx_data                      : out   t_slv_array;
    constant msg                          : in    string;
    signal spi_if                         : inout t_spi_if;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant action_between_words         : in    t_action_between_words         := HOLD_LINE_BETWEEN_WORDS;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT;
    constant ext_proc_call                : in    string                         := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
**Description**
Multi-word
- spi_master_transmit_and_check <font id="function_arguments">(    constant tx_data                      : in    std_logic_vector;
    constant data_exp                     : in    std_logic_vector;
    constant msg                          : in    string;
    signal spi_if                         : inout t_spi_if;
    constant alert_level                  : in    t_alert_level                  := error;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure ...The SPI interface in this procedure is given as a t_spi_if signal record
- spi_master_transmit_and_check <font id="function_arguments">(    constant tx_data                      : in    t_slv_array;
    constant data_exp                     : in    t_slv_array;
    constant msg                          : in    string;
    signal spi_if                         : inout t_spi_if;
    constant alert_level                  : in    t_alert_level                  := error;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant action_between_words         : in    t_action_between_words         := HOLD_LINE_BETWEEN_WORDS;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
Multi-word
- spi_master_transmit <font id="function_arguments">(    constant tx_data                      : in    std_logic_vector;
    constant msg                          : in    string;
    signal spi_if                         : inout t_spi_if;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure transmits data 'tx_data' to the SPI DUTThe SPI interface in this procedure is given as a t_spi_if signal record
- spi_master_transmit <font id="function_arguments">(    constant tx_data                      : in    t_slv_array;
    constant msg                          : in    string;
    signal spi_if                         : inout t_spi_if;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant action_between_words         : in    t_action_between_words         := HOLD_LINE_BETWEEN_WORDS;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
Multi-word
- spi_master_receive <font id="function_arguments">(    variable rx_data                      : out   std_logic_vector;
    constant msg                          : in    string;
    signal spi_if                         : inout t_spi_if;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure receives data 'rx_data' from the SPI DUTThe SPI interface in this procedure is given as a t_spi_if signal record
- spi_master_receive <font id="function_arguments">(    variable rx_data                      : out   t_slv_array;
    constant msg                          : in    string;
    signal spi_if                         : inout t_spi_if;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant action_between_words         : in    t_action_between_words         := HOLD_LINE_BETWEEN_WORDS;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
Multi-word
- spi_master_check <font id="function_arguments">(    constant data_exp                     : in    std_logic_vector;
    constant msg                          : in    string;
    signal spi_if                         : inout t_spi_if;
    constant alert_level                  : in    t_alert_level                  := error;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure receives an SPI transaction, and compares the read datato the expected data in 'data_exp'.If the read data is inconsistent with the expected data, an alert withseverity 'alert_level' is triggered.The SPI interface in this procedure is given as a t_spi_if signal record
- spi_master_check <font id="function_arguments">(    constant data_exp                     : in    t_slv_array;
    constant msg                          : in    string;
    signal spi_if                         : inout t_spi_if;
    constant alert_level                  : in    t_alert_level                  := error;
    constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;
    constant action_between_words         : in    t_action_between_words         := HOLD_LINE_BETWEEN_WORDS;
    constant scope                        : in    string                         := C_SCOPE;
    constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;
    constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
Multi-word
- spi_slave_transmit_and_receive <font id="function_arguments">(    constant tx_data                : in    std_logic_vector;
    variable rx_data                : out   std_logic_vector;
    constant msg                    : in    string;
    signal sclk                     : inout std_logic;
    signal ss_n                     : inout std_logic;
    signal mosi                     : inout std_logic;
    signal miso                     : inout std_logic;
    constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;
    constant scope                  : in    string                   := C_SCOPE;
    constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;
    constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT;
    constant ext_proc_call          : in    string                   := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure transmits data 'tx_data' to the SPI master DUTand receives 'rx_data' from the SPI master DUT.
- spi_slave_transmit_and_receive <font id="function_arguments">(    constant tx_data                : in    std_logic_vector;
    variable rx_data                : out   std_logic_vector;
    constant msg                    : in    string;
    signal spi_if                   : inout t_spi_if;
    constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;
    constant scope                  : in    string                   := C_SCOPE;
    constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;
    constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT;
    constant ext_proc_call          : in    string                   := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure transmits data 'tx_data' to the SPI master DUTand receives 'rx_data' from the SPI master DUT.The SPI interface in this procedure is given as a t_spi_if signal record
- spi_slave_transmit_and_receive <font id="function_arguments">(    constant tx_data                : in    t_slv_array;
    variable rx_data                : out   t_slv_array;
    constant msg                    : in    string;
    signal spi_if                   : inout t_spi_if;
    constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;
    constant scope                  : in    string                   := C_SCOPE;
    constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;
    constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT;
    constant ext_proc_call          : in    string                   := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
**Description**
Multi-word
- spi_slave_transmit_and_check <font id="function_arguments">(    constant tx_data                : in    std_logic_vector;
    constant data_exp               : in    std_logic_vector;
    constant msg                    : in    string;
    signal spi_if                   : inout t_spi_if;
    constant alert_level            : in    t_alert_level            := error;
    constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;
    constant scope                  : in    string                   := C_SCOPE;
    constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;
    constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure ...The SPI interface in this procedure is given as a t_spi_if signal record
- spi_slave_transmit_and_check <font id="function_arguments">(    constant tx_data                : in    t_slv_array;
    constant data_exp               : in    t_slv_array;
    constant msg                    : in    string;
    signal spi_if                   : inout t_spi_if;
    constant alert_level            : in    t_alert_level            := error;
    constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;
    constant scope                  : in    string                   := C_SCOPE;
    constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;
    constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
Multi-word
- spi_slave_transmit <font id="function_arguments">(    constant tx_data                : in    std_logic_vector;
    constant msg                    : in    string;
    signal spi_if                   : inout t_spi_if;
    constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;
    constant scope                  : in    string                   := C_SCOPE;
    constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;
    constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure transmits data 'tx_data' to the SPI DUTThe SPI interface in this procedure is given as a t_spi_if signal record
- spi_slave_transmit <font id="function_arguments">(    constant tx_data                : in    t_slv_array;
    constant msg                    : in    string;
    signal spi_if                   : inout t_spi_if;
    constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;
    constant scope                  : in    string                   := C_SCOPE;
    constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;
    constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
Multi-word
- spi_slave_receive <font id="function_arguments">(    variable rx_data                : out   std_logic_vector;
    constant msg                    : in    string;
    signal spi_if                   : inout t_spi_if;
    constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;
    constant scope                  : in    string                   := C_SCOPE;
    constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;
    constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure receives data 'rx_data' from the SPI DUTThe SPI interface in this procedure is given as a t_spi_if signal record
- spi_slave_receive <font id="function_arguments">(    variable rx_data                : out   t_slv_array;
    constant msg                    : in    string;
    signal spi_if                   : inout t_spi_if;
    constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;
    constant scope                  : in    string                   := C_SCOPE;
    constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;
    constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
Multi-word
- spi_slave_check <font id="function_arguments">(    constant data_exp               : in    std_logic_vector;
    constant msg                    : in    string;
    signal spi_if                   : inout t_spi_if;
    constant alert_level            : in    t_alert_level            := error;
    constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;
    constant scope                  : in    string                   := C_SCOPE;
    constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;
    constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure receives an SPI transaction, and compares the read datato the expected data in 'data_exp'.If the read data is inconsistent with the expected data, an alert withseverity 'alert_level' is triggered.The SPI interface in this procedure is given as a t_spi_if signal record
- spi_slave_check <font id="function_arguments">(    constant data_exp               : in    t_slv_array;
    constant msg                    : in    string;
    signal spi_if                   : inout t_spi_if;
    constant alert_level            : in    t_alert_level            := error;
    constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;
    constant scope                  : in    string                   := C_SCOPE;
    constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;
    constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
Multi-word
