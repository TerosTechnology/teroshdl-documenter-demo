# Package: error_injection_pkg

## Constants

| Name                  | Type                     | Value                                                                                                                                                                                                                                                                                                                                                                    | Description |
| --------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| C_EI_CONFIG_DEFAULT   | t_error_injection_config |  (     error_type          => BYPASS,     initial_delay_min   => 0 ns,     initial_delay_max   => 0 ns,     return_delay_min    => 0 ns,     return_delay_max    => 0 ns,     width_min           => 0 ns,     width_max           => 0 ns,     interval            => 1,     base_value          => '0',     randomization_seed1 => 1,     randomization_seed2 => 2   ) |             |
| C_MAX_EI_INSTANCE_NUM | natural                  |  100                                                                                                                                                                                                                                                                                                                                                                     |             |
## Types

| Name                           | Type                                                                  | Description |
| ------------------------------ | --------------------------------------------------------------------- | ----------- |
| t_error_injection_types        | ( BYPASS, PULSE, DELAY, JITTER, INVERT, STUCK_AT_OLD, STUCK_AT_NEW )  |             |
| t_error_injection_config       |                                                                       |             |
| t_error_injection_config_array |                                                                       |             |
