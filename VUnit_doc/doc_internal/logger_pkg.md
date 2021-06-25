# Package: logger_pkg
## Constants
| Name          | Type     | Value                 | Description                                          |
| ------------- | -------- | --------------------- | ---------------------------------------------------- |
| null_logger   | logger_t |  (p_data => null_ptr) |                                                      |
| no_time_check | time     |  -1 ns                | Constant to ignore time value when checking log call |
## Types
| Name         | Type | Description |
| ------------ | ---- | ----------- |
| logger_t     |      |             |
| logger_vec_t |      |             |
## Functions
- trace <font id="function_arguments">(logger : logger_t;                  msg : string;
                  line_num : natural := 0;
                  file_name : string := "")</font> <font id="function_return">return ()</font>
- debug <font id="function_arguments">(logger : logger_t;                  msg : string;
                  line_num : natural := 0;
                  file_name : string := "")</font> <font id="function_return">return ()</font>
- pass <font id="function_arguments">(logger : logger_t;                 msg : string;
                 line_num : natural := 0;
                 file_name : string := "")</font> <font id="function_return">return ()</font>
- info <font id="function_arguments">(logger : logger_t;                 msg : string;
                 line_num : natural := 0;
                 file_name : string := "")</font> <font id="function_return">return ()</font>
- warning <font id="function_arguments">(logger : logger_t;                    msg : string;
                    line_num : natural := 0;
                    file_name : string := "")</font> <font id="function_return">return ()</font>
- error <font id="function_arguments">(logger : logger_t;                  msg : string;
                  line_num : natural := 0;
                  file_name : string := "")</font> <font id="function_return">return ()</font>
- failure <font id="function_arguments">(logger : logger_t;                    msg : string;
                    line_num : natural := 0;
                    file_name : string := "")</font> <font id="function_return">return ()</font>
- warning_if <font id="function_arguments">(logger : logger_t;                       condition : boolean;
                       msg : string;
                       line_num : natural := 0;
                       file_name : string := "")</font> <font id="function_return">return ()</font>
- error_if <font id="function_arguments">(logger : logger_t;                     condition : boolean;
                     msg : string;
                     line_num : natural := 0;
                     file_name : string := "")</font> <font id="function_return">return ()</font>
- failure_if <font id="function_arguments">(logger : logger_t;                       condition : boolean;
                       msg : string;
                       line_num : natural := 0;
                       file_name : string := "")</font> <font id="function_return">return ()</font>
- trace <font id="function_arguments">(msg : string;                  line_num : natural := 0;
                  file_name : string := "")</font> <font id="function_return">return ()</font>
- debug <font id="function_arguments">(msg : string;                  line_num : natural := 0;
                  file_name : string := "")</font> <font id="function_return">return ()</font>
- pass <font id="function_arguments">(msg : string;                 line_num : natural := 0;
                 file_name : string := "")</font> <font id="function_return">return ()</font>
- info <font id="function_arguments">(msg : string;                 line_num : natural := 0;
                 file_name : string := "")</font> <font id="function_return">return ()</font>
- warning <font id="function_arguments">(msg : string;                    line_num : natural := 0;
                    file_name : string := "")</font> <font id="function_return">return ()</font>
- error <font id="function_arguments">(msg : string;                  line_num : natural := 0;
                  file_name : string := "")</font> <font id="function_return">return ()</font>
- failure <font id="function_arguments">(msg : string;                    line_num : natural := 0;
                    file_name : string := "")</font> <font id="function_return">return ()</font>
- warning_if <font id="function_arguments">(condition : boolean;                       msg : string;
                       line_num : natural := 0;
                       file_name : string := "")</font> <font id="function_return">return ()</font>
- error_if <font id="function_arguments">(condition : boolean;                     msg : string;
                     line_num : natural := 0;
                     file_name : string := "")</font> <font id="function_return">return ()</font>
- failure_if <font id="function_arguments">(condition : boolean;                       msg : string;
                       line_num : natural := 0;
                       file_name : string := "")</font> <font id="function_return">return ()</font>
- log <font id="function_arguments">(logger : logger_t;                msg : string;
                log_level : log_level_t := info;
                line_num : natural := 0;
                file_name : string := "")</font> <font id="function_return">return ()</font>
**Description**
Log procedure with level as argument
- log <font id="function_arguments">(msg : string;                log_level : log_level_t := info;
                line_num : natural := 0;
                file_name : string := "")</font> <font id="function_return">return ()</font>
- set_stop_count <font id="function_arguments">(logger : logger_t;                           log_level : log_level_t;
                           value : positive;
                           unset_children : boolean := false)</font> <font id="function_return">return ()</font>
**Description**
Set the threshold for stopping simulation for a specific log level andlogger tree
- disable_stop <font id="function_arguments">(logger : logger_t;                         log_level : log_level_t;
                         unset_children : boolean := false)</font> <font id="function_return">return ()</font>
**Description**
Disable stopping simulation for a specific log level andlogger tree
- set_stop_count <font id="function_arguments">(log_level : log_level_t;                           value : positive)</font> <font id="function_return">return ()</font>
**Description**
Set the threshold for stopping simulation for a specific log level inthe entire logging tree.NOTE: Removes all other stop count settings for log_level in entire tree.
- disable_stop <font id="function_arguments">(log_level : log_level_t)</font> <font id="function_return">return ()</font>
**Description**
Disable stopping simulation for a specific log level inthe entire logging tree.NOTE: Removes all other stop count settings for log_level in entire tree.
- set_stop_level <font id="function_arguments">(logger : logger_t;                           log_level : alert_log_level_t)</font> <font id="function_return">return ()</font>
**Description**
Shorthand for configuring the stop counts for (warning, error, failure) ina logger subtree. Set stop count to infinite for all levels < log_level and1 for all (warning, error, failure) >= log_level.NOTE: Removes all other stop count settings from logger subtree.
- set_stop_level <font id="function_arguments">(level : alert_log_level_t)</font> <font id="function_return">return ()</font>
**Description**
Shorthand for configuring the stop counts in entire logger tree.Same behavior as set_stop_level for specific logger subtree above
- unset_stop_count <font id="function_arguments">(logger : logger_t;                             log_level : log_level_t;
                             unset_children : boolean := false)</font> <font id="function_return">return ()</font>
**Description**
Unset stop count for stopping simulation for a specific log level andlogger tree
- disable <font id="function_arguments">(logger : logger_t;                    log_level : log_level_t;
                    include_children : boolean := true)</font> <font id="function_return">return ()</font>
**Description**
Disable a log_level from specific logger including all children.Disable is used when a log message is unwanted and it should be ignored.NOTE: A disabled log message is still counted to get a disabled log count      statistics.      errors and failures can be disabled but the final_log_check must      explicitly allow it as well as an extra safety mechanism.
- hide <font id="function_arguments">(log_handler : log_handler_t;                 log_level : log_level_t)</font> <font id="function_return">return ()</font>
**Description**
Hide log messages of specified level to this handler.
- hide <font id="function_arguments">(logger : logger_t;                 log_handler : log_handler_t;
                 log_level : log_level_t;
                 include_children : boolean := true)</font> <font id="function_return">return ()</font>
**Description**
Hide log messages from the logger of the specified level to this handler
- hide <font id="function_arguments">(log_handler : log_handler_t;                 log_levels : log_level_vec_t)</font> <font id="function_return">return ()</font>
**Description**
Hide log messages of the specified levels to this handler.
- hide <font id="function_arguments">(logger : logger_t;                 log_handler : log_handler_t;
                 log_levels : log_level_vec_t;
                 include_children : boolean := true)</font> <font id="function_return">return ()</font>
**Description**
Hide log messages from the logger of the specified levels to this handler
- show <font id="function_arguments">(log_handler : log_handler_t;                 log_level : log_level_t)</font> <font id="function_return">return ()</font>
**Description**
Show log messages of the specified log_level to this handler
- show <font id="function_arguments">(logger : logger_t;                 log_handler : log_handler_t;
                 log_level : log_level_t;
                 include_children : boolean := true)</font> <font id="function_return">return ()</font>
**Description**
Show log messages from the logger of the specified log_level to this handler
- show <font id="function_arguments">(log_handler : log_handler_t;                 log_levels : log_level_vec_t)</font> <font id="function_return">return ()</font>
**Description**
Show log messages of the specified log_levels to this handler
- show <font id="function_arguments">(logger : logger_t;                 log_handler : log_handler_t;
                 log_levels : log_level_vec_t;
                 include_children : boolean := true)</font> <font id="function_return">return ()</font>
**Description**
Show log messages from the logger of the specified log_levels to this handler
- show_all <font id="function_arguments">(log_handler : log_handler_t)</font> <font id="function_return">return ()</font>
**Description**
Show all log levels to the log handler
- show_all <font id="function_arguments">(logger : logger_t;                     log_handler : log_handler_t;
                     include_children : boolean := true)</font> <font id="function_return">return ()</font>
**Description**
Show all log levels to the handler from specific logger
- hide_all <font id="function_arguments">(log_handler : log_handler_t)</font> <font id="function_return">return ()</font>
**Description**
Hide all log levels from this handler
- hide_all <font id="function_arguments">(logger : logger_t;                     log_handler : log_handler_t;
                     include_children : boolean := true)</font> <font id="function_return">return ()</font>
**Description**
Hide all log levels from this handler from specific logger
- set_log_handlers <font id="function_arguments">(logger : logger_t;                             log_handlers : log_handler_vec_t;
                             include_children : boolean := true)</font> <font id="function_return">return ()</font>
**Description**
Set the log handlers for this logger
- reset_log_count <font id="function_arguments">(logger : logger_t;                            log_level : log_level_t := null_log_level;
                            include_children : boolean := true)</font> <font id="function_return">return ()</font>
**Description**
Reset the log call count of a specific level or all levels when level = null_log_level
- final_log_check <font id="function_arguments">(allow_disabled_errors : boolean := false;                            allow_disabled_failures : boolean := false;
                            fail_on_warning : boolean := false)</font> <font id="function_return">return ()</font>
**Description**
Perform a check of the log counts and fail unless there are no errors or failures.By default no disabled errors or failures are not allowed.Disabled errors and failrues can be allowed by setting the correspondingarguments to true.By default warnings are allowed but failure on warning can be enabled.When fail on warning is enabled it also allows disabled warnings.
- mock <font id="function_arguments">(logger : logger_t)</font> <font id="function_return">return ()</font>
**Description**
Mock the logger preventing simulaton abort and recording all logs to it
- mock <font id="function_arguments">(logger : logger_t; log_level : log_level_t)</font> <font id="function_return">return ()</font>
**Description**
Mock log_level of logger preventing simulaton abort and recording all logs to it
- unmock <font id="function_arguments">(logger : logger_t)</font> <font id="function_return">return ()</font>
**Description**
Unmock the logger returning it to its normal stateResults in failures if there are still unchecked log calls recorded
- check_log <font id="function_arguments">(logger : logger_t;                      msg : string;
                      log_level : log_level_t;
                      log_time : time := no_time_check;
                      line_num : natural := 0;
                      file_name : string := "")</font> <font id="function_return">return ()</font>
**Description**
Check that the earliest recorded log call in the mock state matches thiscall or fails. Also consumes this recorded log call such that subsequentcheck_log calls can be used to verify a sequence of log calls
- check_only_log <font id="function_arguments">(logger : logger_t;                           msg : string;
                           log_level : log_level_t;
                           log_time : time := no_time_check;
                           line_num : natural := 0;
                           file_name : string := "")</font> <font id="function_return">return ()</font>
**Description**
Check that there is only one recorded log call remaining
- check_no_log <font id="function_arguments">()</font> <font id="function_return">return ()</font>
**Description**
Check that there are no remaining recorded log calls, automatically calledduring unmock
