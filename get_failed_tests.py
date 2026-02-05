"""Handles text from test result files"""
#!/usr/bin/env python3
import sys
import json

def read_html(path: str) -> list:
    """Reads a given file and searchs for keywords
    Args:
        path (str): the path to the file.
    :Return: list() with keywords as elments."""
    with open(path, 'r') as file:
        text = file.read()
    sub_strings = text.split('"col-result">')
    result_lines = [ line.split('"col-duration"')[0] for line in sub_strings if line.startswith("Failed")]
    failed_tests = []
    for line in result_lines:
        if line.startswith("Failed"):
            dirty_test_name = line.split("::")[2]
            test_name = dirty_test_name.split("<")[0]
            failed_tests.append(test_name)
    return failed_tests

def write_json(failed_tests: list(), path: str) -> None:
    with open(path, "w") as file:
        json.dump(failed_tests, file)

def make_tests_string(failed_tests: list()) -> str:
    if not failed_tests:
        return "List argument was not provided"
    if len(failed_tests) == 1:
        return failed_tests[0]
    tests_string = ""
    for test in failed_tests:
        if test == failed_tests[-1]:
            tests_string += test
        else:
            tests_string += test + " or "
    return tests_string

def read_json(path: str) -> list():
    try:
        with open(path, "r") as file:
            json_string = file.read()
        failed_tests = json.loads(json_string)
    except FileNotFoundError:
        failed_tests = []
    return failed_tests

if __name__ == '__main__':
    html_path = sys.argv[1]
    json_path = sys.argv[2]

    last_failures = read_json(json_path)
    current_failures = read_html(html_path)

    if last_failures == current_failures:
        print("false")
    else:
        write_json(current_failures, json_path)    
        print(make_tests_string(current_failures))
