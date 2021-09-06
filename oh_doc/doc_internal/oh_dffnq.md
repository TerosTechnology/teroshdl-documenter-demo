# Entity: oh_dffnq

- **File**: oh_dffnq.v
## Diagram

![Diagram](oh_dffnq.svg "Diagram")
## Description

#############################################################################
# Function: Negative edge-triggered static D-type flop-flop                 #
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
| d         | input     | [DW-1:0] |             |
| clk       | input     | [DW-1:0] |             |
| q         | output    | [DW-1:0] |             |
## Processes
- unnamed: ( @ (negedge clk) )
  - **Type:** always
