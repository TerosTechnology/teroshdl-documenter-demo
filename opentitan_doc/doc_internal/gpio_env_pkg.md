# Package: gpio_env_pkg

- **File**: gpio_env_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Constants

| Name           | Type   | Value                                               | Description                     |
| -------------- | ------ | --------------------------------------------------- | ------------------------------- |
| uint           | uint   | 32                                                  | no. of gpio pins                |
| uint           | uint   | 16                                                  | no. of cycles for noise filter  |
| uint           | uint   | 1                                                   | No. of alerts                   |
| LIST_OF_ALERTS | string | {<br><span style="padding-left:20px">"fatal_fault"} |                                 |
## Types

| Name                   | Type                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                     |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| gpio_vif               | virtual pins_if #(NUM_GPIOS)                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                 |
| gpio_env_cfg           | undefined                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                 |
| gpio_env_cov           | undefined                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                 |
| gpio_virtual_sequencer | cip_base_virtual_sequencer #(gpio_env_cfg,<br><span style="padding-left:20px"> gpio_env_cov)                                                                                                                                                 |                                                                                                                                                                                                                                                                 |
| gpio_transition_t      | struct packed {<br><span style="padding-left:20px">     bit transition_occurred;<br><span style="padding-left:20px">     bit is_rising_edge;<br><span style="padding-left:20px">   }                                                         | structure to indicate gpio pin transition and type of transition transition_occurred: 1-yes, 0-no is_rising_edge: 1-rising edge transition, 0-falling edge transition                                                                                           |
| gpio_reg_update_due_t  | struct packed {<br><span style="padding-left:20px">     bit needs_update;<br><span style="padding-left:20px">     bit [TL_DW-1:0] reg_value;<br><span style="padding-left:20px">     time eval_time;<br><span style="padding-left:20px">   } | structure to indicate whether or not register update is due for particular gpio register needs_update: 1-update is due, 0-update is not due reg_value: value to be updated when update is due eval_time: time stamp of event, which triggered interrupt update  |
