# Entity: AxiStreamTap

- **File**: AxiStreamTap.vhd
## Diagram

![Diagram](AxiStreamTap.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:
 Block to extract and re-isnert a destination from an interleaved stream.
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
## Generics

| Generic name         | Type                   | Value | Description |
| -------------------- | ---------------------- | ----- | ----------- |
| TPD_G                | time                   | 1 ns  |             |
| TAP_DEST_G           | natural range 0 to 255 | 0     |             |
| PIPE_STAGES_G        | natural range 0 to 16  | 0     |             |
| ILEAVE_ON_NOTVALID_G | boolean                | false |             |
| ILEAVE_REARB_G       | natural                | 0     |             |
## Ports

| Port name    | Direction | Type                | Description      |
| ------------ | --------- | ------------------- | ---------------- |
| sAxisMaster  | in        | AxiStreamMasterType | Slave Interface  |
| sAxisSlave   | out       | AxiStreamSlaveType  |                  |
| mAxisMaster  | out       | AxiStreamMasterType | Master Interface |
| mAxisSlave   | in        | AxiStreamSlaveType  |                  |
| tmAxisMaster | out       | AxiStreamMasterType | Tap Interface    |
| tmAxisSlave  | in        | AxiStreamSlaveType  |                  |
| tsAxisMaster | in        | AxiStreamMasterType |                  |
| tsAxisSlave  | out       | AxiStreamSlaveType  |                  |
| axisClk      | in        | sl                  | Clock and reset  |
| axisRst      | in        | sl                  |                  |
## Signals

| Name        | Type                | Description |
| ----------- | ------------------- | ----------- |
| iAxisMaster | AxiStreamMasterType |             |
| iAxisSlave  | AxiStreamSlaveType  |             |
## Constants

| Name     | Type      | Value                                                                                                                                                      | Description |
| -------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| ROUTES_C | Slv8Array |  (0 => "--------",<br><span style="padding-left:20px">                                      1 => toSlv(TAP_DEST_G,<br><span style="padding-left:20px"> 8)) |             |
## Instantiations

- U_DeMux: surf.AxiStreamDeMux
- U_Mux: surf.AxiStreamMux
