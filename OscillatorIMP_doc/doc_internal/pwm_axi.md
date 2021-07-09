# Entity: pwm_axi

## Diagram

![Diagram](pwm_axi.svg "Diagram")
## Generics

| Generic name         | Type    | Value | Description |
| -------------------- | ------- | ----- | ----------- |
| ID                   | natural | 0     |             |
| COUNTER_SIZE         | natural | 32    |             |
| C_S00_AXI_DATA_WIDTH | integer | 32    |             |
| C_S00_AXI_ADDR_WIDTH | integer | 5     |             |
## Ports

| Port name       | Direction | Type                                                  | Description   |
| --------------- | --------- | ----------------------------------------------------- | ------------- |
| s00_axi_reset   | in        | std_logic                                             | CANDR signals |
| s00_axi_aclk    | in        | std_logic                                             |               |
| s00_axi_awaddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)     | AXI signals   |
| s00_axi_awprot  | in        | std_logic_vector(2 downto 0)                          |               |
| s00_axi_awvalid | in        | std_logic                                             |               |
| s00_axi_awready | out       | std_logic                                             |               |
| s00_axi_wdata   | in        | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)     |               |
| s00_axi_wstrb   | in        | std_logic_vector((C_S00_AXI_DATA_WIDTH/8)-1 downto 0) |               |
| s00_axi_wvalid  | in        | std_logic                                             |               |
| s00_axi_wready  | out       | std_logic                                             |               |
| s00_axi_bresp   | out       | std_logic_vector(1 downto 0)                          |               |
| s00_axi_bvalid  | out       | std_logic                                             |               |
| s00_axi_bready  | in        | std_logic                                             |               |
| s00_axi_araddr  | in        | std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0)     |               |
| s00_axi_arprot  | in        | std_logic_vector(2 downto 0)                          |               |
| s00_axi_arvalid | in        | std_logic                                             |               |
| s00_axi_arready | out       | std_logic                                             |               |
| s00_axi_rdata   | out       | std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0)     |               |
| s00_axi_rresp   | out       | std_logic_vector(1 downto 0)                          |               |
| s00_axi_rvalid  | out       | std_logic                                             |               |
| s00_axi_rready  | in        | std_logic                                             |               |
| ref_rst_i       | in        | std_logic                                             | logic CANDR   |
| ref_clk_i       | in        | std_logic                                             |               |
| pwm_o           | out       | std_logic                                             | out signals   |
## Signals

| Name              | Type                                             | Description |
| ----------------- | ------------------------------------------------ | ----------- |
| addr_s            | std_logic_vector(INTERNAL_ADDR_WIDTH-1 downto 0) | axi         |
| write_en_s        | std_logic                                        |             |
|  read_en_s        | std_logic                                        |             |
| duty_s            | std_logic_vector(COUNTER_SIZE-1 downto 0)        | conf        |
|  duty_sync_s      | std_logic_vector(COUNTER_SIZE-1 downto 0)        | conf        |
| period_s          | std_logic_vector(COUNTER_SIZE-1 downto 0)        |             |
|  period_sync_s    | std_logic_vector(COUNTER_SIZE-1 downto 0)        |             |
| prescaler_s       | std_logic_vector(COUNTER_SIZE-1 downto 0)        |             |
|  prescaler_sync_s | std_logic_vector(COUNTER_SIZE-1 downto 0)        |             |
| enable_s          | std_logic                                        |             |
|  enable_sync_s    | std_logic                                        |             |
| invert_s          | std_logic                                        |             |
|  invert_sync_s    | std_logic                                        |             |
## Constants

| Name                | Type    | Value | Description |
| ------------------- | ------- | ----- | ----------- |
| INTERNAL_ADDR_WIDTH | natural |  3    |             |
## Instantiations

- pwm_log_inst: work.pwm_logic
- sync_duty: work.pwm_sync_vector
- sync_period: work.pwm_sync_vector
- sync_prescaler: work.pwm_sync_vector
- sync_enable: work.pwm_sync_bit
- sync_invert: work.pwm_sync_bit
- pwm_comm_inst: work.pwm_comm
- handle_comm: work.pwm_handCom
**Description**
Instantiation of Axi Bus Interface S00_AXI

