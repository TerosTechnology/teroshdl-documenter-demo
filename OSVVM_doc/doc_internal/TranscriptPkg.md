# Package: TranscriptPkg
## Functions
- TranscriptOpen <font id="function_arguments">(Status: InOut FILE_OPEN_STATUS; ExternalName: STRING; OpenKind: WRITE_APPEND_OPEN_KIND := WRITE_MODE)</font> <font id="function_return">return ()</font>
- TranscriptOpen <font id="function_arguments">(ExternalName: STRING; OpenKind: WRITE_APPEND_OPEN_KIND := WRITE_MODE)</font> <font id="function_return">return ()</font>
- TranscriptClose <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- SetTranscriptMirror <font id="function_arguments">(A : boolean := TRUE)</font> <font id="function_return">return ()</font>
- WriteLine <font id="function_arguments">(buf : inout line)</font> <font id="function_return">return ()</font>
- Print <font id="function_arguments">(s : string)</font> <font id="function_return">return ()</font>
- BlankLine <font id="function_arguments">(count : integer := 1)</font> <font id="function_return">return ()</font>
