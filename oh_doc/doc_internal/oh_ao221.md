# Entity: oh_ao221

- **File**: oh_ao221.v
## Diagram

![Diagram](oh_ao221.svg "Diagram")
## Description

#############################################################################
# Function: And-Or (ao221) Gate                                             #
#                                                                           #
# Copyright: OH Project Authors. All rights Reserved.                       #
# License:  MIT (see LICENSE file in OH repository)                         # 
#############################################################################

## Generics

| Generic name | Type | Value | Description   |
| ------------ | ---- | ----- | ------------- |
| DW           |      | 1     |  array width  |
## Ports

| Port name | Direction | Type     | Description |
| --------- | --------- | -------- | ----------- |
| a0        | input     | [DW-1:0] |             |
| a1        | input     | [DW-1:0] |             |
| b0        | input     | [DW-1:0] |             |
| b1        | input     | [DW-1:0] |             |
| c0        | input     | [DW-1:0] |             |
| z         | output    | [DW-1:0] |             |
