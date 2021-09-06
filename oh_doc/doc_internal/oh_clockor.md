# Entity: oh_clockor

- **File**: oh_clockor.v
## Diagram

![Diagram](oh_clockor.svg "Diagram")
## Description

#############################################################################
# Function: Clock 'OR' gate                                                 #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value     | Description               |
| ------------ | ---- | --------- | ------------------------- |
| N            |      | 2         |  number of clock inputs)  |
| SYN          |      | "TRUE"    |  synthesizable (or not)   |
| TYPE         |      | "DEFAULT" |  implementation type      |
## Ports

| Port name | Direction | Type    | Description  |
| --------- | --------- | ------- | ------------ |
| clkin     | input     | [N-1:0] | clock input  |
| clkout    | output    |         | clock output |
