# Package: test_support_pkg

- **File**: test_support_pkg.vhd
## Functions
- assert_true <font id="function_arguments">(value : boolean;<br><span style="padding-left:20px"> msg : string := "") </font> <font id="function_return">return ()</font>
- assert_false <font id="function_arguments">(value : boolean;<br><span style="padding-left:20px"> msg : string := "") </font> <font id="function_return">return ()</font>
- assert_equal <font id="function_arguments">(got,<br><span style="padding-left:20px"> expected,<br><span style="padding-left:20px"> msg : string := "") </font> <font id="function_return">return ()</font>
- assert_equal <font id="function_arguments">(got,<br><span style="padding-left:20px"> expected : integer;<br><span style="padding-left:20px"> msg : string := "") </font> <font id="function_return">return ()</font>
- check_stop_level <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> pass_level : log_level_t;<br><span style="padding-left:20px"> stop_level : log_level_t) </font> <font id="function_return">return ()</font>
- check_format <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> handler : log_handler_t;<br><span style="padding-left:20px"> expected : deprecated_log_format_t) </font> <font id="function_return">return ()</font>
