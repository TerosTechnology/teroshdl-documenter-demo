# Package: runner_pkg

## Constants

| Name                        | Type     | Value                      | Description |
| --------------------------- | -------- | -------------------------- | ----------- |
| runner_trace_logger         | logger_t |  get_logger("runner")      |             |
| null_runner                 | runner_t |  (p_data => null_ptr)      |             |
| unknown_num_of_test_cases   | integer  |  integer'left              |             |
| unknown_num_of_test_cases_c | integer  |  unknown_num_of_test_cases | Deprecated  |
## Types

| Name     | Type | Description |
| -------- | ---- | ----------- |
| runner_t |      |             |
## Functions
- runner_init <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- set_active_python_runner <font id="function_arguments">(runner : runner_t; value : boolean) </font> <font id="function_return">return ()</font>
- lock_entry <font id="function_arguments">(runner : runner_t; phase : runner_legal_phase_t) </font> <font id="function_return">return ()</font>
- unlock_entry <font id="function_arguments">(runner : runner_t; phase : runner_legal_phase_t) </font> <font id="function_return">return ()</font>
- lock_exit <font id="function_arguments">(runner : runner_t; phase : runner_legal_phase_t) </font> <font id="function_return">return ()</font>
- unlock_exit <font id="function_arguments">(runner : runner_t; phase : runner_legal_phase_t) </font> <font id="function_return">return ()</font>
- set_phase <font id="function_arguments">(runner : runner_t; new_phase : runner_phase_t) </font> <font id="function_return">return ()</font>
- set_test_case_name <font id="function_arguments">(runner : runner_t; index : positive; new_name : string) </font> <font id="function_return">return ()</font>
- set_num_of_test_cases <font id="function_arguments">(runner : runner_t; new_value : integer) </font> <font id="function_return">return ()</font>
- inc_num_of_test_cases <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- inc_active_test_case_index <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- set_test_suite_completed <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- inc_test_suite_iteration <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- set_run_test_case <font id="function_arguments">(runner : runner_t; index : positive; new_name : string) </font> <font id="function_return">return ()</font>
- set_running_test_case <font id="function_arguments">(runner : runner_t; new_name  : string) </font> <font id="function_return">return ()</font>
- inc_num_of_run_test_cases <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- set_has_run_since_last_loop_check <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- clear_has_run_since_last_loop_check <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- set_run_all <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- set_run_all <font id="function_arguments">(runner : runner_t; new_value : boolean) </font> <font id="function_return">return ()</font>
- inc_test_case_iteration <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- init_test_case_iteration <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- set_test_case_exit_after_error <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- clear_test_case_exit_after_error <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- set_test_suite_exit_after_error <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- clear_test_suite_exit_after_error <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
- set_cfg <font id="function_arguments">(runner : runner_t; new_value : string) </font> <font id="function_return">return ()</font>
- set_timeout <font id="function_arguments">(runner : runner_t; timeout : time) </font> <font id="function_return">return ()</font>
- p_disable_simulation_exit <font id="function_arguments">(runner : runner_t) </font> <font id="function_return">return ()</font>
**Description**
Private procedures only use for VUnit internal testing
