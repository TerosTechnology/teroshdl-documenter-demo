# Entity: cache_par2

## Diagram

![Diagram](cache_par2.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:         Martin Zabel
                 Patrick Lehmann
Entity:          Cache with parallel tag-unit and data memory.
Description:
-------------------------------------
Cache with parallel tag-unit and data memory. For the data memory,
:ref:`IP:ocram_sp` is used.
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
| ADDR_BITS          | Number of address bits. Each address identifies    |
|                    | exactly one cache line in memory.                  |
+--------------------+----------------------------------------------------+
| DATA_BITS          | Size of a cache line in bits.                      |
|                    | DATA_BITS must be divisible by 8.                  |
+--------------------+----------------------------------------------------+
Command truth table
*******************
+---------+-----------+-------------+---------+---------------------------------+
| Request | ReadWrite | Invalidate  | Replace | Command                         |
+=========+===========+=============+=========+=================================+
|  0      |    0      |    0        |    0    | None                            |
+---------+-----------+-------------+---------+---------------------------------+
|  1      |    0      |    0        |    0    | Read cache line                 |
+---------+-----------+-------------+---------+---------------------------------+
|  1      |    1      |    0        |    0    | Update cache line               |
+---------+-----------+-------------+---------+---------------------------------+
|  1      |    0      |    1        |    0    | Read cache line and discard it  |
+---------+-----------+-------------+---------+---------------------------------+
|  1      |    1      |    1        |    0    | Write cache line and discard it |
+---------+-----------+-------------+---------+---------------------------------+
|  0      |    0      |    0        |    1    | Read cache line before replace. |
+---------+-----------+-------------+---------+---------------------------------+
|  0      |    1      |    0        |    1    | Replace cache line.             |
+---------+-----------+-------------+---------+---------------------------------+
Operation
*********
All inputs are synchronous to the rising-edge of the clock `clock`.
All commands use ``Address`` to lookup (request) or replace a cache line.
``Address`` and ``OldAddress`` do not include the word/byte select part.
Each command is completed within one clock cycle, but outputs are delayed as
described below.
Upon requests, the outputs ``CacheMiss`` and ``CacheHit`` indicate (high-active)
whether the ``Address`` is stored within the cache, or not. Both outputs have a
latency of one clock cycle (pipelined) if ``HIT_MISS_REG`` is true, otherwise the
result is outputted immediately (combinational).
Upon writing a cache line, the new content is given by ``CacheLineIn``.
Only the bytes which are not masked, i.e. the corresponding bit in WriteMask
is '0', are actually written.
Upon reading a cache line, the current content is outputed on ``CacheLineOut``
with a latency of one clock cycle.
Replacing a cache line requires two steps, both with ``Replace = '1'``:
1. Read old contents of cache line by setting ``ReadWrite`` to '0'. The old
   content is outputed on ``CacheLineOut`` and the old tag on ``OldAddress``,
   both with a latency of one clock cycle.
2. Write new cache line by setting ``ReadWrite`` to '1'. The new content is
   given by ``CacheLineIn``. All bytes shall be written, i.e.
   ``WriteMask = 0``. The new cache line content will be outputed
   again on ``CacheLineOut`` in the next clock cycle (latency = 1).
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

| Generic name       | Type     | Value | Description              |
| ------------------ | -------- | ----- | ------------------------ |
| REPLACEMENT_POLICY | string   | "LRU" |                          |
| CACHE_LINES        | positive | 32    |                          |
| ASSOCIATIVITY      | positive | 32    |                          |
| ADDR_BITS          | positive | 8     |                          |
| DATA_BITS          | positive | 8     |                          |
| HIT_MISS_REG       | boolean  | true  | must be true for Cocotb. |
## Ports

| Port name    | Direction | Type                                       | Description |
| ------------ | --------- | ------------------------------------------ | ----------- |
| Clock        | in        | std_logic                                  |             |
| Reset        | in        | std_logic                                  |             |
| Request      | in        | std_logic                                  |             |
| ReadWrite    | in        | std_logic                                  |             |
| WriteMask    | in        | std_logic_vector(DATA_BITS/8 - 1 downto 0) |             |
| Invalidate   | in        | std_logic                                  |             |
| Replace      | in        | std_logic                                  |             |
| Address      | in        | std_logic_vector(ADDR_BITS-1 downto 0)     |             |
| CacheLineIn  | in        | std_logic_vector(DATA_BITS - 1 downto 0)   |             |
| CacheLineOut | out       | std_logic_vector(DATA_BITS - 1 downto 0)   |             |
| CacheHit     | out       | std_logic                                  |             |
| CacheMiss    | out       | std_logic                                  |             |
| OldAddress   | out       | std_logic_vector(ADDR_BITS-1 downto 0)     |             |
## Signals

| Name                | Type                                           | Description       |
| ------------------- | ---------------------------------------------- | ----------------- |
| TU_LineIndex        | std_logic_vector(LINE_INDEX_BITS - 1 downto 0) | look-up (request) |
| TU_TagHit           | std_logic                                      |                   |
| TU_TagMiss          | std_logic                                      |                   |
| ReplaceWrite        | std_logic                                      | replace           |
| TU_ReplaceLineIndex | std_logic_vector(LINE_INDEX_BITS - 1 downto 0) |                   |
| TU_OldAddress       | std_logic_vector(OldAddress'range)             |                   |
| MemoryIndex_us      | unsigned(LINE_INDEX_BITS - 1 downto 0)         | data memory       |
| MemoryAccess        | std_logic                                      |                   |
## Constants

| Name            | Type     | Value                    | Description |
| --------------- | -------- | ------------------------ | ----------- |
| LINE_INDEX_BITS | positive |  log2ceilnz(CACHE_LINES) |             |
## Types

| Name                | Type | Description |
| ------------------- | ---- | ----------- |
| T_CACHE_LINE_VECTOR |      |             |
## Instantiations

- TU: PoC.cache_tagunit_par
**Description**
Cache TagUnit

