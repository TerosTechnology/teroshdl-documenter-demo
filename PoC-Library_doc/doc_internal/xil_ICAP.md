# Entity: xil_ICAP
## Diagram
![Diagram](xil_ICAP.svg "Diagram")
## Generics
| Generic name      | Type       | Value      | Description |
| ----------------- | ---------- | ---------- | ----------- |
| ICAP_WIDTH        | string     | "X32"      |             |
| DEVICE_ID         | bit_vector | X"1234567" |             |
| SIM_CFG_FILE_NAME | string     | "NONE"     |             |
## Ports
| Port name | Direction | Type                          | Description |
| --------- | --------- | ----------------------------- | ----------- |
| clk       | in        | std_logic                     |             |
| disable   | in        | std_logic                     |             |
| rd_wr     | in        | std_logic                     |             |
| busy      | out       | std_logic                     |             |
| data_in   | in        | std_logic_vector(31 downto 0) |             |
| data_out  | out       | std_logic_vector(31 downto 0) |             |
## Constants
| Name     | Type          | Value        | Description |
| -------- | ------------- | ------------ | ----------- |
| DEV_INFO | T_DEVICE_INFO |  DEVICE_INFO |             |
