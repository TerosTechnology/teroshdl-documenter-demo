# Entity: sync_Strobe
## Diagram
![Diagram](sync_Strobe.svg "Diagram")
## Generics
| Generic name        | Type              | Value                 | Description |
| ------------------- | ----------------- | --------------------- | ----------- |
| BITS                | positive          | 1                     |             |
| GATED_INPUT_BY_BUSY | boolean           | TRUE                  |             |
| SYNC_DEPTH          | T_MISC_SYNC_DEPTH | T_MISC_SYNC_DEPTH'low |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| Clock1    | in        | std_logic                           |             |
| Clock2    | in        | std_logic                           |             |
| Input     | in        | std_logic_vector(BITS - 1 downto 0) |             |
| Output    | out       | std_logic_vector(BITS - 1 downto 0) |             |
| Busy      | out       | std_logic_vector(BITS - 1 downto 0) |             |
## Signals
| Name         | Type                                | Description |
| ------------ | ----------------------------------- | ----------- |
| syncClk1_In  | std_logic_vector(BITS - 1 downto 0) |             |
| syncClk1_Out | std_logic_vector(BITS - 1 downto 0) |             |
| syncClk2_In  | std_logic_vector(BITS - 1 downto 0) |             |
| syncClk2_Out | std_logic_vector(BITS - 1 downto 0) |             |
## Instantiations
- syncClk2: PoC.sync_Bits
- syncClk1: PoC.sync_Bits
