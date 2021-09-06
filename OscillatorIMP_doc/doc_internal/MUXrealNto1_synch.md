# Entity: MUXrealNto1_synch

- **File**: MUXrealNto1_synch.vhd
## Diagram

![Diagram](MUXrealNto1_synch.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 modified: Ivan Ryger <om1air@gmail.com>
 Creation date : 2015/04/08
 last modified : 2021/06/11
-------------------------------------------------------------------------
## Generics

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| STAGES       | natural  | 3     |             |
| REG_WIDTH    | positive | 4     |             |
## Ports

| Port name | Direction | Type                                     | Description |
| --------- | --------- | ---------------------------------------- | ----------- |
| ref_clk_i | in        | std_logic                                |             |
| clk_i     | in        | std_logic                                |             |
| data_i    | in        | std_logic_vector(REG_WIDTH - 1 downto 0) |  ***        |
| data_o    | out       | std_logic_vector(REG_WIDTH - 1 downto 0) |  ***        |
## Signals

| Name          | Type                                        | Description                                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sync_stage0_s | std_logic_vector(REG_WIDTH - 1 downto 0)    |  ***	                                                                                                                                                                                                                                    |
| flipflops     | STD_LOGIC_VECTOR_ARRAY(STAGES - 1 downto 0) | signal flipflops : std_logic_vector(stages -1 downto 0) := (others => '0'); signal flipflops : std_logic_vector(STAGES*REG_WIDTH - 1 downto 0); signal flipflops : STD_LOGIC_VECTOR_ARRAY_T(0 to STAGES - 1)(REG_WIDTH - 1 downto 0);  |
## Types

| Name                   | Type                                                                | Description |
| ---------------------- | ------------------------------------------------------------------- | ----------- |
| STD_LOGIC_VECTOR_ARRAY | array(natural range<>) of std_logic_Vector(REG_WIDTH - 1 downto 0)  |             |
## Processes
- ref_proc: ( ref_clk_i )
- sync_proc: ( clk_i )
