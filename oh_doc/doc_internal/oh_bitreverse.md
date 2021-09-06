# Entity: oh_bitreverse

- **File**: oh_bitreverse.v
## Diagram

![Diagram](oh_bitreverse.svg "Diagram")
## Description

#############################################################################
# Function: Binary to one hot encoder                                       #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value | Description            |
| ------------ | ---- | ----- | ---------------------- |
| N            |      | 32    |  width of data inputs  |
## Ports

| Port name | Direction | Type    | Description         |
| --------- | --------- | ------- | ------------------- |
| in        | input     | [N-1:0] | data input          |
| out       | output    | [N-1:0] | bit reversed output |
