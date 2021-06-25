# Entity: sync_Reset_Xilinx
## Diagram
![Diagram](sync_Reset_Xilinx.svg "Diagram")
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
| Name        | Type      | Description |
| ----------- | --------- | ----------- |
| Reset_async | std_logic |             |
| Reset_meta  | std_logic |             |
| Reset_sync  | std_logic |             |
## Instantiations
- FF2_METASTABILITY_FFS: FDP
- FF3_METASTABILITY_FFS: FDP
