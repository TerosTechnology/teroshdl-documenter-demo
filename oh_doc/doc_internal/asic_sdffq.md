# Entity: asic_sdffq

- **File**: asic_sdffq.v
## Diagram

![Diagram](asic_sdffq.svg "Diagram")
## Description

#############################################################################
# Function: Positive edge-triggered static D-type flop-flop with scan input #
#                                                                           #
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
| q         | output    |      |             |
## Processes
- unnamed: ( @ (posedge clk) )
  - **Type:** always
