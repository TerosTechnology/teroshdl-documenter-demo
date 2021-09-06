# Entity: oh_dffqn

- **File**: oh_dffqn.v
## Diagram

![Diagram](oh_dffqn.svg "Diagram")
## Description

#############################################################################
# Function: Positive edge-triggered inverting static D-type flop-flop       #
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
| qn        | output    | [DW-1:0] |             |
## Processes
- unnamed: ( @ (posedge clk) )
  - **Type:** always
