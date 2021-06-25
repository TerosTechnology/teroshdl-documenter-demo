# Entity: io_FrequencyCounter
## Diagram
![Diagram](io_FrequencyCounter.svg "Diagram")
## Generics
| Generic name | Type     | Value   | Description |
| ------------ | -------- | ------- | ----------- |
| CLOCK_FREQ   | FREQ     | 100 MHz |             |
| TIMEBASE     | time     | 1 sec   |             |
| RESOLUTION   | positive | 8       |             |
## Ports
| Port name | Direction | Type                                      | Description |
| --------- | --------- | ----------------------------------------- | ----------- |
| Clock     | in        | std_logic                                 |             |
| Reset     | in        | std_logic                                 |             |
| FreqIn    | in        | std_logic                                 |             |
| FreqOut   | out       | std_logic_vector(RESOLUTION - 1 downto 0) |             |
## Signals
| Name                | Type                                        | Description |
| ------------------- | ------------------------------------------- | ----------- |
| TimeBaseCounter_us  | unsigned(TIMEBASECOUNTER_BITS - 1 downto 0) |             |
| TimeBaseCounter_ov  | std_logic                                   |             |
| FrequencyCounter_us | unsigned(FREQUENCYCOUNTER_BITS downto 0)    |             |
| FrequencyCounter_ov | std_logic                                   |             |
| FreqIn_d            | std_logic                                   |             |
| FreqIn_re           | std_logic                                   |             |
| FreqOut_d           | std_logic_vector(RESOLUTION - 1 downto 0)   |             |
## Constants
| Name                  | Type     | Value                                 | Description |
| --------------------- | -------- | ------------------------------------- | ----------- |
| TIMEBASECOUNTER_MAX   | positive |  TimingToCycles(TIMEBASE, CLOCK_FREQ) |             |
| TIMEBASECOUNTER_BITS  | positive |  log2ceilnz(TIMEBASECOUNTER_MAX)      |             |
| REQUENCYCOUNTER_MAX   | positive |  2**RESOLUTION                        |             |
| FREQUENCYCOUNTER_BITS | positive |  RESOLUTION                           |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( Clock )_

- unnamed: _( Clock )_

