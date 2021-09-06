# Entity: oh_clockmux2

- **File**: oh_clockmux2.v
## Diagram

![Diagram](oh_clockmux2.svg "Diagram")
## Description

#############################################################################
# Function: 2:1 Clock Mux                                                   #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value     | Description              |
| ------------ | ---- | --------- | ------------------------ |
| N            |      | 1         |  vector width            |
| SYN          |      | "TRUE"    |  synthesizable (or not)  |
| TYPE         |      | "DEFAULT" |  implementation type     |
## Ports

| Port name | Direction | Type    | Description                 |
| --------- | --------- | ------- | --------------------------- |
| en0       | input     | [N-1:0] | clkin0 enable (stable high) |
| en1       | input     | [N-1:0] | clkin1 enable (stable high) |
| clkin0    | input     | [N-1:0] | clock input                 |
| clkin1    | input     | [N-1:0] | clock input                 |
| clkout    | output    | [N-1:0] | clock output                |
