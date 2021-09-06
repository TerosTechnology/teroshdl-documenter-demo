# Package: core_pkg

- **File**: core_pkg.vhd
## Functions
- setup <font id="function_arguments">(file_name : string) </font> <font id="function_return">return ()</font>
- test_start <font id="function_arguments">(test_name : string) </font> <font id="function_return">return ()</font>
- test_suite_done <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- stop <font id="function_arguments">(status : natural) </font> <font id="function_return">return ()</font>
- core_failure <font id="function_arguments">(msg : string) </font> <font id="function_return">return ()</font>
**Description**
 @TODO add core acceptance tests

- mock_core_failure <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- check_core_failure <font id="function_arguments">(msg : string := "") </font> <font id="function_return">return ()</font>
- unmock_core_failure <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- check_and_unmock_core_failure <font id="function_arguments">(msg : string := "") </font> <font id="function_return">return ()</font>
