# Entity: oh_bin2onehot

- **File**: oh_bin2onehot.v
## Diagram

![Diagram](oh_bin2onehot.svg "Diagram")
## Description

#############################################################################
# Function: Binary to one hot encoder                                       #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value     | Description            |
| ------------ | ---- | --------- | ---------------------- |
| N            |      | 2         |  output vector width   |
| NB           |      | $clog2(N) |  binary encoded input  |
## Ports

| Port name | Direction | Type     | Description           |
| --------- | --------- | -------- | --------------------- |
| in        | input     | [NB-1:0] | unsigned binary input |
| out       | output    | [N-1:0]  | one hot output vector |
