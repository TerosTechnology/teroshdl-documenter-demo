# Package: begin

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 program single registers out of the loop
 program multi registers
 start channels
 run then stop channels
 program pwm mode (including programming duty_cycle and pwm_param multiregs)
 program duty_cycle_a and duty_cycle_b in same cycle
 program blink_param_x and blink_param_y in same cycle
 program pwm_mode
 

## Signals

| Name                          | Type                                                        | Description                                            |
| ----------------------------- | ----------------------------------------------------------- | ------------------------------------------------------ |
| body                          | virtual task                                                |                                                        |
| initialize_pwm                | UVM_DEBUG                                                   |                                                        |
| i                             | for                                                         |                                                        |
| num_trans                     | i                                                           |                                                        |
| under_reset                   | wait                                                        | program single registers out of the loop               |
| body                          | endtask                                                     |                                                        |
| program_pwm_mode_regs         | virtual task                                                |                                                        |
| channel                       | for                                                         |                                                        |
| PWM_NUM_CHANNELS              | channel                                                     |                                                        |
| pwm_en                        | channel                                                     |                                                        |
| channel                       | program_pwm_duty_cycle_regs                                 | program duty_cycle_a and duty_cycle_b in same cycle    |
| channel                       | program_pwm_blink_param_regs                                | program blink_param_x and blink_param_y in same cycle  |
| set_dv_base_reg_field_by_name | [channel].name()),<br><span style="padding-left:20px"> UVM_ |                                                        |
| blink_en                      | [channel].name()),<br><span style="padding-left:20px"> UVM_ |                                                        |
| Enable                        | [channel].name()),<br><span style="padding-left:20px"> UVM_ |                                                        |
| channel                       | [channel].name()),<br><span style="padding-left:20px"> UVM_ |                                                        |
| channel                       | [channel].name()),<br><span style="padding-left:20px"> UVM_ |                                                        |
| pwm_param                     | set_dv_base_reg_field_by_name                               |                                                        |
| htbt_en                       | set_dv_base_reg_field_by_name                               |                                                        |
| Enable                        | set_dv_base_reg_field_by_name                               |                                                        |
| channel                       | set_dv_base_reg_field_by_name                               |                                                        |
| channel                       | set_dv_base_reg_field_by_name                               |                                                        |
| base_reg                      | csr_update                                                  |                                                        |
| Standard                      | end                                                         |                                                        |
| pwm_param                     | set_dv_base_reg_field_by_name                               |                                                        |
| blink_en                      | set_dv_base_reg_field_by_name                               |                                                        |
| Disable                       | set_dv_base_reg_field_by_name                               |                                                        |
| channel                       | set_dv_base_reg_field_by_name                               |                                                        |
| channel                       | set_dv_base_reg_field_by_name                               |                                                        |
| pwm_param                     | set_dv_base_reg_field_by_name                               |                                                        |
| htbt_en                       | set_dv_base_reg_field_by_name                               |                                                        |
| Disable                       | set_dv_base_reg_field_by_name                               |                                                        |
| channel                       | set_dv_base_reg_field_by_name                               |                                                        |
| channel                       | set_dv_base_reg_field_by_name                               |                                                        |
| endcase                       | end                                                         |                                                        |
| pwm_param                     | set_dv_base_reg_field_by_name                               |                                                        |
| phase_delay                   | set_dv_base_reg_field_by_name                               |                                                        |
| phase_delay                   | set_dv_base_reg_field_by_name                               |                                                        |
| channel                       | set_dv_base_reg_field_by_name                               |                                                        |
| channel                       | set_dv_base_reg_field_by_name                               |                                                        |
| csr_update                    | set_dv_base_reg_field_by_name                               |                                                        |
| program_pwm_mode_regs         | UVM_DEBUG                                                   |                                                        |
| pwm_rx_tx_vseq                | endclass                                                    |                                                        |
