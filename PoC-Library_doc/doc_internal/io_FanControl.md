# Entity: io_FanControl
## Diagram
![Diagram](io_FanControl.svg "Diagram")
## Generics
| Generic name            | Type    | Value | Description |
| ----------------------- | ------- | ----- | ----------- |
| CLOCK_FREQ              | FREQ    |       |             |
| ADD_INPUT_SYNCHRONIZERS | boolean | TRUE  |             |
| ENABLE_TACHO            | boolean | FALSE |             |
## Ports
| Port name      | Direction | Type                          | Description |
| -------------- | --------- | ----------------------------- | ----------- |
| Clock          | in        | std_logic                     |             |
| Reset          | in        | std_logic                     |             |
| Fan_PWM        | out       | std_logic                     |             |
| Fan_Tacho      | in        | std_logic                     |             |
| TachoFrequency | out       | std_logic_vector(15 downto 0) |             |
## Signals
| Name       | Type                                          | Description |
| ---------- | --------------------------------------------- | ----------- |
| PWM_PWMIn  | std_logic_vector(PWM_RESOLUTION - 1 downto 0) |             |
| PWM_PWMOut | std_logic                                     |             |
## Constants
| Name                 | Type     | Value  | Description |
| -------------------- | -------- | ------ | ----------- |
| TIME_STARTUP_INVERSE | FREQ     |  2 Hz  |             |
| PWM_RESOLUTION       | positive |  4     |             |
| PWM_FREQ             | FREQ     |  10 Hz |             |
| TACHO_RESOLUTION     | positive |  8     |             |
## Instantiations
- PWM: PoC.io_PulseWidthModulation
