# Entity: asic_dffrq

- **File**: asic_dffrq.v
## Diagram

![Diagram](asic_dffrq.svg "Diagram")
## Description

#############################################################################
# Function:  Positive edge-triggered static D-type flop-flop with async     #
#            active low reset.                                              #
# Copyright: OH Project Authors. All rights Reserved.                       #
# License:   MIT (see LICENSE file in OH repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value     | Description |
| ------------ | ---- | --------- | ----------- |
| PROP         |      | "DEFAULT" |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| d         | input     |      |             |
| clk       | input     |      |             |
| nreset    | input     |      |             |
| q         | output    |      |             |
## Processes
- unnamed: ( @ (posedge clk or negedge nreset) )
  - **Type:** always
