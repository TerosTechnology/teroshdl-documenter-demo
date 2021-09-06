# Entity: oh_buf

- **File**: oh_buf.v
## Diagram

![Diagram](oh_buf.svg "Diagram")
## Description

#############################################################################
# Function: Non-inverting Buffer                                            #
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
