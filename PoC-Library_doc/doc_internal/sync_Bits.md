# Entity: sync_Bits
## Diagram
![Diagram](sync_Bits.svg "Diagram")
## Generics
| Generic name | Type              | Value                 | Description |
| ------------ | ----------------- | --------------------- | ----------- |
| BITS         | positive          | 1                     |             |
| INIT         | std_logic_vector  | x"00000000"           |             |
| SYNC_DEPTH   | T_MISC_SYNC_DEPTH | T_MISC_SYNC_DEPTH'low |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| Clock     | in        | std_logic                           |             |
| Input     | in        | std_logic_vector(BITS - 1 downto 0) |             |
| Output    | out       | std_logic_vector(BITS - 1 downto 0) |             |
## Constants
| Name     | Type             | Value                        | Description |
| -------- | ---------------- | ---------------------------- | ----------- |
| INIT_I   | std_logic_vector |  resize(descend(INIT), BITS) |             |
| DEV_INFO | T_DEVICE_INFO    |  DEVICE_INFO                 |             |
