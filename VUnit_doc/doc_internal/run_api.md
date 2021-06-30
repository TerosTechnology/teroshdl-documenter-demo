# Package: run_pkg

## Signals

| Name   | Type          | Description |
| ------ | ------------- | ----------- |
| runner | runner_sync_t |             |
## Constants

| Name         | Type     | Value       | Description |
| ------------ | -------- | ----------- | ----------- |
| runner_state | runner_t |  new_runner |             |
## Functions
- test_runner_setup <font id="function_arguments">( signal runner : inout runner_sync_t; constant runner_cfg : in string := runner_cfg_default) </font> <font id="function_return">return ()</font>
- test_runner_cleanup <font id="function_arguments">( signal runner: inout runner_sync_t; external_failure : boolean := false; allow_disabled_errors : boolean := false; allow_disabled_failures : boolean := false; fail_on_warning : boolean := false) </font> <font id="function_return">return ()</font>
- set_timeout <font id="function_arguments">(signal runner : inout runner_sync_t; constant timeout : in time) </font> <font id="function_return">return ()</font>
**Description**
Set watchdog timeout dynamically relative to current timeOverrides time argument to test_runner_watchdog procedure
- test_runner_watchdog <font id="function_arguments">( signal runner                    : inout runner_sync_t; constant timeout                 : in    time; constant do_runner_cleanup : boolean := true) </font> <font id="function_return">return ()</font>
- timeout_notification <font id="function_arguments">( signal runner : runner_sync_t ) </font> <font id="function_return">return boolean </font>
- lock_entry <font id="function_arguments">( signal runner : inout runner_sync_t; constant phase : in runner_legal_phase_t; constant logger : in logger_t := runner_trace_logger; constant line_num  : in natural := 0; constant file_name : in string := "") </font> <font id="function_return">return ()</font>
- unlock_entry <font id="function_arguments">( signal runner : inout runner_sync_t; constant phase : in runner_legal_phase_t; constant logger : in logger_t := runner_trace_logger; constant line_num  : in natural := 0; constant file_name : in string := "") </font> <font id="function_return">return ()</font>
- lock_exit <font id="function_arguments">( signal runner : inout runner_sync_t; constant phase : in runner_legal_phase_t; constant logger : in logger_t := runner_trace_logger; constant line_num  : in natural := 0; constant file_name : in string := "") </font> <font id="function_return">return ()</font>
- unlock_exit <font id="function_arguments">( signal runner : inout runner_sync_t; constant phase : in runner_legal_phase_t; constant logger : in logger_t := runner_trace_logger; constant line_num  : in natural := 0; constant file_name : in string := "") </font> <font id="function_return">return ()</font>
- wait_until <font id="function_arguments">( signal runner : in runner_sync_t; constant phase : in runner_legal_phase_t; constant logger : in logger_t := runner_trace_logger; constant line_num  : in natural := 0; constant file_name : in string := "") </font> <font id="function_return">return ()</font>
- entry_gate <font id="function_arguments">( signal runner : inout runner_sync_t) </font> <font id="function_return">return ()</font>
- exit_gate <font id="function_arguments">( signal runner : in runner_sync_t) </font> <font id="function_return">return ()</font>
- notify <font id="function_arguments">(signal runner : inout runner_sync_t; idx : natural := runner_event_idx) </font> <font id="function_return">return ()</font>
**Description**
Private
