# Entity: asic_dffrqn

- **File**: asic_dffrqn.v
## Diagram

![Diagram](asic_dffrqn.svg "Diagram")
## Description

#############################################################################
# Function:  Positive edge-triggered static inverting D-type flop-flop with #
             async active low reset.                                        #
# Copyright: OH Project Authors. ALl rights Reserved.                       #
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
| qn        | output    |      |             |
## Processes
- unnamed: ( @ (posedge clk or negedge nreset) )
  - **Type:** always
