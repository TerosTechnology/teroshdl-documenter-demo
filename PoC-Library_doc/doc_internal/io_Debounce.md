# Entity: io_Debounce
## Diagram
![Diagram](io_Debounce.svg "Diagram")
## Generics
| Generic name            | Type             | Value       | Description |
| ----------------------- | ---------------- | ----------- | ----------- |
| CLOCK_FREQ              | FREQ             |             |             |
| BOUNCE_TIME             | time             |             |             |
| BITS                    | positive         | 1           |             |
| INIT                    | std_logic_vector | x"00000000" |             |
| ADD_INPUT_SYNCHRONIZERS | boolean          | true        |             |
| COMMON_LOCK             | boolean          | false       |             |
## Ports
| Port name | Direction | Type                              | Description |
| --------- | --------- | --------------------------------- | ----------- |
| Clock     | in        | std_logic                         |             |
| Reset     | in        | std_logic                         |             |
| Input     | in        | std_logic_vector(BITS-1 downto 0) |             |
| Output    | out       | std_logic_vector(BITS-1 downto 0) |             |
## Signals
| Name   | Type                          | Description |
| ------ | ----------------------------- | ----------- |
| sync   | std_logic_vector(Input'range) |             |
| prev   | std_logic_vector(Input'range) |             |
| active | std_logic_vector(Input'range) |             |
## Constants
| Name         | Type    | Value                                        | Description |
| ------------ | ------- | -------------------------------------------- | ----------- |
| LOCK_COUNT_X | integer |  TimingToCycles(BOUNCE_TIME, CLOCK_FREQ) - 1 |             |
## Processes
- unnamed: _( Clock )_

