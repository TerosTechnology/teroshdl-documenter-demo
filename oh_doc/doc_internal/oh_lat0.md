# Entity: oh_lat0

- **File**: oh_lat0.v
## Diagram

![Diagram](oh_lat0.svg "Diagram")
## Description

#############################################################################
# Function: Active Low Latch                                                #
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
| clk       | input     |         | clk         |
| in        | input     | [N-1:0] | input data  |
| out       | output    | [N-1:0] | output data |
