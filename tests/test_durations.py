import pytest
import import_ipynb
from task2 import extract_durations

def test_extract_full_duration():
    input_text = "The race took 2h 30m 15s."
    expected_output = ["2h 30m 15s"]
    assert extract_durations(input_text) == expected_output

def test_extract_partial_duration():
    input_text = "Workout: 45m 30s."
    expected_output = ["45m 30s"]
    assert extract_durations(input_text) == expected_output

def test_extract_single_hour():
    input_text = "Flight duration: 5h."
    expected_output = ["5h"]
    assert extract_durations(input_text) == expected_output

def test_extract_seconds_only():
    input_text = "Wait for 15s."
    expected_output = ["15s"]
    assert extract_durations(input_text) == expected_output

def test_no_durations_found():
    input_text = "No time durations here."
    expected_output = []
    assert extract_durations(input_text) == expected_output

def test_invalid_durations():
    input_text = "Invalid: 1h 60m, 30s 90s"
    expected_output = []
    assert extract_durations(input_text) == expected_output

def test_mixed_up_duration():
    input_text = "The marathon lasted 10m 2h 5s."
    expected_output = ["10m 2h 5s"]
    assert extract_durations(input_text) == expected_output

def test_multiple_durations():
    input_text = "Task 1: 2h 30m, Task 2: 45m 15s"
    expected_output = ["2h 30m", "45m 15s"]
    assert extract_durations(input_text) == expected_output
