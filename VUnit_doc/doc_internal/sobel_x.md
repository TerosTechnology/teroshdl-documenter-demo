# Entity: sobel_x

- **File**: sobel_x.vhd
## Diagram

![Diagram](sobel_x.svg "Diagram")
## Description

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this file,
 You can obtain one at http://mozilla.org/MPL/2.0/.

 Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| data_width   | natural |       |             |
## Ports

| Port name     | Direction | Type                            | Description |
| ------------- | --------- | ------------------------------- | ----------- |
| clk           | in        | std_logic                       |             |
| input_tvalid  | in        | std_logic                       |             |
| input_tlast   | in        | std_logic                       |             |
| input_tdata   | in        | unsigned(data_width-1 downto 0) |             |
| output_tvalid | out       | std_logic                       |             |
| output_tlast  | out       | std_logic                       |             |
| output_tdata  | out       | signed(data_width downto 0)     |             |
## Processes
- main: (  )
