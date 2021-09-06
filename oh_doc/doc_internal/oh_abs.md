# Entity: oh_abs

- **File**: oh_abs.v
## Diagram

![Diagram](oh_abs.svg "Diagram")
## Description

#############################################################################
# Function: Calculates absolute value of input                              #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value     | Description           |
| ------------ | ---- | --------- | --------------------- |
| N            |      | 32        |  block width          |
| SYN          |      | "TRUE"    |  synthesizable        |
| TYPE         |      | "DEFAULT" |  implementation type  |
## Ports

| Port name | Direction | Type    | Description                             |
| --------- | --------- | ------- | --------------------------------------- |
| in        | input     | [N-1:0] | input operand                           |
| out       | output    | [N-1:0] | out = abs(in) (signed two's complement) |
| overflow  | output    |         | high for max negative #                 |
