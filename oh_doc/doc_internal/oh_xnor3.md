# Entity: oh_xnor3

- **File**: oh_xnor3.v
## Diagram

![Diagram](oh_xnor3.svg "Diagram")
## Description

#############################################################################
# Function: 3-Input Exclusive-NOr Gate                                       #
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
| b         | input     | [DW-1:0] |             |
| c         | input     | [DW-1:0] |             |
| z         | output    | [DW-1:0] |             |
