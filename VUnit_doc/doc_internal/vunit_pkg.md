# Package: vunit_pkg

## Description

This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this file,
 You can obtain one at http://mozilla.org/MPL/2.0/.
 Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
 

## Signals

| Name                | Type     | Description |
| ------------------- | -------- | ----------- |
| phase               | phase_t  |             |
| test_cases_found    | string   |             |
| test_cases_to_run   | string   |             |
| output_path         | string   |             |
| test_idx            | int      |             |
| exit_without_errors | int      |             |
| trace_fd            | int      |             |
| test_runner         | endclass |             |
## Types

| Name    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| phase_t | enum {<br><span style="padding-left:20px">idle,<br><span style="padding-left:20px">                  init,<br><span style="padding-left:20px">                  test_suite_setup,<br><span style="padding-left:20px">                  test_case_setup,<br><span style="padding-left:20px">                  test_case,<br><span style="padding-left:20px">                  test_case_cleanup,<br><span style="padding-left:20px">                  test_suite_cleanup} |             |
## Functions
- search_replace <font id="function_arguments">(string original,<br><span style="padding-left:20px"> string old,<br><span style="padding-left:20px"> string replacement)</font> <font id="function_return">return (string)</font>
- setup <font id="function_arguments">(string runner_cfg)</font> <font id="function_return">return (int)</font>
- cleanup <font id="function_arguments">()</font> <font id="function_return">return (void)</font>
- loop <font id="function_arguments">()</font> <font id="function_return">return (int)</font>
- run <font id="function_arguments">(string test_name)</font> <font id="function_return">return (int)</font>
- is_test_case_setup <font id="function_arguments">()</font> <font id="function_return">return (int)</font>
- is_test_case_cleanup <font id="function_arguments">()</font> <font id="function_return">return (int)</font>
- is_test_suite_setup <font id="function_arguments">()</font> <font id="function_return">return (int)</font>
- is_test_suite_cleanup <font id="function_arguments">()</font> <font id="function_return">return (int)</font>
