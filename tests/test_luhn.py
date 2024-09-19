import pytest
import import_ipynb
from task1 import verify

def test_valid_visa_1():
    card_number = "4539 1488 0343 6467"
    assert verify(card_number) == True

def test_valid_visa_2():
    card_number = "4716 1089 9971 6531"
    assert verify(card_number) == True

def test_valid_discover():
    card_number = "6011 5144 3354 6201"
    assert verify(card_number) == True

def test_valid_jcb():
    card_number = "3530 1113 3330 0000"
    assert verify(card_number) == True

def test_valid_mastercard():
    card_number = "5555 5555 5555 4444"
    assert verify(card_number) == True

def test_invalid_visa():
    card_number = "4539 1488 0343 6468"
    assert verify(card_number) == False

def test_invalid_discover():
    card_number = "6011 1111 1111 1118"
    assert verify(card_number) == False

def test_invalid_amex_1():
    card_number = "3714-4963-5398-432"
    assert verify(card_number) == False

def test_invalid_amex_2():
    card_number = "378282246310006"
    assert verify(card_number) == False

def test_invalid_diners_club():
    card_number = "30569309025905"
    assert verify(card_number) == False

def test_random_invalid_number():
    card_number = "1234 5678 9012 3456"
    assert verify(card_number) == False

def test_too_short():
    card_number = "1234"
    assert verify(card_number) == False
