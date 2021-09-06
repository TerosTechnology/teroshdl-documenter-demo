# Entity: oh_latnq

- **File**: oh_latnq.v
## Diagram

![Diagram](oh_latnq.svg "Diagram")
## Description

#############################################################################
# Function:  D-type active-low transparent latch                            #
#                                                                           #
# Copyright: OH Project Authors. ALl rights Reserved.                       #
# License:   MIT (see LICENSE file in OH repository)                        # 
#############################################################################

## Generics

| Generic name | Type | Value | Description   |
| ------------ | ---- | ----- | ------------- |
| DW           |      | 1     |  array width  |
## Ports

| Port name | Direction | Type     | Description |
| --------- | --------- | -------- | ----------- |
| d         | input     | [DW-1:0] |             |
| gn        | input     | [DW-1:0] |             |
| q         | output    | [DW-1:0] |             |
## Processes
- unnamed: (  )
  - **Type:** always_latch
