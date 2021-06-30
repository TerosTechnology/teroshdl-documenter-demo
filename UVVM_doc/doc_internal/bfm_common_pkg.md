# Package: bfm_common_pkg

## Types

| Name                 | Type                                                                   | Description |
| -------------------- | ---------------------------------------------------------------------- | ----------- |
| t_normalization_mode | (ALLOW_WIDER, ALLOW_NARROWER, ALLOW_WIDER_NARROWER, ALLOW_EXACT_ONLY)  |             |
## Functions
- wait_until_given_time_after_rising_edge <font id="function_arguments">( signal clk         : in std_logic; constant wait_time : in time ) </font> <font id="function_return">return ()</font>
- wait_until_given_time_before_rising_edge <font id="function_arguments">( signal clk            : in std_logic; constant time_to_edge : in time; constant clk_period   : in time ) </font> <font id="function_return">return ()</font>
- wait_num_rising_edge <font id="function_arguments">( signal clk               : in std_logic; constant num_rising_edge : in natural ) </font> <font id="function_return">return ()</font>
- wait_num_rising_edge_plus_margin <font id="function_arguments">( signal clk               : in std_logic; constant num_rising_edge : in natural; constant margin          : in time ) </font> <font id="function_return">return ()</font>
- wait_on_bfm_sync_start <font id="function_arguments">( signal clk                      : in std_logic; constant bfm_sync               : in t_bfm_sync; constant setup_time             : in time  := -1 ns; constant config_clock_period    : in time  := -1 ns; variable time_of_falling_edge   : out time; variable time_of_rising_edge    : out time ) </font> <font id="function_return">return ()</font>
- wait_on_bfm_exit <font id="function_arguments">( signal clk                      : in std_logic; constant bfm_sync               : in t_bfm_sync; constant hold_time              : in time := -1 ns; constant time_of_falling_edge   : in time := -1 ns; constant time_of_rising_edge    : in time := -1 ns ) </font> <font id="function_return">return ()</font>
- check_clock_period_margin <font id="function_arguments">( signal   clock                          : in std_logic; constant bfm_sync                       : in t_bfm_sync; constant time_of_falling_edge           : in time; constant time_of_rising_edge            : in time; constant config_clock_period            : in time; constant config_clock_period_margin     : in time; constant config_clock_margin_severity   : in t_alert_level := TB_ERROR ) </font> <font id="function_return">return ()</font>
