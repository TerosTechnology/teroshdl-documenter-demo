# Entity: oh_pwr_buf

- **File**: oh_pwr_buf.v
## Diagram

![Diagram](oh_pwr_buf.svg "Diagram")
## Description

#############################################################################
# Function: Buffer that propagates "X" if power supply is invalid           #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT  (see LICENSE file in OH! repository)                       #
#############################################################################

## Generics

| Generic name | Type | Value | Description            |
| ------------ | ---- | ----- | ---------------------- |
| N            |      | 1     |  width of data inputs  |
## Ports

| Port name | Direction | Type    | Description                |
| --------- | --------- | ------- | -------------------------- |
| vdd       | input     |         | supply (set to 1 if valid) |
| vss       | input     |         | ground (set to 0 if valid) |
| in        | input     | [N-1:0] | input signal               |
| out       | output    | [N-1:0] | buffered output signal     |
