# Entity: dac_intf

- **File**: dac_intf.v
## Diagram

![Diagram](dac_intf.svg "Diagram")
## Description

 Xianjun jiao. putaoshu@msn.com; xianjun.jiao@imec.be;

## Generics

| Generic name        | Type    | Value | Description |
| ------------------- | ------- | ----- | ----------- |
| IQ_DATA_WIDTH       | integer | 16    |             |
| DAC_PACK_DATA_WIDTH | integer | 64    |             |
## Ports

| Port name           | Direction | Type                             | Description                   |
| ------------------- | --------- | -------------------------------- | ----------------------------- |
| dac_rst             | input     | wire                             |                               |
| dac_clk             | input     | wire                             |                               |
| dac_data            | output    | wire [DAC_PACK_DATA_WIDTH-1 : 0] | connect util_ad9361_dac_upack |
| dac_valid           | output    | wire                             |                               |
| dac_ready           | input     | wire                             |                               |
| dma_data            | input     | wire [DAC_PACK_DATA_WIDTH-1 : 0] | connect axi_ad9361_dac_dma    |
| dma_valid           | input     | wire                             |                               |
| dma_ready           | output    | wire                             |                               |
| src_sel             | input     | wire                             |                               |
| ant_flag            | input     | wire                             |                               |
| acc_clk             | input     | wire                             |                               |
| acc_rstn            | input     | wire                             |                               |
| data_from_acc       | input     | wire [(2*IQ_DATA_WIDTH-1) : 0]   |                               |
| data_valid_from_acc | input     | wire                             |                               |
| fulln_to_acc        | output    | wire                             |                               |
## Signals

| Name                        | Type                               | Description                                                                                                                                                                                                                                                                                                                                |
| --------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ALMOSTEMPTY                 | wire                               |                                                                                                                                                                                                                                                                                                                                            |
| ALMOSTFULL                  | wire                               |                                                                                                                                                                                                                                                                                                                                            |
| EMPTY_internal              | wire                               |                                                                                                                                                                                                                                                                                                                                            |
| FULL_internal               | wire                               |                                                                                                                                                                                                                                                                                                                                            |
| RDERR                       | wire                               |                                                                                                                                                                                                                                                                                                                                            |
| WRERR                       | wire                               |                                                                                                                                                                                                                                                                                                                                            |
| RST_internal                | wire                               |                                                                                                                                                                                                                                                                                                                                            |
| src_sel_in_rf_domain        | wire                               |  reg src_sel_reg0;  reg src_sel_reg1;  reg src_sel_reg2;  reg src_sel_reg3;  reg src_sel_reg4;  reg src_sel_reg5;  reg src_sel_wider;  reg src_sel_in_rf_domain;  reg ant_flag_reg0;  reg ant_flag_reg1;  reg ant_flag_reg2;  reg ant_flag_reg3;  reg ant_flag_reg4;  reg ant_flag_reg5;  reg ant_flag_wider;  reg ant_flag_in_rf_domain;  |
| ant_flag_in_rf_domain       | wire                               |                                                                                                                                                                                                                                                                                                                                            |
| dac_data_internal           | wire [(2*IQ_DATA_WIDTH-1) : 0]     |                                                                                                                                                                                                                                                                                                                                            |
| dac_data_internal_after_sel | wire [(DAC_PACK_DATA_WIDTH-1) : 0] |                                                                                                                                                                                                                                                                                                                                            |
| rden_internal               | wire                               |                                                                                                                                                                                                                                                                                                                                            |
| wren_internal               | wire                               |                                                                                                                                                                                                                                                                                                                                            |
## Instantiations

- xpm_cdc_array_single_inst_src_sel: xpm_cdc_array_single
- xpm_cdc_array_single_inst_ant_flag: xpm_cdc_array_single
- fifo32_2clk_dep32_i: xpm_fifo_async
**Description**
 always @( posedge acc_clk )
 begin
   if ( acc_rstn == 1'b0 ) begin
         src_sel_reg0 <= 1'b0;
         src_sel_reg1 <= 1'b0;
         src_sel_reg2 <= 1'b0;
         src_sel_reg3 <= 1'b0;
         src_sel_reg4 <= 1'b0;
         src_sel_reg5 <= 1'b0;
         src_sel_wider <= 1'b0;
         ant_flag_reg0 <= 1'b0;
         ant_flag_reg1 <= 1'b0;
         ant_flag_reg2 <= 1'b0;
         ant_flag_reg3 <= 1'b0;
         ant_flag_reg4 <= 1'b0;
         ant_flag_reg5 <= 1'b0;
         ant_flag_wider <= 1'b0;
   end 
   else begin
         src_sel_reg0 <= src_sel;
         src_sel_reg1 <= src_sel_reg0;
         src_sel_reg2 <= src_sel_reg1;
         src_sel_reg3 <= src_sel_reg2;
         src_sel_reg4 <= src_sel_reg3;
         src_sel_reg5 <= src_sel_reg4;
         src_sel_wider <= (src_sel_reg0 | src_sel_reg1 | src_sel_reg2 | src_sel_reg3 | src_sel_reg4 | src_sel_reg5);
         ant_flag_reg0 <= ant_flag;
         ant_flag_reg1 <= ant_flag_reg0;
         ant_flag_reg2 <= ant_flag_reg1;
         ant_flag_reg3 <= ant_flag_reg2;
         ant_flag_reg4 <= ant_flag_reg3;
         ant_flag_reg5 <= ant_flag_reg4;
         ant_flag_wider <= (ant_flag_reg0 | ant_flag_reg1 | ant_flag_reg2 | ant_flag_reg3 | ant_flag_reg4 | ant_flag_reg5);
   end
 end
 always @( posedge dac_clk )
 begin
   if ( dac_rst == 1'b1 ) begin
       src_sel_in_rf_domain <= 1'b0;
       ant_flag_in_rf_domain <= 1'b0;
   end 
   else begin  
       if (src_sel_wider == 1'b1)
           src_sel_in_rf_domain <= 1'b1;
       else
           src_sel_in_rf_domain <= 1'b0;
       if (ant_flag_wider == 1'b1)
           ant_flag_in_rf_domain <= 1'b1;
       else
           ant_flag_in_rf_domain <= 1'b0;
   end
 end
 fifo32_2clk_dep32 fifo32_2clk_dep32_i
        (.DATAO(dac_data_internal),
         .DI(data_from_acc),
         .EMPTY(EMPTY_internal),
         .FULL(FULL_internal),
         .RDCLK(dac_clk),
         .RDEN(rden_internal),
         .RD_DATA_COUNT(),
         .RST(RST_internal),
         .WRCLK(acc_clk),
         .WREN(wren_internal),
         .WR_DATA_COUNT());

