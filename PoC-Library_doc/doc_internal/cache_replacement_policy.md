# Entity: cache_replacement_policy
## Diagram
![Diagram](cache_replacement_policy.svg "Diagram")
## Generics
| Generic name       | Type     | Value | Description |
| ------------------ | -------- | ----- | ----------- |
| REPLACEMENT_POLICY | string   | "LRU" |             |
| CACHE_WAYS         | positive | 32    |             |
## Ports
| Port name  | Direction | Type                                                  | Description |
| ---------- | --------- | ----------------------------------------------------- | ----------- |
| Clock      | in        | std_logic                                             |             |
| Reset      | in        | std_logic                                             |             |
| Replace    | in        | std_logic                                             |             |
| ReplaceWay | out       | std_logic_vector(log2ceilnz(CACHE_WAYS) - 1 downto 0) |             |
| TagAccess  | in        | std_logic                                             |             |
| ReadWrite  | in        | std_logic                                             |             |
| Invalidate | in        | std_logic                                             |             |
| HitWay     | in        | std_logic_vector(log2ceilnz(CACHE_WAYS) - 1 downto 0) |             |
## Constants
| Name     | Type     | Value                   | Description |
| -------- | -------- | ----------------------- | ----------- |
| KEY_BITS | positive |  log2ceilnz(CACHE_WAYS) |             |
