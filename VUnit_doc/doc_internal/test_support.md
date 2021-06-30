# Package: test_support

## Functions
- assert_true <font id="function_arguments">( constant expr : in boolean; constant msg  : in string := ""; constant level : in severity_level := error) </font> <font id="function_return">return ()</font>
- verify_passed_checks <font id="function_arguments">( variable stat : inout checker_stat_t; constant expected_n_passed : in integer := -1) </font> <font id="function_return">return ()</font>
- verify_passed_checks <font id="function_arguments">( checker : checker_t; variable stat : inout checker_stat_t; constant expected_n_passed : in integer := -1) </font> <font id="function_return">return ()</font>
- verify_failed_checks <font id="function_arguments">( variable stat : inout checker_stat_t; constant expected_n_failed : in integer := -1) </font> <font id="function_return">return ()</font>
- verify_failed_checks <font id="function_arguments">( checker : checker_t; variable stat : inout checker_stat_t; constant expected_n_failed : in integer := -1) </font> <font id="function_return">return ()</font>
- apply_sequence <font id="function_arguments">( constant seq : in string; signal clk        : in  std_logic; signal data       : out std_logic; constant active_rising_clk_edge : in boolean := true) </font> <font id="function_return">return ()</font>
- apply_sequence <font id="function_arguments">( constant seq : in string; signal clk        : in  std_logic; signal data       : out std_logic_vector; constant active_rising_clk_edge : in boolean := true) </font> <font id="function_return">return ()</font>
- clock_edge <font id="function_arguments">( signal clk                : in std_logic; constant wait_rising_edge : in boolean := true) </font> <font id="function_return">return boolean </font>
