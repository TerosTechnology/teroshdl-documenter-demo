# Entity: jesd204_tx_lane_64b

- **File**: jesd204_tx_lane_64b.v
## Diagram

![Diagram](jesd204_tx_lane_64b.svg "Diagram")
## Description

The ADI JESD204 Core is released under the following license, which is
 different than all other HDL cores in this repository.
 Please read this, and understand the freedoms and responsibilities you have
 by using this source code/core.
 The JESD204 HDL, is copyright © 2016-2017 Analog Devices Inc.
 This core is free software, you can use run, copy, study, change, ask
 questions about and improve this core. Distribution of source, or resulting
 binaries (including those inside an FPGA or ASIC) require you to release the
 source of the entire project (excluding the system libraries provide by the
 tools/compiler/FPGA vendor). These are the terms of the GNU General Public
 License version 2 as published by the Free Software Foundation.
 This core  is distributed in the hope that it will be useful, but WITHOUT ANY
 WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
 A PARTICULAR PURPOSE. See the GNU General Public License for more details.
 You should have received a copy of the GNU General Public License version 2
 along with this source code, and binary.  If not, see
 <http://www.gnu.org/licenses/>.
 Commercial licenses (with commercial support) of this JESD204 core are also
 available under terms different than the General Public License. (e.g. they
 do not require you to accompany any image (FPGA or ASIC) using the JESD204
 core with any corresponding source code.) For these alternate terms you must
 purchase a license from Analog Devices Technology Licensing Office. Users
 interested in such a license should contact jesd204-licensing@analog.com for
 more information. This commercial license is sub-licensable (if you purchase
 chips from Analog Devices, incorporate them into your PCB level product, and
 purchase a JESD204 license, end users of your product will also have a
 license to use this core in a commercial setting without releasing their
 source code).
 In addition, we kindly ask you to acknowledge ADI in any program, application
 or publication in which you use this JESD204 HDL core. (You are not required
 to do so; it is up to your common sense to decide whether you want to comply
 with this request or not.) For general publications, we suggest referencing :
 “The design and implementation of the JESD204 HDL Core used in this project
 is copyright © 2016-2017, Analog Devices, Inc.”
 
## Ports

| Port name             | Direction | Type   | Description                                                      |
| --------------------- | --------- | ------ | ---------------------------------------------------------------- |
| clk                   | input     |        |                                                                  |
| reset                 | input     |        |                                                                  |
| tx_data               | input     | [63:0] |                                                                  |
| tx_ready              | input     |        |                                                                  |
| phy_data              | output    | [63:0] |                                                                  |
| phy_header            | output    | [1:0]  |                                                                  |
| lmc_edge              | input     |        |                                                                  |
| lmc_quarter_edge      | input     |        |                                                                  |
| eoemb                 | input     |        |                                                                  |
| cfg_disable_scrambler | input     |        | Scrambling mandatory in 64bxxb, keep this for debugging purposes |
| cfg_header_mode       | input     | [1:0]  |                                                                  |
| cfg_lane_disable      | input     |        |                                                                  |
## Signals

| Name                | Type        | Description |
| ------------------- | ----------- | ----------- |
| scrambled_data      | reg [63:0]  |             |
| lmc_edge_d1         | reg         |             |
| lmc_edge_d2         | reg         |             |
| lmc_quarter_edge_d1 | reg         |             |
| lmc_quarter_edge_d2 | reg         |             |
| tx_ready_d1         | reg         |             |
| tx_data_msb_s       | wire [63:0] |             |
| scrambled_data_r    | wire [63:0] |             |
| crc12               | wire [11:0] |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
## Instantiations

- i_scrambler: jesd204_scrambler_64b
- i_crc12: jesd204_crc12
- i_header_gen: jesd204_tx_header
