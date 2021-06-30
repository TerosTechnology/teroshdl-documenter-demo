# Entity: axi_read_slave

## Diagram

![Diagram](axi_read_slave.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type        | Value | Description |
| ------------ | ----------- | ----- | ----------- |
| axi_slave    | axi_slave_t |       |             |
## Ports

| Port name | Direction | Type             | Description |
| --------- | --------- | ---------------- | ----------- |
| aclk      | in        | std_logic        |             |
| arvalid   | in        | std_logic        |             |
| arready   | out       | std_logic        |             |
| arid      | in        | std_logic_vector |             |
| araddr    | in        | std_logic_vector |             |
| arlen     | in        | std_logic_vector |             |
| arsize    | in        | std_logic_vector |             |
| arburst   | in        | axi_burst_type_t |             |
| rvalid    | out       | std_logic        |             |
| rready    | in        | std_logic        |             |
| rid       | out       | std_logic_vector |             |
| rdata     | out       | std_logic_vector |             |
| rresp     | out       | axi_resp_t       |             |
| rlast     | out       | std_logic        |             |
## Signals

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| initialized | boolean |             |
## Processes
- control_process: (  )
- axi_process: (  )
- well_behaved_check: (  )
