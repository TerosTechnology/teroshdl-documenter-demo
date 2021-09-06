# Entity: cache_mem

- **File**: cache_mem.vhdl
## Diagram

![Diagram](cache_mem.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:         Martin Zabel

 Entity:          Cache with :ref:`INT:PoC.Mem` interface on the "CPU" side

 Description:
 -------------------------------------
 This unit provides a cache (:ref:`IP:cache_par2`) together
 with a cache controller which reads / writes cache lines from / to memory.
 It has two :ref:`INT:PoC.Mem` interfaces:

 * one for the "CPU" side  (ports with prefix ``cpu_``), and
 * one for the memory side (ports with prefix ``mem_``).

 Thus, this unit can be placed into an already available memory path between
 the CPU and the memory (controller). If you want to plugin a cache into a
 CPU pipeline, see :ref:`IP:cache_cpu`.


 Configuration
 *************

 +--------------------+-----------------------------------------------------+
 | Parameter          | Description                                         |
 +====================+=====================================================+
 | REPLACEMENT_POLICY | Replacement policy of embedded cache. For supported |
 |                    | values see PoC.cache_replacement_policy.            |
 +--------------------+-----------------------------------------------------+
 | CACHE_LINES        | Number of cache lines.                              |
 +--------------------+-----------------------------------------------------+
 | ASSOCIATIVITY      | Associativity of embedded cache.                    |
 +--------------------+-----------------------------------------------------+
 | CPU_ADDR_BITS      | Number of address bits on the CPU side. Each address|
 |                    | identifies one memory word as seen from the CPU.    |
 |                    | Calculated from other parameters as described below.|
 +--------------------+-----------------------------------------------------+
 | CPU_DATA_BITS      | Width of the data bus (in bits) on the CPU side.    |
 |                    | CPU_DATA_BITS must be divisible by 8.               |
 +--------------------+-----------------------------------------------------+
 | MEM_ADDR_BITS      | Number of address bits on the memory side. Each     |
 |                    | address identifies one word in the memory.          |
 +--------------------+-----------------------------------------------------+
 | MEM_DATA_BITS      | Width of a memory word and of a cache line in bits. |
 |                    | MEM_DATA_BITS must be divisible by CPU_DATA_BITS.   |
 +--------------------+-----------------------------------------------------+
 | OUTSTANDING_REQ    | Number of oustanding requests, see notes below.     |
 +--------------------+-----------------------------------------------------+

 If the CPU data-bus width is smaller than the memory data-bus width, then
 the CPU needs additional address bits to identify one CPU data word inside a
 memory word. Thus, the CPU address-bus width is calculated from::

   CPU_ADDR_BITS=log2ceil(MEM_DATA_BITS/CPU_DATA_BITS)+MEM_ADDR_BITS

 The write policy is: write-through, no-write-allocate.

 The maximum throughput is one request per clock cycle, except for
 ``OUSTANDING_REQ = 1``.

 If ``OUTSTANDING_REQ`` is:

 * 1: then 1 request is buffered by a single register. To give a short
   critical path (clock-to-output delay) for ``cpu_rdy``, the throughput is
   degraded to one request per 2 clock cycles at maximum.

 * 2: then 2 requests are buffered by :ref:`IP:fifo_glue`. This setting has
   the lowest area requirements without degrading the performance.

 * >2: then the requests are buffered by :ref:`IP:fifo_cc_got`. The number of
   outstanding requests is rounded up to the next suitable value. This setting
   is useful in applications with out-of-order execution (of other
   operations). The CPU requests to the cache are always processed in-order.


 Operation
 *********

 Memory accesses are always aligned to a word boundary. Each memory word
 (and each cache line) consists of MEM_DATA_BITS bits.
 For example if MEM_DATA_BITS=128:

 * memory address 0 selects the bits   0..127 in memory,
 * memory address 1 selects the bits 128..256 in memory, and so on.

 Cache accesses are always aligned to a CPU word boundary. Each CPU word
 consists of CPU_DATA_BITS bits. For example if CPU_DATA_BITS=32:

 * CPU address 0 selects the bits   0.. 31 in memory word 0,
 * CPU address 1 selects the bits  32.. 63 in memory word 0,
 * CPU address 2 selects the bits  64.. 95 in memory word 0,
 * CPU address 3 selects the bits  96..127 in memory word 0,
 * CPU address 4 selects the bits   0.. 31 in memory word 1,
 * CPU address 5 selects the bits  32.. 63 in memory word 1, and so on.

 A synchronous reset must be applied even on a FPGA.

 The interface is documented in detail :ref:`here <INT:PoC.Mem>`.

 .. WARNING::

    If the design is synthesized with Xilinx ISE / XST, then the synthesis
    option "Keep Hierarchy" must be set to SOFT or TRUE.

 SeeAlso:
   :ref:`IP:cache_cpu`

 License:
 =============================================================================
 Copyright 2016-2016 Technische Universitaet Dresden - Germany
										 Chair of VLSI-Design, Diagnostics and Architecture

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

		http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 =============================================================================
## Generics

| Generic name       | Type     | Value | Description |
| ------------------ | -------- | ----- | ----------- |
| REPLACEMENT_POLICY | string   | "LRU" |             |
| CACHE_LINES        | positive |       |             |
| ASSOCIATIVITY      | positive |       |             |
| CPU_DATA_BITS      | positive |       |             |
| MEM_ADDR_BITS      | positive |       |             |
| MEM_DATA_BITS      | positive |       |             |
| OUTSTANDING_REQ    | positive | 2     |             |
## Ports

| Port name | Direction | Type                                                                     | Description |
| --------- | --------- | ------------------------------------------------------------------------ | ----------- |
| clk       | in        | std_logic                                                                |  clock      |
| rst       | in        | std_logic                                                                |  reset      |
| cpu_req   | in        | std_logic                                                                | "CPU" side  |
| cpu_write | in        | std_logic                                                                |             |
| cpu_addr  | in        | unsigned(log2ceil(MEM_DATA_BITS/CPU_DATA_BITS)+MEM_ADDR_BITS-1 downto 0) |             |
| cpu_wdata | in        | std_logic_vector(CPU_DATA_BITS-1 downto 0)                               |             |
| cpu_wmask | in        | std_logic_vector(CPU_DATA_BITS/8-1 downto 0)                             |             |
| cpu_rdy   | out       | std_logic                                                                |             |
| cpu_rstb  | out       | std_logic                                                                |             |
| cpu_rdata | out       | std_logic_vector(CPU_DATA_BITS-1 downto 0)                               |             |
| mem_req   | out       | std_logic                                                                | Memory side |
| mem_write | out       | std_logic                                                                |             |
| mem_addr  | out       | unsigned(MEM_ADDR_BITS-1 downto 0)                                       |             |
| mem_wdata | out       | std_logic_vector(MEM_DATA_BITS-1 downto 0)                               |             |
| mem_wmask | out       | std_logic_vector(MEM_DATA_BITS/8-1 downto 0)                             |             |
| mem_rdy   | in        | std_logic                                                                |             |
| mem_rstb  | in        | std_logic                                                                |             |
| mem_rdata | in        | std_logic_vector(MEM_DATA_BITS-1 downto 0)                               |             |
## Signals

| Name      | Type                                         | Description                     |
| --------- | -------------------------------------------- | ------------------------------- |
| int_req   | std_logic                                    |  signals to internal cache_cpu  |
| int_write | std_logic                                    |                                 |
| int_addr  | unsigned(CPU_ADDR_BITS-1 downto 0)           |                                 |
| int_wdata | std_logic_vector(CPU_DATA_BITS-1 downto 0)   |                                 |
| int_wmask | std_logic_vector(CPU_DATA_BITS/8-1 downto 0) |                                 |
| int_got   | std_logic                                    |                                 |
| int_rdata | std_logic_vector(CPU_DATA_BITS-1 downto 0)   |                                 |
## Constants

| Name          | Type     | Value                                                | Description |
| ------------- | -------- | ---------------------------------------------------- | ----------- |
| CPU_ADDR_BITS | positive |  log2ceil(MEM_DATA_BITS/CPU_DATA_BITS)+MEM_ADDR_BITS |             |
## Instantiations

- cache_cpu_inst: work.cache_cpu
