# Entity: cache_par

## Diagram

![Diagram](cache_par.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:         Patrick Lehmann
                 Martin Zabel
Entity:          Cache with parallel tag-unit and data memory.
Description:
-------------------------------------
Implements a cache with parallel tag-unit and data memory.
.. NOTE::
   This component infers a single-port memory with read-first behavior, that
   is, upon writes the old-data is returned on the read output. Such memory
   (e.g. LUT-RAM) is not available on all devices. Thus, synthesis may
   infer a lot of flip-flops plus multiplexers instead, which is very inefficient.
   It is recommended to use :doc:`PoC.cache.par2 <cache_par2>` instead which has a
   slightly different interface.
All inputs are synchronous to the rising-edge of the clock `clock`.
**Command truth table:**
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
|  0      |           |    0        |    1    | Replace cache line.             |
+---------+-----------+-------------+---------+---------------------------------+
All commands use ``Address`` to lookup (request) or replace a cache line.
``Address`` and ``OldAddress`` do not include the word/byte select part.
Each command is completed within one clock cycle, but outputs are delayed as
described below.
Upon requests, the outputs ``CacheMiss`` and ``CacheHit`` indicate (high-active)
whether the ``Address`` is stored within the cache, or not. Both outputs have a
latency of one clock cycle.
Upon writing a cache line, the new content is given by ``CacheLineIn``.
Upon reading a cache line, the current content is outputed on ``CacheLineOut``
with a latency of one clock cycle.
Upon replacing a cache line, the new content is given by ``CacheLineIn``. The
old content is outputed on ``CacheLineOut`` and the old tag on ``OldAddress``,
both with a latency of one clock cycle.
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
| DATA_BITS          | positive | 8     |             |
## Ports

| Port name    | Direction | Type                                        | Description |
| ------------ | --------- | ------------------------------------------- | ----------- |
| Clock        | in        | std_logic                                   |             |
| Reset        | in        | std_logic                                   |             |
| Request      | in        | std_logic                                   |             |
| ReadWrite    | in        | std_logic                                   |             |
| Invalidate   | in        | std_logic                                   |             |
| Replace      | in        | std_logic                                   |             |
| Address      | in        | std_logic_vector(ADDRESS_BITS - 1 downto 0) |             |
| CacheLineIn  | in        | std_logic_vector(DATA_BITS - 1 downto 0)    |             |
| CacheLineOut | out       | std_logic_vector(DATA_BITS - 1 downto 0)    |             |
| CacheHit     | out       | std_logic                                   |             |
| CacheMiss    | out       | std_logic                                   |             |
| OldAddress   | out       | std_logic_vector(ADDRESS_BITS - 1 downto 0) |             |
## Signals

| Name                | Type                                           | Description       |
| ------------------- | ---------------------------------------------- | ----------------- |
| TU_LineIndex        | std_logic_vector(LINE_INDEX_BITS - 1 downto 0) | look-up (request) |
| TU_TagHit           | std_logic                                      |                   |
| TU_TagMiss          | std_logic                                      |                   |
| TU_ReplaceLineIndex | std_logic_vector(LINE_INDEX_BITS - 1 downto 0) | replace           |
| TU_OldAddress       | std_logic_vector(ADDRESS_BITS - 1 downto 0)    |                   |
| MemoryIndex_us      | unsigned(LINE_INDEX_BITS - 1 downto 0)         |                   |
| CacheMemory         | T_CACHE_LINE_VECTOR(CACHE_LINES - 1 downto 0)  |                   |
## Constants

| Name            | Type     | Value                    | Description |
| --------------- | -------- | ------------------------ | ----------- |
| LINE_INDEX_BITS | positive |  log2ceilnz(CACHE_LINES) |             |
## Types

| Name                | Type                                      | Description |
| ------------------- | ----------------------------------------- | ----------- |
| T_CACHE_LINE_VECTOR | array (natural range <>) of T_CACHE_LINE  |             |
## Processes
- unnamed: ( Clock )
## Instantiations

- TU: PoC.cache_tagunit_par
