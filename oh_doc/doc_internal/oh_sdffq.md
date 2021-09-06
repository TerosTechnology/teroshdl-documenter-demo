# Entity: oh_sdffq

- **File**: oh_sdffq.v
## Diagram

![Diagram](oh_sdffq.svg "Diagram")
## Description

#############################################################################
# Function: Positive edge-triggered static D-type flop-flop with scan input #
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
| d         | input     | [DW-1:0] |             |
| si        | input     | [DW-1:0] |             |
| se        | input     | [DW-1:0] |             |
| clk       | input     | [DW-1:0] |             |
| q         | output    | [DW-1:0] |             |
## Processes
- unnamed: ( @ (posedge clk) )
  - **Type:** always
