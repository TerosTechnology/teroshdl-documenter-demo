# Entity: ddrio_in_xilinx
## Diagram
![Diagram](ddrio_in_xilinx.svg "Diagram")
## Generics
| Generic name | Type       | Value       | Description |
| ------------ | ---------- | ----------- | ----------- |
| BITS         | positive   |             |             |
| INIT_VALUE   | bit_vector | x"FFFFFFFF" |             |
## Ports
| Port name   | Direction | Type                                | Description |
| ----------- | --------- | ----------------------------------- | ----------- |
| Clock       | in        | std_logic                           |             |
| ClockEnable | in        | std_logic                           |             |
| DataIn_high | out       | std_logic_vector(BITS - 1 downto 0) |             |
| DataIn_low  | out       | std_logic_vector(BITS - 1 downto 0) |             |
| Pad         | in        | std_logic_vector(BITS - 1 downto 0) |             |
