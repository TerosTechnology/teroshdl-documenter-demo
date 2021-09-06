# Entity: dataComplex_resizer

- **File**: dataComplex_resizer.vhd
## Diagram

![Diagram](dataComplex_resizer.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 Creation date : 2018/11/30
-------------------------------------------------------------------------
## Generics

| Generic name | Type    | Value    | Description |
| ------------ | ------- | -------- | ----------- |
| IN_SZ        | natural | 32       |             |
| OUT_SZ       | natural | 32       |             |
| DATA_FORMAT  | string  | "signed" |             |
## Ports

| Port name | Direction | Type                                    | Description |
| --------- | --------- | --------------------------------------- | ----------- |
| data_i_i  | in        | std_logic_vector(IN_SZ-1 downto 0)      |             |
| data_q_i  | in        | std_logic_vector(IN_SZ-1 downto 0)      |             |
| data_o    | out       | std_logic_vector((2*OUT_SZ)-1 downto 0) |             |
