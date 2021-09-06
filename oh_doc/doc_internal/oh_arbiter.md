# Entity: oh_arbiter

- **File**: oh_arbiter.v
## Diagram

![Diagram](oh_arbiter.svg "Diagram")
## Description

#############################################################################
# Function: Statically configured arbiter                                   #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value   | Description           |
| ------------ | ---- | ------- | --------------------- |
| N            |      | 1       |                       |
| TYPE         |      | "FIXED" |  or ROUNDROBIN, FAIR  |
## Ports

| Port name | Direction | Type    | Description     |
| --------- | --------- | ------- | --------------- |
| requests  | input     | [N-1:0] | request vector  |
| grants    | output    | [N-1:0] | grant (one hot) |
## Signals

| Name     | Type         | Description |
| -------- | ------------ | ----------- |
| waitmask | wire [N-1:0] |             |
