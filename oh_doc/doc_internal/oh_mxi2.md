# Entity: oh_mxi2

- **File**: oh_mxi2.v
## Diagram

![Diagram](oh_mxi2.svg "Diagram")
## Description

#############################################################################
# Function: 2-Input Inverting Mux                                           #
#                                                                           #
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
| d0        | input     | [DW-1:0] |             |
| d1        | input     | [DW-1:0] |             |
| s         | input     | [DW-1:0] |             |
| z         | output    | [DW-1:0] |             |
