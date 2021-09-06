# Entity: oh_isobufhi

- **File**: oh_isobufhi.v
## Diagram

![Diagram](oh_isobufhi.svg "Diagram")
## Description

#############################################################################
# Function: Isolation buffer (high) for multi supply domains                #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT  (see LICENSE file in OH! repository)                       #
#############################################################################

## Generics

| Generic name | Type | Value     | Description            |
| ------------ | ---- | --------- | ---------------------- |
| N            |      | 1         |  width of data inputs  |
| SYN          |      | "TRUE"    |  true=synthesizable    |
| TYPE         |      | "DEFAULT" |  scell type/size       |
## Ports

| Port name | Direction | Type    | Description                 |
| --------- | --------- | ------- | --------------------------- |
| iso       | input     |         | active low isolation signal |
| in        | input     | [N-1:0] | input signal                |
| out       | output    | [N-1:0] | out = iso | in              |
