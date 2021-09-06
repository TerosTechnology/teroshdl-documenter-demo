# Entity: asic_dffnq

- **File**: asic_dffnq.v
## Diagram

![Diagram](asic_dffnq.svg "Diagram")
## Description

#############################################################################
# Function: Negative edge-triggered static D-type flop-flop                 #
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
- unnamed: ( @ (negedge clk) )
  - **Type:** always
