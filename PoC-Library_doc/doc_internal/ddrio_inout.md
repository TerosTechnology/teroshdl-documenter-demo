# Entity: ddrio_inout
## Diagram
![Diagram](ddrio_inout.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| BITS         | positive |       |             |
## Ports
| Port name      | Direction | Type                                | Description |
| -------------- | --------- | ----------------------------------- | ----------- |
| ClockOut       | in        | std_logic                           |             |
| ClockOutEnable | in        | std_logic                           |             |
| OutputEnable   | in        | std_logic                           |             |
| DataOut_high   | in        | std_logic_vector(BITS - 1 downto 0) |             |
| DataOut_low    | in        | std_logic_vector(BITS - 1 downto 0) |             |
| ClockIn        | in        | std_logic                           |             |
| ClockInEnable  | in        | std_logic                           |             |
| DataIn_high    | out       | std_logic_vector(BITS - 1 downto 0) |             |
| DataIn_low     | out       | std_logic_vector(BITS - 1 downto 0) |             |
| Pad            | inout     | std_logic_vector(BITS - 1 downto 0) |             |
