# Package: monitor_cmd_pkg
## Constants
| Name                                    | Type                    | Value                                                                                                                                                                                                                                                                   | Description |
| --------------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_MAX_BITS_IN_DATA                      | positive                |  8                                                                                                                                                                                                                                                                      |             |
| C_UART_MONITOR_MSG_ID_PANEL_DEFAULT     | t_msg_id_panel          |  (     ID_MONITOR => ENABLED,     others     => DISABLED   )                                                                                                                                                                                                            |             |
| C_UART_MONITOR_INTERFACE_CONFIG_DEFAULT | t_uart_interface_config |  (     bit_time         => 0 ns,     num_data_bits    => 8,     parity           => PARITY_ODD,     num_stop_bits    => STOP_BITS_ONE   )                                                                                                                               |             |
| C_UART_MONITOR_CONFIG_DEFAULT           | t_uart_monitor_config   |  (     scope_name               => (1 to 14 => "set scope name", others => NUL),     msg_id_panel             => C_UART_MONITOR_MSG_ID_PANEL_DEFAULT,     interface_config         => C_UART_MONITOR_INTERFACE_CONFIG_DEFAULT,     transaction_display_time => 0 ns   ) |             |
## Types
| Name                        | Type | Description |
| --------------------------- | ---- | ----------- |
| t_uart_interface_config     |      |             |
| t_uart_monitor_config       |      |             |
| t_uart_monitor_config_array |      |             |
## Functions
- monitor_constructor <font id="function_arguments">(    constant monitor_config        : in  t_uart_monitor_config;
    variable shared_monitor_config : out t_uart_monitor_config
  )</font> <font id="function_return">return ()</font>
