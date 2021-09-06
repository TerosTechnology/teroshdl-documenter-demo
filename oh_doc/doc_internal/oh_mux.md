# Entity: oh_mux

- **File**: oh_mux.v
## Diagram

![Diagram](oh_mux.svg "Diagram")
## Description

#############################################################################
# Function: One hot N:1 MUX                                                 #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value     | Description              |
| ------------ | ---- | --------- | ------------------------ |
| N            |      | 32        |  vector width            |
| M            |      | 2         |  number of vectors       |
| SYN          |      | "TRUE"    |  synthesizable (or not)  |
| TYPE         |      | "DEFAULT" |  implementation type     |
## Ports

| Port name | Direction | Type      | Description                                  |
| --------- | --------- | --------- | -------------------------------------------- |
| sel       | input     | [M-1:0]   | select vector                                |
| in        | input     | [M*N-1:0] | concatenated input {..,in1[N-1:0],in0[N-1:0] |
| out       | output    | [N-1:0]   | output                                       |
