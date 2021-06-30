# Package: log_levels_pkg

## Constants

| Name                      | Type                    | Value                                                                          | Description |
| ------------------------- | ----------------------- | ------------------------------------------------------------------------------ | ----------- |
| null_vec                  | log_level_vec_t(1 to 0) |  (others => info)                                                              |             |
| max_num_custom_log_levels | natural                 |  (     1 + log_level_t'pos(log_level_t'high) - log_level_t'pos(custom_level1)) |             |
## Types

| Name            | Type                                                                                                                                                                                            | Description |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| log_level_t     | ( null_log_level,  trace, debug, pass, info, warning, error, failure,  custom_level1, custom_level2, custom_level3, custom_level4, custom_level5, custom_level6, custom_level7, custom_level8)  |             |
| log_level_vec_t |                                                                                                                                                                                                 |             |
## Functions
