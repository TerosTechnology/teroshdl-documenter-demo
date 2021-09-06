# Entity: fifo

- **File**: fifo.vhd
## Diagram

![Diagram](fifo.svg "Diagram")
## Description

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this file,
 You can obtain one at http://mozilla.org/MPL/2.0/.

 Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| data_width   | positive | 8     |             |
| fifo_depth   | positive | 8     |             |
## Ports

| Port name | Direction | Type                                    | Description |
| --------- | --------- | --------------------------------------- | ----------- |
| clkw      | in        | std_logic                               |             |
| clkr      | in        | std_logic                               |             |
| rst       | in        | std_logic                               |             |
| wr        | in        | std_logic                               |             |
| rd        | in        | std_logic                               |             |
| d         | in        | std_logic_vector(data_width-1 downto 0) |             |
| e         | out       | std_logic                               |             |
| f         | out       | std_logic                               |             |
| q         | out       | std_logic_vector(data_width-1 downto 0) |             |
## Signals

| Name | Type                          | Description |
| ---- | ----------------------------- | ----------- |
| mem  | fifo_t                        |             |
| rdp  | unsigned(fifo_depth downto 0) |             |
|  wrp | unsigned(fifo_depth downto 0) |             |
## Types

| Name   | Type | Description |
| ------ | ---- | ----------- |
| fifo_t |      |             |
## Processes
- unnamed: ( clkw )
- unnamed: ( clkw )
- unnamed: ( clkr )
- unnamed: ( clkr )
