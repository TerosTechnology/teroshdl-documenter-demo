# Entity: oh_csa32

- **File**: oh_csa32.v
## Diagram

![Diagram](oh_csa32.svg "Diagram")
## Description

#############################################################################
# Function: Carry Save Adder (3:2)                                          #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value     | Description              |
| ------------ | ---- | --------- | ------------------------ |
| N            |      | 1         |  vector width            |
| SYN          |      | "TRUE"    |  synthesizable (or not)  |
| TYPE         |      | "DEFAULT" |  scell type/size         |
## Ports

| Port name | Direction | Type    | Description |
| --------- | --------- | ------- | ----------- |
| in0       | input     | [N-1:0] | input       |
| in1       | input     | [N-1:0] | input       |
| in2       | input     | [N-1:0] | input       |
| s         | output    | [N-1:0] | sum         |
| c         | output    | [N-1:0] | carry       |
