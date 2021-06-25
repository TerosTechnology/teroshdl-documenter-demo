# Entity: io_GlitchFilter
## Diagram
![Diagram](io_GlitchFilter.svg "Diagram")
## Generics
| Generic name                  | Type    | Value | Description |
| ----------------------------- | ------- | ----- | ----------- |
| HIGH_SPIKE_SUPPRESSION_CYCLES | natural | 5     |             |
| LOW_SPIKE_SUPPRESSION_CYCLES  | natural | 5     |             |
## Ports
| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| Clock     | in        | std_logic |             |
| Input     | in        | std_logic |             |
| Output    | out       | std_logic |             |
## Signals
| Name       | Type      | Description |
| ---------- | --------- | ----------- |
| State      | std_logic |             |
| NextState  | std_logic |             |
| TC_en      | std_logic |             |
| TC_Load    | std_logic |             |
| TC_Slot    | natural   |             |
| TC_Timeout | std_logic |             |
## Constants
| Name            | Type     | Value                                                                                                          | Description |
| --------------- | -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| TTID_HIGH_SPIKE | natural  |  0                                                                                                             |             |
| TTID_LOW_SPIKE  | natural  |  1                                                                                                             |             |
| TIMING_TABLE    | T_NATVEC |  ( 		TTID_HIGH_SPIKE			=> HIGH_SPIKE_SUPPRESSION_CYCLES, 		TTID_LOW_SPIKE			=> LOW_SPIKE_SUPPRESSION_CYCLES 	) |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( State, Input, TC_Timeout )_

## Instantiations
- TC: PoC.io_TimingCounter
