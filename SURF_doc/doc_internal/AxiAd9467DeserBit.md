# Entity: AxiAd9467DeserBit

- **File**: AxiAd9467DeserBit.vhd
## Diagram

![Diagram](AxiAd9467DeserBit.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: AD9467 Deserializer Bit Module
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

| Generic name    | Type            | Value                    | Description |
| --------------- | --------------- | ------------------------ | ----------- |
| TPD_G           | time            | 1 ns                     |             |
| DELAY_INIT_G    | slv(4 downto 0) | (others => '0')          |             |
| IODELAY_GROUP_G | string          | "AXI_AD9467_IODELAY_GRP" |             |
## Ports

| Port name    | Direction | Type            | Description                    |
| ------------ | --------- | --------------- | ------------------------------ |
| dataP        | in        | sl              | ADC Data (clk domain)          |
| dataN        | in        | sl              |                                |
| Q1           | out       | sl              |                                |
| Q2           | out       | sl              |                                |
| delayInLoad  | in        | sl              | IO_Delay (refClk200MHz domain) |
| delayInData  | in        | slv(4 downto 0) |                                |
| delayOutData | out       | slv(4 downto 0) |                                |
| clk          | in        | sl              | Clocks                         |
| refClk200MHz | in        | sl              |                                |
## Signals

| Name           | Type | Description |
| -------------- | ---- | ----------- |
| data           | sl   |             |
| 
      dataDly | sl   |             |
## Instantiations

- IBUFDS_Inst: IBUFDS
- IDELAYE2_inst: IDELAYE2
- IDDR_Inst: IDDR
</br>**Description**
 1-bit input: Active-high reset tap-delay input

