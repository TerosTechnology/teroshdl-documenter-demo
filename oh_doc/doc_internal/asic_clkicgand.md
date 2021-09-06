# Entity: asic_clkicgand

- **File**: asic_clkicgand.v
## Diagram

![Diagram](asic_clkicgand.svg "Diagram")
## Description

#############################################################################
# Function: Integrated "And" Clock Gating Cell (And)                        #
# Copyright: OH Project Authors. ALl rights Reserved.                       #
# License:  MIT (see LICENSE file in OH repository)                         #
#############################################################################

## Generics

| Generic name | Type | Value     | Description |
| ------------ | ---- | --------- | ----------- |
| PROP         |      | "DEFAULT" |             |
## Ports

| Port name | Direction | Type | Description                    |
| --------- | --------- | ---- | ------------------------------ |
| clk       | input     |      | clock input                    |
| te        | input     |      | test enable                    |
| en        | input     |      | enable (from positive edge FF) |
| eclk      | output    |      | enabled clock output           |
## Signals

| Name      | Type | Description |
| --------- | ---- | ----------- |
| en_stable | reg  |             |
## Processes
- unnamed: ( @ (clk or en or te) )
  - **Type:** always
