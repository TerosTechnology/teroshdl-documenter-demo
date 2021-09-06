# Package: logger_pkg

- **File**: logger_pkg.vhd
## Constants

| Name          | Type     | Value                 | Description                                            |
| ------------- | -------- | --------------------- | ------------------------------------------------------ |
| null_logger   | logger_t |  (p_data => null_ptr) |                                                        |
| no_time_check | time     |  -1 ns                |  Constant to ignore time value when checking log call  |
## Types

| Name         | Type                                  | Description |
| ------------ | ------------------------------------- | ----------- |
| logger_t     |                                       |             |
| logger_vec_t | array (natural range <>) of logger_t  |             |
## Functions
- trace <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
**Description**
-----------------------------------
 Log procedures for each log level
-----------------------------------

- debug <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- pass <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- info <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- warning <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- error <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- failure <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- warning_if <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> condition : boolean;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- error_if <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> condition : boolean;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- failure_if <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> condition : boolean;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- trace <font id="function_arguments">(msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- debug <font id="function_arguments">(msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- pass <font id="function_arguments">(msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- info <font id="function_arguments">(msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- warning <font id="function_arguments">(msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- error <font id="function_arguments">(msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- failure <font id="function_arguments">(msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- warning_if <font id="function_arguments">(condition : boolean;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- error_if <font id="function_arguments">(condition : boolean;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- failure_if <font id="function_arguments">(condition : boolean;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- log <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> log_level : log_level_t := info;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
**Description**
 Log procedure with level as argument

- log <font id="function_arguments">(msg : string;<br><span style="padding-left:20px"> log_level : log_level_t := info;<br><span style="padding-left:20px"> path_offset : natural := 0;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- set_stop_count <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_level : log_level_t;<br><span style="padding-left:20px"> value : positive;<br><span style="padding-left:20px"> unset_children : boolean := false) </font> <font id="function_return">return ()</font>
**Description**
 Set the threshold for stopping simulation for a specific log level and
 logger tree

- disable_stop <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_level : log_level_t;<br><span style="padding-left:20px"> unset_children : boolean := false) </font> <font id="function_return">return ()</font>
**Description**
 Disable stopping simulation for a specific log level and
 logger tree

- set_stop_count <font id="function_arguments">(log_level : log_level_t;<br><span style="padding-left:20px"> value : positive) </font> <font id="function_return">return ()</font>
**Description**
 Set the threshold for stopping simulation for a specific log level in
 the entire logging tree.
 NOTE: Removes all other stop count settings for log_level in entire tree.

- disable_stop <font id="function_arguments">(log_level : log_level_t) </font> <font id="function_return">return ()</font>
**Description**
 Disable stopping simulation for a specific log level in
 the entire logging tree.
 NOTE: Removes all other stop count settings for log_level in entire tree.

- set_stop_level <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_level : alert_log_level_t) </font> <font id="function_return">return ()</font>
**Description**
 Shorthand for configuring the stop counts for (warning, error, failure) in
 a logger subtree. Set stop count to infinite for all levels < log_level and
 1 for all (warning, error, failure) >= log_level.
 NOTE: Removes all other stop count settings from logger subtree.

- set_stop_level <font id="function_arguments">(level : alert_log_level_t) </font> <font id="function_return">return ()</font>
**Description**
 Shorthand for configuring the stop counts in entire logger tree.
 Same behavior as set_stop_level for specific logger subtree above

- unset_stop_count <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_level : log_level_t;<br><span style="padding-left:20px"> unset_children : boolean := false) </font> <font id="function_return">return ()</font>
**Description**
 Unset stop count for stopping simulation for a specific log level and
 logger tree

- disable <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_level : log_level_t;<br><span style="padding-left:20px"> include_children : boolean := true) </font> <font id="function_return">return ()</font>
**Description**
 Disable a log_level from specific logger including all children.
 Disable is used when a log message is unwanted and it should be ignored.
 NOTE: A disabled log message is still counted to get a disabled log count
       statistics.
       errors and failures can be disabled but the final_log_check must
       explicitly allow it as well as an extra safety mechanism.

- hide <font id="function_arguments">(log_handler : log_handler_t;<br><span style="padding-left:20px"> log_level : log_level_t) </font> <font id="function_return">return ()</font>
**Description**
 Hide log messages of specified level to this handler.

- hide <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_handler : log_handler_t;<br><span style="padding-left:20px"> log_level : log_level_t;<br><span style="padding-left:20px"> include_children : boolean := true) </font> <font id="function_return">return ()</font>
**Description**
 Hide log messages from the logger of the specified level to this handler

- hide <font id="function_arguments">(log_handler : log_handler_t;<br><span style="padding-left:20px"> log_levels : log_level_vec_t) </font> <font id="function_return">return ()</font>
**Description**
 Hide log messages of the specified levels to this handler.

- hide <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_handler : log_handler_t;<br><span style="padding-left:20px"> log_levels : log_level_vec_t;<br><span style="padding-left:20px"> include_children : boolean := true) </font> <font id="function_return">return ()</font>
**Description**
 Hide log messages from the logger of the specified levels to this handler

- show <font id="function_arguments">(log_handler : log_handler_t;<br><span style="padding-left:20px"> log_level : log_level_t) </font> <font id="function_return">return ()</font>
**Description**
 Show log messages of the specified log_level to this handler

- show <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_handler : log_handler_t;<br><span style="padding-left:20px"> log_level : log_level_t;<br><span style="padding-left:20px"> include_children : boolean := true) </font> <font id="function_return">return ()</font>
**Description**
 Show log messages from the logger of the specified log_level to this handler

- show <font id="function_arguments">(log_handler : log_handler_t;<br><span style="padding-left:20px"> log_levels : log_level_vec_t) </font> <font id="function_return">return ()</font>
**Description**
 Show log messages of the specified log_levels to this handler

- show <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_handler : log_handler_t;<br><span style="padding-left:20px"> log_levels : log_level_vec_t;<br><span style="padding-left:20px"> include_children : boolean := true) </font> <font id="function_return">return ()</font>
**Description**
 Show log messages from the logger of the specified log_levels to this handler

- show_all <font id="function_arguments">(log_handler : log_handler_t) </font> <font id="function_return">return ()</font>
**Description**
 Show all log levels to the log handler

- show_all <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_handler : log_handler_t;<br><span style="padding-left:20px"> include_children : boolean := true) </font> <font id="function_return">return ()</font>
**Description**
 Show all log levels to the handler from specific logger

- hide_all <font id="function_arguments">(log_handler : log_handler_t) </font> <font id="function_return">return ()</font>
**Description**
 Hide all log levels from this handler

- hide_all <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_handler : log_handler_t;<br><span style="padding-left:20px"> include_children : boolean := true) </font> <font id="function_return">return ()</font>
**Description**
 Hide all log levels from this handler from specific logger

- set_log_handlers <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_handlers : log_handler_vec_t;<br><span style="padding-left:20px"> include_children : boolean := true) </font> <font id="function_return">return ()</font>
**Description**
 Set the log handlers for this logger

- reset_log_count <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_level : log_level_t := null_log_level;<br><span style="padding-left:20px"> include_children : boolean := true) </font> <font id="function_return">return ()</font>
**Description**
 Reset the log call count of a specific level or all levels when level = null_log_level

- final_log_check <font id="function_arguments">(allow_disabled_errors : boolean := false;<br><span style="padding-left:20px"> allow_disabled_failures : boolean := false;<br><span style="padding-left:20px"> fail_on_warning : boolean := false) </font> <font id="function_return">return ()</font>
**Description**
 Perform a check of the log counts and fail unless there are no errors or failures.
 By default no disabled errors or failures are not allowed.
 Disabled errors and failrues can be allowed by setting the corresponding
 arguments to true.
 By default warnings are allowed but failure on warning can be enabled.
 When fail on warning is enabled it also allows disabled warnings.

- mock <font id="function_arguments">(logger : logger_t) </font> <font id="function_return">return ()</font>
**Description**
-------------------------------------------------------------------
 Mock procedures to enable unit testing of code performing logging
-------------------------------------------------------------------
 Mock the logger preventing simulaton abort and recording all logs to it

- mock <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> log_level : log_level_t) </font> <font id="function_return">return ()</font>
**Description**
 Mock log_level of logger preventing simulaton abort and recording all logs to it

- unmock <font id="function_arguments">(logger : logger_t) </font> <font id="function_return">return ()</font>
**Description**
 Unmock the logger returning it to its normal state
 Results in failures if there are still unchecked log calls recorded

- check_log <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> log_level : log_level_t;<br><span style="padding-left:20px"> log_time : time := no_time_check;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
**Description**
 Check that the earliest recorded log call in the mock state matches this
 call or fails. Also consumes this recorded log call such that subsequent
 check_log calls can be used to verify a sequence of log calls

- check_only_log <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> log_level : log_level_t;<br><span style="padding-left:20px"> log_time : time := no_time_check;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
**Description**
 Check that there is only one recorded log call remaining

- check_no_log <font id="function_arguments">()</font> <font id="function_return">return ()</font>
**Description**
 Check that there are no remaining recorded log calls, automatically called
 during unmock

