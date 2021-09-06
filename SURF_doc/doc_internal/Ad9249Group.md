# Entity: Ad9249Group

- **File**: Ad9249Group.vhd
## Diagram

![Diagram](Ad9249Group.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: AD9249 Group Module
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

| Generic name     | Type    | Value | Description |
| ---------------- | ------- | ----- | ----------- |
| TPD_G            | time    | 1 ns  |             |
| CLK_PERIOD_G     | time    | 24 ns |             |
| DIVCLK_DIVIDE_G  | integer | 1     |             |
| CLKFBOUT_MULT_G  | integer | 49    |             |
| CLK_DCO_DIVIDE_G | integer | 49    |             |
| CLK_FCO_DIVIDE_G | integer | 7     |             |
## Ports

| Port name | Direction | Type                  | Description |
| --------- | --------- | --------------------- | ----------- |
| clk       | in        | sl                    |             |
| vin       | in        | RealArray(7 downto 0) |             |
| dP        | out       | slv(7 downto 0)       |             |
| dN        | out       | slv(7 downto 0)       |             |
| dcoP      | out       | sl                    |             |
| dcoN      | out       | sl                    |             |
| fcoP      | out       | sl                    |             |
| fcoN      | out       | sl                    |             |
| sclk      | in        | sl                    |             |
| sdio      | inout     | sl                    |             |
| csb       | in        | sl                    |             |
## Signals

| Name      | Type             | Description                                                                                                                                                                                                                                                                            |
| --------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| wrEn      | sl               |  ConfigSlave signals                                                                                                                                                                                                                                                                   |
| addr      | slv(12 downto 0) |                                                                                                                                                                                                                                                                                        |
| wrData    | slv(31 downto 0) |                                                                                                                                                                                                                                                                                        |
| byteValid | slv(3 downto 0)  |                                                                                                                                                                                                                                                                                        |
| r         | ConfigRegType    |                                                                                                                                                                                                                                                                                        |
| rin       | ConfigRegType    |                                                                                                                                                                                                                                                                                        |
| adcR      | AdcRegType       |                                                                                                                                                                                                                                                                                        |
| adcRin    | AdcRegType       |                                                                                                                                                                                                                                                                                        |
| pllRst    | sl               | -----------------------------------------------------------------------------------------------  Output constants and signals -----------------------------------------------------------------------------------------------    constant DCLK_PERIOD_C : time := CLK_PERIOD_G / 7.0;  |
| locked    | sl               |                                                                                                                                                                                                                                                                                        |
| rst       | sl               |                                                                                                                                                                                                                                                                                        |
| dClk      | sl               |                                                                                                                                                                                                                                                                                        |
| fClk      | sl               |                                                                                                                                                                                                                                                                                        |
| dco       | sl               |                                                                                                                                                                                                                                                                                        |
| fco       | sl               |                                                                                                                                                                                                                                                                                        |
| serData   | slv(7 downto 0)  |                                                                                                                                                                                                                                                                                        |
| cfgClk    | sl               |                                                                                                                                                                                                                                                                                        |
## Constants

| Name                  | Type              | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| --------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| CLK_PERIOD_C          | real              |  real(CLK_PERIOD_G / 1 ns)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |             |
| PN_SHORT_TAPS_C       | NaturalArray      |  (0 => 4,<br><span style="padding-left:20px"> 1 => 8)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  X9+X5+1    |
| PN_SHORT_INIT_C       | slv(8 downto 0)   |  "011011111"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| PN_LONG_TAPS_C        | NaturalArray      |  (0 => 16,<br><span style="padding-left:20px"> 1 => 22)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |  X23+X18+1  |
| PN_LONG_INIT_C        | slv(22 downto 0)  |  "01001101110000000101000"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |             |
| GLOBAL_CONFIG_INIT_C  | GlobalConfigType  |  (       pdwnMode          => "000",<br><span style="padding-left:20px">       pdwnPin           => '0',<br><span style="padding-left:20px">       stabilizer        => '1',<br><span style="padding-left:20px">       clockDivRatio     => "000",<br><span style="padding-left:20px">       outputLvds        => '0',<br><span style="padding-left:20px">       outputInvert      => '0',<br><span style="padding-left:20px">       binFormat         => "00",<br><span style="padding-left:20px">       termination       => "00",<br><span style="padding-left:20px">       driveStrength     => '0',<br><span style="padding-left:20px">       lsbFirst          => '0',<br><span style="padding-left:20px">       lowRate           => '0',<br><span style="padding-left:20px">       bits              => "000",<br><span style="padding-left:20px">       fullScaleAdj      => "100",<br><span style="padding-left:20px">       sampleRate        => "000",<br><span style="padding-left:20px">       resolution        => "00",<br><span style="padding-left:20px">       resSampleOverride => '0') |             |
| CHANNEL_CONFIG_INIT_C | ChannelConfigType |  (       pn23            => PN_LONG_INIT_C,<br><span style="padding-left:20px">       resetPnLongGen  => '0',<br><span style="padding-left:20px">       pn9             => PN_SHORT_INIT_C,<br><span style="padding-left:20px">       resetPnShortGen => '0',<br><span style="padding-left:20px">       userTestMode    => "00",<br><span style="padding-left:20px">       outputTestMode  => "0000",<br><span style="padding-left:20px">       outputPhase     => "0011",<br><span style="padding-left:20px">       userPattern1    => X"0000",<br><span style="padding-left:20px">       userPattern2    => X"0000",<br><span style="padding-left:20px">       outputReset     => '0',<br><span style="padding-left:20px">       powerDown       => '0',<br><span style="padding-left:20px">       chopMode        => '0',<br><span style="padding-left:20px">       offsetAdjust    => X"00")                                                                                                                                                                                                            |             |
| CONFIG_REG_INIT_C     | ConfigRegType     |  (       rdData          => X"00000000",<br><span style="padding-left:20px">       lsbFirst        => '0',<br><span style="padding-left:20px">       softReset       => '0',<br><span style="padding-left:20px">       channelConfigEn => "1111111111",<br><span style="padding-left:20px">       global          => GLOBAL_CONFIG_INIT_C,<br><span style="padding-left:20px">       channel         => (others => CHANNEL_CONFIG_INIT_C))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |             |
| ADC_REG_INIT_C        | AdcRegType        |  (       sample => (others => (others => (others => '0'))),<br><span style="padding-left:20px">       word   => '0')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |             |
## Types

| Name               | Type                                                | Description                                                                                      |
| ------------------ | --------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| GlobalConfigType   |                                                     |                                                                                                  |
| ChannelConfigType  |                                                     |                                                                                                  |
| ChannelConfigArray | array (natural range <>) of ChannelConfigType       |                                                                                                  |
| Slv14x8Array       | array (natural range <>) of Slv14Array(7 downto 0)  |                                                                                                  |
| ConfigRegType      |                                                     |                                                                                                  |
| AdcRegType         |                                                     | -----------------------------------------------------------------------------------------------  |
## Processes
- unnamed: (  )
</br>**Description**
 [out] -----------------------------------------------------------------------------------------------  Create local clocks -----------------------------------------------------------------------------------------------    ClkRst_1 : entity surf.ClkRst       generic map (          RST_HOLD_TIME_G => 50 us)       port map (          rst => pllRst); 
- comb: ( addr, r, vin, wrData, wrEn )
</br>**Description**
-----------------------------------------------------------------------------------------------  Configuration register logic ----------------------------------------------------------------------------------------------- 
- seq: ( cfgClk )
- adcComb: ( adcR )
- adcSeq: ( fClk )
## Instantiations

- U_ClkRst_1: surf.ClkRst
- U_CtrlClockManager7: surf.ClockManager7
</br>**Description**
-----------------------------------------------------------------------------------------------
 Use a clock manager to create the serial clock
 There's probably a better way but this works.
-----------------------------------------------------------------------------------------------

- RstSync_1: surf.RstSync
- AdiConfigSlave_1: surf.AdiConfigSlave
</br>**Description**
-----------------------------------------------------------------------------------------------
 Instantiate configuration interface
-----------------------------------------------------------------------------------------------

- FCLK_OUT_BUFF: surf.ClkOutBufDiff
- DCLK_OUT_BUFF: surf.ClkOutBufDiff
