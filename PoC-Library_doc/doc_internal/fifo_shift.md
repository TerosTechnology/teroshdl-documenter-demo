# Entity: fifo_shift

## Diagram

![Diagram](fifo_shift.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Thomas B. Preusser
Entity:					FIFO, common clock, pipelined interface
Description:
-------------------------------------
This FIFO implementation is based on an internal shift register. This is
especially useful for smaller FIFO sizes, which can be implemented in LUT
storage on some devices (e.g. Xilinx' SRLs). Only a single read pointer is
maintained, which determines the number of valid entries within the
underlying shift register.
The specified depth (``MIN_DEPTH``) is rounded up to the next suitable value.
License:
=============================================================================
Copyright 2007-2014 Technische Universitaet Dresden - Germany,
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

| Generic name | Type     | Value | Description                |
| ------------ | -------- | ----- | -------------------------- |
| D_BITS       | positive |       | Data Width                 |
| MIN_DEPTH    | positive |       | Minimum FIFO Size in Words |
## Ports

| Port name | Direction | Type                                | Description        |
| --------- | --------- | ----------------------------------- | ------------------ |
| clk       | in        | std_logic                           | Global Control     |
| rst       | in        | std_logic                           |                    |
| put       | in        | std_logic                           | Write Request      |
| din       | in        | std_logic_vector(D_BITS-1 downto 0) | Input Data         |
| ful       | out       | std_logic                           | Capacity Exhausted |
| got       | in        | std_logic                           | Read Done Strobe   |
| dout      | out       | std_logic_vector(D_BITS-1 downto 0) | Output Data        |
| vld       | out       | std_logic                           | Data Valid         |
## Signals

| Name | Type                                     | Description |
| ---- | ---------------------------------------- | ----------- |
| Dat  | tData(0 to MIN_DEPTH-1)                  |             |
| Ptr  | unsigned(log2ceilnz(MIN_DEPTH) downto 0) |             |
## Types

| Name  | Type                                                           | Description |
| ----- | -------------------------------------------------------------- | ----------- |
| tData | array(natural range<>) of std_logic_vector(D_BITS-1 downto 0)  |             |
## Processes
- unnamed: ( clk )
- unnamed: ( clk )
