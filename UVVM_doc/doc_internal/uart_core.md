# Entity: uart_core
## Diagram
![Diagram](uart_core.svg "Diagram")
## Description
Copyright 2020 Bitvis
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
Note : Any functionality not explicitly described in the documentation is subject to change at any time
Description   : This is NOT an example of how to implement a UART core. This is just
                a simple test vehicle that can be used to demonstrate the functionality
                of the UVVM VVC Framework.
                See library quick reference (under 'doc') and README-file(s)
## Generics
| Generic name                 | Type      | Value | Description |
| ---------------------------- | --------- | ----- | ----------- |
| GC_START_BIT                 | std_logic | '0'   |             |
| GC_STOP_BIT                  | std_logic | '1'   |             |
| GC_CLOCKS_PER_BIT            | integer   | 16    |             |
| GC_MIN_EQUAL_SAMPLES_PER_BIT | integer   | 15    |             |
## Ports
| Port name | Direction | Type      | Description                               |
| --------- | --------- | --------- | ----------------------------------------- |
| clk       | in        | std_logic | DSP interface and general control signals |
| arst      | in        | std_logic |                                           |
| p2c       | in        | t_p2c     | PIF-core interface                        |
| c2p       | out       | t_c2p     |                                           |
| rx_a      | in        | std_logic | Interrupt related signals                 |
| tx        | out       | std_logic |                                           |
## Signals
| Name           | Type                                           | Description                            |
| -------------- | ---------------------------------------------- | -------------------------------------- |
| tx_data        | t_slv_array                                    | tx signals                             |
| tx_buffer      | std_logic_vector(7 downto 0)                   |                                        |
| tx_data_valid  | std_logic                                      |                                        |
| tx_ready       | std_logic                                      |                                        |
| tx_active      | std_logic                                      |                                        |
| tx_clk_counter | unsigned(f_log2(GC_CLOCKS_PER_BIT)-1 downto 0) |                                        |
| tx_bit_counter | unsigned(3 downto 0)                           | count through the bits (12 total)      |
| rx_buffer      | std_logic_vector(7 downto 0)                   | receive signals                        |
| rx_active      | std_logic                                      |                                        |
| rx_clk_counter | unsigned(f_log2(GC_CLOCKS_PER_BIT)-1 downto 0) |                                        |
| rx_bit_counter | unsigned(3 downto 0)                           | count through the bits (12 total)      |
| rx_bit_samples | std_logic_vector(GC_CLOCKS_PER_BIT-1 downto 0) |                                        |
| rx_data        | t_slv_array                                    |                                        |
| rx_data_valid  | std_logic                                      |                                        |
| rx_data_full   | std_logic                                      |                                        |
| rx_s           | std_logic_vector(1 downto 0)                   | synchronized serial data input         |
| rx_just_active | boolean                                        | helper signal when we start receiving  |
| parity_err     | std_logic                                      | parity error detected                  |
| stop_err       | std_logic                                      | stop error detected                    |
| transient_err  | std_logic                                      | data value is transient                |
| c2p_i          | t_c2p                                          |                                        |
## Types
| Name        | Type | Description |
| ----------- | ---- | ----------- |
| t_slv_array |      |             |
## Processes
- p_rx_s: _( clk, arst )_
synchronize rx input (async)

**Description**
synchronize rx input (async)

- uart_tx: _( clk, arst )_
Transmit process; drives tx serial output.
Stores 4 pending bytes in the tx_data array, and the byte currently
being output in the tx_buffer register.
Tx_buffer is filled with data from tx_data(0) if there is valid data
available (tx_data_valid is active), and no other byte is currently
being output (tx_active is inactive).
Data received via SBI is inserted in tx_data at the index pointed to
by vr_tx_data_idx. vr_tx_data_idx is incremented when a new byte is
received via SBI, and decremented when a new byte is loaded into
tx_buffer.

**Description**
Transmit process; drives tx serial output.
Stores 4 pending bytes in the tx_data array, and the byte currently
being output in the tx_buffer register.
Tx_buffer is filled with data from tx_data(0) if there is valid data
available (tx_data_valid is active), and no other byte is currently
being output (tx_active is inactive).
Data received via SBI is inserted in tx_data at the index pointed to
by vr_tx_data_idx. vr_tx_data_idx is incremented when a new byte is
received via SBI, and decremented when a new byte is loaded into
tx_buffer.

- uart_rx: _( clk, arst )_
Receive process

**Description**
Receive process

- p_busy_assert: _( clk )_

