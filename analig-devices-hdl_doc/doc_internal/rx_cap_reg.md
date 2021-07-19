# Entity: rx_cap_reg

- **File**: rx_cap_reg.vhd
## Diagram

![Diagram](rx_cap_reg.svg "Diagram")
## Description

CVS Revision History
$Log: not supported by cvs2svn $
Revision 1.4  2004/07/19 16:58:37  gedra
Fixed bug.
Revision 1.3  2004/06/27 16:16:55  gedra
Signal renaming and bug fix.
Revision 1.2  2004/06/26 14:14:47  gedra
Converted to numeric_std and fixed a few bugs.
Revision 1.1  2004/06/05 17:16:46  gedra
Channel status/user data capture register
## Ports

| Port name      | Direction | Type                          | Description                 |
| -------------- | --------- | ----------------------------- | --------------------------- |
| clk            | in        | std_logic                     | clock                       |
| rst            | in        | std_logic                     | reset                       |
| cap_reg        | in        | std_logic_vector(31 downto 0) |                             |
| cap_din        | in        | std_logic_vector(31 downto 0) | write data                  |
| rx_block_start | in        | std_logic                     | start of block signal       |
| ch_data        | in        | std_logic                     | channel status/user data    |
| ud_a_en        | in        | std_logic                     | user data ch. A enable      |
| ud_b_en        | in        | std_logic                     | user data ch. B enable      |
| cs_a_en        | in        | std_logic                     | channel status ch. A enable |
| cs_b_en        | in        | std_logic                     | channel status ch. B enable |
| cap_dout       | out       | std_logic_vector(31 downto 0) | read data                   |
| cap_evt        | out       | std_logic                     |                             |
## Signals

| Name           | Type                          | Description |
| -------------- | ----------------------------- | ----------- |
| cap_ctrl_bits  | std_logic_vector(31 downto 0) |             |
|  cap_ctrl_dout | std_logic_vector(31 downto 0) |             |
| cap_reg_1      | std_logic_vector(31 downto 0) |             |
|  cap_new       | std_logic_vector(31 downto 0) |             |
| bitlen         | integer range 0 to 63         |             |
|  cap_len       | integer range 0 to 63         |             |
| bitpos         | integer range 0 to 255        |             |
|  cur_pos       | integer range 0 to 255        |             |
| chid           | std_logic                     |             |
|  cdata         | std_logic                     |             |
|  compared      | std_logic                     |             |
| d_enable       | std_logic_vector(3 downto 0)  |             |
## Processes
- CDAT: ( clk, rst )
**Description**
capture data register

