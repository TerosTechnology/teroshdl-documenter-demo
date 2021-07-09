# Entity: dataReal_dma_direct_handCom

## Diagram

![Diagram](dataReal_dma_direct_handCom.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2020/01/10
## Generics

| Generic name        | Type    | Value | Description                 |
| ------------------- | ------- | ----- | --------------------------- |
| C_S_AXI_DATA_WIDTH  | integer | 32    | Width of S_AXI data bus     |
| C_S_AXI_ADDR_WIDTH  | integer | 4     | Width of S_AXI address bus  |
| INTERNAL_ADDR_WIDTH | integer | 2     |                             |
## Ports

| Port name     | Direction | Type                                                | Description                                                                                                                                                                      |
| ------------- | --------- | --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S_AXI_ACLK    | in        | std_logic                                           | Global Clock Signal                                                                                                                                                              |
| S_AXI_RESET   | in        | std_logic                                           | Global Reset Signal. This Signal is Active LOW                                                                                                                                   |
| S_AXI_AWADDR  | in        | std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0)     | Write address (issued by master, acceped by Slave)                                                                                                                               |
| S_AXI_AWPROT  | in        | std_logic_vector(2 downto 0)                        | Write channel Protection type. This signal indicates theprivilege and security level of the transaction, and whether the transaction is a data access or an instruction access.  |
| S_AXI_AWVALID | in        | std_logic                                           | Write address valid. This signal indicates that the master signalingvalid write address and control information.                                                                 |
| S_AXI_AWREADY | out       | std_logic                                           | Write address ready. This signal indicates that the slave is readyto accept an address and associated control signals.                                                           |
| S_AXI_WSTRB   | in        | std_logic_vector((C_S_AXI_DATA_WIDTH/8)-1 downto 0) | Write strobes. This signal indicates which byte lanes holdvalid data. There is one write strobe bit for each eight bits of the write data bus.                                   |
| S_AXI_WVALID  | in        | std_logic                                           | Write valid. This signal indicates that valid writedata and strobes are available.                                                                                               |
| S_AXI_WREADY  | out       | std_logic                                           | Write ready. This signal indicates that the slavecan accept the write data.                                                                                                      |
| S_AXI_BRESP   | out       | std_logic_vector(1 downto 0)                        | Write response. This signal indicates the statusof the write transaction.                                                                                                        |
| S_AXI_BVALID  | out       | std_logic                                           | Write response valid. This signal indicates that the channelis signaling a valid write response.                                                                                 |
| S_AXI_BREADY  | in        | std_logic                                           | Response ready. This signal indicates that the mastercan accept a write response.                                                                                                |
| S_AXI_ARADDR  | in        | std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0)     | Read address (issued by master, acceped by Slave)                                                                                                                                |
| S_AXI_ARPROT  | in        | std_logic_vector(2 downto 0)                        | Protection type. This signal indicates the privilegeand security level of the transaction, and whether the transaction is a data access or an instruction access.                |
| S_AXI_ARVALID | in        | std_logic                                           | Read address valid. This signal indicates that the channelis signaling valid read address and control information.                                                               |
| S_AXI_ARREADY | out       | std_logic                                           | Read address ready. This signal indicates that the slave isready to accept an address and associated control signals.                                                            |
| S_AXI_RRESP   | out       | std_logic_vector(1 downto 0)                        | Read response. This signal indicates the status of theread transfer.                                                                                                             |
| S_AXI_RVALID  | out       | std_logic                                           | Read valid. This signal indicates that the channel issignaling the required read data.                                                                                           |
| S_AXI_RREADY  | in        | std_logic                                           | Read ready. This signal indicates that the master canaccept the read data and response information.                                                                              |
| addr_o        | out       | std_logic_vector(INTERNAL_ADDR_WIDTH-1 downto 0)    |                                                                                                                                                                                  |
| read_en_o     | out       | std_logic                                           |                                                                                                                                                                                  |
| write_en_o    | out       | std_logic                                           |                                                                                                                                                                                  |
## Signals

| Name          | Type                                             | Description |
| ------------- | ------------------------------------------------ | ----------- |
| axi_awaddr    | std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0)  |             |
| axi_awready   | std_logic                                        |             |
| axi_wready    | std_logic                                        |             |
| axi_bresp     | std_logic_vector(1 downto 0)                     |             |
| axi_bvalid    | std_logic                                        |             |
| axi_araddr    | std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0)  |             |
| axi_arready   | std_logic                                        |             |
| axi_rresp     | std_logic_vector(1 downto 0)                     |             |
| axi_rvalid    | std_logic                                        |             |
| slv_reg_rden  | std_logic                                        |             |
| slv_reg_wren  | std_logic                                        |             |
| addr_reg      | std_logic_vector(INTERNAL_ADDR_WIDTH-1 downto 0) |             |
|  addr_s       | std_logic_vector(INTERNAL_ADDR_WIDTH-1 downto 0) |             |
|  write_addr_s | std_logic_vector(INTERNAL_ADDR_WIDTH-1 downto 0) |             |
|  read_addr_s  | std_logic_vector(INTERNAL_ADDR_WIDTH-1 downto 0) |             |
## Constants

| Name     | Type    | Value                       | Description                                                                                                                                                                                                                            |
| -------- | ------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ADDR_LSB | integer |  (C_S_AXI_DATA_WIDTH/32)+ 1 | Example-specific design signalslocal parameter for addressing 32 bit / 64 bit C_S_AXI_DATA_WIDTHADDR_LSB is used for addressing 32/64 bit registers/memoriesADDR_LSB = 2 for 32 bits (n downto 2)ADDR_LSB = 3 for 64 bits (n downto 3) |
## Processes
- unnamed: ( S_AXI_ACLK )
**Description**
Implement axi_awready generation
axi_awready is asserted for one S_AXI_ACLK clock cycle when both
S_AXI_AWVALID and S_AXI_WVALID are asserted. axi_awready is
de-asserted when reset is low.

- unnamed: ( S_AXI_ACLK )
**Description**
Implement axi_awaddr latching
This process is used to latch the address when both 
S_AXI_AWVALID and S_AXI_WVALID are valid. 

- unnamed: ( S_AXI_ACLK )
**Description**
Implement axi_wready generation
axi_wready is asserted for one S_AXI_ACLK clock cycle when both
S_AXI_AWVALID and S_AXI_WVALID are asserted. axi_wready is 
de-asserted when reset is low. 

- unnamed: ( S_AXI_ACLK )
**Description**
Implement write response logic generation
The write response and response valid signals are asserted by the slave 
when axi_wready, S_AXI_WVALID, axi_wready and S_AXI_WVALID are asserted.  
This marks the acceptance of address and indicates the status of 
write transaction.

- unnamed: ( S_AXI_ACLK )
**Description**
Implement axi_arready generation
axi_arready is asserted for one S_AXI_ACLK clock cycle when
S_AXI_ARVALID is asserted. axi_awready is 
de-asserted when reset (active low) is asserted. 
The read address is also latched when S_AXI_ARVALID is 
asserted. axi_araddr is reset to zero on reset assertion.

- unnamed: ( S_AXI_ACLK )
**Description**
Implement axi_arvalid generation
axi_rvalid is asserted for one S_AXI_ACLK clock cycle when both 
S_AXI_ARVALID and axi_arready are asserted. The slave registers 
data are available on the axi_rdata bus at this instance. The 
assertion of axi_rvalid marks the validity of read data on the 
bus and axi_rresp indicates the status of read transaction.axi_rvalid 
is deasserted on reset (active low). axi_rresp and axi_rdata are 
cleared to zero on reset (active low).  

