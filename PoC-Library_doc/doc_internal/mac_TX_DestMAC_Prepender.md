# Entity: mac_TX_DestMAC_Prepender

## Diagram

![Diagram](mac_TX_DestMAC_Prepender.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	TODO
Description:
-------------------------------------
.. TODO:: No documentation available.
License:
=============================================================================
Copyright 2007-2015 Technische Universitaet Dresden - Germany
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
=============================================================================
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

| Name    | Type                                                                                                                                                                                                                                                                                                                                                                | Description |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| T_STATE | ( ST_IDLE,<br><span style="padding-left:20px"> ST_PREPEND_DEST_MAC_1,<br><span style="padding-left:20px"> ST_PREPEND_DEST_MAC_2,<br><span style="padding-left:20px"> ST_PREPEND_DEST_MAC_3,<br><span style="padding-left:20px"> ST_PREPEND_DEST_MAC_4,<br><span style="padding-left:20px"> ST_PREPEND_DEST_MAC_5,<br><span style="padding-left:20px"> ST_PAYLOAD )  |             |
## Processes
- unnamed: ( Clock )
- unnamed: ( State, In_Valid, In_Data, In_EOF, Is_DataFlow, Is_SOF, Is_EOF, Out_Ack, In_Meta_DestMACAddress_Data )
