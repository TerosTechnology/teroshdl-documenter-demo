# Entity: cache_replacement_policy
## Diagram
![Diagram](cache_replacement_policy.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Patrick Lehmann
									Martin Zabel
Entity:					Wrap different cache replacement policies.
Description:
-------------------------------------
**Supported policies:**
+----------+-----------------------+-----------+
| Abbr.    | Policies              | supported |
+==========+=======================+===========+
| RR       | round robin           | not yet   |
+----------+-----------------------+-----------+
| RAND     | random                | not yet   |
+----------+-----------------------+-----------+
| CLOCK    | clock algorithm       | not yet   |
+----------+-----------------------+-----------+
| LRU      | least recently used   | YES       |
+----------+-----------------------+-----------+
| LFU      | least frequently used | not yet   |
+----------+-----------------------+-----------+
**Command thruth table:**
+-----------+-----------+-------------+---------+-----------------------------------------------------+
| TagAccess | ReadWrite | Invalidate  | Replace | Command                                             |
+===========+===========+=============+=========+=====================================================+
|  0        |           |             |    0    | None                                                |
+-----------+-----------+-------------+---------+-----------------------------------------------------+
|  1        |    0      |    0        |    0    | TagHit and reading a cache line                     |
+-----------+-----------+-------------+---------+-----------------------------------------------------+
|  1        |    1      |    0        |    0    | TagHit and writing a cache line                     |
+-----------+-----------+-------------+---------+-----------------------------------------------------+
|  1        |    0      |    1        |    0    | TagHit and invalidate a  cache line (while reading) |
+-----------+-----------+-------------+---------+-----------------------------------------------------+
|  1        |    1      |    1        |    0    | TagHit and invalidate a  cache line (while writing) |
+-----------+-----------+-------------+---------+-----------------------------------------------------+
|  0        |           |    0        |    1    | Replace cache line                                  |
+-----------+-----------+-------------+---------+-----------------------------------------------------+
In a set-associative cache, each cache-set has its own instance of this component.
The input ``HitWay`` specifies the accessed way in a fully-associative or
set-associative cache.
The output ``ReplaceWay`` identifies the way which will be replaced as next by
a replace command. In a set-associative cache, this is the way in a specific
cache set (see above).
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
| CACHE_WAYS         | positive | 32    |             |
## Ports
| Port name  | Direction | Type                                                  | Description                      |
| ---------- | --------- | ----------------------------------------------------- | -------------------------------- |
| Clock      | in        | std_logic                                             |                                  |
| Reset      | in        | std_logic                                             |                                  |
| Replace    | in        | std_logic                                             | replacement interface            |
| ReplaceWay | out       | std_logic_vector(log2ceilnz(CACHE_WAYS) - 1 downto 0) |                                  |
| TagAccess  | in        | std_logic                                             | cacheline usage update interface |
| ReadWrite  | in        | std_logic                                             |                                  |
| Invalidate | in        | std_logic                                             |                                  |
| HitWay     | in        | std_logic_vector(log2ceilnz(CACHE_WAYS) - 1 downto 0) |                                  |
## Constants
| Name     | Type     | Value                   | Description |
| -------- | -------- | ----------------------- | ----------- |
| KEY_BITS | positive |  log2ceilnz(CACHE_WAYS) |             |
