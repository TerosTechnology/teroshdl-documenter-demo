# Package: logger_pkg
## Constants
| Name          | Type     | Value                 | Description |
| ------------- | -------- | --------------------- | ----------- |
| null_logger   | logger_t |  (p_data => null_ptr) |             |
| no_time_check | time     |  -1 ns                |             |
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
- log <font id="function_arguments">(msg : string;                log_level : log_level_t := info;
                line_num : natural := 0;
                file_name : string := "")</font> <font id="function_return">return ()</font>
- set_stop_count <font id="function_arguments">(logger : logger_t;                           log_level : log_level_t;
                           value : positive;
                           unset_children : boolean := false)</font> <font id="function_return">return ()</font>
- disable_stop <font id="function_arguments">(logger : logger_t;                         log_level : log_level_t;
                         unset_children : boolean := false)</font> <font id="function_return">return ()</font>
- set_stop_count <font id="function_arguments">(log_level : log_level_t;                           value : positive)</font> <font id="function_return">return ()</font>
- disable_stop <font id="function_arguments">(log_level : log_level_t)</font> <font id="function_return">return ()</font>
- set_stop_level <font id="function_arguments">(logger : logger_t;                           log_level : alert_log_level_t)</font> <font id="function_return">return ()</font>
- set_stop_level <font id="function_arguments">(level : alert_log_level_t)</font> <font id="function_return">return ()</font>
- unset_stop_count <font id="function_arguments">(logger : logger_t;                             log_level : log_level_t;
                             unset_children : boolean := false)</font> <font id="function_return">return ()</font>
- disable <font id="function_arguments">(logger : logger_t;                    log_level : log_level_t;
                    include_children : boolean := true)</font> <font id="function_return">return ()</font>
- hide <font id="function_arguments">(log_handler : log_handler_t;                 log_level : log_level_t)</font> <font id="function_return">return ()</font>
- hide <font id="function_arguments">(logger : logger_t;                 log_handler : log_handler_t;
                 log_level : log_level_t;
                 include_children : boolean := true)</font> <font id="function_return">return ()</font>
- hide <font id="function_arguments">(log_handler : log_handler_t;                 log_levels : log_level_vec_t)</font> <font id="function_return">return ()</font>
- hide <font id="function_arguments">(logger : logger_t;                 log_handler : log_handler_t;
                 log_levels : log_level_vec_t;
                 include_children : boolean := true)</font> <font id="function_return">return ()</font>
- show <font id="function_arguments">(log_handler : log_handler_t;                 log_level : log_level_t)</font> <font id="function_return">return ()</font>
- show <font id="function_arguments">(logger : logger_t;                 log_handler : log_handler_t;
                 log_level : log_level_t;
                 include_children : boolean := true)</font> <font id="function_return">return ()</font>
- show <font id="function_arguments">(log_handler : log_handler_t;                 log_levels : log_level_vec_t)</font> <font id="function_return">return ()</font>
- show <font id="function_arguments">(logger : logger_t;                 log_handler : log_handler_t;
                 log_levels : log_level_vec_t;
                 include_children : boolean := true)</font> <font id="function_return">return ()</font>
- show_all <font id="function_arguments">(log_handler : log_handler_t)</font> <font id="function_return">return ()</font>
- show_all <font id="function_arguments">(logger : logger_t;                     log_handler : log_handler_t;
                     include_children : boolean := true)</font> <font id="function_return">return ()</font>
- hide_all <font id="function_arguments">(log_handler : log_handler_t)</font> <font id="function_return">return ()</font>
- hide_all <font id="function_arguments">(logger : logger_t;                     log_handler : log_handler_t;
                     include_children : boolean := true)</font> <font id="function_return">return ()</font>
- set_log_handlers <font id="function_arguments">(logger : logger_t;                             log_handlers : log_handler_vec_t;
                             include_children : boolean := true)</font> <font id="function_return">return ()</font>
- reset_log_count <font id="function_arguments">(logger : logger_t;                            log_level : log_level_t := null_log_level;
                            include_children : boolean := true)</font> <font id="function_return">return ()</font>
- final_log_check <font id="function_arguments">(allow_disabled_errors : boolean := false;                            allow_disabled_failures : boolean := false;
                            fail_on_warning : boolean := false)</font> <font id="function_return">return ()</font>
- mock <font id="function_arguments">(logger : logger_t)</font> <font id="function_return">return ()</font>
- mock <font id="function_arguments">(logger : logger_t; log_level : log_level_t)</font> <font id="function_return">return ()</font>
- unmock <font id="function_arguments">(logger : logger_t)</font> <font id="function_return">return ()</font>
- check_log <font id="function_arguments">(logger : logger_t;                      msg : string;
                      log_level : log_level_t;
                      log_time : time := no_time_check;
                      line_num : natural := 0;
                      file_name : string := "")</font> <font id="function_return">return ()</font>
- check_only_log <font id="function_arguments">(logger : logger_t;                           msg : string;
                           log_level : log_level_t;
                           log_time : time := no_time_check;
                           line_num : natural := 0;
                           file_name : string := "")</font> <font id="function_return">return ()</font>
- check_no_log <font id="function_arguments">()</font> <font id="function_return">return ()</font>
