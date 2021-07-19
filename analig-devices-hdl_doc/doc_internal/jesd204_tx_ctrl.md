# Entity: jesd204_tx_ctrl

- **File**: jesd204_tx_ctrl.v
## Diagram

![Diagram](jesd204_tx_ctrl.svg "Diagram")
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
 
## Generics

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| NUM_LANES       |      | 1     |             |
| NUM_LINKS       |      | 1     |             |
| DATA_PATH_WIDTH |      | 4     |             |
## Ports

| Port name                 | Direction | Type                              | Description |
| ------------------------- | --------- | --------------------------------- | ----------- |
| clk                       | input     |                                   |             |
| reset                     | input     |                                   |             |
| sync                      | input     | [NUM_LINKS-1:0]                   |             |
| lmfc_edge                 | input     |                                   |             |
| somf                      | input     | [DATA_PATH_WIDTH-1:0]             |             |
| somf_early2               | input     | [DATA_PATH_WIDTH-1:0]             |             |
| eomf                      | input     | [DATA_PATH_WIDTH-1:0]             |             |
| lane_cgs_enable           | output    | [NUM_LANES-1:0]                   |             |
| eof_reset                 | output    |                                   |             |
| tx_ready                  | output    |                                   |             |
| tx_ready_nx               | output    |                                   |             |
| tx_next_mf_ready          | output    |                                   |             |
| ilas_data                 | output    | [DATA_PATH_WIDTH*8*NUM_LANES-1:0] |             |
| ilas_charisk              | output    | [DATA_PATH_WIDTH*NUM_LANES-1:0]   |             |
| ilas_config_addr          | output    | [1:0]                             |             |
| ilas_config_rd            | output    |                                   |             |
| ilas_config_data          | input     | [DATA_PATH_WIDTH*8*NUM_LANES-1:0] |             |
| cfg_lanes_disable         | input     | [NUM_LANES-1:0]                   |             |
| cfg_links_disable         | input     | [NUM_LINKS-1:0]                   |             |
| cfg_continuous_cgs        | input     |                                   |             |
| cfg_continuous_ilas       | input     |                                   |             |
| cfg_skip_ilas             | input     |                                   |             |
| cfg_mframes_per_ilas      | input     | [7:0]                             |             |
| cfg_octets_per_multiframe | input     | [9:0]                             |             |
| ctrl_manual_sync_request  | input     |                                   |             |
| status_sync               | output    | [NUM_LINKS-1:0]                   |             |
| status_state              | output    | [1:0]                             |             |
## Signals

| Name                     | Type                          | Description                                                                                                                                                                                              |
| ------------------------ | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cfg_beats_per_multiframe | wire [BEATS_PER_MF_WIDTH-1:0] | For DATA_PATH_WIDTH = 8, special case if F*K%8=4 Multiframe boundaries can occur in the middle of a beat jesd204_lmfc will assert lmfc_edge once per two LMFC periods cfg_mframes_per_ilas must be even  |
| octets_per_mf_4_mod_8    | wire                          |                                                                                                                                                                                                          |
| cfg_lmfc_per_ilas        | wire [7:0]                    |                                                                                                                                                                                                          |
| lmfc_edge_d1             | reg                           |                                                                                                                                                                                                          |
| lmfc_edge_d2             | reg                           |                                                                                                                                                                                                          |
| eof_reset_d              | reg                           |                                                                                                                                                                                                          |
| ilas_reset               | reg                           |                                                                                                                                                                                                          |
| ilas_data_reset          | reg                           |                                                                                                                                                                                                          |
| sync_request             | reg                           |                                                                                                                                                                                                          |
| sync_request_received    | reg                           |                                                                                                                                                                                                          |
| last_ilas_mframe         | reg                           |                                                                                                                                                                                                          |
| mframe_counter           | reg [7:0]                     |                                                                                                                                                                                                          |
| ilas_counter             | reg [ILAS_COUNTER_WIDTH-1:0]  |                                                                                                                                                                                                          |
| ilas_config_rd_start     | wire                          |                                                                                                                                                                                                          |
| ilas_config_rd_d1        | reg                           |                                                                                                                                                                                                          |
| cgs_enable               | reg                           |                                                                                                                                                                                                          |
| ilas_default_data        | wire [DATA_PATH_WIDTH*8-1:0]  |                                                                                                                                                                                                          |
| status_sync_masked       | wire [NUM_LINKS-1:0]          |                                                                                                                                                                                                          |
## Constants

| Name               | Type | Value                                                   | Description |
| ------------------ | ---- | ------------------------------------------------------- | ----------- |
| ILAS_DATA_LENGTH   |      | 4                                                       |             |
| ILAS_COUNTER_WIDTH |      | 6                                                       |             |
| DPW_LOG2           |      | DATA_PATH_WIDTH == 8 ? 3 : DATA_PATH_WIDTH == 4 ? 2 : 1 |             |
| BEATS_PER_MF_WIDTH |      | 10-DPW_LOG2                                             |             |
| STATE_WAIT         |      | 2'b00                                                   |             |
| STATE_CGS          |      | 2'b01                                                   |             |
| STATE_ILAS         |      | 2'b10                                                   |             |
| STATE_DATA         |      | 2'b11                                                   |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(*) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
Timeline
 *
 * #1 lmfc_edge == 1, ilas_reset update
 * #3 {lane_,}cgs_enable, tx_ready update
 *
 * One multi-frame should at least be 3 clock cycles (TBD 64-bit data path)
 */

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
## Instantiations

- i_cdc_sync: sync_bits
