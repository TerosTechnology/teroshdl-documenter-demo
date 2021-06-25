# Entity: xil_BSCAN
## Diagram
![Diagram](xil_BSCAN.svg "Diagram")
## Generics
| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| JTAG_CHAIN   | natural |       |             |
| DISABLE_JTAG | boolean | FALSE |             |
## Ports
| Port name       | Direction | Type      | Description |
| --------------- | --------- | --------- | ----------- |
| Reset           | out       | std_logic |             |
| RunTest         | out       | std_logic |             |
| Sel             | out       | std_logic |             |
| Capture         | out       | std_logic |             |
| drck            | out       | std_logic |             |
| Shift           | out       | std_logic |             |
| Test_Clock      | out       | std_logic |             |
| Test_DataIn     | out       | std_logic |             |
| Test_DataOut    | in        | std_logic |             |
| Test_ModeSelect | out       | std_logic |             |
| Update          | out       | std_logic |             |
## Constants
| Name     | Type          | Value        | Description |
| -------- | ------------- | ------------ | ----------- |
| DEV_INFO | T_DEVICE_INFO |  DEVICE_INFO |             |
