# Entity: oh_inv

- **File**: oh_inv.v
## Diagram

![Diagram](oh_inv.svg "Diagram")
## Description

#############################################################################
# Function: Inverter                                                        #
# Copyright: OH Project Authors. ALl rights Reserved.                       #
# License:  MIT (see LICENSE file in OH repository)                         # 
#############################################################################

## Generics

| Generic name | Type | Value | Description   |
| ------------ | ---- | ----- | ------------- |
| DW           |      | 1     |  array width  |
## Ports

| Port name | Direction | Type     | Description |
| --------- | --------- | -------- | ----------- |
| a         | input     | [DW-1:0] |             |
| z         | output    | [DW-1:0] |             |
