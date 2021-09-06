# Entity: asic_footer

- **File**: asic_footer.v
## Diagram

![Diagram](asic_footer.svg "Diagram")
## Description

#############################################################################
# Function: Power supply header switch                                      #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value     | Description |
| ------------ | ---- | --------- | ----------- |
| PROP         |      | "DEFAULT" |             |
## Ports

| Port name | Direction | Type | Description         |
| --------- | --------- | ---- | ------------------- |
| nsleep    | input     |      | 0 = disabled ground |
| vssin     | input     |      | input supply        |
| vssout    | output    |      | gated output supply |
