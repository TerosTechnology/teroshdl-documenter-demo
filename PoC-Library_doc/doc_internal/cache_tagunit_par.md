# Entity: cache_tagunit_par
## Diagram
![Diagram](cache_tagunit_par.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Patrick Lehmann
Entity:					Tag-unit with fully-parallel compare of tag.
Description:
-------------------------------------
Tag-unit with fully-parallel compare of tag.
Configuration
*************
+--------------------+----------------------------------------------------+
| Parameter          | Description                                        |
+====================+====================================================+
| REPLACEMENT_POLICY | Replacement policy. For supported policies see     |
|                    | PoC.cache_replacement_policy.                      |
+--------------------+----------------------------------------------------+
| CACHE_LINES        | Number of cache lines.                             |
+--------------------+----------------------------------------------------+
| ASSOCIATIVITY      | Associativity of the cache.                        |
+--------------------+----------------------------------------------------+
| ADDRESS_BITS       | Number of address bits. Each address identifies    |
|                    | exactly one cache line in memory.                  |
+--------------------+----------------------------------------------------+
Command truth table
*******************
+---------+-----------+-------------+---------+----------------------------------+
| Request | ReadWrite | Invalidate  | Replace | Command                          |
+=========+===========+=============+=========+==================================+
|   0     |    0      |    0        |    0    | None                             |
+---------+-----------+-------------+---------+----------------------------------+
|   1     |    0      |    0        |    0    | Read cache line                  |
+---------+-----------+-------------+---------+----------------------------------+
|   1     |    1      |    0        |    0    | Update cache line                |
+---------+-----------+-------------+---------+----------------------------------+
|   1     |    0      |    1        |    0    | Read cache line and discard it   |
+---------+-----------+-------------+---------+----------------------------------+
|   1     |    1      |    1        |    0    | Write cache line and discard it  |
+---------+-----------+-------------+---------+----------------------------------+
|   0     |           |    0        |    1    | Replace cache line.              |
+---------+-----------+-------------+---------+----------------------------------+
Operation
*********
All inputs are synchronous to the rising-edge of the clock `clock`.
All commands use ``Address`` to lookup (request) or replace a cache line.
Each command is completed within one clock cycle.
Upon requests, the outputs ``CacheMiss`` and ``CacheHit`` indicate (high-active)
immediately (combinational) whether the ``Address`` is stored within the cache, or not.
But, the cache-line usage is updated at the rising-edge of the clock.
If hit, ``LineIndex`` specifies the cache line where to find the content.
The output ``ReplaceLineIndex`` indicates which cache line will be replaced as
next by a replace command. The output ``OldAddress`` specifies the old tag stored at this
index. The replace command will store the ``Address`` and update the cache-line
usage at the rising-edge of the clock.
For a direct-mapped cache, the number of ``CACHE_LINES`` must be a power of 2.
For a set-associative cache, the expression ``CACHE_LINES / ASSOCIATIVITY``
must be a power of 2.
.. NOTE::
   The port ``NewAddress`` has been removed. Use ``Address`` instead as
   described above.
   If ``Address`` is fed from a register and an Altera FPGA is used, then
   Quartus Map converts the tag memory from a memory with asynchronous read to a
   memory with synchronous read by adding a pass-through logic. Quartus Map
   reports warning 276020 which is intended.
.. WARNING::
   If the design is synthesized with Xilinx ISE / XST, then the synthesis
   option "Keep Hierarchy" must be set to SOFT or TRUE.
License:
=============================================================================
Copyright 2007-2016 Technische Universitaet Dresden - Germany
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
| Generic name       | Type     | Value | Description |
| ------------------ | -------- | ----- | ----------- |
| REPLACEMENT_POLICY | string   | "LRU" |             |
| CACHE_LINES        | positive | 32    |             |
| ASSOCIATIVITY      | positive | 32    |             |
| ADDRESS_BITS       | positive | 8     |             |
## Ports
| Port name        | Direction | Type                                                   | Description |
| ---------------- | --------- | ------------------------------------------------------ | ----------- |
| Clock            | in        | std_logic                                              |             |
| Reset            | in        | std_logic                                              |             |
| Replace          | in        | std_logic                                              |             |
| ReplaceLineIndex | out       | std_logic_vector(log2ceilnz(CACHE_LINES) - 1 downto 0) |             |
| OldAddress       | out       | std_logic_vector(ADDRESS_BITS - 1 downto 0)            |             |
| Request          | in        | std_logic                                              |             |
| ReadWrite        | in        | std_logic                                              |             |
| Invalidate       | in        | std_logic                                              |             |
| Address          | in        | std_logic_vector(ADDRESS_BITS - 1 downto 0)            |             |
| LineIndex        | out       | std_logic_vector(log2ceilnz(CACHE_LINES) - 1 downto 0) |             |
| TagHit           | out       | std_logic                                              |             |
| TagMiss          | out       | std_logic                                              |             |
## Constants
| Name | Type     | Value                        | Description |
| ---- | -------- | ---------------------------- | ----------- |
| SETS | positive |  CACHE_LINES / ASSOCIATIVITY |             |
## Functions
- contains_x <font id="function_arguments">(value : unsigned)</font> <font id="function_return">return boolean</font>
**Description**
Returns true if unsigned value contains metalogical values.Similar function is_x(unsigned) is only shipped with VHDL'08.
