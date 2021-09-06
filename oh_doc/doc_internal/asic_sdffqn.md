# Entity: asic_sdffqn

- **File**: asic_sdffqn.v
## Diagram

![Diagram](asic_sdffqn.svg "Diagram")
## Description

#############################################################################
# Function: Positive edge-triggered inverting static D-type flop-flop       #
#           with scan input.                                                #
# Copyright: OH Project Authors. ALl rights Reserved.                       #
# License:  MIT (see LICENSE file in OH repository)                         #
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
| qn        | output    |      |             |
## Processes
- unnamed: ( @ (posedge clk) )
  - **Type:** always
