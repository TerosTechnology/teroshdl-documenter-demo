# Package: checker_pkg

- **File**: checker_pkg.vhd
## Constants

| Name         | Type      | Value                 | Description |
| ------------ | --------- | --------------------- | ----------- |
| null_checker | checker_t |  (p_data => null_ptr) |             |
## Types

| Name           | Type | Description |
| -------------- | ---- | ----------- |
| checker_t      |      |             |
| checker_stat_t |      |             |
## Functions
- set_default_log_level <font id="function_arguments">(checker : checker_t;<br><span style="padding-left:20px"> default_log_level : log_level_t) </font> <font id="function_return">return ()</font>
- passing_check <font id="function_arguments">(checker : checker_t) </font> <font id="function_return">return ()</font>
- passing_check <font id="function_arguments">( checker   : checker_t;<br><span style="padding-left:20px"> msg       : string;<br><span style="padding-left:20px"> line_num  : natural := 0;<br><span style="padding-left:20px"> file_name : string  := "") </font> <font id="function_return">return ()</font>
- failing_check <font id="function_arguments">( checker   : checker_t;<br><span style="padding-left:20px"> msg       : string;<br><span style="padding-left:20px"> level     : log_level_t := null_log_level;<br><span style="padding-left:20px"> line_num  : natural                := 0;<br><span style="padding-left:20px"> file_name : string                 := "") </font> <font id="function_return">return ()</font>
- to_string <font id="function_arguments">(stat : checker_stat_t) </font> <font id="function_return">return string </font>
- reset_checker_stat <font id="function_arguments">(checker     : checker_t) </font> <font id="function_return">return ()</font>
- get_checker_stat <font id="function_arguments">(checker       :     checker_t;<br><span style="padding-left:20px"> variable stat : out checker_stat_t) </font> <font id="function_return">return ()</font>
