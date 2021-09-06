# Entity: uvvm_demo_th

- **File**: uvvm_demo_th.vhd
## Diagram

![Diagram](uvvm_demo_th.svg "Diagram")
## Description

================================================================================================================================
 Copyright 2020 Bitvis
 Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
 You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.

 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
 an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and limitations under the License.
================================================================================================================================
 Note : Any functionality not explicitly described in the documentation is subject to change at any time
--------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
 Description   : See library quick reference (under 'doc') and README-file(s)
----------------------------------------------------------------------------------------
 Test harness entity
## Generics

| Generic name                 | Type                 | Value              | Description                    |
| ---------------------------- | -------------------- | ------------------ | ------------------------------ |
| GC_CLK_PERIOD                | time                 | 10 ns              | Clock and bit period settings  |
| GC_BIT_PERIOD                | time                 | 16 * GC_CLK_PERIOD |                                |
| GC_ADDR_RX_DATA              | unsigned(2 downto 0) | "000"              | DUT addresses                  |
| GC_ADDR_RX_DATA_VALID        | unsigned(2 downto 0) | "001"              |                                |
| GC_ADDR_TX_DATA              | unsigned(2 downto 0) | "010"              |                                |
| GC_ADDR_TX_READY             | unsigned(2 downto 0) | "011"              |                                |
| GC_ACTIVITY_WATCHDOG_TIMEOUT | time                 | 50 * GC_BIT_PERIOD | Activity watchdog setting      |
## Signals

| Name        | Type                         | Description               |
| ----------- | ---------------------------- | ------------------------- |
| clk         | std_logic                    |  Clock and reset signals  |
| arst        | std_logic                    |                           |
| cs          | std_logic                    |  SBI VVC signals          |
| addr        | unsigned(2 downto 0)         |                           |
| wr          | std_logic                    |                           |
| rd          | std_logic                    |                           |
| wdata       | std_logic_vector(7 downto 0) |                           |
| rdata       | std_logic_vector(7 downto 0) |                           |
| ready       | std_logic                    |                           |
| uart_vvc_rx | std_logic                    |  UART VVC signals         |
| uart_vvc_tx | std_logic                    |                           |
## Constants

| Name                            | Type                    | Value                                                                                                                                                                                                                                                                                                                                                                                                           | Description    |
| ------------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| C_SBI_VVC                       | natural                 |  1                                                                                                                                                                                                                                                                                                                                                                                                              |                |
| C_UART_TX_VVC                   | natural                 |  1                                                                                                                                                                                                                                                                                                                                                                                                              |                |
| C_UART_RX_VVC                   | natural                 |  1                                                                                                                                                                                                                                                                                                                                                                                                              |                |
| C_CLOCK_GEN_VVC                 | natural                 |  1                                                                                                                                                                                                                                                                                                                                                                                                              |                |
| C_DATA_WIDTH                    | natural                 |  8                                                                                                                                                                                                                                                                                                                                                                                                              |  UART if       |
| C_ADDR_WIDTH                    | natural                 |  3                                                                                                                                                                                                                                                                                                                                                                                                              |                |
| C_UART_MONITOR_INTERFACE_CONFIG | t_uart_interface_config |  (     bit_time         => GC_BIT_PERIOD,<br><span style="padding-left:20px">     num_data_bits    => 8,<br><span style="padding-left:20px">     parity           => PARITY_ODD,<br><span style="padding-left:20px">     num_stop_bits    => STOP_BITS_ONE     )                                                                                                                                                |  UART Monitor  |
| C_UART_MONITOR_CONFIG           | t_uart_monitor_config   |  (     scope_name               => (1 to 12 => "UART Monitor",<br><span style="padding-left:20px"> others => NUL),<br><span style="padding-left:20px">     msg_id_panel             => C_UART_MONITOR_MSG_ID_PANEL_DEFAULT,<br><span style="padding-left:20px">     interface_config         => C_UART_MONITOR_INTERFACE_CONFIG,<br><span style="padding-left:20px">     transaction_display_time => 0 ns     ) |                |
## Processes
- p_model: (  )
</br>**Description**
---------------------------------------------------------------------------  Model<br>    Subscribe to SBI and UART transaction infos, and send to Scoreboard or    send VVC commands based on transaction info content.<br> --------------------------------------------------------------------------- 
## Instantiations

- i_ti_uvvm_engine: uvvm_vvc_framework.ti_uvvm_engine
- i_uart: bitvis_uart.uart
</br>**Description**
---------------------------------------------------------------------------
 Instantiate DUT
---------------------------------------------------------------------------

- i1_sbi_vvc: bitvis_vip_sbi.sbi_vvc
</br>**Description**
---------------------------------------------------------------------------
 SBI VVC
---------------------------------------------------------------------------

- i1_uart_vvc: bitvis_vip_uart.uart_vvc
</br>**Description**
---------------------------------------------------------------------------
 UART VVC
---------------------------------------------------------------------------

- i1_uart_monitor: bitvis_vip_uart.uart_monitor
</br>**Description**
---------------------------------------------------------------------------
 Monitor - UART

   Monitor and validate UART transactions.

---------------------------------------------------------------------------

- i_clock_generator_vvc: bitvis_vip_clock_generator.clock_generator_vvc
</br>**Description**
---------------------------------------------------------------------------
 Clock Generator VVC
---------------------------------------------------------------------------

