# Package: check_deprecated_pkg
## Constants
| Name               | Type   | Value             | Description                                                    |
| ------------------ | ------ | ----------------- | -------------------------------------------------------------- |
| check_result_tag_c | string |  check_result_tag | Deprecated constant with _c suffix. Use without suffix instead |
## Functions
- checker_init <font id="function_arguments">(    variable checker : inout checker_t;
    constant default_level  : in log_level_t  := error;
    constant default_src    : in string       := "";
    constant file_name      : in string       := "error.csv";
    constant display_format : in deprecated_log_format_t := level;
    constant file_format    : in deprecated_log_format_t := off;
    constant stop_level : in log_level_t := failure;
    constant separator      : in character    := ',';
    constant append         : in boolean      := false)</font> <font id="function_return">return ()</font>
- checker_init <font id="function_arguments">(    constant default_level  : in log_level_t  := error;
    constant default_src    : in string       := "";
    constant file_name      : in string       := "error.csv";
    constant display_format : in deprecated_log_format_t := level;
    constant file_format    : in deprecated_log_format_t := off;
    constant stop_level : in log_level_t := failure;
    constant separator      : in character    := ',';
    constant append         : in boolean      := false)</font> <font id="function_return">return ()</font>
**Description**
This checker_init is used to reinitialize the default_checker
- enable_pass_msg <font id="function_arguments">(checker : checker_t; handler : log_handler_t)</font> <font id="function_return">return ()</font>
**Description**
Enabling pass messages is done by setting the log level to pass unlessthe current log level already allows pass messages. Disabling pass messageswill set log level to debug unless the current log level already suppressespass messages.
- disable_pass_msg <font id="function_arguments">(checker : checker_t; handler : log_handler_t)</font> <font id="function_return">return ()</font>
- enable_pass_msg <font id="function_arguments">(checker : checker_t)</font> <font id="function_return">return ()</font>
- disable_pass_msg <font id="function_arguments">(checker : checker_t)</font> <font id="function_return">return ()</font>
- enable_pass_msg <font id="function_arguments">(handler : log_handler_t)</font> <font id="function_return">return ()</font>
- disable_pass_msg <font id="function_arguments">(handler : log_handler_t)</font> <font id="function_return">return ()</font>
- enable_pass_msg <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- disable_pass_msg <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- checker_found_errors <font id="function_arguments">(    variable result : out boolean)</font> <font id="function_return">return ()</font>
**Description**
These subprograms can be replaced by calls to get_checker_stat and check for n_failed > 0
- checker_found_errors <font id="function_arguments">(    constant checker : in checker_t;
    variable result : out   boolean)</font> <font id="function_return">return ()</font>
