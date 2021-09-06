# Package: spi_bfm_pkg

- **File**: spi_bfm_pkg.vhd
## Description

=================================================================================================

## Constants

| Name                     | Type             | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description |
| ------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_SCOPE                  | string           |  "SPI BFM"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |             |
| C_SPI_BFM_CONFIG_DEFAULT | t_spi_bfm_config |  (     CPOL             => '0',<br><span style="padding-left:20px">     CPHA             => '0',<br><span style="padding-left:20px">     spi_bit_time     => -1 ns,<br><span style="padding-left:20px">  -- Make sure we notice if we forget to set bit time.     ss_n_to_sclk     => 20 ns,<br><span style="padding-left:20px">     sclk_to_ss_n     => 20 ns,<br><span style="padding-left:20px">     inter_word_delay => 0 ns,<br><span style="padding-left:20px">     match_strictness => MATCH_EXACT,<br><span style="padding-left:20px">     id_for_bfm       => ID_BFM,<br><span style="padding-left:20px">     id_for_bfm_wait  => ID_BFM_WAIT,<br><span style="padding-left:20px">     id_for_bfm_poll  => ID_BFM_POLL     ) |             |
## Types

| Name             | Type | Description                                                |
| ---------------- | ---- | ---------------------------------------------------------- |
| t_spi_if         |      |                                                            |
| t_spi_bfm_config |      |  Configuration record to be assigned in the test harness.  |
## Functions
- init_spi_if_signals <font id="function_arguments">( constant config      : in t_spi_bfm_config;<br><span style="padding-left:20px"> constant master_mode : in boolean := true ) </font> <font id="function_return">return t_spi_if </font>
</br>**Description**
===============================================================================================
 BFM procedures
===============================================================================================
----------------------------------------
 init_spi_if_signals
----------------------------------------
 - This function returns an SPI interface with initialized signals.
 - master_mode = true:
    - ss_n initialized to 'H'
    - if config.CPOL = '1', sclk initialized to 'H',
      otherwise sclk initialized to 'L'
    - miso and mosi initialized to 'Z'
 - master_mode = false:
    - all signals initialized to 'Z'

- spi_master_transmit_and_receive <font id="function_arguments">( constant tx_data                      : in    std_logic_vector;<br><span style="padding-left:20px"> variable rx_data                      : out   std_logic_vector;<br><span style="padding-left:20px"> constant msg                          : in    string;<br><span style="padding-left:20px"> signal sclk                           : inout std_logic;<br><span style="padding-left:20px"> signal ss_n                           : inout std_logic;<br><span style="padding-left:20px"> signal mosi                           : inout std_logic;<br><span style="padding-left:20px"> signal miso                           : inout std_logic;<br><span style="padding-left:20px"> constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;<br><span style="padding-left:20px"> constant scope                        : in    string                         := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT;<br><span style="padding-left:20px"> constant ext_proc_call                : in    string                         := ""  -- External proc_call. Overwrite if called from another BFM procedure ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 spi_master_transmit_and_receive
----------------------------------------
 This procedure transmits data 'tx_data' to the SPI slave DUT
 and receives 'rx_data' from the SPI slave DUT.

- spi_master_transmit_and_receive <font id="function_arguments">( constant tx_data                      : in    std_logic_vector;<br><span style="padding-left:20px"> variable rx_data                      : out   std_logic_vector;<br><span style="padding-left:20px"> constant msg                          : in    string;<br><span style="padding-left:20px"> signal spi_if                         : inout t_spi_if;<br><span style="padding-left:20px"> constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;<br><span style="padding-left:20px"> constant scope                        : in    string                         := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT;<br><span style="padding-left:20px"> constant ext_proc_call                : in    string                         := ""  -- External proc_call. Overwrite if called from another BFM procedure ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 spi_master_transmit_and_receive
----------------------------------------
 This procedure transmits data 'tx_data' to the SPI slave DUT
 and receives 'rx_data' from the SPI slave DUT.
 The SPI interface in this procedure is given as a t_spi_if signal record

- spi_master_transmit_and_receive <font id="function_arguments">( constant tx_data                      : in    t_slv_array;<br><span style="padding-left:20px"> variable rx_data                      : out   t_slv_array;<br><span style="padding-left:20px"> constant msg                          : in    string;<br><span style="padding-left:20px"> signal spi_if                         : inout t_spi_if;<br><span style="padding-left:20px"> constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;<br><span style="padding-left:20px"> constant action_between_words         : in    t_action_between_words         := HOLD_LINE_BETWEEN_WORDS;<br><span style="padding-left:20px"> constant scope                        : in    string                         := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT;<br><span style="padding-left:20px"> constant ext_proc_call                : in    string                         := ""  -- External proc_call. Overwrite if called from another BFM procedure ) </font> <font id="function_return">return ()</font>
</br>**Description**
 Multi-word

- spi_master_transmit_and_check <font id="function_arguments">( constant tx_data                      : in    std_logic_vector;<br><span style="padding-left:20px"> constant data_exp                     : in    std_logic_vector;<br><span style="padding-left:20px"> constant msg                          : in    string;<br><span style="padding-left:20px"> signal spi_if                         : inout t_spi_if;<br><span style="padding-left:20px"> constant alert_level                  : in    t_alert_level                  := error;<br><span style="padding-left:20px"> constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;<br><span style="padding-left:20px"> constant scope                        : in    string                         := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 spi_master_transmit_and_check
----------------------------------------
 This procedure ...
 The SPI interface in this procedure is given as a t_spi_if signal record

- spi_master_transmit_and_check <font id="function_arguments">( constant tx_data                      : in    t_slv_array;<br><span style="padding-left:20px"> constant data_exp                     : in    t_slv_array;<br><span style="padding-left:20px"> constant msg                          : in    string;<br><span style="padding-left:20px"> signal spi_if                         : inout t_spi_if;<br><span style="padding-left:20px"> constant alert_level                  : in    t_alert_level                  := error;<br><span style="padding-left:20px"> constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;<br><span style="padding-left:20px"> constant action_between_words         : in    t_action_between_words         := HOLD_LINE_BETWEEN_WORDS;<br><span style="padding-left:20px"> constant scope                        : in    string                         := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
 Multi-word

- spi_master_transmit <font id="function_arguments">( constant tx_data                      : in    std_logic_vector;<br><span style="padding-left:20px"> constant msg                          : in    string;<br><span style="padding-left:20px"> signal spi_if                         : inout t_spi_if;<br><span style="padding-left:20px"> constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;<br><span style="padding-left:20px"> constant scope                        : in    string                         := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 spi_master_transmit
----------------------------------------
 This procedure transmits data 'tx_data' to the SPI DUT
 The SPI interface in this procedure is given as a t_spi_if signal record

- spi_master_transmit <font id="function_arguments">( constant tx_data                      : in    t_slv_array;<br><span style="padding-left:20px"> constant msg                          : in    string;<br><span style="padding-left:20px"> signal spi_if                         : inout t_spi_if;<br><span style="padding-left:20px"> constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;<br><span style="padding-left:20px"> constant action_between_words         : in    t_action_between_words         := HOLD_LINE_BETWEEN_WORDS;<br><span style="padding-left:20px"> constant scope                        : in    string                         := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
 Multi-word

- spi_master_receive <font id="function_arguments">( variable rx_data                      : out   std_logic_vector;<br><span style="padding-left:20px"> constant msg                          : in    string;<br><span style="padding-left:20px"> signal spi_if                         : inout t_spi_if;<br><span style="padding-left:20px"> constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;<br><span style="padding-left:20px"> constant scope                        : in    string                         := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 spi_master_receive
----------------------------------------
 This procedure receives data 'rx_data' from the SPI DUT
 The SPI interface in this procedure is given as a t_spi_if signal record

- spi_master_receive <font id="function_arguments">( variable rx_data                      : out   t_slv_array;<br><span style="padding-left:20px"> constant msg                          : in    string;<br><span style="padding-left:20px"> signal spi_if                         : inout t_spi_if;<br><span style="padding-left:20px"> constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;<br><span style="padding-left:20px"> constant action_between_words         : in    t_action_between_words         := HOLD_LINE_BETWEEN_WORDS;<br><span style="padding-left:20px"> constant scope                        : in    string                         := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
 Multi-word

- spi_master_check <font id="function_arguments">( constant data_exp                     : in    std_logic_vector;<br><span style="padding-left:20px"> constant msg                          : in    string;<br><span style="padding-left:20px"> signal spi_if                         : inout t_spi_if;<br><span style="padding-left:20px"> constant alert_level                  : in    t_alert_level                  := error;<br><span style="padding-left:20px"> constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;<br><span style="padding-left:20px"> constant scope                        : in    string                         := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 spi_master_check
----------------------------------------
 This procedure receives an SPI transaction, and compares the read data
 to the expected data in 'data_exp'.
 If the read data is inconsistent with the expected data, an alert with
 severity 'alert_level' is triggered.
 The SPI interface in this procedure is given as a t_spi_if signal record

- spi_master_check <font id="function_arguments">( constant data_exp                     : in    t_slv_array;<br><span style="padding-left:20px"> constant msg                          : in    string;<br><span style="padding-left:20px"> signal spi_if                         : inout t_spi_if;<br><span style="padding-left:20px"> constant alert_level                  : in    t_alert_level                  := error;<br><span style="padding-left:20px"> constant action_when_transfer_is_done : in    t_action_when_transfer_is_done := RELEASE_LINE_AFTER_TRANSFER;<br><span style="padding-left:20px"> constant action_between_words         : in    t_action_between_words         := HOLD_LINE_BETWEEN_WORDS;<br><span style="padding-left:20px"> constant scope                        : in    string                         := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel                 : in    t_msg_id_panel                 := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                       : in    t_spi_bfm_config               := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
 Multi-word

- spi_slave_transmit_and_receive <font id="function_arguments">( constant tx_data                : in    std_logic_vector;<br><span style="padding-left:20px"> variable rx_data                : out   std_logic_vector;<br><span style="padding-left:20px"> constant msg                    : in    string;<br><span style="padding-left:20px"> signal sclk                     : inout std_logic;<br><span style="padding-left:20px"> signal ss_n                     : inout std_logic;<br><span style="padding-left:20px"> signal mosi                     : inout std_logic;<br><span style="padding-left:20px"> signal miso                     : inout std_logic;<br><span style="padding-left:20px"> constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;<br><span style="padding-left:20px"> constant scope                  : in    string                   := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT;<br><span style="padding-left:20px"> constant ext_proc_call          : in    string                   := ""  -- External proc_call. Overwrite if called from another BFM procedure ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 spi_slave_transmit_and_receive
----------------------------------------
 This procedure transmits data 'tx_data' to the SPI master DUT
 and receives 'rx_data' from the SPI master DUT.

- spi_slave_transmit_and_receive <font id="function_arguments">( constant tx_data                : in    std_logic_vector;<br><span style="padding-left:20px"> variable rx_data                : out   std_logic_vector;<br><span style="padding-left:20px"> constant msg                    : in    string;<br><span style="padding-left:20px"> signal spi_if                   : inout t_spi_if;<br><span style="padding-left:20px"> constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;<br><span style="padding-left:20px"> constant scope                  : in    string                   := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT;<br><span style="padding-left:20px"> constant ext_proc_call          : in    string                   := ""  -- External proc_call. Overwrite if called from another BFM procedure ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 spi_slave_transmit_and_receive
----------------------------------------
 This procedure transmits data 'tx_data' to the SPI master DUT
 and receives 'rx_data' from the SPI master DUT.
 The SPI interface in this procedure is given as a t_spi_if signal record

- spi_slave_transmit_and_receive <font id="function_arguments">( constant tx_data                : in    t_slv_array;<br><span style="padding-left:20px"> variable rx_data                : out   t_slv_array;<br><span style="padding-left:20px"> constant msg                    : in    string;<br><span style="padding-left:20px"> signal spi_if                   : inout t_spi_if;<br><span style="padding-left:20px"> constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;<br><span style="padding-left:20px"> constant scope                  : in    string                   := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT;<br><span style="padding-left:20px"> constant ext_proc_call          : in    string                   := ""  -- External proc_call. Overwrite if called from another BFM procedure ) </font> <font id="function_return">return ()</font>
</br>**Description**
 Multi-word

- spi_slave_transmit_and_check <font id="function_arguments">( constant tx_data                : in    std_logic_vector;<br><span style="padding-left:20px"> constant data_exp               : in    std_logic_vector;<br><span style="padding-left:20px"> constant msg                    : in    string;<br><span style="padding-left:20px"> signal spi_if                   : inout t_spi_if;<br><span style="padding-left:20px"> constant alert_level            : in    t_alert_level            := error;<br><span style="padding-left:20px"> constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;<br><span style="padding-left:20px"> constant scope                  : in    string                   := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 spi_slave_transmit_and_check
----------------------------------------
 This procedure ...
 The SPI interface in this procedure is given as a t_spi_if signal record

- spi_slave_transmit_and_check <font id="function_arguments">( constant tx_data                : in    t_slv_array;<br><span style="padding-left:20px"> constant data_exp               : in    t_slv_array;<br><span style="padding-left:20px"> constant msg                    : in    string;<br><span style="padding-left:20px"> signal spi_if                   : inout t_spi_if;<br><span style="padding-left:20px"> constant alert_level            : in    t_alert_level            := error;<br><span style="padding-left:20px"> constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;<br><span style="padding-left:20px"> constant scope                  : in    string                   := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
 Multi-word

- spi_slave_transmit <font id="function_arguments">( constant tx_data                : in    std_logic_vector;<br><span style="padding-left:20px"> constant msg                    : in    string;<br><span style="padding-left:20px"> signal spi_if                   : inout t_spi_if;<br><span style="padding-left:20px"> constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;<br><span style="padding-left:20px"> constant scope                  : in    string                   := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 spi_slave_transmit
----------------------------------------
 This procedure transmits data 'tx_data' to the SPI DUT
 The SPI interface in this procedure is given as a t_spi_if signal record

- spi_slave_transmit <font id="function_arguments">( constant tx_data                : in    t_slv_array;<br><span style="padding-left:20px"> constant msg                    : in    string;<br><span style="padding-left:20px"> signal spi_if                   : inout t_spi_if;<br><span style="padding-left:20px"> constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;<br><span style="padding-left:20px"> constant scope                  : in    string                   := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
 Multi-word

- spi_slave_receive <font id="function_arguments">( variable rx_data                : out   std_logic_vector;<br><span style="padding-left:20px"> constant msg                    : in    string;<br><span style="padding-left:20px"> signal spi_if                   : inout t_spi_if;<br><span style="padding-left:20px"> constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;<br><span style="padding-left:20px"> constant scope                  : in    string                   := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 spi_slave_receive
----------------------------------------
 This procedure receives data 'rx_data' from the SPI DUT
 The SPI interface in this procedure is given as a t_spi_if signal record

- spi_slave_receive <font id="function_arguments">( variable rx_data                : out   t_slv_array;<br><span style="padding-left:20px"> constant msg                    : in    string;<br><span style="padding-left:20px"> signal spi_if                   : inout t_spi_if;<br><span style="padding-left:20px"> constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;<br><span style="padding-left:20px"> constant scope                  : in    string                   := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
 Multi-word

- spi_slave_check <font id="function_arguments">( constant data_exp               : in    std_logic_vector;<br><span style="padding-left:20px"> constant msg                    : in    string;<br><span style="padding-left:20px"> signal spi_if                   : inout t_spi_if;<br><span style="padding-left:20px"> constant alert_level            : in    t_alert_level            := error;<br><span style="padding-left:20px"> constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;<br><span style="padding-left:20px"> constant scope                  : in    string                   := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 spi_slave_check
----------------------------------------
 This procedure receives an SPI transaction, and compares the read data
 to the expected data in 'data_exp'.
 If the read data is inconsistent with the expected data, an alert with
 severity 'alert_level' is triggered.
 The SPI interface in this procedure is given as a t_spi_if signal record

- spi_slave_check <font id="function_arguments">( constant data_exp               : in    t_slv_array;<br><span style="padding-left:20px"> constant msg                    : in    string;<br><span style="padding-left:20px"> signal spi_if                   : inout t_spi_if;<br><span style="padding-left:20px"> constant alert_level            : in    t_alert_level            := error;<br><span style="padding-left:20px"> constant when_to_start_transfer : in    t_when_to_start_transfer := START_TRANSFER_ON_NEXT_SS;<br><span style="padding-left:20px"> constant scope                  : in    string                   := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel           : in    t_msg_id_panel           := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config                 : in    t_spi_bfm_config         := C_SPI_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
 Multi-word

