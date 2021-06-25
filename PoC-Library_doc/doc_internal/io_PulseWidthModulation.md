# Entity: io_PulseWidthModulation
## Diagram
![Diagram](io_PulseWidthModulation.svg "Diagram")
## Generics
| Generic name   | Type     | Value   | Description |
| -------------- | -------- | ------- | ----------- |
| CLOCK_FREQ     | FREQ     | 100 MHz |             |
| PWM_FREQ       | FREQ     | 1 kHz   |             |
| PWM_RESOLUTION | positive | 8       |             |
## Ports
| Port name | Direction | Type                                          | Description |
| --------- | --------- | --------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                     |             |
| Reset     | in        | std_logic                                     |             |
| PWMIn     | in        | std_logic_vector(PWM_RESOLUTION - 1 downto 0) |             |
| PWMOut    | out       | std_logic                                     |             |
## Signals
| Name                    | Type                                         | Description |
| ----------------------- | -------------------------------------------- | ----------- |
| PWM_FrequencyCounter_us | unsigned(PWM_FREQUENCYCOUNTER_BITS downto 0) |             |
| PWM_FrequencyCounter_ov | std_logic                                    |             |
| PWM_PulseCounter_us     | unsigned(PWM_RESOLUTION - 1 downto 0)        |             |
| PWM_PulseCounter_ov     | std_logic                                    |             |
## Constants
| Name                      | Type     | Value                                            | Description |
| ------------------------- | -------- | ------------------------------------------------ | ----------- |
| PWM_STEPS                 | positive |  2**PWM_RESOLUTION                               |             |
| PWM_STEP_FREQ             | FREQ     |  PWM_FREQ * (PWM_STEPS - 1)                      |             |
| PWM_FREQUENCYCOUNTER_MAX  | positive |  (CLOCK_FREQ+PWM_STEP_FREQ-1 Hz) / PWM_STEP_FREQ |             |
| PWM_FREQUENCYCOUNTER_BITS | positive |  log2ceilnz(PWM_FREQUENCYCOUNTER_MAX)            |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( Clock )_

