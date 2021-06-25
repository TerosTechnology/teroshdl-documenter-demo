# Entity: mac_TX_DestMAC_Prepender
## Diagram
![Diagram](mac_TX_DestMAC_Prepender.svg "Diagram")
## Generics
| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DEBUG        | boolean | FALSE |             |
## Ports
| Port name                   | Direction | Type      | Description |
| --------------------------- | --------- | --------- | ----------- |
| Clock                       | in        | std_logic |             |
| Reset                       | in        | std_logic |             |
| In_Valid                    | in        | std_logic |             |
| In_Data                     | in        | T_SLV_8   |             |
| In_SOF                      | in        | std_logic |             |
| In_EOF                      | in        | std_logic |             |
| In_Ack                      | out       | std_logic |             |
| In_Meta_rst                 | out       | std_logic |             |
| In_Meta_DestMACAddress_nxt  | out       | std_logic |             |
| In_Meta_DestMACAddress_Data | in        | T_SLV_8   |             |
| Out_Valid                   | out       | std_logic |             |
| Out_Data                    | out       | T_SLV_8   |             |
| Out_SOF                     | out       | std_logic |             |
| Out_EOF                     | out       | std_logic |             |
| Out_Ack                     | in        | std_logic |             |
## Signals
| Name        | Type      | Description |
| ----------- | --------- | ----------- |
| State       | T_STATE   |             |
| NextState   | T_STATE   |             |
| Is_DataFlow | std_logic |             |
| Is_SOF      | std_logic |             |
| Is_EOF      | std_logic |             |
## Types
| Name    | Type                                                                                                                                                            | Description |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| T_STATE | ( 		ST_IDLE, 			ST_PREPEND_DEST_MAC_1, 			ST_PREPEND_DEST_MAC_2, 			ST_PREPEND_DEST_MAC_3, 			ST_PREPEND_DEST_MAC_4, 			ST_PREPEND_DEST_MAC_5, 			ST_PAYLOAD 	) |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( State, In_Valid, In_Data, In_EOF, Is_DataFlow, Is_SOF, Is_EOF, Out_Ack, In_Meta_DestMACAddress_Data )_

