# Package: TranscriptPkg

- **File**: TranscriptPkg.vhd
## Functions
- TranscriptOpen <font id="function_arguments">(Status: InOut FILE_OPEN_STATUS;<br><span style="padding-left:20px"> ExternalName: STRING;<br><span style="padding-left:20px"> OpenKind: WRITE_APPEND_OPEN_KIND := WRITE_MODE) </font> <font id="function_return">return ()</font>
</br>**Description**
 Open and close TranscriptFile.  Function allows declarative opens 

- TranscriptOpen <font id="function_arguments">(ExternalName: STRING;<br><span style="padding-left:20px"> OpenKind: WRITE_APPEND_OPEN_KIND := WRITE_MODE) </font> <font id="function_return">return ()</font>
- TranscriptClose <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- SetTranscriptMirror <font id="function_arguments">(A : boolean := TRUE) </font> <font id="function_return">return ()</font>
</br>**Description**
 Mirroring.  When using TranscriptPkw WriteLine and Print, uses both TranscriptFile and OUTPUT 

- WriteLine <font id="function_arguments">(buf : inout line) </font> <font id="function_return">return ()</font>
</br>**Description**
 Write to TranscriptFile when open.  Write to OUTPUT when not open or IsTranscriptMirrored

- Print <font id="function_arguments">(s : string) </font> <font id="function_return">return ()</font>
- BlankLine <font id="function_arguments">(count : integer := 1) </font> <font id="function_return">return ()</font>
</br>**Description**
 Create "count" number of blank lines

