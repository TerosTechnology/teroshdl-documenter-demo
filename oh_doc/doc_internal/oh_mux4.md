# Entity: oh_mux4

- **File**: oh_mux4.v
## Diagram

![Diagram](oh_mux4.svg "Diagram")
## Description

#############################################################################
# Function: 4:1 one hot mux                                                 #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value | Description    |
| ------------ | ---- | ----- | -------------- |
| N            |      | 1     |  width of mux  |
## Ports

| Port name | Direction | Type    | Description          |
| --------- | --------- | ------- | -------------------- |
| sel3      | input     |         |                      |
| sel2      | input     |         |                      |
| sel1      | input     |         |                      |
| sel0      | input     |         |                      |
| in3       | input     | [N-1:0] |                      |
| in2       | input     | [N-1:0] |                      |
| in1       | input     | [N-1:0] |                      |
| in0       | input     | [N-1:0] |                      |
| out       | output    | [N-1:0] | selected data output |
## Signals

| Name  | Type | Description |
| ----- | ---- | ----------- |
| error | wire |             |
## Processes
- unnamed: ( @ (posedge error) )
  - **Type:** always
