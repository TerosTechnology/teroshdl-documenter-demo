# Entity: oh_bin2gray

- **File**: oh_bin2gray.v
## Diagram

![Diagram](oh_bin2gray.svg "Diagram")
## Description

#############################################################################
# Function: Binary to gray encoder                                          #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value | Description            |
| ------------ | ---- | ----- | ---------------------- |
| N            |      | 32    |  width of data inputs  |
## Ports

| Port name | Direction | Type    | Description          |
| --------- | --------- | ------- | -------------------- |
| in        | input     | [N-1:0] | binary encoded input |
| out       | output    | [N-1:0] | gray encoded output  |
## Signals

| Name | Type         | Description |
| ---- | ------------ | ----------- |
| gray | reg [N-1:0]  |             |
| bin  | wire [N-1:0] |             |
| i    | integer      |             |
## Processes
- unnamed: ( @* )
  - **Type:** always
