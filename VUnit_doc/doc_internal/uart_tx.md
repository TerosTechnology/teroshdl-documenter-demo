# Entity: uart_tx
## Diagram
![Diagram](uart_tx.svg "Diagram")
## Description
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
pragma translate_on
## Generics
| Generic name   | Type    | Value | Description |
| -------------- | ------- | ----- | ----------- |
| cycles_per_bit | natural | 434   |             |
## Ports
| Port name | Direction | Type                         | Description                |
| --------- | --------- | ---------------------------- | -------------------------- |
| clk       | in        | std_logic                    |                            |
| tx        | out       | std_logic                    | Serial output bit          |
| tready    | out       | std_logic                    | AXI stream for input bytes |
| tvalid    | in        | std_Logic                    |                            |
| tdata     | in        | std_logic_vector(7 downto 0) |                            |
## Signals
| Name       | Type      | Description |
| ---------- | --------- | ----------- |
| tready_int | std_logic |             |
## Processes
- main: _( clk )_

## State machines
![Diagram_state_machine_0]( stm_uart_tx_00.svg "Diagram")