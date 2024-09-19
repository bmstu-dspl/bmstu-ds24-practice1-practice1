import pytest
import import_ipynb
from task2 import extract_emails

def test_extract_single_email():
    input_text = "My email is john.doe@example.com"
    expected_output = ["john.doe@example.com"]
    assert extract_emails(input_text) == expected_output

def test_extract_multiple_emails():
    input_text = "Contact us at admin@example.org, support@example.co.uk"
    expected_output = ["admin@example.org", "support@example.co.uk"]
    assert extract_emails(input_text) == expected_output

def test_no_email_found():
    input_text = "There is no email here."
    expected_output = []
    assert extract_emails(input_text) == expected_output

def test_invalid_emails():
    input_text = "Invalid: john@example, jane@@example.com"
    expected_output = []
    assert extract_emails(input_text) == expected_output

def test_mixed_valid_and_invalid_emails():
    input_text = "Valid: jane.doe@example.com, Invalid: joe@@example, admin@site."
    expected_output = ["jane.doe@example.com"]
    assert extract_emails(input_text) == expected_output

def test_complex_email_addresses():
    input_text = "Contact me at my_email123@domain.co.in or me_2@sub.domain.com"
    expected_output = ["my_email123@domain.co.in", "me_2@sub.domain.com"]
    assert extract_emails(input_text) == expected_output

def test_uppercase_email():
    input_text = "Contact at JOHN.DOE@EXAMPLE.COM"
    expected_output = ["JOHN.DOE@EXAMPLE.COM"]
    assert extract_emails(input_text) == expected_output

