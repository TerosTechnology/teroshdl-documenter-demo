# Entity: i2c_master_byte_ctrl

- **File**: i2c_master_byte_ctrl.vhd
## Diagram

![Diagram](i2c_master_byte_ctrl.svg "Diagram")
## Description

 CVS Log
 $Id: i2c_master_byte_ctrl.vhd,v 1.5 2004/02/18 11:41:48 rherveille Exp $
 $Date: 2004/02/18 11:41:48 $
 $Revision: 1.5 $
 $Author: rherveille $
 $Locker:  $
 $State: Exp $
Change History:
              $Log: i2c_master_byte_ctrl.vhd,v $
              Revision 1.5  2004/02/18 11:41:48  rherveille
              Fixed a potential bug in the statemachine. During a 'stop' 2 cmd_ack signals were generated. Possibly canceling a new start command.
              Revision 1.4  2003/08/09 07:01:13  rherveille
              Fixed a bug in the Arbitration Lost generation caused by delay on the (external) sda line.
              Fixed a potential bug in the byte controller's host-acknowledge generation.
              Revision 1.3  2002/12/26 16:05:47  rherveille
              Core is now a Multimaster I2C controller.
              Revision 1.2  2002/11/30 22:24:37  rherveille
              Cleaned up code
              Revision 1.1  2001/11/05 12:02:33  rherveille
              Split i2c_master_core.vhd into separate files for each entity; same layout as verilog version.
              Code updated, is now up-to-date to doc. rev.0.4.
              Added headers.
Modified by Jan Andersson (jan@gaisler.com:.
     Changed std_logic_arith to numeric_std.
     Propagate filter generic
Byte controller section
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| filter       | integer |       |             |
| dynfilt      | integer |       |             |
## Ports

| Port name | Direction | Type                                          | Description                                         |
| --------- | --------- | --------------------------------------------- | --------------------------------------------------- |
| clk       | in        | std_logic                                     |                                                     |
| rst       | in        | std_logic                                     | synchronous active high reset (WISHBONE compatible) |
| nReset    | in        | std_logic                                     | asynchornous active low reset (FPGA compatible)     |
| ena       | in        | std_logic                                     | core enable signal                                  |
| clk_cnt   | in        | std_logic_vector(15 downto 0)                 | 4x SCL                                              |
| start     | in        | std_logic                                     | input signals                                       |
| stop      | in        | std_logic                                     |                                                     |
| read      | in        | std_logic                                     |                                                     |
| write     | in        | std_logic                                     |                                                     |
| ack_in    | in        | std_logic                                     |                                                     |
| din       | in        | std_logic_vector(7 downto 0)                  |                                                     |
| filt      | in        | std_logic_vector((filter-1)*dynfilt downto 0) |                                                     |
| cmd_ack   | out       | std_logic                                     | command done                                        |
| ack_out   | out       | std_logic                                     |                                                     |
| i2c_busy  | out       | std_logic                                     | arbitration lost                                    |
| i2c_al    | out       | std_logic                                     | i2c bus busy                                        |
| dout      | out       | std_logic_vector(7 downto 0)                  |                                                     |
| scl_i     | in        | std_logic                                     | i2c clock line input                                |
| scl_o     | out       | std_logic                                     | i2c clock line output                               |
| scl_oen   | out       | std_logic                                     | i2c clock line output enable, active low            |
| sda_i     | in        | std_logic                                     | i2c data line input                                 |
| sda_o     | out       | std_logic                                     | i2c data line output                                |
| sda_oen   | out       | std_logic                                     | i2c data line output enable, active low             |
## Signals

| Name      | Type                         | Description                                                                                                                                           |
| --------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| core_cmd  | std_logic_vector(3 downto 0) | signals for bit_controller                                                                                                                            |
| core_ack  | std_logic                    |                                                                                                                                                       |
|  core_txd | std_logic                    |                                                                                                                                                       |
|  core_rxd | std_logic                    |                                                                                                                                                       |
| al        | std_logic                    |                                                                                                                                                       |
| sr        | std_logic_vector(7 downto 0) | 8bit shift register                                                                                                                                   |
| shift     | std_logic                    |                                                                                                                                                       |
|  ld       | std_logic                    |                                                                                                                                                       |
| go        | std_logic                    | signals for state machine                                                                                                                             |
|  host_ack | std_logic                    | signals for state machine                                                                                                                             |
| dcnt      | std_logic_vector(2 downto 0) | Added init value to dcnt to prevent simulation meta-value- jan@gaisler.comremoved init value as it is not compatible with Formality- jiri@gaisler.com |
| cnt_done  | std_logic                    | data counter                                                                                                                                          |
## Constants

| Name          | Type                         | Value   | Description                       |
| ------------- | ---------------------------- | ------- | --------------------------------- |
| I2C_CMD_NOP   | std_logic_vector(3 downto 0) |  "0000" | commands for bit_controller block |
| I2C_CMD_START | std_logic_vector(3 downto 0) |  "0001" |                                   |
| I2C_CMD_STOP  | std_logic_vector(3 downto 0) |  "0010" |                                   |
| I2C_CMD_READ  | std_logic_vector(3 downto 0) |  "0100" |                                   |
| I2C_CMD_WRITE | std_logic_vector(3 downto 0) |  "1000" |                                   |
## Processes
- shift_register: ( clk, nReset )
**Description**
generate shift register

- data_cnt: ( clk, nReset )
**Description**
generate data-counter

## Instantiations

- bit_ctrl: i2c_master_bit_ctrl
