# Entity: mean_vector_axi_logic

## Diagram

![Diagram](mean_vector_axi_logic.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
2013-2019
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| ADDR_SIZE    | natural | 10    |             |
| ACCUM_SIZE   | natural | 10    |             |
| SHIFT_SIZE   | natural | 4     |             |
| DATA_SIZE    | natural | 16    |             |
## Ports

| Port name   | Direction | Type                                    | Description   |
| ----------- | --------- | --------------------------------------- | ------------- |
| rst_i       | in        | std_logic                               |               |
| clk_i       | in        | std_logic                               |               |
| shift_val_i | in        | std_logic_vector(SHIFT_SIZE-1 downto 0) | configuration |
| nb_iter_i   | in        | std_logic_vector(ACCUM_SIZE-1 downto 0) |               |
| data_i_i    | in        | std_logic_vector(DATA_SIZE-1 downto 0)  | input         |
| data_q_i    | in        | std_logic_vector(DATA_SIZE-1 downto 0)  |               |
| data_en_i   | in        | std_logic                               |               |
| data_eof_i  | in        | std_logic                               |               |
| data_i_o    | out       | std_logic_vector(DATA_SIZE-1 downto 0)  | output        |
| data_q_o    | out       | std_logic_vector(DATA_SIZE-1 downto 0)  |               |
| data_en_o   | out       | std_logic                               |               |
| data_eof_o  | out       | std_logic                               |               |
## Signals

| Name             | Type                                            | Description          |
| ---------------- | ----------------------------------------------- | -------------------- |
| first_data_en_s  | std_logic                                       |                      |
| ready_s          | std_logic                                       |                      |
| count_s          | natural range 0 to 2**ADDR_SIZE-1               |                      |
| count_frame_s    | std_logic_vector(ACCUM_SIZE-1 downto 0)         |                      |
| data_en_s        | std_logic                                       |                      |
| data_eof_s       | std_logic                                       |                      |
|  data_eof_next_s | std_logic                                       |                      |
| data_i_s         | std_logic_vector(DATA_SIZE-1 downto 0)          |                      |
|  data_q_s        | std_logic_vector(DATA_SIZE-1 downto 0)          |                      |
| dat_add_i_s      | std_logic_vector(INTERNAL_DATA_SIZE-1 downto 0) |                      |
| dat_add_q_s      | std_logic_vector(INTERNAL_DATA_SIZE-1 downto 0) |                      |
| last_frame_s     | std_logic                                       |                      |
| data_in_i_s      | std_logic_vector(INTERNAL_DATA_SIZE-1 downto 0) | ram                  |
| data_in_q_s      | std_logic_vector(INTERNAL_DATA_SIZE-1 downto 0) |                      |
| d_ram_read_i_s   | std_logic_vector(INTERNAL_DATA_SIZE-1 downto 0) |                      |
| d_ram_read_q_s   | std_logic_vector(INTERNAL_DATA_SIZE-1 downto 0) |                      |
| write_addr_s     | std_logic_vector(ADDR_SIZE-1 downto 0)          |                      |
| read_addr_s      | std_logic_vector(ADDR_SIZE-1 downto 0)          |                      |
| prep_next_tr_s   | std_logic                                       | prepare transmission |
| d_final_i_s      | std_logic_vector(TEMP_SIZE-1 downto 0)          |                      |
| d_final_q_s      | std_logic_vector(TEMP_SIZE-1 downto 0)          |                      |
## Constants

| Name               | Type    | Value                        | Description |
| ------------------ | ------- | ---------------------------- | ----------- |
| INTERNAL_DATA_SIZE | natural |  DATA_SIZE + (2**SHIFT_SIZE) |             |
| TEMP_SIZE          | natural |  INTERNAL_DATA_SIZE          |             |
## Processes
- unnamed: ( clk_i )
**Description**
latch data from previous block
for security and time propagation

- unnamed: ( clk_i )
**Description**
frame synchro:
wait for the first eof before starting
propagation.
Avoid to propagate a partial frame

- unnamed: ( clk_i )
**Description**
when count_frame = NB_FRAME 
ie last accum
serie of data is propagated instead of
storing in a ram

- unnamed: ( clk_i )
**Description**
counter data part
incr for each new data
reset when eof is received

- unnamed: ( clk_i )
**Description**
counter frame part
incr for each new eof
reset when overflow

## Instantiations

- d_i: work.mean_vector_axi_shift
- d_q: work.mean_vector_axi_shift
- ram_i: work.mean_vector_axi_ram
- ram_q: work.mean_vector_axi_ram
