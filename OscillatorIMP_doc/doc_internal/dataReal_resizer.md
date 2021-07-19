# Entity: dataReal_resizer

- **File**: dataReal_resizer.vhd
## Diagram

![Diagram](dataReal_resizer.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2018/12/16
## Generics

| Generic name | Type    | Value    | Description |
| ------------ | ------- | -------- | ----------- |
| IN_SZ        | natural | 32       |             |
| OUT_SZ       | natural | 32       |             |
| DATA_FORMAT  | string  | "signed" |             |
## Ports

| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| data_i    | in        | std_logic_vector(IN_SZ-1 downto 0)  |             |
| data_o    | out       | std_logic_vector(OUT_SZ-1 downto 0) |             |
