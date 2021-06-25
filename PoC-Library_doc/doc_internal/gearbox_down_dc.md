# Entity: gearbox_down_dc
## Diagram
![Diagram](gearbox_down_dc.svg "Diagram")
## Generics
| Generic name         | Type        | Value     | Description |
| -------------------- | ----------- | --------- | ----------- |
| INPUT_BITS           | positive    | 32        |             |
| OUTPUT_BITS          | positive    | 8         |             |
| OUTPUT_ORDER         | T_BIT_ORDER | LSB_FIRST |             |
| ADD_INPUT_REGISTERS  | boolean     | FALSE     |             |
| ADD_OUTPUT_REGISTERS | boolean     | FALSE     |             |
## Ports
| Port name | Direction | Type                                       | Description |
| --------- | --------- | ------------------------------------------ | ----------- |
| Clock1    | in        | std_logic                                  |             |
| Clock2    | in        | std_logic                                  |             |
| In_Data   | in        | std_logic_vector(INPUT_BITS - 1 downto 0)  |             |
| Out_Data  | out       | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
## Signals
| Name           | Type                                       | Description |
| -------------- | ------------------------------------------ | ----------- |
| WordBoundary   | std_logic                                  |             |
| WordBoundary_d | std_logic                                  |             |
| Align          | std_logic                                  |             |
| Data_d         | std_logic_vector(INPUT_BITS - 1 downto 0)  |             |
| DataIn         | std_logic_vector(INPUT_BITS - 1 downto 0)  |             |
| DataOut_d      | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| MuxInput       | T_MUX_INPUT(2**COUNTER_BITS - 1 downto 0)  |             |
| MuxOutput      | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| MuxCounter_us  | unsigned(COUNTER_BITS - 1 downto 0)        |             |
| MuxSelect_us   | unsigned(COUNTER_BITS - 1 downto 0)        |             |
## Constants
| Name         | Type     | Value                                 | Description |
| ------------ | -------- | ------------------------------------- | ----------- |
| BIT_RATIO    | REAL     |  real(INPUT_BITS) / real(OUTPUT_BITS) |             |
| COUNTER_BITS | positive |  log2ceil(integer(BIT_RATIO))         |             |
## Types
| Name        | Type | Description |
| ----------- | ---- | ----------- |
| T_MUX_INPUT |      |             |
