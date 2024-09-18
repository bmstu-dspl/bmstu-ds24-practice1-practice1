import pytest
import import_ipynb
from task1 import verify

# List of valid card numbers (in different formats)
valid_card_numbers = [
    "4539 1488 0343 6467",  # Visa
    "6011 1111 1111 1117",  # Discover
    "3714-4963-5398-431",   # AmEx (15 digits)
    "378282246310005",      # AmEx (no spaces)
    "30569309025904",       # Diners Club (14 digits)
]

# List of invalid card numbers (wrong check digit, invalid lengths)
invalid_card_numbers = [
    "4539 1488 0343 6468",  # Invalid Visa
    "6011 1111 1111 1118",  # Invalid Discover
    "3714-4963-5398-432",   # Invalid AmEx
    "378282246310006",      # Invalid AmEx
    "30569309025905",       # Invalid Diners Club
    "1234 5678 9012 3456",  # Random invalid number
    "1234",                 # Too short
]

@pytest.mark.parametrize("card_number", valid_card_numbers)
def test_valid_card_numbers(card_number):
    """
    Test that valid card numbers return True.
    """
    assert verify(card_number) is True

@pytest.mark.parametrize("card_number", invalid_card_numbers)
def test_invalid_card_numbers(card_number):
    """
    Test that invalid card numbers return False.
    """
    assert verify(card_number) is False

