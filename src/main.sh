#!/bin/bash
ls -la | awk '{print $9, $5, $6" "$7} > table_files_bash.csv
