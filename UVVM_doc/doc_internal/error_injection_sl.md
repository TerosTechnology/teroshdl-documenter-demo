# Entity: error_injection_sl
## Diagram
![Diagram](error_injection_sl.svg "Diagram")
## Generics
| Generic name    | Type    | Value | Description |
| --------------- | ------- | ----- | ----------- |
| GC_START_TIME   | time    | 0 ns  |             |
| GC_INSTANCE_IDX | natural | 1     |             |
## Ports
| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| ei_in     | in        | std_logic |             |
| ei_out    | out       | std_logic |             |
## Instantiations
- error_injector_slv: error_injection_slv
