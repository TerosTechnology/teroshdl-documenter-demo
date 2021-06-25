# Entity: xil_SystemMonitor
## Diagram
![Diagram](xil_SystemMonitor.svg "Diagram")
## Ports
| Port name      | Direction | Type      | Description |
| -------------- | --------- | --------- | ----------- |
| Reset          | in        | std_logic |             |
| Alarm_UserTemp | out       | std_logic |             |
| Alarm_OverTemp | out       | std_logic |             |
| Alarm          | out       | std_logic |             |
| VP             | in        | std_logic |             |
| VN             | in        | std_logic |             |
## Signals
| Name          | Type                          | Description |
| ------------- | ----------------------------- | ----------- |
| aux_channel_p | std_logic_vector(15 downto 0) |             |
| aux_channel_n | std_logic_vector(15 downto 0) |             |
