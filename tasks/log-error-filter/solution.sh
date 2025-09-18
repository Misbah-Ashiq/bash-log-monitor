#!/bin/bash
# Reference solution: filter unique ERROR lines
awk '/ERROR/ && !seen[$0]++' /app/system.log > /app/errors.log
echo "Filtered errors saved to /app/errors.log"
