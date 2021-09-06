# Entity: asic_dffsqn

- **File**: asic_dffsqn.v
## Diagram

![Diagram](asic_dffsqn.svg "Diagram")
## Description

#############################################################################
# Function:  Positive edge-triggered static inverting D-type flop-flop with #
             async active low set.                                          #
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
| nset      | input     |      |             |
| qn        | output    |      |             |
## Processes
- unnamed: ( @ (posedge clk or negedge nset) )
  - **Type:** always
