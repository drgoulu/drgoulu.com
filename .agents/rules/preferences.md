# Workspace Preferences

## File Inspection
- Always use the native `view_file` tool (with `StartLine` and `EndLine` for line ranges) to read or inspect files.
- Do NOT use terminal commands like `sed`, `head`, `tail`, or `cat` via `run_command` just to inspect files, as this requires unnecessary user permission prompts.
