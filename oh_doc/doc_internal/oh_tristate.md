# Entity: oh_tristate

- **File**: oh_tristate.v
## Diagram

![Diagram](oh_tristate.svg "Diagram")
## Description

#############################################################################
# Function: Tristate Driver                                                 #
#############################################################################
# Author:  Andreas Olofsson                                                 #
# SPDX-License-Identifier:     MIT                                          #
#############################################################################

## Generics

| Generic name | Type | Value     | Description           |
| ------------ | ---- | --------- | --------------------- |
| N            |      | 1         |  block width          |
| SYN          |      | "TRUE"    |  synthesizable        |
| TYPE         |      | "DEFAULT" |  implementation type  |
## Ports

| Port name | Direction | Type    | Description                           |
| --------- | --------- | ------- | ------------------------------------- |
| in        | input     | [N-1:0] | signal to io                          |
| oe        | input     | [N-1:0] | output enable (1 = drive, 0 = high-z) |
| out       | output    | [N-1:0] | output                                |
