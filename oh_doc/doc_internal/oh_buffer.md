# Entity: oh_buffer

- **File**: oh_buffer.v
## Diagram

![Diagram](oh_buffer.svg "Diagram")
## Description

#############################################################################
# Function: Buffer                                                          #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value     | Description         |
| ------------ | ---- | --------- | ------------------- |
| N            |      | 1         |  vector width       |
| SYN          |      | "TRUE"    |  synthesize buffer  |
| TYPE         |      | "DEFAULT" |  buffer type        |
## Ports

| Port name | Direction | Type    | Description |
| --------- | --------- | ------- | ----------- |
| in        | input     | [N-1:0] | input       |
| out       | output    | [N-1:0] | output      |
