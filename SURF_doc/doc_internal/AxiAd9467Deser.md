# Entity: AxiAd9467Deser

## Diagram

![Diagram](AxiAd9467Deser.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Wrapper for AxiAd9467DeserBit modules
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name    | Type              | Value                    | Description |
| --------------- | ----------------- | ------------------------ | ----------- |
| TPD_G           | time              | 1 ns                     |             |
| DELAY_INIT_G    | Slv5Array(0 to 7) | (others => "00000")      |             |
| IODELAY_GROUP_G | string            | "AXI_AD9467_IODELAY_GRP" |             |
## Ports

| Port name    | Direction | Type                  | Description      |
| ------------ | --------- | --------------------- | ---------------- |
| adcDataOrP   | in        | sl                    |                  |
| adcDataOrN   | in        | sl                    |                  |
| adcDataInP   | in        | slv(7 downto 0)       |                  |
| adcDataInN   | in        | slv(7 downto 0)       |                  |
| adcClk       | in        | sl                    | ADC Interface    |
| adcRst       | in        | sl                    |                  |
| adcData      | out       | slv(15 downto 0)      |                  |
| refClk200Mhz | in        | sl                    | IDELAY Interface |
| delayin      | in        | AxiAd9467DelayInType  |                  |
| delayOut     | out       | AxiAd9467DelayOutType |                  |
## Signals

| Name             | Type            | Description |
| ---------------- | --------------- | ----------- |
| adcDataPs        | slv(7 downto 0) |             |
| 
      adcDataNs | slv(7 downto 0) |             |
| 
      adcDataP  | slv(7 downto 0) |             |
| 
      adcDataN  | slv(7 downto 0) |             |
| 
      adcDataNd | slv(7 downto 0) |             |
| 
      adcDmuxA  | slv(7 downto 0) |             |
| 
      adcDmuxB  | slv(7 downto 0) |             |
## Processes
- unnamed: ( adcClk )
## Instantiations

- IBUFDS_OR: IBUFDS
- IDELAYCTRL_Inst: IDELAYCTRL
