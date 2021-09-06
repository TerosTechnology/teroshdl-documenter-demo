# Entity: oh_edge2pulse

- **File**: oh_edge2pulse.v
## Diagram

![Diagram](oh_edge2pulse.svg "Diagram")
## Description

#############################################################################
# Function: Converts an edge to a single cycle pulse                        #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value | Description            |
| ------------ | ---- | ----- | ---------------------- |
| N            |      | 1     |  width of data inputs  |
## Ports

| Port name | Direction | Type    | Description            |
| --------- | --------- | ------- | ---------------------- |
| clk       | input     |         | clock                  |
| nreset    | input     |         | async active low reset |
| in        | input     | [N-1:0] | edge input             |
| out       | output    | [N-1:0] | one cycle pulse        |
## Signals

| Name   | Type        | Description |
| ------ | ----------- | ----------- |
| in_reg | reg [N-1:0] |             |
## Processes
- unnamed: ( @ (posedge clk or negedge nreset) )
  - **Type:** always
