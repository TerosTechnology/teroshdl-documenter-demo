# Entity: sortnet_MergeSort_Streamed
## Diagram
![Diagram](sortnet_MergeSort_Streamed.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| FIFO_DEPTH   | positive | 32    |             |
| KEY_BITS     | positive | 32    |             |
| DATA_BITS    | positive | 32    |             |
## Ports
| Port name | Direction | Type                                     | Description |
| --------- | --------- | ---------------------------------------- | ----------- |
| Clock     | in        | std_logic                                |             |
| Reset     | in        | std_logic                                |             |
| Inverse   | in        | std_logic                                |             |
| In_Valid  | in        | std_logic                                |             |
| In_Data   | in        | std_logic_vector(DATA_BITS - 1 downto 0) |             |
| In_SOF    | in        | std_logic                                |             |
| In_IsKey  | in        | std_logic                                |             |
| In_EOF    | in        | std_logic                                |             |
| In_Ack    | out       | std_logic                                |             |
| Out_Sync  | out       | std_logic                                |             |
| Out_Valid | out       | std_logic                                |             |
| Out_Data  | out       | std_logic_vector(DATA_BITS - 1 downto 0) |             |
| Out_SOF   | out       | std_logic                                |             |
| Out_IsKey | out       | std_logic                                |             |
| Out_EOF   | out       | std_logic                                |             |
| Out_Ack   | in        | std_logic                                |             |
## Signals
| Name           | Type        | Description |
| -------------- | ----------- | ----------- |
| FIFO_sel_r     | std_logic   |             |
| FIFO_0_put     | std_logic   |             |
| FIFO_0_DataIn  | T_FIFO_DATA |             |
| FIFO_0_Full    | std_logic   |             |
| FIFO_0_got     | std_logic   |             |
| FIFO_0_DataOut | T_FIFO_DATA |             |
| FIFO_0_Valid   | std_logic   |             |
| FIFO_1_put     | std_logic   |             |
| FIFO_1_DataIn  | T_FIFO_DATA |             |
| FIFO_1_Full    | std_logic   |             |
| FIFO_1_got     | std_logic   |             |
| FIFO_1_DataOut | T_FIFO_DATA |             |
| FIFO_1_Valid   | std_logic   |             |
| Greater        | std_logic   |             |
| Switch_d       | std_logic   |             |
| Switch_en      | std_logic   |             |
| Switch_r       | std_logic   |             |
| Switch         | std_logic   |             |
| State          | T_STATE     |             |
| NextState      | T_STATE     |             |
## Constants
| Name           | Type     | Value          | Description |
| -------------- | -------- | -------------- | ----------- |
| DATA_SOF_BIT   | natural  |  DATA_BITS + 0 |             |
| DATA_ISKEY_BIT | natural  |  DATA_BITS + 1 |             |
| DATA_EOF_BIT   | natural  |  DATA_BITS + 2 |             |
| FIFO_BITS      | positive |  DATA_BITS + 3 |             |
## Types
| Name    | Type                                                  | Description |
| ------- | ----------------------------------------------------- | ----------- |
| T_STATE | (ST_IDLE, ST_MERGE, ST_EMPTY_FIFO_0, ST_EMPTY_FIFO_1) |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( State, FIFO_0_Valid, FIFO_0_DataOut, FIFO_1_Valid, FIFO_1_DataOut, Switch, Out_Ack )_

## Instantiations
- FIFO_0: PoC.fifo_cc_got
- FIFO_1: PoC.fifo_cc_got
