# Entity: jesd204_eof_generator

- **File**: jesd204_eof_generator.v
## Diagram

![Diagram](jesd204_eof_generator.svg "Diagram")
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

| Generic name         | Type | Value | Description |
| -------------------- | ---- | ----- | ----------- |
| DATA_PATH_WIDTH      |      | 4     |             |
| MAX_OCTETS_PER_FRAME |      | 256   |             |
## Ports

| Port name            | Direction | Type                  | Description |
| -------------------- | --------- | --------------------- | ----------- |
| clk                  | input     |                       |             |
| reset                | input     |                       |             |
| lmfc_edge            | input     |                       |             |
| cfg_octets_per_frame | input     | [7:0]                 |             |
| cfg_generate_eomf    | input     |                       |             |
| sof                  | output    | [DATA_PATH_WIDTH-1:0] |             |
| eof                  | output    | [DATA_PATH_WIDTH-1:0] |             |
| eomf                 | output    |                       |             |
## Signals

| Name                   | Type    | Description |
| ---------------------- | ------- | ----------- |
| lmfc_edge_d1           | reg     |             |
| beat_counter_sof       | wire    |             |
| beat_counter_eof       | wire    |             |
| small_octets_per_frame | wire    |             |
| i                      | integer |             |
## Constants

| Name     | Type | Value              | Description |
| -------- | ---- | ------------------ | ----------- |
| CW       |      | MAX_OCTETS_PER_FRA |             |
| DPW_LOG2 |      | DATA_PAT           |             |
## Functions
- ffs <font id="function_arguments">()</font> <font id="function_return">return ([1:0])</font>
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
**Description**
 Only 1, 2 and multiples of 4 are supported atm */ 
