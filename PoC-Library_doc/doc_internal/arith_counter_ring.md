# Entity: arith_counter_ring

## Diagram

![Diagram](arith_counter_ring.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	Ring counter/Johnson Counter
Description:
-------------------------------------
This module implements an up/down ring-counter with loadable initial value
(``seed``) on reset. The counter can be configured to a Johnson counter by
enabling ``INVERT_FEEDBACK``. The number of counter bits is configurable with
``BITS``.
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

| Generic name    | Type     | Value | Description                                     |
| --------------- | -------- | ----- | ----------------------------------------------- |
| BITS            | positive |       |                                                 |
| INVERT_FEEDBACK | boolean  | FALSE | FALSE -> ring counter;		TRUE -> johnson counter |
## Ports

| Port name | Direction | Type                                | Description                         |
| --------- | --------- | ----------------------------------- | ----------------------------------- |
| Clock     | in        | std_logic                           | Clock                               |
| Reset     | in        | std_logic                           | Reset                               |
| seed      | in        | std_logic_vector(BITS - 1 downto 0) | initial counter vector / load value |
| inc       | in        | std_logic                           | increment counter                   |
| dec       | in        | std_logic                           | decrement counter                   |
| value     | out       | std_logic_vector(BITS - 1 downto 0) | counter value                       |
## Signals

| Name    | Type                                | Description |
| ------- | ----------------------------------- | ----------- |
| Counter | std_logic_vector(BITS - 1 downto 0) |             |
## Constants

| Name   | Type      | Value                   | Description |
| ------ | --------- | ----------------------- | ----------- |
| invert | std_logic |  to_sl(INVERT_FEEDBACK) |             |
## Processes
- unnamed: ( Clock )
