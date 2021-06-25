# Entity: stream_FrameGenerator
## Diagram
![Diagram](stream_FrameGenerator.svg "Diagram")
## Generics
| Generic name | Type                           | Value                              | Description |
| ------------ | ------------------------------ | ---------------------------------- | ----------- |
| DATA_BITS    | positive                       | 8                                  |             |
| WORD_BITS    | positive                       | 16                                 |             |
| APPEND       | T_FRAMEGEN_APPEND              | FRAMEGEN_APP_NONE                  |             |
| FRAMEGROUPS  | T_FRAMEGEN_FRAMEGROUP_VECTOR_8 | (0 => C_FRAMEGEN_FRAMEGROUP_EMPTY) |             |
## Ports
| Port name       | Direction | Type                                     | Description |
| --------------- | --------- | ---------------------------------------- | ----------- |
| Clock           | in        | std_logic                                |             |
| Reset           | in        | std_logic                                |             |
| Command         | in        | T_FRAMEGEN_COMMAND                       |             |
| Status          | out       | T_FRAMEGEN_STATUS                        |             |
| Pause           | in        | T_SLV_16                                 |             |
| FrameGroupIndex | in        | T_SLV_8                                  |             |
| FrameIndex      | in        | T_SLV_8                                  |             |
| Sequences       | in        | T_SLV_16                                 |             |
| FrameLength     | in        | T_SLV_16                                 |             |
| Out_Valid       | out       | std_logic                                |             |
| Out_Data        | out       | std_logic_vector(DATA_BITS - 1 downto 0) |             |
| Out_SOF         | out       | std_logic                                |             |
| Out_EOF         | out       | std_logic                                |             |
| Out_Ack         | in        | std_logic                                |             |
## Signals
| Name                   | Type                                     | Description |
| ---------------------- | ---------------------------------------- | ----------- |
| State                  | T_STATE                                  |             |
| NextState              | T_STATE                                  |             |
| FrameLengthCounter_rst | std_logic                                |             |
| FrameLengthCounter_en  | std_logic                                |             |
| FrameLengthCounter_us  | unsigned(15 downto 0)                    |             |
| SequencesCounter_rst   | std_logic                                |             |
| SequencesCounter_en    | std_logic                                |             |
| SequencesCounter_us    | unsigned(15 downto 0)                    |             |
| ContentCounter_rst     | std_logic                                |             |
| ContentCounter_en      | std_logic                                |             |
| ContentCounter_us      | unsigned(WORD_BITS - 1 downto 0)         |             |
| PRNG_rst               | std_logic                                |             |
| PRNG_got               | std_logic                                |             |
| PRNG_Data              | std_logic_vector(DATA_BITS - 1 downto 0) |             |
## Types
| Name    | Type                                                                                                                                 | Description |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| T_STATE | ( 		ST_IDLE, 			ST_SEQUENCE_SOF,	ST_SEQUENCE_DATA,	ST_SEQUENCE_EOF, 			ST_RANDOM_SOF,		ST_RANDOM_DATA,		ST_RANDOM_EOF, 		ST_ERROR 	) |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( State, Command, Out_Ack,
					Sequences, FrameLength,
					FrameLengthCounter_us,
					SequencesCounter_us, ContentCounter_us,
					PRNG_Data )_

- unnamed: _( Clock )_

- unnamed: _( Clock )_

- unnamed: _( Clock )_

## Instantiations
- PRNG: PoC.arith_prng
