# Entity: misc_FrequencyMeasurement
## Diagram
![Diagram](misc_FrequencyMeasurement.svg "Diagram")
## Generics
| Generic name         | Type | Value   | Description |
| -------------------- | ---- | ------- | ----------- |
| REFERENCE_CLOCK_FREQ | FREQ | 100 MHz |             |
## Ports
| Port name       | Direction | Type      | Description |
| --------------- | --------- | --------- | ----------- |
| Reference_Clock | in        | std_logic |             |
| Input_Clock     | in        | std_logic |             |
| Start           | in        | std_logic |             |
| Done            | out       | std_logic |             |
| Result          | out       | T_SLV_32  |             |
## Signals
| Name                   | Type                                   | Description |
| ---------------------- | -------------------------------------- | ----------- |
| TimeBase_Counter_rst   | std_logic                              |             |
| TimeBase_Counter_s     | signed(TIMEBASE_COUNTER_BITS downto 0) |             |
| TimeBase_Counter_nxt   | signed(TIMEBASE_COUNTER_BITS downto 0) |             |
| TimeBase_Counter_uf    | std_logic                              |             |
| Stop                   | std_logic                              |             |
| sync_Start             | std_logic                              |             |
| sync_Stop              | std_logic                              |             |
| sync1_Busy             | T_SLV_2                                |             |
| Frequency_Counter_en_r | std_logic                              |             |
| Frequency_Counter_us   | unsigned(31 downto 0)                  |             |
| CaptureResult          | std_logic                              |             |
| CaptureResult_d        | std_logic                              |             |
| Result_en              | std_logic                              |             |
| Result_d               | T_SLV_32                               |             |
| Done_r                 | std_logic                              |             |
## Constants
| Name                  | Type     | Value                                                                | Description |
| --------------------- | -------- | -------------------------------------------------------------------- | ----------- |
| TIMEBASE_COUNTER_MAX  | positive |  TimingToCycles(ite(SIMULATION, 10 us, 1 sec), REFERENCE_CLOCK_FREQ) |             |
| TIMEBASE_COUNTER_BITS | positive |  log2ceilnz(TIMEBASE_COUNTER_MAX)                                    |             |
## Processes
- unnamed: _( Reference_Clock )_

- unnamed: _( Input_Clock )_

- unnamed: _( Reference_Clock )_

## Instantiations
- sync1: poc.sync_Strobe
