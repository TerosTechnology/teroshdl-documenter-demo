# Entity: asic_dffq

- **File**: asic_dffq.v
## Diagram

![Diagram](asic_dffq.svg "Diagram")
## Description

#############################################################################
# Function: Positive edge-triggered static D-type flop-flop                 #
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
| clk       | input     |      |             |
| q         | output    |      |             |
## Processes
- unnamed: ( @ (posedge clk) )
  - **Type:** always
