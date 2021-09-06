# Entity: oh_rise2pulse

- **File**: oh_rise2pulse.v
## Diagram

![Diagram](oh_rise2pulse.svg "Diagram")
## Description

#############################################################################
# Function: Converts a rising edge to a single cycle pulse                  #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value | Description  |
| ------------ | ---- | ----- | ------------ |
| N            |      | 1     |  data width  |
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
