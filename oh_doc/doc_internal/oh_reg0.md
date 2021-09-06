# Entity: ohr_reg0

- **File**: oh_reg0.v
## Diagram

![Diagram](oh_reg0.svg "Diagram")
## Description

#############################################################################
# Function: Falling Edge Sampled Register                                   #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value | Description  |
| ------------ | ---- | ----- | ------------ |
| N            |      | 1     |  data width  |
## Ports

| Port name | Direction | Type    | Description                             |
| --------- | --------- | ------- | --------------------------------------- |
| nreset    | input     |         | async active low reset                  |
| clk       | input     |         | clk, latch when clk=0                   |
| in        | input     | [N-1:0] | input data                              |
| out       | output    | [N-1:0] | output data (stable/latched when clk=1) |
## Signals

| Name    | Type        | Description |
| ------- | ----------- | ----------- |
| out_reg | reg [N-1:0] |             |
## Processes
- unnamed: ( @ (negedge clk or negedge nreset) )
  - **Type:** always
