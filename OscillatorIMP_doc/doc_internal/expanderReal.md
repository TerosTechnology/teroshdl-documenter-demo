# Expander Real

- **File**: expanderReal.vhd
- **Copyright:** OscillatorIMP Digital
- **File:** expanderReal
- **Author:** Gwenhael Goavec-Merou <gwenhael.goavec-merou@trabucayre.com>
- **Version:** 1
- **Date:** 2017/05/27
- **Brief:** Resize data stream by adding or suppressing Most Significant Bits

## Diagram

![Diagram](expanderReal.svg "Diagram")
## Description



 

 


 

 
## Generics

| Generic name  | Type    | Value    | Description                           |
| ------------- | ------- | -------- | ------------------------------------- |
| format        | string  | "signed" |  tell if stream is signed or unsigned |
| DATA_IN_SIZE  | natural | 16       |  size of the input data stream        |
| DATA_OUT_SIZE | natural | 16       |  size of the output data stream       |
## Ports

| Port name  | Direction | Type                                       | Description            |
| ---------- | --------- | ------------------------------------------ | ---------------------- |
| data_i     | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  | input data             |
| data_en_i  | in        | std_logic                                  |                        |
| data_sof_i | in        | std_logic                                  |                        |
| data_eof_i | in        | std_logic                                  |                        |
| data_rst_i | in        | std_logic                                  |                        |
| data_clk_i | in        | std_logic                                  |                        |
| data_o     | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) | for the next component |
| data_en_o  | out       | std_logic                                  |                        |
| data_sof_o | out       | std_logic                                  |                        |
| data_eof_o | out       | std_logic                                  |                        |
| data_rst_o | out       | std_logic                                  |                        |
| data_clk_o | out       | std_logic                                  |                        |
## Signals

| Name    | Type                                  | Description                            |
| ------- | ------------------------------------- | -------------------------------------- |
| msb_s   | std_logic_vector(MSB_SIZE-1 downto 0) |  dropped part of the I input signal    |
| is_zero | boolean                               |  check is high slice is fully 0 and 1  |
|  is_one | boolean                               |  check is high slice is fully 0 and 1  |
## Constants

| Name     | Type    | Value                                                                               | Description                                |
| -------- | ------- | ----------------------------------------------------------------------------------- | ------------------------------------------ |
| MSB_SIZE | natural |  comp_unused_slice(DATA_IN_SIZE,<br><span style="padding-left:20px"> DATA_OUT_SIZE) |  size of the dropped part of input signal  |
## Functions
- comp_unused_slice <font id="function_arguments">(in_size,<br><span style="padding-left:20px"> out_size: natural) </font> <font id="function_return">return natural </font>
