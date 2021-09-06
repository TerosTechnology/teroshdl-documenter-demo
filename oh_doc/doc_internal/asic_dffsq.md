# Entity: asic_dffsq

- **File**: asic_dffsq.v
## Diagram

![Diagram](asic_dffsq.svg "Diagram")
## Description

#############################################################################
# Function:  Positive edge-triggered static D-type flop-flop with async     #
#            active low preset.                                             #
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
| q         | output    |      |             |
## Processes
- unnamed: ( @ (posedge clk or negedge nset) )
  - **Type:** always
