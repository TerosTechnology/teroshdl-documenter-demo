# Entity: oh_csa92

- **File**: oh_csa92.v
## Diagram

![Diagram](oh_csa92.svg "Diagram")
## Description

#############################################################################
# Function: Carry Save Adder (9:2)                                          #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value     | Description              |
| ------------ | ---- | --------- | ------------------------ |
| N            |      | 1         |  number of sync stages   |
| SYN          |      | "TRUE"    |  synthesizable (or not)  |
| TYPE         |      | "DEFAULT" |  scell type/size         |
## Ports

| Port name | Direction | Type    | Description |
| --------- | --------- | ------- | ----------- |
| in0       | input     | [N-1:0] | input       |
| in1       | input     | [N-1:0] | input       |
| in2       | input     | [N-1:0] | input       |
| in3       | input     | [N-1:0] | input       |
| in4       | input     | [N-1:0] | input       |
| in5       | input     | [N-1:0] | input       |
| in6       | input     | [N-1:0] | input       |
| in7       | input     | [N-1:0] | input       |
| in8       | input     | [N-1:0] | input       |
| cin0      | input     | [N-1:0] | carry in    |
| cin1      | input     | [N-1:0] | carry in    |
| cin2      | input     | [N-1:0] | carry in    |
| cin3      | input     | [N-1:0] | carry in    |
| cin4      | input     | [N-1:0] | carry in    |
| cin5      | input     | [N-1:0] | carry in    |
| s         | output    | [N-1:0] | sum         |
| c         | output    | [N-1:0] | carry       |
| cout0     | output    | [N-1:0] | carry out   |
| cout1     | output    | [N-1:0] | carry out   |
| cout2     | output    | [N-1:0] | carry out   |
| cout3     | output    | [N-1:0] | carry out   |
| cout4     | output    | [N-1:0] | carry out   |
| cout5     | output    | [N-1:0] | carry out   |
## Signals

| Name   | Type         | Description |
| ------ | ------------ | ----------- |
| s_int0 | wire [N-1:0] |             |
| s_int1 | wire [N-1:0] |             |
| s_int2 | wire [N-1:0] |             |
