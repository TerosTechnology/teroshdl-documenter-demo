# Entity: asic_sdffsq

- **File**: asic_sdffsq.v
## Diagram

![Diagram](asic_sdffsq.svg "Diagram")
## Description

#############################################################################
# Function:  Positive edge-triggered static D-type flop-flop with async     #
#            active low preset and scan input.                              #
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
| q         | output    |      |             |
## Processes
- unnamed: ( @ (posedge clk or negedge nset) )
  - **Type:** always
