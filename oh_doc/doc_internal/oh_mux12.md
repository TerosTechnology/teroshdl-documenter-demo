# Entity: oh_mux12

- **File**: oh_mux12.v
## Diagram

![Diagram](oh_mux12.svg "Diagram")
## Description

#############################################################################
# Function: 12:1 one hot mux                                                #
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
| sel11     | input     |         |                      |
| sel10     | input     |         |                      |
| sel9      | input     |         |                      |
| sel8      | input     |         |                      |
| sel7      | input     |         |                      |
| sel6      | input     |         |                      |
| sel5      | input     |         |                      |
| sel4      | input     |         |                      |
| sel3      | input     |         |                      |
| sel2      | input     |         |                      |
| sel1      | input     |         |                      |
| sel0      | input     |         |                      |
| in11      | input     | [N-1:0] |                      |
| in10      | input     | [N-1:0] |                      |
| in9       | input     | [N-1:0] |                      |
| in8       | input     | [N-1:0] |                      |
| in7       | input     | [N-1:0] |                      |
| in6       | input     | [N-1:0] |                      |
| in5       | input     | [N-1:0] |                      |
| in4       | input     | [N-1:0] |                      |
| in3       | input     | [N-1:0] |                      |
| in2       | input     | [N-1:0] |                      |
| in1       | input     | [N-1:0] |                      |
| in0       | input     | [N-1:0] |                      |
| out       | output    | [N-1:0] | selected data output |
