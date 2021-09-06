# Entity: oh_reg1

- **File**: oh_reg1.v
## Diagram

![Diagram](oh_reg1.svg "Diagram")
## Description

#############################################################################
# Function: Rising Edge Sampled Register                                    #
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

| Port name | Direction | Type    | Description                             |
| --------- | --------- | ------- | --------------------------------------- |
| nreset    | input     |         | async active low reset                  |
| clk       | input     |         | clk                                     |
| en        | input     |         | write enable                            |
| in        | input     | [N-1:0] | input data                              |
| out       | output    | [N-1:0] | output data (stable/latched when clk=1) |
