# Entity: asic_dmux2

- **File**: asic_dmux2.v
## Diagram

![Diagram](asic_dmux2.svg "Diagram")
## Description

#############################################################################
# Function: 2:1 one hot mux                                                 #
#############################################################################
# Author:   Andreas Olofsson                                                #
# License:  MIT (see LICENSE file in OH! repository)                        #
#############################################################################

## Generics

| Generic name | Type | Value     | Description |
| ------------ | ---- | --------- | ----------- |
| PROP         |      | "DEFAULT" |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| sel1      | input     |      |             |
| sel0      | input     |      |             |
| in1       | input     |      |             |
| in0       | input     |      |             |
| out       | output    |      |             |
