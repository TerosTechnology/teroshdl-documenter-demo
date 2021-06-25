# Entity: sync_Reset_Altera
## Diagram
![Diagram](sync_Reset_Altera.svg "Diagram")
## Generics
| Generic name | Type              | Value                 | Description |
| ------------ | ----------------- | --------------------- | ----------- |
| SYNC_DEPTH   | T_MISC_SYNC_DEPTH | T_MISC_SYNC_DEPTH'low |             |
## Ports
| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| Clock     | in        | std_logic |             |
| Input     | in        | std_logic |             |
| Output    | out       | std_logic |             |
## Signals
| Name       | Type                                      | Description |
| ---------- | ----------------------------------------- | ----------- |
| Data_async | std_logic                                 |             |
| Data_meta  | std_logic                                 |             |
| Data_sync  | std_logic_vector(SYNC_DEPTH - 1 downto 0) |             |
## Processes
- unnamed: _( Clock, Input )_

