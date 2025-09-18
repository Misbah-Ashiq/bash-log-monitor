Realistic Bash Task: Log Error Filter
------------------------------------
Goal:
From system.log, extract only ERROR lines (unique) into errors.log.

Example:
  Input: system.log
    INFO Starting service
    ERROR Connection failed
    ERROR Disk full
  Output: errors.log
    ERROR Connection failed
    ERROR Disk full

To test locally (from terminal-bench root):
  uv run tb run --agent oracle --task-id log-error-filter

Zip name for upload: misbah-ashiq-18-09-2025.zip
