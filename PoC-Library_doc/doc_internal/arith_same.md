# Entity: arith_same
## Diagram
![Diagram](arith_same.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| N            | positive |       |             |
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| g         | in        | std_logic                      |             |
| x         | in        | std_logic_vector(N-1 downto 0) |             |
| y         | out       | std_logic                      |             |
## Signals
| Name | Type                           | Description |
| ---- | ------------------------------ | ----------- |
| p    | std_logic_vector(M-1 downto 0) |             |
## Constants
| Name     | Type          | Value                | Description |
| -------- | ------------- | -------------------- | ----------- |
| DEV_INFO | T_DEVICE_INFO |  DEVICE_INFO         |             |
| K        | positive      |  DEV_INFO.LUT_FanIn  |             |
| M        | positive      |  (N-2+1/N)/(K-1) + 1 |             |
