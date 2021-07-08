# Entity: DCIRESET

## Diagram

![Diagram](DCIRESET.svg "Diagram")
## Description

   Copyright (c) 1995/2009 Xilinx, Inc.
 
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
 
        http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
   ____  ____
  /   /\/   /
 /___/  \  /    Vendor : Xilinx
 \   \   \/     Version : 10.1
  \   \         Description : Xilinx Functional Simulation Library Component
  /   /                  Reset for DCI State Machine
 /___/   /\     Filename : DCIRESET.v
 \   \  /  \    Timestamp : Thu Mar 25 16:43:43 PST 2004
  \___\/\___\
 Revision:
    03/23/04 - Initial version.
    12/13/11 - Added `celldefine and `endcelldefine (CR 524859).
 End Revision
 
## Generics

| Generic name | Type | Value      | Description |
| ------------ | ---- | ---------- | ----------- |
| LOC          |      | "UNPLACED" |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| LOCKED    | output    |      |             |
| RST       | input     |      |             |
## Signals

| Name           | Type | Description |
| -------------- | ---- | ----------- |
| sample_rising  | time |             |
| sample_falling | time |             |
## Processes
- unnamed: ( @(RST) )
