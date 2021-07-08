# Package: generic_sb_support_pkg

## Constants

| Name                | Type        | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_SB_CONFIG_DEFAULT | t_sb_config |  (mismatch_alert_level      => ERROR,<br><span style="padding-left:20px">                                                  allow_lossy               => false,<br><span style="padding-left:20px">                                                  allow_out_of_order        => false,<br><span style="padding-left:20px">                                                  overdue_check_alert_level => ERROR,<br><span style="padding-left:20px">                                                  overdue_check_time_limit  => 0 ns,<br><span style="padding-left:20px">                                                  ignore_initial_garbage    => false) |             |
## Types

| Name              | Type                                    | Description |
| ----------------- | --------------------------------------- | ----------- |
| t_sb_config       |                                         |             |
| t_sb_config_array | array(integer range <>) of t_sb_config  |             |
## Functions
- pad_sb_slv <font id="function_arguments">( constant pad_data   : std_logic_vector;<br><span style="padding-left:20px"> constant pad_width  : positive := C_SB_SLV_WIDTH ) </font> <font id="function_return">return std_logic_vector </font>
