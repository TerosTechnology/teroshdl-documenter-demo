# Package: check_deprecated_pkg

- **File**: check_deprecated_pkg.vhd
## Constants

| Name               | Type   | Value             | Description                                                    |
| ------------------ | ------ | ----------------- | -------------------------------------------------------------- |
| check_result_tag_c | string |  check_result_tag | Deprecated constant with _c suffix. Use without suffix instead |
## Functions
- checker_init <font id="function_arguments">( variable checker : inout checker_t;<br><span style="padding-left:20px"> constant default_level  : in log_level_t  := error;<br><span style="padding-left:20px"> constant default_src    : in string       := "";<br><span style="padding-left:20px"> constant file_name      : in string       := "error.csv";<br><span style="padding-left:20px"> constant display_format : in deprecated_log_format_t := level;<br><span style="padding-left:20px"> constant file_format    : in deprecated_log_format_t := off;<br><span style="padding-left:20px"> constant stop_level : in log_level_t := failure;<br><span style="padding-left:20px"> constant separator      : in character    := ',<br><span style="padding-left:20px">';<br><span style="padding-left:20px"> constant append         : in boolean      := false) </font> <font id="function_return">return ()</font>
- checker_init <font id="function_arguments">( constant default_level  : in log_level_t  := error;<br><span style="padding-left:20px"> constant default_src    : in string       := "";<br><span style="padding-left:20px"> constant file_name      : in string       := "error.csv";<br><span style="padding-left:20px"> constant display_format : in deprecated_log_format_t := level;<br><span style="padding-left:20px"> constant file_format    : in deprecated_log_format_t := off;<br><span style="padding-left:20px"> constant stop_level : in log_level_t := failure;<br><span style="padding-left:20px"> constant separator      : in character    := ',<br><span style="padding-left:20px">';<br><span style="padding-left:20px"> constant append         : in boolean      := false) </font> <font id="function_return">return ()</font>
**Description**
This checker_init is used to reinitialize the default_checker
- enable_pass_msg <font id="function_arguments">(checker : checker_t;<br><span style="padding-left:20px"> handler : log_handler_t) </font> <font id="function_return">return ()</font>
**Description**
Enabling pass messages is done by setting the log level to pass unlessthe current log level already allows pass messages. Disabling pass messageswill set log level to debug unless the current log level already suppressespass messages.
- disable_pass_msg <font id="function_arguments">(checker : checker_t;<br><span style="padding-left:20px"> handler : log_handler_t) </font> <font id="function_return">return ()</font>
- enable_pass_msg <font id="function_arguments">(checker : checker_t) </font> <font id="function_return">return ()</font>
- disable_pass_msg <font id="function_arguments">(checker : checker_t) </font> <font id="function_return">return ()</font>
- enable_pass_msg <font id="function_arguments">(handler : log_handler_t) </font> <font id="function_return">return ()</font>
- disable_pass_msg <font id="function_arguments">(handler : log_handler_t) </font> <font id="function_return">return ()</font>
- enable_pass_msg <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- disable_pass_msg <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- checker_found_errors <font id="function_arguments">( variable result : out boolean) </font> <font id="function_return">return ()</font>
**Description**
These subprograms can be replaced by calls to get_checker_stat and check for n_failed > 0
- checker_found_errors <font id="function_arguments">( constant checker : in checker_t;<br><span style="padding-left:20px"> variable result : out   boolean) </font> <font id="function_return">return ()</font>
