# Package: run_types_pkg
## Constants
| Name                       | Type      | Value                                                                         | Description |
| -------------------------- | --------- | ----------------------------------------------------------------------------- | ----------- |
| max_locked_time            | time      |  1 ms                                                                         |             |
| max_n_test_cases           | natural   |  1024                                                                         |             |
| max_locked_time_c          | time      |  max_locked_time                                                              |             |
| max_n_test_cases_c         | natural   |  max_n_test_cases                                                             |             |
| runner_cfg_default         | string    |  "enabled_test_cases : __all__, output path : , active python runner : false" |             |
| runner_event_idx           | natural   |  0                                                                            |             |
| runner_exit_status_idx     | natural   |  1                                                                            |             |
| runner_timeout_update_idx  | natural   |  2                                                                            |             |
| runner_timeout_idx         | natural   |  3                                                                            |             |
| runner_event               | std_logic |  '1'                                                                          |             |
| idle_runner                | std_logic |  'Z'                                                                          |             |
| runner_exit_with_errors    | std_logic |  'Z'                                                                          |             |
| runner_exit_without_errors | std_logic |  '1'                                                                          |             |
## Types
| Name            | Type                                                                                                                                                                                                                   | Description |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| runner_phase_t  | (test_runner_entry, test_runner_setup, test_suite_setup, test_case_setup,                           test_case, test_case_cleanup, test_suite_cleanup, test_runner_cleanup,                           test_runner_exit) |             |
| phase_locks_t   |                                                                                                                                                                                                                        |             |
| boolean_array_t |                                                                                                                                                                                                                        |             |
