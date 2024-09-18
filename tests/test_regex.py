import pytest
import import_ipynb
from task2 import extract_durations, extract_emails

@pytest.mark.parametrize("input_text, expected_output", [
    ("My email is john.doe@example.com", ["john.doe@example.com"]),
    ("Contact us at admin@example.org, support@example.co.uk", ["admin@example.org", "support@example.co.uk"]),
    ("There is no email here.", []),
    ("Invalid: john@example, jane@@example.com", []),
    ("Valid: jane.doe@example.com, Invalid: joe@@example, admin@site.", ["jane.doe@example.com"]),
    ("Contact me at my_email123@domain.co.in or me_2@sub.domain.com", ["my_email123@domain.co.in", "me_2@sub.domain.com"]),
    ("Contact at JOHN.DOE@EXAMPLE.COM", ["JOHN.DOE@EXAMPLE.COM"]),
])
def test_extract_emails(input_text, expected_output):
    assert extract_emails(input_text) == expected_output

@pytest.mark.parametrize("input_text, expected_output", [
    ("The race took 2h 30m 15s.", ["2h 30m 15s"]),
    ("Workout: 45m 30s.", ["45m 30s"]),
    ("Flight duration: 5h.", ["5h"]),
    ("Wait for 15s.", ["15s"]),
    ("No time durations here.", []),
    ("Invalid: 1h 60m, 30s 90s", []),
    ("The marathon lasted 10m 2h 5s.", ["10m 2h 5s"]),
    ("Task 1: 2h 30m, Task 2: 45m 15s", ["2h 30m", "45m 15s"]),
])
def test_extract_durations(input_text, expected_output):
    assert extract_durations(input_text) == expected_output
