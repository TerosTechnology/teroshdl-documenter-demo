# Package: gpio_bfm_pkg

## Constants

| Name                      | Type              | Value                                                                                                                                                                         | Description                                 |
| ------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| C_SCOPE                   | string            |  "GPIO BFM"                                                                                                                                                                   |                                             |
| C_GPIO_BFM_CONFIG_DEFAULT | t_gpio_bfm_config |  (     clock_period     => -1 ns,     match_strictness => MATCH_STD,     id_for_bfm       => ID_BFM,     id_for_bfm_wait  => ID_BFM_WAIT,     timeout          => -1 ns     ) | Define the default value for the BFM config |
## Types

| Name              | Type | Description                                              |
| ----------------- | ---- | -------------------------------------------------------- |
| t_gpio_bfm_config |      | Configuration record to be assigned in the test harness. |
## Functions
- gpio_set <font id="function_arguments">( constant data_value   : in    std_logic_vector;  -- '-' means don't change constant msg          : in    string; signal data_port      : inout std_logic_vector; constant scope        : in    string            := C_SCOPE; constant msg_id_panel : in    t_msg_id_panel    := shared_msg_id_panel; constant config       : in    t_gpio_bfm_config := C_GPIO_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
- gpio_get <font id="function_arguments">( variable data_value   : out std_logic_vector; constant msg          : in  string; signal data_port      : in  std_logic_vector; constant scope        : in  string            := C_SCOPE; constant msg_id_panel : in  t_msg_id_panel    := shared_msg_id_panel; constant config       : in  t_gpio_bfm_config := C_GPIO_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
- gpio_check <font id="function_arguments">( constant data_exp     : in std_logic_vector;  -- '-' means don't care constant msg          : in string; signal data_port      : in std_logic_vector; constant alert_level  : in t_alert_level     := error; constant scope        : in string            := C_SCOPE; constant msg_id_panel : in t_msg_id_panel    := shared_msg_id_panel; constant config       : in t_gpio_bfm_config := C_GPIO_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
**Description**
Perform a read operation, then compare the read value to the expected value.
- gpio_check_stable <font id="function_arguments">( constant data_exp     : in std_logic_vector;  -- '-' means don't care constant stable_req   : in time; constant msg          : in string; signal data_port      : in std_logic_vector; constant alert_level  : in t_alert_level     := error; constant scope        : in string            := C_SCOPE; constant msg_id_panel : in t_msg_id_panel    := shared_msg_id_panel; constant config       : in t_gpio_bfm_config := C_GPIO_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
**Description**
Perform a read operation, then compare the read value to the expected value.Verify that the read value has been stable for a certain time.
- gpio_expect <font id="function_arguments">( constant data_exp     : in std_logic_vector; constant msg          : in string; signal data_port      : in std_logic_vector; constant timeout      : in time              := -1 ns;  -- -1 = no timeout constant alert_level  : in t_alert_level     := error; constant scope        : in string            := C_SCOPE; constant msg_id_panel : in t_msg_id_panel    := shared_msg_id_panel; constant config       : in t_gpio_bfm_config := C_GPIO_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
**Description**
Perform a read operation, then compare the read value to the expected value.
- gpio_expect_stable <font id="function_arguments">( constant data_exp        : in std_logic_vector; constant stable_req      : in time; constant stable_req_from : in t_from_point_in_time;  -- Which point in time stable_req starts constant msg             : in string; signal data_port         : in std_logic_vector; constant timeout         : in time              := -1 ns;  -- -1 = no timeout constant alert_level     : in t_alert_level     := error; constant scope           : in string            := C_SCOPE; constant msg_id_panel    : in t_msg_id_panel    := shared_msg_id_panel; constant config          : in t_gpio_bfm_config := C_GPIO_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
**Description**
Perform a read operation, then compare the read value to the expected value.Verify that the read value remains stable for a certain time after the datais same as expected or after the data last event.
