# Bisect Agent

A generalizable script to bisect and verify a list of values

## Interface

### get_list_cmd

This should be a command that generate a list of ordered value to standard output, separated by newline.

Example: A list of commits ordered by timestamp. The top commits are expected to succeed and the bottom commits are expected to fail.
See `debug_uctable/get_list.sh`

### verify_cmd

This is a script that takes in one positional argument, which is a value from `get_list_cmd`, and verify
if the value can produce successful result. Exit code of 0 indicates success, 1 indicates failure,
and other values indicate unknown error that can be retried (default retry 3 times before quitting).

Example: checkout the commit provided `get_list_cmd` and run a test script. Parsed from the test script to
detect if the test case has passed or failed. See `debug_uctable/verify.sh`

## Usage

```bash
python3 main.py "<get_list_cmd>" "<verify_cmd>"
```

Example:

```bash
python3 main.py "./debug_uctable/get_list.sh" "./debug_uctable/verify.sh"
```
