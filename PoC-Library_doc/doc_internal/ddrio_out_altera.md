# Entity: ddrio_out_altera
## Diagram
![Diagram](ddrio_out_altera.svg "Diagram")
## Generics
| Generic name     | Type       | Value       | Description |
| ---------------- | ---------- | ----------- | ----------- |
| NO_OUTPUT_ENABLE | boolean    | false       |             |
| BITS             | positive   |             |             |
| INIT_VALUE       | bit_vector | x"FFFFFFFF" |             |
## Ports
| Port name    | Direction | Type                                | Description |
| ------------ | --------- | ----------------------------------- | ----------- |
| Clock        | in        | std_logic                           |             |
| ClockEnable  | in        | std_logic                           |             |
| OutputEnable | in        | std_logic                           |             |
| DataOut_high | in        | std_logic_vector(BITS - 1 downto 0) |             |
| DataOut_low  | in        | std_logic_vector(BITS - 1 downto 0) |             |
| Pad          | out       | std_logic_vector(BITS - 1 downto 0) |             |
## Signals
| Name | Type      | Description |
| ---- | --------- | ----------- |
| oe   | std_logic |             |
