# Entity: oh_dffrqn

- **File**: oh_dffrqn.v
## Diagram

![Diagram](oh_dffrqn.svg "Diagram")
## Description

#############################################################################
# Function:  Positive edge-triggered static inverting D-type flop-flop with #
             async active low reset.                                        # 
# Copyright: OH Project Authors. ALl rights Reserved.                       #
# License:   MIT (see LICENSE file in OH repository)                        # 
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
| nreset    | input     | [DW-1:0] |             |
| qn        | output    | [DW-1:0] |             |
## Processes
- unnamed: ( @ (posedge clk or negedge nreset) )
  - **Type:** always
