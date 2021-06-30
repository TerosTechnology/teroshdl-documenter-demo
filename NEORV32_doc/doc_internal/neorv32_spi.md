# Entity: neorv32_spi

## Diagram

![Diagram](neorv32_spi.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - Serial Peripheral Interface Controller (SPI) >>                                  #
# ********************************************************************************************* #
# Frame format: 8/16/24/32-bit receive/transmit data, always MSB first, 2 clock modes,          #
# 8 pre-scaled clocks (derived from system clock), 8 dedicated chip-select lines (low-active).  #
# Interrupt: SPI_transfer_done                                                                  #
# ********************************************************************************************* #
# BSD 3-Clause License                                                                          #
#                                                                                               #
# Copyright (c) 2021, Stephan Nolting. All rights reserved.                                     #
#                                                                                               #
# Redistribution and use in source and binary forms, with or without modification, are          #
# permitted provided that the following conditions are met:                                     #
#                                                                                               #
# 1. Redistributions of source code must retain the above copyright notice, this list of        #
#    conditions and the following disclaimer.                                                   #
#                                                                                               #
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of     #
#    conditions and the following disclaimer in the documentation and/or other materials        #
#    provided with the distribution.                                                            #
#                                                                                               #
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to  #
#    endorse or promote products derived from this software without specific prior written      #
#    permission.                                                                                #
#                                                                                               #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS   #
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF               #
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE    #
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,     #
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE #
# GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED    #
# AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING     #
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED  #
# OF THE POSSIBILITY OF SUCH DAMAGE.                                                            #
# ********************************************************************************************* #
# The NEORV32 Processor - https://github.com/stnolting/neorv32              (c) Stephan Nolting #
#################################################################################################
## Ports

| Port name   | Direction | Type                           | Description                             |
| ----------- | --------- | ------------------------------ | --------------------------------------- |
| clk_i       | in        | std_ulogic                     | global clock line                       |
| addr_i      | in        | std_ulogic_vector(31 downto 0) | address                                 |
| rden_i      | in        | std_ulogic                     | read enable                             |
| wren_i      | in        | std_ulogic                     | write enable                            |
| data_i      | in        | std_ulogic_vector(31 downto 0) | data in                                 |
| data_o      | out       | std_ulogic_vector(31 downto 0) | data out                                |
| ack_o       | out       | std_ulogic                     | transfer acknowledge                    |
| clkgen_en_o | out       | std_ulogic                     | enable clock generator                  |
| clkgen_i    | in        | std_ulogic_vector(07 downto 0) |                                         |
| spi_sck_o   | out       | std_ulogic                     | SPI serial clock                        |
| spi_sdo_o   | out       | std_ulogic                     | controller data out, peripheral data in |
| spi_sdi_i   | in        | std_ulogic                     | controller data in, peripheral data out |
| spi_csn_o   | out       | std_ulogic_vector(07 downto 0) | SPI CS                                  |
| irq_o       | out       | std_ulogic                     | transmission done interrupt             |
## Signals

| Name           | Type                           | Description          |
| -------------- | ------------------------------ | -------------------- |
| acc_en         | std_ulogic                     | module access enable |
| addr           | std_ulogic_vector(31 downto 0) | access address       |
| wren           | std_ulogic                     | word write enable    |
| rden           | std_ulogic                     | read enable          |
| ctrl           | std_ulogic_vector(14 downto 0) | accessible regs --   |
| tx_data_reg    | std_ulogic_vector(31 downto 0) |                      |
| rx_data        | std_ulogic_vector(31 downto 0) |                      |
| spi_clk        | std_ulogic                     | clock generator --   |
| spi_start      | std_ulogic                     | spi transceiver --   |
| spi_busy       | std_ulogic                     |                      |
| spi_state0     | std_ulogic                     |                      |
| spi_state1     | std_ulogic                     |                      |
| spi_rtx_sreg   | std_ulogic_vector(31 downto 0) |                      |
| spi_rx_data    | std_ulogic_vector(31 downto 0) |                      |
| spi_bitcnt     | std_ulogic_vector(05 downto 0) |                      |
| spi_bitcnt_max | std_ulogic_vector(05 downto 0) |                      |
| spi_sdi_ff0    | std_ulogic                     |                      |
| spi_sdi_ff1    | std_ulogic                     |                      |
## Constants

| Name             | Type    | Value                      | Description                             |
| ---------------- | ------- | -------------------------- | --------------------------------------- |
| hi_abb_c         | natural |  index_size_f(io_size_c)-1 | high address boundary bit               |
| lo_abb_c         | natural |  index_size_f(spi_size_c)  | low address boundary bit                |
| ctrl_spi_cs0_c   | natural |   0                        | r/w: spi CS 0                           |
| ctrl_spi_cs1_c   | natural |   1                        | r/w: spi CS 1                           |
| ctrl_spi_cs2_c   | natural |   2                        | r/w: spi CS 2                           |
| ctrl_spi_cs3_c   | natural |   3                        | r/w: spi CS 3                           |
| ctrl_spi_cs4_c   | natural |   4                        | r/w: spi CS 4                           |
| ctrl_spi_cs5_c   | natural |   5                        | r/w: spi CS 5                           |
| ctrl_spi_cs6_c   | natural |   6                        | r/w: spi CS 6                           |
| ctrl_spi_cs7_c   | natural |   7                        | r/w: spi CS 7                           |
| ctrl_spi_en_c    | natural |   8                        | r/w: spi enable                         |
| ctrl_spi_cpha_c  | natural |   9                        | r/w: spi clock phase                    |
| ctrl_spi_prsc0_c | natural |  10                        | r/w: spi prescaler select bit 0         |
| ctrl_spi_prsc1_c | natural |  11                        | r/w: spi prescaler select bit 1         |
| ctrl_spi_prsc2_c | natural |  12                        | r/w: spi prescaler select bit 2         |
| ctrl_spi_size0_c | natural |  13                        | r/w: data size (00:  8-bit, 01: 16-bit) |
| ctrl_spi_size1_c | natural |  14                        | r/w: data size (10: 24-bit, 11: 32-bit) |
| ctrl_spi_busy_c  | natural |  31                        | r/-: spi transceiver is busy            |
## Processes
- rw_access: ( clk_i )
**Description**
Read/Write Access ----------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- spi_rtx_unit: ( clk_i )
**Description**
SPI Transceiver ------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- data_size: ( ctrl )
**Description**
RTX Data size ------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- rx_mapping: ( ctrl, spi_rtx_sreg )
**Description**
RX-Data Masking ------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

