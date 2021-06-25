# Package: checker_pkg
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
- set_default_log_level <font id="function_arguments">(checker : checker_t; default_log_level : log_level_t)</font> <font id="function_return">return ()</font>
- passing_check <font id="function_arguments">(checker : checker_t)</font> <font id="function_return">return ()</font>
- passing_check <font id="function_arguments">(    checker   : checker_t;
    msg       : string;
    line_num  : natural := 0;
    file_name : string  := "")</font> <font id="function_return">return ()</font>
- failing_check <font id="function_arguments">(    checker   : checker_t;
    msg       : string;
    level     : log_level_t := null_log_level;
    line_num  : natural                := 0;
    file_name : string                 := "")</font> <font id="function_return">return ()</font>
- to_string <font id="function_arguments">(stat : checker_stat_t)</font> <font id="function_return">return string</font>
- reset_checker_stat <font id="function_arguments">(checker     : checker_t)</font> <font id="function_return">return ()</font>
- get_checker_stat <font id="function_arguments">(checker       :     checker_t;                             variable stat : out checker_stat_t)</font> <font id="function_return">return ()</font>
