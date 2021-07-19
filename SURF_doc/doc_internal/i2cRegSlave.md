# Entity: i2cRegSlave

- **File**: i2cRegSlave.sv
## Diagram

![Diagram](i2cRegSlave.svg "Diagram")
## Description

                             -*- Mode: Verilog -*-
 Filename        : i2cRegSlave.sv
 Description     : Implements an I2C slave attached to a generic RAM interface.
 Author          : Benjamin Reese
 Created On      : Mon Apr 22 10:04:49 2013
 Last Modified By: Benjamin Reese
 Last Modified On: Mon Apr 22 10:04:49 2013
 Update Count    : 0
 Status          : Unknown, Use with caution!
 i2cRegSlaveIntf
 
## Generics

| Generic name         | Type | Value | Description |
| -------------------- | ---- | ----- | ----------- |
| TPD_P                |      | 1     |             |
| TENBIT_P             |      | 0     |             |
| TENBIT_P             |      | 111   |             |
| OUTPUT_EN_POLARITY_P |      | 0     |             |
| FILTER_P             |      | 4     |             |
| ADDR_SIZE_P          |      | 2     | in bytes    |
| DATA_SIZE_P          |      | 2     | in bytes    |
| ENDIANNESS_P         |      | 0     |             |
## Ports

| Port name     | Direction | Type | Description |
| ------------- | --------- | ---- | ----------- |
| clk           | input     |      |             |
| sRst          | input     |      |             |
| i2cRegSlaveIO | input     |      |             |
| i2cBusIO      | input     |      |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | enum logic[1:0] {<br><span style="padding-left:20px"> IDLE_S,<br><span style="padding-left:20px"> ADDR_S,<br><span style="padding-left:20px"> WRITE_DATA_S,<br><span style="padding-left:20px"> READ_DATA_S }                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |             |
| RegType   | struct {<br><span style="padding-left:20px">       StateType state;<br><span style="padding-left:20px">       logic [3:0] 		   byteCount;<br><span style="padding-left:20px">       logic 			   enable;<br><span style="padding-left:20px">       logic [ADDR_SIZE_P-1:0][7:0] addr ;<br><span style="padding-left:20px">       logic [DATA_SIZE_P-1:0][7:0] wrData;<br><span style="padding-left:20px">       logic 			   wrEn;<br><span style="padding-left:20px">       logic 			   rdEn;<br><span style="padding-left:20px">               logic 			   txValid;<br><span style="padding-left:20px">       logic [7:0] 		   txData;<br><span style="padding-left:20px">      } |             |
## Processes
- unnamed: (  )
- unnamed: ( @(posedge clk) )
**Description**
always_comb

## Instantiations

- i2cSlaveIO: i2cSlaveIntf
- i2cSlaveInst: i2cSlave
**Description**
Instantiate I2C Slave

