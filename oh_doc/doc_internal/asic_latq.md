# Entity: asic_latq

- **File**: asic_latq.v
## Diagram

![Diagram](asic_latq.svg "Diagram")
## Description

#############################################################################
# Function:  D-type active-high transparent latch                           #
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
| q         | output    |      |             |
## Processes
- unnamed: ( @ (clk or d) )
  - **Type:** always
