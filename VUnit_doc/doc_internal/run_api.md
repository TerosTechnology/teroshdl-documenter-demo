# Package: run_pkg

- **File**: run_api.vhd
## Signals

| Name   | Type          | Description |
| ------ | ------------- | ----------- |
| runner | runner_sync_t |             |
## Constants

| Name         | Type     | Value       | Description |
| ------------ | -------- | ----------- | ----------- |
| runner_state | runner_t |  new_runner |             |
## Functions
- test_runner_setup <font id="function_arguments">( signal runner : inout runner_sync_t;<br><span style="padding-left:20px"> constant runner_cfg : in string := runner_cfg_default) </font> <font id="function_return">return ()</font>
- test_runner_cleanup <font id="function_arguments">( signal runner: inout runner_sync_t;<br><span style="padding-left:20px"> external_failure : boolean := false;<br><span style="padding-left:20px"> allow_disabled_errors : boolean := false;<br><span style="padding-left:20px"> allow_disabled_failures : boolean := false;<br><span style="padding-left:20px"> fail_on_warning : boolean := false) </font> <font id="function_return">return ()</font>
- set_timeout <font id="function_arguments">(signal runner : inout runner_sync_t;<br><span style="padding-left:20px"> constant timeout : in time) </font> <font id="function_return">return ()</font>
**Description**
Set watchdog timeout dynamically relative to current timeOverrides time argument to test_runner_watchdog procedure
- test_runner_watchdog <font id="function_arguments">( signal runner                    : inout runner_sync_t;<br><span style="padding-left:20px"> constant timeout                 : in    time;<br><span style="padding-left:20px"> constant do_runner_cleanup : boolean := true) </font> <font id="function_return">return ()</font>
- timeout_notification <font id="function_arguments">( signal runner : runner_sync_t ) </font> <font id="function_return">return boolean </font>
- lock_entry <font id="function_arguments">( signal runner : inout runner_sync_t;<br><span style="padding-left:20px"> constant phase : in runner_legal_phase_t;<br><span style="padding-left:20px"> constant logger : in logger_t := runner_trace_logger;<br><span style="padding-left:20px"> constant line_num  : in natural := 0;<br><span style="padding-left:20px"> constant file_name : in string := "") </font> <font id="function_return">return ()</font>
- unlock_entry <font id="function_arguments">( signal runner : inout runner_sync_t;<br><span style="padding-left:20px"> constant phase : in runner_legal_phase_t;<br><span style="padding-left:20px"> constant logger : in logger_t := runner_trace_logger;<br><span style="padding-left:20px"> constant line_num  : in natural := 0;<br><span style="padding-left:20px"> constant file_name : in string := "") </font> <font id="function_return">return ()</font>
- lock_exit <font id="function_arguments">( signal runner : inout runner_sync_t;<br><span style="padding-left:20px"> constant phase : in runner_legal_phase_t;<br><span style="padding-left:20px"> constant logger : in logger_t := runner_trace_logger;<br><span style="padding-left:20px"> constant line_num  : in natural := 0;<br><span style="padding-left:20px"> constant file_name : in string := "") </font> <font id="function_return">return ()</font>
- unlock_exit <font id="function_arguments">( signal runner : inout runner_sync_t;<br><span style="padding-left:20px"> constant phase : in runner_legal_phase_t;<br><span style="padding-left:20px"> constant logger : in logger_t := runner_trace_logger;<br><span style="padding-left:20px"> constant line_num  : in natural := 0;<br><span style="padding-left:20px"> constant file_name : in string := "") </font> <font id="function_return">return ()</font>
- wait_until <font id="function_arguments">( signal runner : in runner_sync_t;<br><span style="padding-left:20px"> constant phase : in runner_legal_phase_t;<br><span style="padding-left:20px"> constant logger : in logger_t := runner_trace_logger;<br><span style="padding-left:20px"> constant line_num  : in natural := 0;<br><span style="padding-left:20px"> constant file_name : in string := "") </font> <font id="function_return">return ()</font>
- entry_gate <font id="function_arguments">( signal runner : inout runner_sync_t) </font> <font id="function_return">return ()</font>
- exit_gate <font id="function_arguments">( signal runner : in runner_sync_t) </font> <font id="function_return">return ()</font>
- notify <font id="function_arguments">(signal runner : inout runner_sync_t;<br><span style="padding-left:20px"> idx : natural := runner_event_idx) </font> <font id="function_return">return ()</font>
**Description**
Private
