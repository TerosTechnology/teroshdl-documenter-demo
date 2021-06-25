# Entity: io_TimingCounter
## Diagram
![Diagram](io_TimingCounter.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| TIMING_TABLE | T_NATVEC |       |             |
## Ports
| Port name | Direction | Type                                         | Description |
| --------- | --------- | -------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                    |             |
| Enable    | in        | std_logic                                    |             |
| Load      | in        | std_logic                                    |             |
| Slot      | in        | natural range 0 to (TIMING_TABLE'length - 1) |             |
| Timeout   | out       | std_logic                                    |             |
## Signals
| Name      | Type                          | Description |
| --------- | ----------------------------- | ----------- |
| Counter_s | signed(COUNTER_BITS downto 0) |             |
## Constants
| Name          | Type     | Value                       | Description |
| ------------- | -------- | --------------------------- | ----------- |
| TIMING_TABLE2 | T_INTVEC |  transform(TIMING_TABLE)    |             |
| TIMING_MAX    | natural  |  imax(TIMING_TABLE2)        |             |
| COUNTER_BITS  | natural  |  log2ceilnz(TIMING_MAX + 1) |             |
## Functions
- transform <font id="function_arguments">(vec : T_NATVEC)</font> <font id="function_return">return T_INTVEC</font>
## Processes
- unnamed: _( Clock )_

