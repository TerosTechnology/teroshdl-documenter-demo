# Entity: jesd204_tx_gearbox

- **File**: jesd204_tx_gearbox.v
## Diagram

![Diagram](jesd204_tx_gearbox.svg "Diagram")
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
 Constraints:
   - IN_DATA_PATH_WIDTH >= OUT_DATA_PATH_WIDTH
 
## Generics

| Generic name        | Type | Value | Description |
| ------------------- | ---- | ----- | ----------- |
| IN_DATA_PATH_WIDTH  |      | 6     |             |
| OUT_DATA_PATH_WIDTH |      | 4     |             |
| NUM_LANES           |      | 1     |             |
| DEPTH               |      | 16    |             |
## Ports

| Port name        | Direction | Type                                  | Description |
| ---------------- | --------- | ------------------------------------- | ----------- |
| link_clk         | input     |                                       |             |
| reset            | input     |                                       |             |
| device_clk       | input     |                                       |             |
| device_reset     | input     |                                       |             |
| device_data      | input     | [NUM_LANES*IN_DATA_PATH_WIDTH*8-1:0]  |             |
| device_lmfc_edge | input     |                                       |             |
| link_data        | output    | [NUM_LANES*OUT_DATA_PATH_WIDTH*8-1:0] |             |
| output_ready     | input     |                                       |             |
## Signals

| Name              | Type                 | Description |
| ----------------- | -------------------- | ----------- |
| mem               | reg [MEM_W-1:0]      |             |
| in_addr           | reg [D_LOG2-1:0]     |             |
| out_addr          | reg [D_LOG2-1:0]     |             |
| mem_rd_valid      | reg                  |             |
| mem_rd_data       | reg [MEM_W-1:0]      |             |
| mem_wr_en         | wire                 |             |
| mem_rd_en         | wire                 |             |
| in_out_addr       | wire [D_LOG2-1:0]    |             |
| out_in_addr       | wire [D_LOG2-1:0]    |             |
| unpacker_ready    | wire [NUM_LANES-1:0] |             |
| output_ready_sync | wire                 |             |
## Constants

| Name   | Type | Value                          | Description |
| ------ | ---- | ------------------------------ | ----------- |
| MEM_W  |      | IN_DATA_PATH_WIDTH*8*NUM_LANES |             |
| D_LOG2 |      | $clog2(DEPTH)                  |             |
## Processes
- unnamed: ( @(posedge device_clk) )
- unnamed: ( @(posedge device_clk) )
- unnamed: ( @(posedge link_clk) )
- unnamed: ( @(posedge link_clk) )
## Instantiations

- i_sync_ready: sync_bits
