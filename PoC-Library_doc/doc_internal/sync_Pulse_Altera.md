# Entity: sync_Pulse_Altera
## Diagram
![Diagram](sync_Pulse_Altera.svg "Diagram")
## Generics
| Generic name | Type              | Value                 | Description |
| ------------ | ----------------- | --------------------- | ----------- |
| BITS         | positive          | 1                     |             |
| SYNC_DEPTH   | T_MISC_SYNC_DEPTH | T_MISC_SYNC_DEPTH'low |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| Clock     | in        | std_logic                           |             |
| Input     | in        | std_logic_vector(BITS - 1 downto 0) |             |
| Output    | out       | std_logic_vector(BITS - 1 downto 0) |             |
