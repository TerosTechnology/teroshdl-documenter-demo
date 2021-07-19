# Entity: pmod_USBUART

- **File**: pmod_USBUART.vhdl
## Diagram

![Diagram](pmod_USBUART.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	Digilent Peripherial Module: USB-UART (Pmod_USBUART)
Description:
-------------------------------------
This module abstracts a FTDI FT232R USB-UART bridge by instantiating a
:doc:`PoC.io.uart.fifo <../uart/uart_fifo>`. The FT232R supports up to
3 MBaud. A synchronous FIFO interface with a 32 words buffer is provided.
Hardware flow control (RTS_CTS) is enabled.
License:
=============================================================================
Copyright 2007-2015 Technische Universitaet Dresden - Germany
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
=============================================================================
## Generics

| Generic name | Type | Value     | Description |
| ------------ | ---- | --------- | ----------- |
| CLOCK_FREQ   | FREQ | 100 MHz   |             |
| BAUDRATE     | BAUD | 115200 Bd |             |
## Ports

| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| Clock     | in        | std_logic                    |             |
| Reset     | in        | std_logic                    |             |
| TX_put    | in        | std_logic                    |             |
| TX_Data   | in        | std_logic_vector(7 downto 0) |             |
| TX_Full   | out       | std_logic                    |             |
| RX_Valid  | out       | std_logic                    |             |
| RX_Data   | out       | std_logic_vector(7 downto 0) |             |
| RX_got    | in        | std_logic                    |             |
| UART_TX   | out       | std_logic                    |             |
| UART_RX   | in        | std_logic                    |             |
| UART_RTS  | out       | std_logic                    |             |
| UART_CTS  | in        | std_logic                    |             |
## Instantiations

- UART: PoC.uart_fifo
