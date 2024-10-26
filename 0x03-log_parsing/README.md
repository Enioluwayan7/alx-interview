# Log Parsing

This Python script reads log entries from standard input, processes each line to extract specific information, and computes metrics. It outputs the total file size and the count of HTTP status codes every 10 lines or upon receiving a keyboard interruption (Ctrl+C).

## Table of Contents
1. [Requirements](#requirements)
2. [Usage](#usage)
3. [Input Format](#input-format)
4. [Output Format](#output-format)
5. [Functionality](#functionality)
6. [Error Handling](#error-handling)
7. [Example](#example)

## Requirements
- Python 3.x

## Usage
To run the script, execute it in a terminal and provide log data through standard input. Examples:

```bash
python3 log_parser.py < log_file.txt
