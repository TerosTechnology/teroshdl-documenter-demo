# Entity: random

## Diagram

![Diagram](fpga-random.svg "Diagram")
## Description

Random number generator for Microwatt
Based on https://pdfs.semanticscholar.org/83ac/9e9c1bb3dad5180654984604c8d5d8137412.pdf
"High Speed True Random Number Generators in Xilinx FPGAs"
by Catalin Baetoniu, Xilinx Inc.
## Ports

| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| clk       | in        | std_ulogic                     |             |
| data      | out       | std_ulogic_vector(63 downto 0) |             |
| raw       | out       | std_ulogic_vector(63 downto 0) |             |
| err       | out       | std_ulogic                     |             |
## Signals

| Name    | Type                           | Description |
| ------- | ------------------------------ | ----------- |
| ringosc | std_ulogic_vector(63 downto 0) |             |
| ro_reg  | std_ulogic_vector(63 downto 0) |             |
| lhca    | std_ulogic_vector(63 downto 0) |             |
## Constants

| Name      | Type                           | Value                | Description |
| --------- | ------------------------------ | -------------------- | ----------- |
| lhca_diag | std_ulogic_vector(63 downto 0) |  x"fffffffffffffffb" |             |
## Processes
- random_osc: ( all )
- lhca_update: ( clk )
