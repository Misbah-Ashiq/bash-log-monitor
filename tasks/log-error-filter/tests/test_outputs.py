import os
from pathlib import Path

def test_errors_log_exists():
    path = Path('/app/errors.log')
    assert path.exists(), "Expected /app/errors.log to exist."

def test_errors_log_content():
    system_log = Path('/app/system.log').read_text().splitlines()
    errors_log = Path('/app/errors.log').read_text().splitlines()

    expected = []
    seen = set()
    for line in system_log:
        if "ERROR" in line and line not in seen:
            expected.append(line)
            seen.add(line)

    assert errors_log == expected, f"Expected {expected}, but got {errors_log}"
