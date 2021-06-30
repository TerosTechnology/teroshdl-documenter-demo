# Entity: fifo_ic_assembly

## Diagram

![Diagram](fifo_ic_assembly.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Thomas B. Preusser
Entity:					Address-based FIFO stream assembly, independent clocks (ic)
Description:
-------------------------------------
This module assembles a FIFO stream from data blocks that may arrive
slightly out of order. The arriving data is ordered according to their
address. The streamed output starts with the data word written to
address zero (0) and may proceed all the way to just before the first yet
missing data. The association of data with addresses is used on the input
side for the sole purpose of reconstructing the correct order of the data.
It is assumed to wrap so as to allow an infinite input sequence. Addresses
are not actively exposed to the purely stream-based FIFO output.
The implemented functionality enables the reconstruction of streams that
are tunnelled across address-based transports that are allowed to reorder
the transmission of data blocks. This applies to many DMA implementations.
License:
=============================================================================
Copyright 2007-2016 Technische Universitaet Dresden - Germany
                    Chair of VLSI-Design, Diagnostics and Architecture
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

| Generic name | Type     | Value | Description           |
| ------------ | -------- | ----- | --------------------- |
| D_BITS       | positive |       | Data Width            |
| A_BITS       | positive |       | Address Bits          |
| G_BITS       | positive |       | Generation Guard Bits |
## Ports

| Port name | Direction | Type                                | Description                                                                                                                                                                                                                                                                                                                                                                          |
| --------- | --------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| clk_wr    | in        | std_logic                           | Write Interface                                                                                                                                                                                                                                                                                                                                                                      |
| rst_wr    | in        | std_logic                           |                                                                                                                                                                                                                                                                                                                                                                                      |
| base      | out       | std_logic_vector(A_BITS-1 downto 0) | Only write addresses in the range [base, base+2**(A_BITS-G_BITS)) areacceptable. This is equivalent to the test   tmp(A_BITS-1 downto A_BITS-G_BITS) = 0 where tmp = addr - base. Writes performed outside the allowable range will assert the failure indicator, which will stick until the next reset. No write is to be performed before base turns zero (0) for the first time.  |
| failed    | out       | std_logic                           |                                                                                                                                                                                                                                                                                                                                                                                      |
| addr      | in        | std_logic_vector(A_BITS-1 downto 0) |                                                                                                                                                                                                                                                                                                                                                                                      |
| din       | in        | std_logic_vector(D_BITS-1 downto 0) |                                                                                                                                                                                                                                                                                                                                                                                      |
| put       | in        | std_logic                           |                                                                                                                                                                                                                                                                                                                                                                                      |
| clk_rd    | in        | std_logic                           | Read Interface                                                                                                                                                                                                                                                                                                                                                                       |
| rst_rd    | in        | std_logic                           |                                                                                                                                                                                                                                                                                                                                                                                      |
| dout      | out       | std_logic_vector(D_BITS-1 downto 0) |                                                                                                                                                                                                                                                                                                                                                                                      |
| vld       | out       | std_logic                           |                                                                                                                                                                                                                                                                                                                                                                                      |
| got       | in        | std_logic                           |                                                                                                                                                                                                                                                                                                                                                                                      |
## Signals

| Name   | Type                                | Description         |
| ------ | ----------------------------------- | ------------------- |
| wa     | unsigned(AN-1 downto 0)             | Memory Connectivity |
| we     | std_logic                           |                     |
| di     | std_logic_vector(DN-1 downto 0)     |                     |
| ra     | unsigned(AN-1 downto 0)             |                     |
| do     | std_logic_vector(DN-1 downto 0)     |                     |
| OPgray | std_logic_vector(A_BITS-1 downto 0) | Cross-clock         |
## Constants

| Name | Type     | Value            | Description |
| ---- | -------- | ---------------- | ----------- |
| AN   | positive |  A_BITS - G_BITS |             |
| DN   | positive |  G_BITS + D_BITS |             |
## Instantiations

- ram: ocram_sdp
**Description**
Backing internal assembly memory

