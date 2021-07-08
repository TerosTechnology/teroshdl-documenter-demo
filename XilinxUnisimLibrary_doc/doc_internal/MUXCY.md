# Entity: MUXCY

## Diagram

![Diagram](MUXCY.svg "Diagram")
## Description

   Copyright (c) 1995/2004 Xilinx, Inc.
 
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
  /   /                  2-to-1 Multiplexer for Carry Logic with General Output
 /___/   /\     Filename : MUXCY.v
 \   \  /  \    Timestamp : Thu Mar 25 16:42:55 PST 2004
  \___\/\___\
 Revision:
    03/23/04 - Initial version.
    02/04/05 - Rev 0.0.1 Remove input/output bufs; Remove unnessasary begin/end;
    05/10/07 - When input same, output same for any sel value. (CR434611).
    08/23/07 - User block statement (CR446704).
    12/13/11 - Added `celldefine and `endcelldefine (CR 524859).
 End Revision
 
## Generics

| Generic name | Type | Value      | Description |
| ------------ | ---- | ---------- | ----------- |
| LOC          |      | "UNPLACED" |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| O         | output    |      |             |
| CI        | input     |      |             |
|  DI       | input     |      |             |
|  S        | input     |      |             |
## Signals

| Name  | Type | Description |
| ----- | ---- | ----------- |
| O_out | reg  |             |
## Processes
- unnamed: ( @(CI or DI or S) )
