# Package: vectors
## Types
| Name       | Type | Description |
| ---------- | ---- | ----------- |
| T_SLVV_2   |      |             |
| T_SLVV_3   |      |             |
| T_SLVV_4   |      |             |
| T_SLVV_8   |      |             |
| T_SLVV_12  |      |             |
| T_SLVV_16  |      |             |
| T_SLVV_24  |      |             |
| T_SLVV_32  |      |             |
| T_SLVV_48  |      |             |
| T_SLVV_64  |      |             |
| T_SLVV_128 |      |             |
| T_SLVV_256 |      |             |
| T_SLVV_512 |      |             |
| T_SLM      |      |             |
## Functions
- low <font id="function_arguments">(lenvec : T_POSVEC; index : natural)</font> <font id="function_return">return natural</font>
- high <font id="function_arguments">(lenvec : T_POSVEC; index : natural)</font> <font id="function_return">return natural</font>
- assign_row <font id="function_arguments">(signal slm : out T_SLM; slv : std_logic_vector; constant RowIndex : natural)</font> <font id="function_return">return ()</font>
- assign_row <font id="function_arguments">(signal slm : out T_SLM; slv : std_logic_vector; constant RowIndex : natural; Position : natural)</font> <font id="function_return">return ()</font>
- assign_row <font id="function_arguments">(signal slm : out T_SLM; slv : std_logic_vector; constant RowIndex : natural; High : natural; Low : natural)</font> <font id="function_return">return ()</font>
- assign_col <font id="function_arguments">(signal slm : out T_SLM; slv : std_logic_vector; constant ColIndex : natural)</font> <font id="function_return">return ()</font>
- slm_slice <font id="function_arguments">(slm : T_SLM; RowIndex : natural; ColIndex : natural; Height : natural; Width : natural)</font> <font id="function_return">return T_SLM</font>
- slm_slice_rows <font id="function_arguments">(slm : T_SLM; High : natural; Low : natural)</font> <font id="function_return">return T_SLM</font>
- slm_slice_cols <font id="function_arguments">(slm : T_SLM; High : natural; Low : natural)</font> <font id="function_return">return T_SLM</font>
- slm_merge_rows <font id="function_arguments">(slm1 : T_SLM; slm2 : T_SLM)</font> <font id="function_return">return T_SLM</font>
- slm_merge_cols <font id="function_arguments">(slm1 : T_SLM; slm2 : T_SLM)</font> <font id="function_return">return T_SLM</font>
- get_col <font id="function_arguments">(slm : T_SLM; ColIndex : natural)</font> <font id="function_return">return std_logic_vector</font>
- get_row <font id="function_arguments">(slm : T_SLM; RowIndex : natural)</font> <font id="function_return">return std_logic_vector</font>
- get_row <font id="function_arguments">(slm : T_SLM; RowIndex : natural; Length : positive)</font> <font id="function_return">return std_logic_vector</font>
- get_row <font id="function_arguments">(slm : T_SLM; RowIndex : natural; High : natural; Low : natural)</font> <font id="function_return">return std_logic_vector</font>
- to_slv <font id="function_arguments">(slvv : T_SLVV_2)</font> <font id="function_return">return std_logic_vector</font>
- to_slv <font id="function_arguments">(slvv : T_SLVV_4)</font> <font id="function_return">return std_logic_vector</font>
- to_slv <font id="function_arguments">(slvv : T_SLVV_8)</font> <font id="function_return">return std_logic_vector</font>
- to_slv <font id="function_arguments">(slvv : T_SLVV_12)</font> <font id="function_return">return std_logic_vector</font>
- to_slv <font id="function_arguments">(slvv : T_SLVV_16)</font> <font id="function_return">return std_logic_vector</font>
- to_slv <font id="function_arguments">(slvv : T_SLVV_24)</font> <font id="function_return">return std_logic_vector</font>
- to_slv <font id="function_arguments">(slvv : T_SLVV_32)</font> <font id="function_return">return std_logic_vector</font>
- to_slv <font id="function_arguments">(slvv : T_SLVV_64)</font> <font id="function_return">return std_logic_vector</font>
- to_slv <font id="function_arguments">(slvv : T_SLVV_128)</font> <font id="function_return">return std_logic_vector</font>
- to_slv <font id="function_arguments">(slm : T_SLM)</font> <font id="function_return">return std_logic_vector</font>
- to_slvv_4 <font id="function_arguments">(slv : std_logic_vector)</font> <font id="function_return">return T_SLVV_4</font>
- to_slvv_8 <font id="function_arguments">(slv : std_logic_vector)</font> <font id="function_return">return T_SLVV_8</font>
- to_slvv_12 <font id="function_arguments">(slv : std_logic_vector)</font> <font id="function_return">return T_SLVV_12</font>
- to_slvv_16 <font id="function_arguments">(slv : std_logic_vector)</font> <font id="function_return">return T_SLVV_16</font>
- to_slvv_32 <font id="function_arguments">(slv : std_logic_vector)</font> <font id="function_return">return T_SLVV_32</font>
- to_slvv_64 <font id="function_arguments">(slv : std_logic_vector)</font> <font id="function_return">return T_SLVV_64</font>
- to_slvv_128 <font id="function_arguments">(slv : std_logic_vector)</font> <font id="function_return">return T_SLVV_128</font>
- to_slvv_256 <font id="function_arguments">(slv : std_logic_vector)</font> <font id="function_return">return T_SLVV_256</font>
- to_slvv_512 <font id="function_arguments">(slv : std_logic_vector)</font> <font id="function_return">return T_SLVV_512</font>
- to_slvv_4 <font id="function_arguments">(slm : T_SLM)</font> <font id="function_return">return T_SLVV_4</font>
- to_slvv_8 <font id="function_arguments">(slm : T_SLM)</font> <font id="function_return">return T_SLVV_8</font>
- to_slvv_12 <font id="function_arguments">(slm : T_SLM)</font> <font id="function_return">return T_SLVV_12</font>
- to_slvv_16 <font id="function_arguments">(slm : T_SLM)</font> <font id="function_return">return T_SLVV_16</font>
- to_slvv_32 <font id="function_arguments">(slm : T_SLM)</font> <font id="function_return">return T_SLVV_32</font>
- to_slvv_64 <font id="function_arguments">(slm : T_SLM)</font> <font id="function_return">return T_SLVV_64</font>
- to_slvv_128 <font id="function_arguments">(slm : T_SLM)</font> <font id="function_return">return T_SLVV_128</font>
- to_slvv_256 <font id="function_arguments">(slm : T_SLM)</font> <font id="function_return">return T_SLVV_256</font>
- to_slvv_512 <font id="function_arguments">(slm : T_SLM)</font> <font id="function_return">return T_SLVV_512</font>
- to_slm <font id="function_arguments">(slv : std_logic_vector; ROWS : positive; COLS : positive)</font> <font id="function_return">return T_SLM</font>
- to_slm <font id="function_arguments">(slvv : T_SLVV_4)</font> <font id="function_return">return T_SLM</font>
- to_slm <font id="function_arguments">(slvv : T_SLVV_8)</font> <font id="function_return">return T_SLM</font>
- to_slm <font id="function_arguments">(slvv : T_SLVV_12)</font> <font id="function_return">return T_SLM</font>
- to_slm <font id="function_arguments">(slvv : T_SLVV_16)</font> <font id="function_return">return T_SLM</font>
- to_slm <font id="function_arguments">(slvv : T_SLVV_32)</font> <font id="function_return">return T_SLM</font>
- to_slm <font id="function_arguments">(slvv : T_SLVV_48)</font> <font id="function_return">return T_SLM</font>
- to_slm <font id="function_arguments">(slvv : T_SLVV_64)</font> <font id="function_return">return T_SLM</font>
- to_slm <font id="function_arguments">(slvv : T_SLVV_128)</font> <font id="function_return">return T_SLM</font>
- to_slm <font id="function_arguments">(slvv : T_SLVV_256)</font> <font id="function_return">return T_SLM</font>
- to_slm <font id="function_arguments">(slvv : T_SLVV_512)</font> <font id="function_return">return T_SLM</font>
- dir <font id="function_arguments">(slvv : T_SLVV_8)</font> <font id="function_return">return T_SLVV_8</font>
- rev <font id="function_arguments">(slvv : T_SLVV_4)</font> <font id="function_return">return T_SLVV_4</font>
- rev <font id="function_arguments">(slvv : T_SLVV_8)</font> <font id="function_return">return T_SLVV_8</font>
- rev <font id="function_arguments">(slvv : T_SLVV_12)</font> <font id="function_return">return T_SLVV_12</font>
- rev <font id="function_arguments">(slvv : T_SLVV_16)</font> <font id="function_return">return T_SLVV_16</font>
- rev <font id="function_arguments">(slvv : T_SLVV_32)</font> <font id="function_return">return T_SLVV_32</font>
- rev <font id="function_arguments">(slvv : T_SLVV_64)</font> <font id="function_return">return T_SLVV_64</font>
- rev <font id="function_arguments">(slvv : T_SLVV_128)</font> <font id="function_return">return T_SLVV_128</font>
- rev <font id="function_arguments">(slvv : T_SLVV_256)</font> <font id="function_return">return T_SLVV_256</font>
- rev <font id="function_arguments">(slvv : T_SLVV_512)</font> <font id="function_return">return T_SLVV_512</font>
- resize <font id="function_arguments">(slm : T_SLM; size : positive)</font> <font id="function_return">return T_SLM</font>
- to_string <font id="function_arguments">(slvv : T_SLVV_8; sep : character := ':')</font> <font id="function_return">return string</font>
- to_string <font id="function_arguments">(slm : T_SLM; groups : positive := 4; format : character := 'b')</font> <font id="function_return">return string</font>
