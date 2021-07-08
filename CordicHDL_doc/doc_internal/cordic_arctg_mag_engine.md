# Entity: cordic_arctg_mag_engine

## Diagram

![Diagram](cordic_arctg_mag_engine.svg "Diagram")
## Description

 Standard library.
 Implementation of arctg-magnitude cordic
## Ports

| Port name | Direction | Type                           | Description              |
| --------- | --------- | ------------------------------ | ------------------------ |
| clk       | in        | std_logic                      |  Clock.                  |
| dv_in     | in        | std_logic                      |  Data valid input.       |
| x_in      | in        | std_logic_vector (19 downto 0) |  x in Q2.17 format [0,1] |
| y_in      | in        | std_logic_vector (19 downto 0) |  y in Q2.17 format [0,1] |
| arctg_out | out       | std_logic_vector (19 downto 0) |  arctan(y/x)             |
| mag_out   | out       | std_logic_vector (19 downto 0) |  magnitude sqrt(x*x+y*y) |
| dv_out    | out       | std_logic                      |  Data valid output.      |
## Signals

| Name        | Type                                         | Description |
| ----------- | -------------------------------------------- | ----------- |
| r0_x        | signed(c_SIZE_INPUT-1 downto 0)              |             |
| r0_y        | signed(c_SIZE_INPUT-1 downto 0)              |             |
| r0_dv       | std_logic                                    |             |
| r1_x_input  | typea_input                                  |             |
| r1_y_input  | typea_input                                  |             |
| r1_x        | typea_input                                  |             |
| r1b_x_bis   | typea_input                                  |             |
| r1_y        | typea_input                                  |             |
| r1b_y_bis   | typea_input                                  |             |
| r1_z        | typea_input                                  |             |
| r1_shift_dv | std_logic_vector(c_SIZE_INPUT-1 downto 0)    |             |
| r2_arctg    | signed(c_SIZE_INPUT-1 downto 0)              |             |
| r2_mag      | signed(2*c_SIZE_INPUT-c_SIZE_INT-1 downto 0) |             |
| r2b_mag     | signed(c_SIZE_INPUT-1 downto 0)              |             |
| r2_dv       | std_logic                                    |             |
## Constants

| Name         | Type                                       | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description |
| ------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| c_SIZE_INPUT | integer                                    |  20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| c_SIZE_INT   | integer                                    |   2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| c_SIZE_DECIM | integer                                    |  17                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| c_Z_INIT     | signed(c_SIZE_INPUT-1 downto 0)            |  "00000000000000000000"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
| c_NUM_STAGES | integer                                    |  16                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| r1_ang       | typea_inputa                               |  (     "011001001000011111",<br><span style="padding-left:20px">"001110110101100011",<br><span style="padding-left:20px">"000111110101101101",<br><span style="padding-left:20px">"000011111110101011",<br><span style="padding-left:20px">     "000001111111110101",<br><span style="padding-left:20px">"000000111111111110",<br><span style="padding-left:20px">"000000011111111111",<br><span style="padding-left:20px">"000000001111111111",<br><span style="padding-left:20px">     "000000000111111111",<br><span style="padding-left:20px">"000000000011111111",<br><span style="padding-left:20px">"000000000001111111",<br><span style="padding-left:20px">"000000000000111111",<br><span style="padding-left:20px">     "000000000000011111",<br><span style="padding-left:20px">"000000000000001111",<br><span style="padding-left:20px">"000000000000000111",<br><span style="padding-left:20px">"000000000000000011"   ) |             |
| c_CORRECTION | signed(c_SIZE_INPUT-c_SIZE_INT-1 downto 0) |  "010011011011101001"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |             |
## Types

| Name         | Type | Description |
| ------------ | ---- | ----------- |
| typea_input  |      |             |
| typea_inputa |      |             |
## Processes
- r0_reg_input: ( clk )
- r1_shift: ( clk )
- r1_start_cordic: ( clk )
- r2_cordic_correction: ( clk )
