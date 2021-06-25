# Entity: sync_Pulse_Xilinx
## Diagram
![Diagram](sync_Pulse_Xilinx.svg "Diagram")
## Generics
| Generic name | Type              | Value | Description |
| ------------ | ----------------- | ----- | ----------- |
| BITS         | positive          | 1     |             |
| SYNC_DEPTH   | T_MISC_SYNC_DEPTH | 2     |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| Clock     | in        | std_logic                           |             |
| Input     | in        | std_logic_vector(BITS - 1 downto 0) |             |
| Output    | out       | std_logic_vector(BITS - 1 downto 0) |             |
## Signals
| Name           | Type                                | Description |
| -------------- | ----------------------------------- | ----------- |
| Captured_async | std_logic_vector(BITS - 1 downto 0) |             |
| Input_sync     | std_logic_vector(BITS - 1 downto 0) |             |
## Constants
| Name   | Type       | Value                   | Description |
| ------ | ---------- | ----------------------- | ----------- |
| INIT_I | bit_vector |  (0 to BITS - 1 => '0') |             |
## Instantiations
- Sync: PoC.sync_Bits_Xilinx
