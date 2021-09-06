# Entity: asic_sdffsqn

- **File**: asic_sdffsqn.v
## Diagram

![Diagram](asic_sdffsqn.svg "Diagram")
## Description

#############################################################################
# Function:  Positive edge-triggered static inverting D-type flop-flop with #
             async active low set and scan input                            #
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
| si        | input     |      |             |
| se        | input     |      |             |
| clk       | input     |      |             |
| nset      | input     |      |             |
| qn        | output    |      |             |
## Processes
- unnamed: ( @ (posedge clk or negedge nset) )
  - **Type:** always
