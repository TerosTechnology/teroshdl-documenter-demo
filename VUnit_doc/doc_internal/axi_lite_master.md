# Entity: axi_lite_master

## Diagram

![Diagram](axi_lite_master.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type         | Value | Description |
| ------------ | ------------ | ----- | ----------- |
| bus_handle   | bus_master_t |       |             |
## Ports

| Port name | Direction | Type                                                          | Description |
| --------- | --------- | ------------------------------------------------------------- | ----------- |
| aclk      | in        | std_logic                                                     |             |
| arready   | in        | std_logic                                                     |             |
| arvalid   | out       | std_logic                                                     |             |
| araddr    | out       | std_logic_vector(address_length(bus_handle) - 1 downto 0)     |             |
| rready    | out       | std_logic                                                     |             |
| rvalid    | in        | std_logic                                                     |             |
| rdata     | in        | std_logic_vector(data_length(bus_handle) - 1 downto 0)        |             |
| rresp     | in        | axi_resp_t                                                    |             |
| awready   | in        | std_logic                                                     |             |
| awvalid   | out       | std_logic                                                     |             |
| awaddr    | out       | std_logic_vector(address_length(bus_handle) - 1 downto 0)     |             |
| wready    | in        | std_logic                                                     |             |
| wvalid    | out       | std_logic                                                     |             |
| wdata     | out       | std_logic_vector(data_length(bus_handle) - 1 downto 0)        |             |
| wstrb     | out       | std_logic_vector(byte_enable_length(bus_handle) - 1 downto 0) |             |
| bvalid    | in        | std_logic                                                     |             |
| bready    | out       | std_logic                                                     |             |
| bresp     | in        | axi_resp_t                                                    |             |
## Constants

| Name           | Type    | Value      | Description |
| -------------- | ------- | ---------- | ----------- |
| reply_queue    | queue_t |  new_queue |             |
|  message_queue | queue_t |  new_queue |             |
## Processes
- main: (  )
- bus_process: (  )
**Description**
Use separate process to always align to rising edge of clock

- read_reply: (  )
**Description**
Reply in separate process do not destroy alignment with the clock

