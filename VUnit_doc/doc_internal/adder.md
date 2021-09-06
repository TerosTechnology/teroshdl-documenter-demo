# Entity: adder

- **File**: adder.vhd
## Diagram

![Diagram](adder.svg "Diagram")
## Description

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this file,
 You can obtain one at http://mozilla.org/MPL/2.0/.

 Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Ports

| Port name | Direction | Type                 | Description |
| --------- | --------- | -------------------- | ----------- |
| clk       | in        | std_logic            |             |
| op_a      | in        | unsigned(7 downto 0) |             |
| op_b      | in        | unsigned(7 downto 0) |             |
| dv_in     | in        | std_logic            |             |
| sum       | out       | unsigned(8 downto 0) |             |
| dv_out    | out       | std_logic            |             |
## Processes
- main: (  )
