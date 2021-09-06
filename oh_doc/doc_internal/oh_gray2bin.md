# Entity: oh_gray2bin

- **File**: oh_gray2bin.v
## Diagram

![Diagram](oh_gray2bin.svg "Diagram")
## Description

#############################################################################
# Function: Gray to binary encoder                                          #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value | Description            |
| ------------ | ---- | ----- | ---------------------- |
| N            |      | 32    |  width of data inputs  |
## Ports

| Port name | Direction | Type    | Description           |
| --------- | --------- | ------- | --------------------- |
| in        | input     | [N-1:0] | gray encoded input    |
| out       | output    | [N-1:0] | binary encoded output |
## Signals

| Name | Type         | Description |
| ---- | ------------ | ----------- |
| bin  | reg [N-1:0]  |             |
| gray | wire [N-1:0] |             |
| i    | integer      |             |
| j    | integer      |             |
## Processes
- unnamed: ( @* )
  - **Type:** always
