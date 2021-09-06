# Entity: asic_latnq

- **File**: asic_latnq.v
## Diagram

![Diagram](asic_latnq.svg "Diagram")
## Description

#############################################################################
# Function:  D-type active-low transparent latch                            #
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
