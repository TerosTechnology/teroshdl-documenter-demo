# Entity: UdpDebugBridge

- **File**: UdpDebugBridge_stub.vhd
## Diagram

![Diagram](UdpDebugBridge_stub.svg "Diagram")
## Description

Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
--------------------------------------------------------------------------------
Tool Version: Vivado v.2018.3 (lin64) Build 2405991 Thu Dec  6 23:36:41 MST 2018
Date        : Wed Jun 26 13:06:07 2019
Host        : rdsrv107.slac.stanford.edu running 64-bit Red Hat Enterprise Linux Server release 6.10 (Santiago)
Command     : write_vhdl -force -mode synth_stub
              /u/re/ruckman/projects/dpm-remote-ibert-tester/firmware/submodules/xvc-udp-debug-bridge/dcp/UltraScale/Stub/images/UdpDebugBridge_stub.vhd
Design      : UdpDebugBridge
Purpose     : Stub declaration of top-level module interface
Device      : xcku040-ffva1156-2-e
--------------------------------------------------------------------------------
## Ports

| Port name          | Direction | Type                              | Description |
| ------------------ | --------- | --------------------------------- | ----------- |
| axisClk            | in        | STD_LOGIC                         |             |
| axisRst            | in        | STD_LOGIC                         |             |
| \mAxisReq[tValid]\ | in        | STD_LOGIC                         |             |
| \mAxisReq[tData]\  | in        | STD_LOGIC_VECTOR ( 511 downto 0 ) |             |
| \mAxisReq[tStrb]\  | in        | STD_LOGIC_VECTOR ( 63 downto 0 )  |             |
| \mAxisReq[tKeep]\  | in        | STD_LOGIC_VECTOR ( 63 downto 0 )  |             |
| \mAxisReq[tLast]\  | in        | STD_LOGIC                         |             |
| \mAxisReq[tDest]\  | in        | STD_LOGIC_VECTOR ( 7 downto 0 )   |             |
| \mAxisReq[tId]\    | in        | STD_LOGIC_VECTOR ( 7 downto 0 )   |             |
| \mAxisReq[tUser]\  | in        | STD_LOGIC_VECTOR ( 511 downto 0 ) |             |
| \sAxisReq[tReady]\ | out       | STD_LOGIC                         |             |
| \mAxisTdo[tValid]\ | out       | STD_LOGIC                         |             |
| \mAxisTdo[tData]\  | out       | STD_LOGIC_VECTOR ( 511 downto 0 ) |             |
| \mAxisTdo[tStrb]\  | out       | STD_LOGIC_VECTOR ( 63 downto 0 )  |             |
| \mAxisTdo[tKeep]\  | out       | STD_LOGIC_VECTOR ( 63 downto 0 )  |             |
| \mAxisTdo[tLast]\  | out       | STD_LOGIC                         |             |
| \mAxisTdo[tDest]\  | out       | STD_LOGIC_VECTOR ( 7 downto 0 )   |             |
| \mAxisTdo[tId]\    | out       | STD_LOGIC_VECTOR ( 7 downto 0 )   |             |
| \mAxisTdo[tUser]\  | out       | STD_LOGIC_VECTOR ( 511 downto 0 ) |             |
| \sAxisTdo[tReady]\ | in        | STD_LOGIC                         |             |
