# Entity: oh_datagate

- **File**: oh_datagate.v
## Diagram

![Diagram](oh_datagate.svg "Diagram")
## Description

#############################################################################
# Function: Low power data gate                                             #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################


## Generics

| Generic name | Type | Value     | Description              |
| ------------ | ---- | --------- | ------------------------ |
| N            |      | 2         |  number of sync stages   |
| SYN          |      | "TRUE"    |  synthesizable (or not)  |
| TYPE         |      | "DEFAULT" |  scell type/size         |
## Ports

| Port name | Direction | Type    | Description |
| --------- | --------- | ------- | ----------- |
| clk       | input     |         | clock       |
| en        | input     |         | data valid  |
| in        | input     | [N-1:0] | data input  |
| out       | output    | [N-1:0] | data output |
